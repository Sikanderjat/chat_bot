import requests

url = "https://chatgpt-42.p.rapidapi.com/geminipro"

payload = {
	"messages": [
		{
			"role": "user",
			"content": input('Enter your question:-> ')
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

data = (response.json())
print(data)