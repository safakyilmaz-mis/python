from pymongo import MongoClient
from bson.objectid import ObjectId
import ollama
from concurrent.futures import ThreadPoolExecutor, as_completed

# Connect to your MongoDB instance using the provided URI
client = MongoClient("mongodb://root:p2f9FXGxhdmPtEp8rmOv6ykKm0v8i1FNTmBWUqcDk9O0BiDsAzlDdQCLYQKuFc4R@95.217.39.116:5424/?directConnection=true")

# Connect to the 'cursor_directory' database and 'cursor_codes' collection
db = client["cursor_directory"]
cursor_codes_collection = db["cursor_codes"]

# Define the collection to save translated prompts
translated_collection = db["translated_cursor_codes"]

# Function to translate prompts using Ollama Gemma model
def translate_prompt(prompt):
    try:
        client = ollama.Client(host='http://localhost:11434')
        response = client.generate(model="mistral", prompt=f"Translate the following text to Turkish: {prompt}")
        return response['response']
    except Exception as e:
        print(f"Hata oluştu: {e}")
    return None

# Function to translate all fields that contain prompt lists
def translate_document(document):
    translated_document = {"_id": document["_id"]}  # Keep the original _id
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_field = {}
        for field, value in document.items():
            if isinstance(value, list):
                future = executor.submit(translate_field, value)
                future_to_field[future] = field
            else:
                translated_document[field] = value

        for future in as_completed(future_to_field):
            field = future_to_field[future]
            try:
                result = future.result()
                translated_document[f"translated_{field}"] = result
            except Exception as exc:
                print(f'{field} generated an exception: {exc}')

    return translated_document

def translate_field(value_list):
    return [translate_prompt(text) for text in value_list]

# Fetch the data from 'cursor_codes' collection, translate and store
def main():
    documents = list(cursor_codes_collection.find({}))  # Fetch all documents

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_doc = {executor.submit(translate_document, doc): doc for doc in documents}
        for future in as_completed(future_to_doc):
            doc = future_to_doc[future]
            try:
                translated_document = future.result()
                translated_collection.insert_one(translated_document)
                print(f"Translated and saved document with _id: {doc['_id']}")
            except Exception as exc:
                print(f'Document {doc["_id"]} generated an exception: {exc}')

if __name__ == "__main__":
    main()
