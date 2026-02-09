from flask import Flask, render_template, request, redirect, send_from_directory
from datetime import datetime
import json
import os

app = Flask(__name__)
FILE_PATH = 'data.json'

def load_messages():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    return []

def save_messages(msgs):
    with open(FILE_PATH, 'w') as f:
        json.dump(msgs, f)

@app.route('/', methods=['GET', 'POST'])
def home():
    messages = load_messages()
    if request.method == 'POST':
        user_msg = request.form.get('content')
        if user_msg:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            messages.append({"text": user_msg, "time": timestamp})
            save_messages(messages)
        return redirect('/')
    return render_template('index.html', messages=messages)

@app.route('/download-cv')
def download_cv():
    return send_from_directory('static', 'my_cv.pdf')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
