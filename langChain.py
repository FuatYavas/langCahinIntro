from dotenv import load_dotenv , dotenv_values

load_dotenv()

print(dotenv_values(".env").get('openai_api_key'))
print('heloo')


