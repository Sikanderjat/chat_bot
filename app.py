from flask import Flask, request, render_template
import requests
app = Flask(__name__)

@app.route('/')
def chat_bot():
    return render_template("home.html")

@app.route('/result', methods=['POST','get'])
def search():
    url = "https://chatgpt-42.p.rapidapi.com/geminipro"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": request.form.get("chat")
            }
        ],
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256,
        "web_access": False
    }
    headers = {
        "x-rapidapi-key": "15d460188bmshb9d1514b7c69293p12aeb5jsnee9ff1265b22",
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        c=request.form.get("chat")
        print(c)
        print(data)
        data=data["result"]
        return render_template("home.html", data=data)
    else:
        return "Error: Unable to retrieve response from API", 500


app.run(debug=True, host="localhost", port=5500)