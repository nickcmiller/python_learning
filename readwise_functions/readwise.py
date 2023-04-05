import datetime
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

token = os.getenv('READWISE_TOKEN')

def fetch_from_export_api(days_passed=None):
    full_data = []
    next_page_cursor = None
    while True:
        params = {}
        if next_page_cursor:
            params['pageCursor'] = next_page_cursor
        if days_passed:
            day = datetime.datetime.now() - datetime.timedelta(days=days_passed)  # use your own stored date
            updated_after = day.isoformat()
            params['updatedAfter'] = updated_after
        print("Making export api request with params " + str(params) + "...")
        response = requests.get(
            url="https://readwise.io/api/v2/export/",
            params=params,
            headers={"Authorization": f"Token {token}"}, verify=False
        )
        full_data.extend(response.json()['results'])
        next_page_cursor = response.json().get('nextPageCursor')
        if not next_page_cursor:
            break
    return full_data

def extract_highlights(books):
    highlights = []
    for book in books:
        for highlight in book['highlights']:
            
            new_highlight_object = {
                "highlight_id": highlight['id'],
                "book_id": book['user_book_id'],
                "author": book['author'],
                "book_title": book['readable_title'],
                "highlight_text": highlight['text'],
                "highlight_created": highlight['created_at'],
                "highlight_updated": highlight['updated_at'],
                "reader_url": highlight['url'],
                "readwise_url": highlight['readwise_url']
            }
            highlights.append(new_highlight_object)
    return highlights