from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.chroma import Chroma
import warnings

# Ignore all deprecation warnings
warnings.filterwarnings("ignore", category=Warning)

# embeddings
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=model_name)

text = "This is a sample text"
embedding = embeddings.embed_query(text)
# print(embedding)

# text splitter
textSplitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)

loader = TextLoader("./facts.txt")
docs = loader.load_and_split(text_splitter=textSplitter)

# setup DB instantly (eg from a file (facts.txt))
db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="emb"
)

# search similar sentence in database
results = db.similarity_search_with_score("Tell me something about chocolates", k=5)

for result in results:
    print('\n')
    print(result[1])
    print(result[0].page_content)