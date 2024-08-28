from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Initialize the LLM
llm = OllamaLLM(model="qwen2")

# Define the prompt templates
code_prompt = PromptTemplate(
    input_variables=["language", "task"],
    template="write a {language} function to {task} \n Just give me the output for code and no other prompt"
)

test_prompt = PromptTemplate(
    input_variables=["language", "code"],
    template="write a test for the following {language} code: \n {code} \n Just give me the output for test and no other prompt"
)

# Define the LLM chains with input and output keys
code_chain = LLMChain(
    prompt=code_prompt,
    llm=llm,
    output_key="code"
)

test_chain = LLMChain(
    prompt=test_prompt,
    llm=llm,
    output_key="test"
)

# Combine them into a SequentialChain
chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=["task", "language"],
    output_variables=["test", "code"]
)

# Invoke the chain with the input data
result = chain({
    "language": "javascript",
    "task": "detect prime numbers in an array"
})

print(result["code"])

print()

print(result["test"])