import os
from dotenv import load_dotenv
load_dotenv()
import groq
from models import LocalModels
local_models = LocalModels()
from langchain_groq import ChatGroq


os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

#response = local_models.local_llm(system_message=llm_prompt, user_message=u_prompt)


llm=ChatGroq(model="llama3-8b-8192")
print(llm)
result=llm.invoke("What is Agentic AI?")

print(result)
