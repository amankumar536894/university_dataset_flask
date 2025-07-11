
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv
load_dotenv()

df = pd.read_csv("./colleges.csv", header=None, names=['University Name', 'Location', 'Rating', 'Price'])

data_str = df.to_string(index=False)

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324",
    task="text-generation"
)

llm = ChatHuggingFace(llm=llm)

# Prompt template
template = """
You are a data analyst. Answer the user's question using the following CSV data(if user ask different from this data refuse him to reply with humble that i can't help with these questions. make the answer very concise and short use around 50 words):

{data}

Question: {question}
Answer:"""

prompt = PromptTemplate(
    input_variables=["data", "question"],
    template=template
)

# user_question = "Jawaharlal Institute of Technology, (JIT) Borawan?"
# final_prompt = prompt.format(data=data_str, question=user_question) 
# response = llm.invoke(final_prompt)

def answer_question(question):
    final_prompt = prompt.format(data=data_str, question=question)
    response = llm.invoke(final_prompt)
    return response.content
