from openai import OpenAI 
import os

api_key = os.getenv("API_KEY")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key
)

chat_history=[]

personas = {
    "default": "You are a helpful AI Assinstant",
    "sarcastic": "You are a sarcastic AI who gives witty and mocking responses ",
    "poet": "You are a poet AI that responds in rhymes and verses"
}

print("Chose a persona : (default / sarcastic / poet)")

user_persona_input =input("Enter Persona:").strip().lower()

chat_history.append({
    "role": "system",
    "content": personas[user_persona_input]
})

while True :

    user_input = input("enter your prompt :")

    chat_history.append({
        "role": "user",
        "content": user_input
    })
    
    if user_input == "exit":
        break 

    completion = client.chat.completions.create(
  
    model="deepseek/deepseek-r1-zero:free",
    messages=chat_history
    )
    response = completion.choices[0].message.content
    print(response)

    chat_history.append({
        "role" : "user",
        "content" : response
    })