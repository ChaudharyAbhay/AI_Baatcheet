import config
from openai import OpenAI  
import google.generativeai as genai 

#models initialization
def initgemini():
    genai.configure(api_key=config.API_KEY_GOOGLE)
    global model_gemini
    model_gemini=genai.GenerativeModel('gemini-2.5-flash-preview-04-17',system_instruction="You are a Human being named Eve. You have to take part in a completely natural and normal conversation and keep it human")


def initgpt():
    token_OAI = config.API_KEY_O4
    global clientgpt
    global model_gpt
    endpoint_gpt = "https://models.github.ai/inference"
    model_gpt = "openai/gpt-4.1"
    clientgpt = OpenAI(
        base_url=endpoint_gpt,
        api_key=token_OAI,
        )


#model call initilization
initgemini()
initgpt()
message_gemini = "helloww"
while True:
    response_gpt = clientgpt.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a very smart Person named Alex, you have to pretend you are a human and have a completely normal and logical conversation and you have to keep the convo continued and do not stop",
        },
        {
            "role": "user",
            "content": message_gemini,
        }
    ],
    temperature=1,
    top_p=1,
    model=model_gpt
    )
    message_gpt = response_gpt.choices[0].message.content
    print(message_gpt, "By GPT")



    
    response_gemini=model_gemini.generate_content(message_gpt)
    print(response_gemini.text , "By Gemini")
    message_gemini = response_gemini.text







