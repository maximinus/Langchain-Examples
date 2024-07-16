from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

# This keeps looping the conversation until "exit" is entered

ollama = ChatOllama(model='mistral:latest')

messages = [SystemMessage('You are a helpful assistant')]


def print_reply(message):
    for line in message.content.split('\n'):
        print(line)


while True:
    query = input('> ')
    if query.lower() == 'exit':
        break
    messages.append(HumanMessage(query))
    reply = ollama.invoke(messages)
    messages.append(reply)
    print_reply(reply)
