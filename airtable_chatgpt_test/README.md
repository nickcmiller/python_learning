# Introduction

## Overview

This code provides an example of how the OpenAI GPT-3 API can be integrated with Airtable to automate the process of generating and storing responses to questions, which can be useful for applications such as customer service, technical support, and educational content generation.

## Setting up Variables and API Keys

All of the variables are stored in a .env file in my local directory. Be sure to add `*.env*` to your `.gitignore` file. 
```
AIRTABLE_API_KEY=<Your Airtable API key>
AIRTABLE_BASE_ID=<Airtable Base containing the Table used for your flash cards>
AIRTABLE_TABLE_NAME=<Airtable Table Name containing flash cards>
OPENAI_API_KEY=<Your OpenAI API Key>
```

You'll an Airtable API token that has the `data.records:read` and `data.records:read` permissions. Make sure you're replace spaces in the Table Name with "%20" as it will be passed into a URL endpoint.

Generate your Airtable API token here: https://airtable.com/create/tokens 

Get your OpenAI API key here: https://platform.openai.com/account/api-keys

## How the Code Works

# Airtable Functions

The `airtable_functions()` contains the `get_records()` and `write_record()` functions.

The `get_records()` function will retrieve all records for the defined Airtable Table(`AIRTABLE_TABLE_NAME`) within Airtable base (`AIRTABLE_BASE_ID`). The get_records() function takes an optional parameters argument, which can be used to filter the records returned by the API. The function first sets the API endpoint by combining the base ID and table name, then sets the headers and parameters for the API request. It sends a GET request to the API endpoint using the requests library, then extracts the records from the response JSON and returns them as a list.

The `write_record()` function will be used to write ChatGPT's answers back to the table. It takes a record\_id argument and a dictionary of new\_fields that represent the updated field values for the record. The function sets the API endpoint, headers, and request body based on the given arguments, then sends a PATCH request to the API to update the record. It finished by returning the JSON response from the API as a formatted string.

# ChatGPT Function

The `question_chatGPT()` function generates a response to a given question using the OpenAI API. It does this by calling the `openai.ChatCompletion.create()` function, which takes a text question as input and generates a text response based on the provided context. The OpenAI model I've opted to use for this project is `gpt-3.5-turbo`. In this project, I've instructed the model to give detailed responses to a student studying for a technical exam.

To handle potential API connection errors, the function is wrapped in a loop and try block that will try the API call up to three times with a 10-second delay between each attempt. If the API call fails after three attempts, the original exception is raised and the function terminates. The retry mechanism ensures that the function can handle temporary API connection issues and (hopefully!) still respond.

## Main Function

This Python code uses `chatgpt_functions.py` and `airtable_functions.py` to automate the process of generating ChatGPT responses to questions in an Airtable database. It first filters for records without filled ChatGPT Answer fields using the Airtable API, then retrieves those records using the `get_records()` function. For each record, it extracts the record ID and question text, generates a ChatGPT response to the question using the `question_chatGPT()` function, and writes the response back to the Airtable record using the `write_record()` function.