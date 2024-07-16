from langchain_community.llms import Ollama

# simplest example of chat
# This sends a line of text to the LLM and prints the output

LLM_INPUT = 'What is more important for a musician, melody or rhythm?'

llm = Ollama(model='mistral:latest')
print(llm.invoke(LLM_INPUT))
