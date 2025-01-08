import pandas as pd
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import os
import shutil
from dotenv import load_dotenv

load_dotenv()

def loader(file_path):
    embeddings = OpenAIEmbeddings()

    # Clear previous Chroma database
    if os.path.exists("./chromadb"):
        shutil.rmtree("./chromadb")

    # Initialize Chroma vectorstore
    vectorstore = Chroma(
        persist_directory="./chromadb",
        embedding_function=embeddings,
        collection_name="tourism"
    )

    # Load CSV data
    df = pd.read_csv(file_path)

    # Combine relevant columns into a single text field
    df["combined"] = (
        "Destination: " + df["Destination"] + "\n" +
        "Category: " + df["Category"] + "\n" +
        "Budget Range: " + df["Budget Range"] + "\n" +
        "Best Season: " + df["Best Season"] + "\n" +
        "Activities: " + df["Activities"] + "\n" +
        "Likes: " + df["Likes"] + "\n" +
        "Dislikes: " + df["Dislikes"] + "\n" +
        "Accessibility: " + df["Accessibility"] + "\n" +
        "Suitable For: " + df["Suitable For"]
    )

    # Prepare the data for embeddings
    text_data = df["combined"].tolist()

    # Split texts into smaller chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = [chunk for text in text_data for chunk in text_splitter.split_text(text)]

    # Add texts to the vectorstore
    vectorstore.add_texts(texts=chunks)
    print(f"Added {len(chunks)} chunks to the vectorstore.")

def retriever(question: str):
    embeddings = OpenAIEmbeddings()

    # Load Chroma vectorstore
    vectorstore = Chroma(
        persist_directory="./chromadb",
        embedding_function=embeddings,
        collection_name="tourism"
    )

    # Perform similarity search
    results = vectorstore.similarity_search(question, k=4)
    return [result.page_content for result in results]

# Example usage
file_path = "tourism.csv"  # Path to your dataset
if os.path.exists(file_path):
    loader(file_path)

    question = "What is a good winter destination for families?"
    docs = retriever(question)
    print("Retrieved Documents:")
    for doc in docs:
        print(doc)
else:
    print(f"File not found: {os.path.abspath(file_path)}")
