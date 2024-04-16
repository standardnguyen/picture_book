from openai import OpenAI
import os

name_of_book = "whitenights"
full_book_txt = "whitenights_full.txt"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
model_to_use="gpt-3.5-turbo-0125"
backup_model="gpt-4-turbo"
