from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_ollama.chat_models import ChatOllama

model_name = "sentence-transformers/all-MiniLM-L6-v2"
hf_embeddings = HuggingFaceEmbeddings(model_name=model_name)

text = "This is a sample text"
embedding = hf_embeddings.embed_query(text)
print(embedding)

textSplitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)

loader = TextLoader("./facts.txt")
docs = loader.load_and_split(text_splitter=textSplitter)

print(docs)
