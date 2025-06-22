from flask import Flask, render_template, request, jsonify
from transformers import T5Tokenizer, T5ForConditionalGeneration
import os

app = Flask(__name__)

# Ensure local path is used
MODEL_PATH = os.path.join(os.path.dirname(__file__), "trained_model")

# Confirm the path and files
print("Loading model from:", MODEL_PATH)
print("Contents:", os.listdir(MODEL_PATH))

# Load model and tokenizer
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)

def generate_answer(prompt, max_length=64):
    input_text = "question: " + prompt
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output_ids = model.generate(
        input_ids,
        max_length=max_length,
        num_beams=4,
        early_stopping=True
    )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_answer', methods=['POST'])
def get_answer():
    question = request.form['question']
    answer = generate_answer(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
