from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger_execution', methods=['POST'])
def trigger_execution():
    try:
        # Simulate execution by making an HTTP call
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        if response.status_code == 200:
            execution_status = "Success"
        else:
            execution_status = "Failed"
    except Exception as e:
        execution_status = "Failed: " + str(e)
    
    return render_template('index.html', execution_status=execution_status)

@app.route('/read_data', methods=['POST'])
def read_data():
    try:
        # Simulate reading data by making an HTTP call
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        data = response.json()
    except Exception as e:
        data = {"error": str(e)}
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

