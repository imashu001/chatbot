import requests
from ollama import chat
from ollama import ChatResponse
OLLAMA_URL = "http://localhost:11434/api/chat"
def generate_response(input: str):
    response: ChatResponse = chat(model='llama3.2:3b', messages=[
        {
            'role': 'user',
            'content': input,
        },
    ])
    return (response['message']['content'])