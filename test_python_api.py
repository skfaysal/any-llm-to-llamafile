# #!/usr/bin/env python3
# from openai import OpenAI
# client = OpenAI(
#     base_url="http://localhost:8000/v1", # "http://<Your api-server IP>:port"
#     api_key = "sk-no-key-required"
# )
# completion = client.chat.completions.create(
#     model="LLaMA_CPP",
#     messages=[
#         {"role": "system", "content": "You are ChatGPT, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
#         {"role": "user", "content": "Write a limerick about python exceptions"}
#     ]
# )
# print(completion.choices[0].message)


from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# point to your local llama-serve
llm = ChatOpenAI(
    openai_api_base="http://localhost:8000/v1",  # llama-serve endpoint
    model_name="LLaMA_CPP",                        # whatever your model is named in llama-serve
    openai_api_key="sk-no-key-required",           # local server doesn't need a real key
    temperature=0.7
)

response = llm.invoke([HumanMessage(content="Hello, Can you write a story?")])
print(response.content)
 