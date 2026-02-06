from flask import Flask, request, render_template
import requests

BackendUrl="http://0.0.0.0:5050"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    form_data = dict(request.form)
    
    try:
        response = requests.post(BackendUrl + '/submit', json=form_data, timeout=5)
        
        if response.status_code == 200:
            return "Success! Account created."
        else:
            return render_template('index.html', error="Backend rejected the request.")
            
    except Exception as e:
        return render_template('index.html', error="Could not connect to the server.")

if  __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)