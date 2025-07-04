import requests
url = "https://api.theb.ai/v1/models"
# url = "https://api.baizhi.ai/v1/models"
headers = {
  'Authorization': 'Bearer sk-5q7j1BBv9b9Ousv9i6sfVGhlQi5BSQp0P4O3a6ezCQsAz0az'
}
response = requests.request("GET", url, headers=headers)
print(response.json())
