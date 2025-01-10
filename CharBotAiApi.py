import openai

openai.api_key = "secret key genrated by openAI"

def chat_with_gpt(prompt):
    responce = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo" ,
        message=[{"role": "user", "content": prompt}]
    )

    return responce.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
       user_input = input("You: ")
       if user_input.lower() in ["quit", "exit", "bye"]:
           break

       responce = chat_with_gpt(user_input)
       print("Chatbot: ", responce)
