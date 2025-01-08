#from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.csv_loader import CSVLoader
#from chromadb_service import load_chunks

#loader = PyPDFLoader(    "./hackers.pdf")




loader = CSVLoader(file_path='tourism.csv', encoding="utf-8")
docs = loader.load()

print(docs[0])
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 2000,
    chunk_overlap = 20,
    length_function = len,
    is_separator_regex = False
)

chunks = []
for i in docs:
    text = i.page_content
    peices = text_splitter.create_documents([text])
    chunks.extend(peices)

#load_chunks(chunks)
#print(chunks[0])
#print(len(chunks))
