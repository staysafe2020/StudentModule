import requests

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"Wh21bjaYI367mZMxdCpFkf5cuiJtnXg8SGKerURsBTDzV4loLHRWYJ6fNEKhcgUy9T0pB1XIP5Fq3rno","sender_id":"FSTSMS","message":"This is test message","language":"english","route":"p","numbers":"8770925794"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)