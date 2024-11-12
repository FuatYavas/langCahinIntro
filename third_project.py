from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
model = ChatOpenAI(model="gpt-4")

system_template = "Translate the following into {language}:" # Burda modeli daha dinamik hale getirdik gelen txt in içerisini otamatik olarak hangi dil olduğunu algılayacak

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

parser = StrOutputParser()

chain = prompt_template | model | parser


if __name__ == "__main__":
    print(chain.invoke({"language": "italian", "text": "hi"}))
#Yukarıda ki kısımda language olarak verdiğimiz dict in 1. kısmında convert etmesini istediğimiz dil
#2. kısmında ise convert etmesini istediğimiz metni belirttik