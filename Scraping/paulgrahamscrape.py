import requests
from bs4 import BeautifulSoup
import re
url = "http://paulgraham.com/"

def get_links(base_url):
    response = requests.get(f"{base_url}articles.html")
    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all("table")
    links_arr = []

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

    full_link = base_url + url
    html = requests.get(full_link).content
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table")

    for i, table in enumerate(tables):
        if i == 1:
            text = table.get_text()
            cleaned_text = re.sub(r"\s+", " ", text)
            cleaned_text = re.sub(r"\.([a-zA-Z])", r". \1", cleaned_text)

            date = re.search(r"([A-Z][a-z]+ [0-9]{4})", cleaned_text)
            date_str = ""
            text_without_date = ""

            if date:
                date_str = date.group(0)
                text_without_date = re.sub(date_str, "", cleaned_text)

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

            trimmed_content = essay_text.strip()
            tokens = len(trimmed_content.split())

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

    return essay
    
links = get_links(url)
print(links[0])
print(get_essay(links[0], url))
# print(test)