import boto3
import json

def extract_text_from_document(document_path):
    client = boto3.client('textract')
    with open(document_path, 'rb') as document:
        response = client.analyze_document(
            Document={'Bytes': document.read()},
            FeatureTypes=["FORMS"]
        )
    return response
