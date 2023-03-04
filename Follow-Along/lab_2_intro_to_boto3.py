import boto3

client = boto3.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='I am hungry and I will eat', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )

    print(response['TranslatedText'])

translate_text()

