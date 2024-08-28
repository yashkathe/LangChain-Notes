from langchain_ollama.chat_models import ChatOllama
from langchain.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain.memory import ConversationSummaryMemory
from langchain.chains import LLMChain
import warnings

# Ignore all deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# initialise the LLM
llm = ChatOllama(model="llama3")

# initialise memory
memory = ConversationSummaryMemory(memory_key="messages", return_messages=True, llm=llm)

# create prompt templates
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)

# create chain
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    output_key="response",
    verbose=True,  # debug flag
)

# create a chat
while True:
    content = input(">>")
    result = chain({"content": content})

    print(result["response"])
