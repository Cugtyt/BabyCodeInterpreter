import openai
import time
import random

openai.api_key = 'xxx'
openai.api_version = "2023-07-01-preview"
openai.api_type = "azure"
openai.api_base = "xxx"


system = [
    {
        "role": "system",
        "content": """You are a very smart AI assistant that can use given tools to solve problems.
1. You should not use tools not provided.
2. If there are multiple solutions, you should always ask user to choose one.
3. If you can't solve the problem, you should tell user that you can't solve the problem and ask user to provide more information.
4. You should carefully understand the problem and plan the solution before you start to solve the problem with correct step order and tools."""
    }
]

functions= [  
    {
        "name": "execute_python_code",
        "description": "Run python code with pandas and numpy to get the result.",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The python code to run, the packages you can use are pandas, numpy.",
                },
                "reason": {
                    "type": "string",
                    "description": "The reason why you want to run this code and what problem you want to solve.",
                },
                "explanation": {
                    "type": "string",
                    "description": "How this code will solve the problem.",
                },
                "information_to_user": {
                    "type": "string",
                    "description": "The guiding information you want to tell user clearly about what you are doing and how it will solve user problem before you run this.",
                },
            },
            "required": ["code", "reason", "explanation", "information_to_user"],
        },
    },
    {
        "name": "mail_paper_copy_to",
        "description": "Mail a paper copy of file to someone.",
        "parameters": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "The path of file to print.",
                },
                "mode": {
                    "type": "string",
                    "description": "The mode of printer, can be 'color' or 'black and white', default is 'color'.",
                },
                "to": {
                    "type": "string",
                    "description": "The name of the receiver.",
                },
                "reason": {
                    "type": "string",
                    "description": "The reason why you want to run this and what problem you want to solve.",
                },
                "explanation": {
                    "type": "string",
                    "description": "How this will solve the problem.",
                },
                "information_to_user": {
                    "type": "string",
                    "description": "The guiding information you want to tell user clearly about what you are doing and how it will solve user problem before you run this.",
                },
            },
            "required": ["file", "to", "reason", "explanation", "information_to_user"],
        },
    }
]


def call(messages):
    while True:
        try:
            response = openai.ChatCompletion.create(
                engine="xxx",
                messages=system + messages,
                temperature=0.1,
                functions=functions,
                function_call="auto", 
            )
            break
        except:
            time.sleep(random.randint(5, 10))
            continue

    return response['choices'][0]['message']