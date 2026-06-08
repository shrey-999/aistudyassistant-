from flask import Flask, request, render_template_string
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Study Assistant</title>
</head>
<body>
    <h1>AI Study Assistant</h1>

    <form method="POST">
        <select name="feature">
            <option value="1">Explain Concept</option>
            <option value="2">Summarize Text</option>
            <option value="3">Generate Quiz Questions</option>
        </select>

        <br><br>

        <textarea name="text" rows="10" cols="60"></textarea>

        <br><br>

        <button type="submit">Generate</button>
    </form>

    {% if result %}
    <h2>Response</h2>
    <pre>{{ result }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form["text"]
        feature = request.form["feature"]

        if text.strip():

            if feature == "1":
                prompt = f"Explain this concept simply:\n{text}"

            elif feature == "2":
                prompt = f"Summarize this in 5 bullet points:\n{text}"

            else:
                prompt = f"Generate 5 quiz questions about:\n{text}"

            result = model.generate_content(prompt).text

        else:
            result = "Please enter some text."

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)