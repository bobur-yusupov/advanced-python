from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

MONGO_DB_URL = os.getenv("MONGO_URL")
client = AsyncIOMotorClient(MONGO_DB_URL)
db = client["test_db"]
collection = db["items"]

async def create_document(document: dict):
    result = await collection.insert_one(document)
    return str(result.inserted_id)

async def read_document(query: dict):
    document = await collection.find_one(query)
    return document

async def read_documents():
    documents = []
    async for document in collection.find():
        documents.append(document)
    return documents

async def update_document(doc_id, update_data: dict):
    result = await collection.update_one({"_id": ObjectId(doc_id)}, {"$set": update_data})
    return result.modified_count

async def delete_document(doc_id):
    result = await collection.delete_one({"_id": ObjectId(doc_id)})
    return result.deleted_count

async def main():
    # document = {"name": "Roman Budaragin", "description": "The smartest person in the world"}
    # doc_id = await create_document(document)
    # print(f"Document created with ID: {doc_id}")

    query = {"name": "Roman Budaragin"}
    document = await read_document(query)
    print(f"Document found: {document}")

    # documents = await read_documents()
    # print(f"All documents: {documents}")

    # document_id = "68c84de4311bf1eabb1b7433"
    # update_data = {"price": 39.99}
    # modified_count = await update_document(document_id, update_data)
    # print(f"Number of documents updated: {modified_count}")

    # deleted_count = await delete_document(document_id)
    # print(f"Number of documents deleted: {deleted_count}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())