import os
from google.oauth2 import service_account
from google.cloud import language_v1
# from google.cloud.language_v1 import enums
from google.cloud.language_v1 import types

print(os.getcwd())


credentials = service_account.Credentials.from_service_account_file("C:/Users/cxysz/Downloads/ec601phase2-5034049bb0eb.json")



def language_analysis(text):
    client = language_v1.LanguageServiceClient(credentials=credentials)
    document = types.Document(
        content = text,
        type = language_v1.Document.Type.PLAIN_TEXT
    )

    sentiment = client.analyze_sentiment(
        request={"document":document}
    ).document_sentiment

    print("Text: {}".format(text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
    return sentiment

example_text = "Please make sure you do NOT put your keys in GitHub or any public domain site.Please make sure you track your usage so you dont encounter financial payment.  The class needs should be free"
language_analysis(example_text)
# print("hello world")
# example_text = "Please make sure you do NOT put your keys in GitHub or any public domain site.Please make sure you track your usage so you dont encounter financial payment.  The class needs should be free"
# sentiment, entities = language_analysis(example_text)
# print('hello world')
# print(sentiment.score, sentiment.magnitude)

# for e in entities:
#     print(e.name, e.entity_type, e.metadata,e.salience)
