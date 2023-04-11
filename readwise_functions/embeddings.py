
import os
import re
import requests
import json
import openai
from transformers import AutoTokenizer
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")

def token_length(text):
    tokenized_text = tokenizer(text)["input_ids"]
    return len(tokenized_text)

def split_by_punctuation(text, max_token_length):
    punctuations = r"[.!?;]"
    sentence_pattern = re.compile(rf"([^?.!]*[?.!])(?:\s|$)")
    sentences = sentence_pattern.findall(text)
    chunks = []
    current_chunk = ""
    i = 1 
    for sentence in sentences:
        i += 1
        if token_length(current_chunk + sentence) <= max_token_length:
            current_chunk += sentence
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return [chunk for chunk in chunks if chunk]

def split_text_into_chunks(text, max_token_length):
    # Check if text is below or equal to max_token_length
    if token_length(text) <= max_token_length:
        # If so, return text as a single chunk
        return [text]
    
    # Otherwise, split text into paragraphs based on newlines
    paragraphs = text.split("\n\n")
    chunks = []

    for paragraph in paragraphs:
        # Check if paragraph exceeds max_token_length
        if token_length(paragraph) > max_token_length:
            # If so, split paragraph into chunks based on sentence-ending punctuation marks
            punctuated_chunks = split_by_punctuation(paragraph, max_token_length)
            for chunk in punctuated_chunks:
                # Check if chunk still exceeds max_token_length after splitting by punctuation
                if token_length(chunk) > max_token_length:
                    # If so, split chunk into smaller chunks based on token length
                    words = chunk.split()
                    current_chunk = []
                    for word in words:
                        current_chunk.append(word)
                        if token_length(" ".join(current_chunk)) >= max_token_length:
                            last_word = current_chunk.pop()
                            chunks.append(" ".join(current_chunk))
                            current_chunk = [last_word]
                    if current_chunk:
                        chunks.append(" ".join(current_chunk))
                else:
                    chunks.append(chunk)
        else:
            chunks.append(paragraph)

    return chunks

def create_embedding(text):
    
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    
    embedding = response['data'][0]['embedding']
    return embedding

def chunk_and_embed (long_text, max_token_length):
    chunks = split_text_into_chunks(long_text, max_token_length)
    embedding_list = []
    
    for chunk in chunks:
        embedding = create_embedding(chunk)
        embedding_list.append({
            "chunk": chunk,
            "embedding": embedding
        })
        
    return embedding_list
    
        
        