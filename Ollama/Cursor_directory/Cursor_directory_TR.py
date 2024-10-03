from pymongo import MongoClient
from bson.objectid import ObjectId
import ollama
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import hashlib

# Connect to your MongoDB instance using the provided URI
client = MongoClient("mongodb://root:p2f9FXGxhdmPtEp8rmOv6ykKm0v8i1FNTmBWUqcDk9O0BiDsAzlDdQCLYQKuFc4R@95.217.39.116:5424/?directConnection=true")

# Connect to the 'cursor_directory' database and 'cursor_codes' collection
db = client["cursor_directory"]
cursor_codes_collection = db["cursor_codes"]

# Define the collection to save translated prompts
translated_collection = db["translated_cursor_codes"]

# Çeviri önbelleği için basit bir sınıf
class TranslationCache:
    def __init__(self):
        self.cache = {}

    def get(self, text):
        return self.cache.get(hashlib.md5(text.encode()).hexdigest())

    def set(self, text, translation):
        self.cache[hashlib.md5(text.encode()).hexdigest()] = translation

translation_cache = TranslationCache()

# Ollama istemcisini global olarak oluştur
ollama_client = ollama.Client(host='http://localhost:11434')

# Function to translate prompts using Ollama Gemma model
def translate_prompt(prompt):
    cached = translation_cache.get(prompt)
    if cached:
        return cached

    try:
        response = ollama_client.generate(model="gemma:2b", prompt=f"Translate the following text to Turkish: {prompt}")
        translation = response['response']
        translation_cache.set(prompt, translation)
        return translation
    except Exception as e:
        print(f"Hata oluştu: {e}")
    return None

# Function to translate all fields that contain prompt lists
def translate_document(document, pbar):
    translated_document = {"_id": document["_id"]}
    
    total_fields = sum(1 for value in document.values() if isinstance(value, list))
    field_pbar = tqdm(total=total_fields, desc=f"Document {document['_id']}", leave=False)
    
    for field, value in document.items():
        if isinstance(value, list):
            translated_document[f"translated_{field}"] = translate_field(value, field_pbar)
        else:
            translated_document[field] = value
        pbar.update(1)
    
    field_pbar.close()
    return translated_document

def translate_field(value_list, pbar):
    translated_list = []
    for text in value_list:
        translated_list.append(translate_prompt(text))
        pbar.update(1)
    return translated_list

# Fetch the data from 'cursor_codes' collection, translate and store
def main():
    documents = list(cursor_codes_collection.find({}))  # Fetch all documents
    total_documents = len(documents)
    
    print(f"Total documents to process: {total_documents}")

    total_fields = sum(sum(1 for value in doc.values() if isinstance(value, list)) for doc in documents)
    
    with tqdm(total=total_fields, desc="Total progress") as pbar:
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_doc = {executor.submit(translate_document, doc, pbar): doc for doc in documents}
            
            for future in as_completed(future_to_doc):
                doc = future_to_doc[future]
                try:
                    translated_document = future.result()
                    translated_collection.insert_one(translated_document)
                except Exception as exc:
                    print(f'Document {doc["_id"]} generated an exception: {exc}')

    print("Translation completed!")

if __name__ == "__main__":
    main()
