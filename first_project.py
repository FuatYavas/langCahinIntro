from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()
model = ChatOpenAI(model="gpt-3.5-turbo")
# temprature 0 a ne kadar yakınsa o kadar kesin 1 e ne kadar yakınsa o kadar yaratıcı cevaplar verir
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content)

