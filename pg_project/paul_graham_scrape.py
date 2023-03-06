# import required modules
from bs4 import BeautifulSoup
import requests
import re
import asyncio
import json
from transformers import AutoTokenizer

# initialize the tokenizer from the Hugging Face transformers library
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")

# define the base URL and chunk size for essay chunking
url = "http://paulgraham.com/"
chunk_size = 200

# define a function to encode text using the GPT-3 tokenizer
def encode(text):
    return tokenizer(text)["input_ids"]

# define a function to get all links to essays from the website
def get_links(base_url):
    # make a GET request to the website's articles page
    response = requests.get(f"{base_url}articles.html")
    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all("table")
    links_arr = []

    # iterate over each table element in the HTML and find links to essays
    for table in tables:
        if table.find_previous("table") and table.find_previous("table").find_previous("table"):
            links = table.find_all("a")
            for link in links:
                url = link.get("href")
                title = link.text
                if url and re.search(r"\.html$", url):
                    link_obj = {"url": url, "title": title}
                    links_arr.append(link_obj)

    return links_arr

def get_essay(link_obj, base_url):
    # Get the title and url of the link_obj passed as parameter and store them in separate variables
    title, url = link_obj["title"], link_obj["url"]
    essay = {
        "title": "",
        "url": "",
        "date": "",
        "thanks": "",
        "content": "",
        "length": 0,
        "tokens": 0,
        "chunks": []
    }

    # Construct the full link by appending the url to the base_url passed as parameter
    full_link = base_url + url
    
    # Get the content of the webpage by making a request to the constructed link
    html = requests.get(full_link).content
    
    # Use BeautifulSoup to parse the HTML content and get all the tables in the webpage
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table")
    
    # Loop through the tables and find the second table
    for i, table in enumerate(tables):
        if i == 1:
            # Get the text content of the second table and clean it
            text = table.get_text()
            cleaned_text = re.sub(r"\s+", " ", text)
            cleaned_text = re.sub(r"\.([a-zA-Z])", r". \1", cleaned_text)
    
            # Use regular expressions to extract the date of the essay from the cleaned text
            date = re.search(r"([A-Z][a-z]+ [0-9]{4})", cleaned_text)
            date_str = ""
            text_without_date = ""
    
            if date:
                date_str = date.group(0)
                text_without_date = re.sub(date_str, "", cleaned_text)
            else:
                text_without_date = cleaned_text
    
            # Remove all newlines from the text and extract any 'Thanks to' section if it exists
            essay_text = re.sub(r"\n", " ", text_without_date)
            thanks_to = ""
    
            split = essay_text.split(". ")
            split = [s for s in split if s]
            last_sentence = split[-1]
    
            if last_sentence and "Thanks to" in last_sentence:
                thanks_to_split = last_sentence.split("Thanks to")
    
                if thanks_to_split[1].strip()[-1] == ".":
                    thanks_to = "Thanks to " + thanks_to_split[1].strip()
                else:
                    thanks_to = "Thanks to " + thanks_to_split[1].strip() + "."
    
                essay_text = essay_text.replace(thanks_to, "")
    
            # Get the trimmed content and token count of the essay
            trimmed_content = essay_text.strip()
            tokens = len(trimmed_content.split())
    
            # Update the essay dictionary with the extracted information
            essay = {
                "title": title,
                "url": full_link,
                "date": date_str,
                "thanks": thanks_to.strip(),
                "content": trimmed_content,
                "length": len(trimmed_content),
                "tokens": tokens,
                "chunks": []
            }
    
    # Return the updated essay dictionary
    return essay

def chunk_essay(essay, chunk_size):
    # unpacking values from dictionary
    title, url, date, thanks, content, length, tokens, *chunkless_section = essay.values()

    # create a list to store essay text chunks
    essay_text_chunks = []

    # check if content is longer than the chunk size
    if len(encode(content)) > chunk_size:
        # split the content into sentences
        split = content.split(". ")
        chunk_text = ""

        # iterate over the sentences
        for sentence in split:
            
            # get the token lengths of the sentence and the current chunk
            sentence_token_length = len(encode(sentence))
            chunk_text_token_length = len(encode(chunk_text))


            # if adding the sentence to the current chunk would exceed the chunk size, add the chunk to the list
            # and start a new chunk
            if chunk_text_token_length + sentence_token_length > chunk_size:
                essay_text_chunks.append(chunk_text)
                chunk_text = ""
                
            # add the sentence to the current chunk
            if sentence[-1].isalnum():
                chunk_text += sentence + ". "
            else:
                chunk_text += sentence + " "

        # add the final chunk to the list
        essay_text_chunks.append(chunk_text.strip())
    else:
        # if content is shorter than the chunk size, add it as a single chunk
        essay_text_chunks.append(content.strip())

    # create a list to store essay chunks
    essay_chunks = []

    # iterate over the essay text chunks
    for text in essay_text_chunks:
        # strip leading/trailing whitespace from the chunk
        trimmed_text = text.strip()

        # create a dictionary to store the chunk metadata
        chunk = {
            "essay_title": title,
            "essay_url": url,
            "essay_date": date,
            "essay_thanks": thanks,
            "content": trimmed_text,
            "content_length": len(trimmed_text),
            "content_tokens": len(encode(trimmed_text)),
            "embedding": []
        }

        # add the chunk dictionary to the essay_chunks list
        essay_chunks.append(chunk)

    # if there is more than one essay chunk and the last chunk is shorter than 100 tokens, merge it with the previous chunk
    if len(essay_chunks) > 1:
        i = 0

        while i < len(essay_chunks):
            chunk = essay_chunks[i]
            prev_chunk = essay_chunks[i - 1] if i > 0 else None

            if chunk["content_tokens"] < 100 and prev_chunk:
                prev_chunk["content"] += " " + chunk["content"]
                prev_chunk["content_length"] += chunk["content_length"]
                prev_chunk["content_tokens"] += chunk["content_tokens"]
                essay_chunks.pop(i)
                i -= 1

            i += 1

    # create a dictionary to store the chunked essay section
    chunked_essay = {
        "title": title,
        "url": url,
        "date": date,
        "thanks": thanks,
        "content": content,
        "length": length,
        "tokens": tokens,
        "chunks": essay_chunks
    }

    # return the chunked essay section
    return chunked_essay

def create_pg_json(url, chunk_size):
    links = get_links(url)
    print("Links: ", len(links))
    essays = []
    i = 0
    for link in links:
        i+=1
        essay = get_essay(link, url)
        print(i, " ", essay['title'], essay['url'])
        chunked_essay = chunk_essay(essay, chunk_size)
        essays.append(chunked_essay)
    
    pg_json = {
        "current_date": "2023-03-01",
        "author": "Paul Graham",
        "url": "http://www.paulgraham.com/articles.html",
        "length": sum(essay['length'] for essay in essays),
        "tokens": sum(essay['tokens'] for essay in essays),
        "essays": essays
    }
    
    return pg_json

if __name__ == '__main__':
    #retrieve and chunk all the essays from Paul Graham's website
    pg_json = create_pg_json(url, chunk_size)
    
    #once the essays are chunked, it saves the data to a JSON file
    with open("json_storage/pg_data.json", "w") as f:
        json.dump(pg_json, f, indent=4)