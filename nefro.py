from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=key)

prompt = 'Your goal is to orchestrate mutiple AI agents that require multiple steps to complete a task. You will be given a task and you will need to determine the best way to orchestrate the agents to complete the task in the most efficient way. You will also need to provide a detailed plan of the steps that will be taken and the results that will be achieved at each step.'
task = input("Enter the task: ")

messages = [{"role": "system", "content": prompt}, {"role": "user", "content": task}]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages
)

print(response.choices[0].message.content)

with open("plan.txt", "w") as f:
    f.write(response.choices[0].message.content)

