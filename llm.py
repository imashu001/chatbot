import requests
from ollama import chat
from ollama import ChatResponse
OLLAMA_URL = "http://localhost:11434/api/chat"
SYSTEM_PROMPT = """
You are a helpful Assitant and your job is to assit user only when user is not talking about wars.
 politely say no and ask user to ask relevent dobts or questions when user asks something which is related to wars in anyway
"""
def generate_response(input: str):

    try:
        response: ChatResponse = chat(
            model='llama3.2:3b', messages=[
                {
                    'role': 'system',
                    'content': SYSTEM_PROMPT

                },
                {
                    'role': 'user',
                    'content': input,
                },
            ], 
            stream=True
        )
        for chunk in response:
            yield chunk
            # print(chunk)
            # yield chunk["message"]["content"]
    except Exception as e:
        print(f"exception detected {e}")
        raise