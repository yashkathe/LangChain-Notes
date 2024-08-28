from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--task")
parser.add_argument("--language", default="python")

args = parser.parse_args()


llm = OllamaLLM(model="llama3")

code_prompt = PromptTemplate(
    template="write a {language} function to {task}",
    input_variables=["language", "task"],
)

code_chain = code_prompt | llm

result = code_chain.invoke({
    "language": args.language,
    "task": args.task  
})

print(result)