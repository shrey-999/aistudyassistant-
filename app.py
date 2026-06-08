import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

print("\nAI Study Assistant")
print("1. Explain a concept")
print("2. Summarize text")
print("3. Generate quiz questions")

feature = input("\nSelect an option: ")
user_text = input("Enter your text: ")

if user_text.strip() == "":
    print("Please enter some text.")
    quit()

if feature == "1":
    prompt = f"Explain the following concept in simple terms:\n\n{user_text}"

elif feature == "2":
    prompt = f"Summarize the following text into 5 bullet points:\n\n{user_text}"

elif feature == "3":
    prompt = f"Create 5 quiz questions based on:\n\n{user_text}"

else:
    print("Invalid option selected.")
    quit()

response = model.generate_content(prompt)

print("\nResponse:\n")
print(response.text)