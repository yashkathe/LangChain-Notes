from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from redundant_filter_retriever import RedundantFilterRetriever
import warnings
import langchain

langchain.debug = True

# Ignore all deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=Warning)

# llm
llm = OllamaLLM(model='qwen2:latest')
# llm = OllamaLLM(model='qwen:0.5b')

# embeddings
model_emb = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=model_emb)

# setup database (not instanly from file)
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

# retriever = db.as_retriever()
retriever = RedundantFilterRetriever(
    embeddings=embeddings,
    chroma=db
)

# retrieval chain
chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

# result = chain.run('Tell me something about dolphins')
result = chain.run('Tell me something about a desert')

print(result)