
import requests
import json

API_KEY = "sk-5q7j1BBv9b9Ousv9i6sfVGhlQi5BSQp0P4O3a6ezCQsAz0az"  # Replace with your actual key
API_BASE = "https://api.theb.ai/v1"
MODEL = "llama-3.1-8b-chat"

def test_openai_api_direct():
    url = f"{API_BASE}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": "Hello, can you respond?"}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }

    try:
        resp = requests.post(url, headers=headers, data=json.dumps(data))
        resp.raise_for_status()
        result = resp.json()
        print("✅ API call succeeded! Model response:")
        print(result["choices"][0]["message"]["content"])
    except requests.exceptions.HTTPError as e:
        print("❌ HTTP error occurred:", e)
        print(resp.text)
    except Exception as e:
        print("❌ API call failed with error:", e)

if __name__ == "__main__":
    test_openai_api_direct()
