from langchain_community.llms import Ollama

# simplest example of chat
# This sends a line of text to the LLM and prints the output with streams

LLM_INPUT = 'What is more important for a musician, melody or rhythm?'

llm = Ollama(model='mistral:latest')

for chunks in llm.stream(LLM_INPUT):
    print(chunks, end='')
