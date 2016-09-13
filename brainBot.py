import requests

url = "http://api.brainshop.ai/get"

querystring = {"bid":"303","key":"UMVEIqUn9ncSty88","uid":"100","msg":"how are you doing"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "7a10acb3-38f2-64a5-79aa-49a5f631ea4b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
