import requests

url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "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"  # replace this with your real API key

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {
            "role": "user",
            "content": "Explain the importance of fast language models"
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)

if response.ok:
    print("✅ Success!")
    print("Response:\n", response.json()["choices"][0]["message"]["content"])
else:
    print("❌ Failed with status code:", response.status_code)
    print("Details:", response.text)
