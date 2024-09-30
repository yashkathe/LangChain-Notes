# LangChain

Notes + Code for Langchain

## Table of Content

- [Introduction - Integrating LLM with Langchain](./1.Integrate-Model-and-Langchain/)

  - [Normal Program](./1.Integrate-Model-and-Langchain/main.py)
  - [Adding CLI support](./1.Integrate-Model-and-Langchain/main-cli.py)

- [Memory Management](./2.Memory-Management/)
  - [ConversationBufferMemory - Save Entire Conversation Data](./2.Memory-Management/main.py)
  - [ConversationSummaryMemory - Save Summary of Previous Conversation](./2.Memory-Management/main2.py)

- [Embeddings](./3.Adding-Context-with-Embedding/)
  - [Use TextSplitter and generate Text Embeddings](./3.Adding-Context-with-Embedding/main.py)

- [Custom Document Retrievers](./4.Custom-Document-Retrievers/)
  - [Create Chunk and Store Embeddings](./4.Custom-Document-Retrievers/main.py) -> Run this file only once to generate and store embeddings of files
  - [Give User Prompts via RetrievalQA](4.Custom-Document-Retrievers/prompt.py)
  - [Custom Retriever to eliminate Duplicate Content](4.Custom-Document-Retrievers/redundant_filter_retriever.py)
