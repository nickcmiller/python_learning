# Introduction

## Setting up Variables and API Keys

All of the variables are stored in a .env file in my local directory. Be sure to add `*.env*` to your `.gitignore` file. 
```
YOUR_API_KEY=<Your Airtable API key>
YOUR_BASE_ID=<Airtable Base containing the Table used for your flash cards>
YOUR_TABLE_NAME=<Airtable Table Name containing flash cards>
OPENAI_API_KEY=<Your OpenAI API Key>
```

At a minimum, you'll an Airtable API token that has the `data.records:read` and `data.records:read` permissions. Make sure you're replace spaces in the Table Name with "%20" as it will be passed into a URL endpoint.
Generate your Airtable API token here: https://airtable.com/create/tokens 


Get your OpenAI API key here: https://platform.openai.com/account/api-keys

# Airtable Functions

The `airtable_functions.py` contains the `get_records` and `write_record` functions, which will be used in the main function to retrieve all records