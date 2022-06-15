import requests  # pip install request

HOST = 'http://127.0.0.1:8000/post/1/'
# TOKEN = '185bc91601276c7839be56731c7f110a2578876e'
JWT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6InVzZXIiLCJleHAiOjE2NTUyNzk1ODMsImVtYWlsIjoiIn0.UBnlXGv7iCHW1uDmMghRcjnOcKO9PMcAnkyT86MtYyE'
# JWT_TOKEN = (
#     'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
#     '.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6InV'
#     'zZXIiLCJleHAiOjE2NTUyNzk1ODMsImVtYWl'
#     'sIjoiIn0.UBnlXGv7iCHW1uDmMghRcjnOcKO'
#     '9PMcAnkyT86MtYyE'
# )

headers = {
    # 'Authorization': f'Token {TOKEN}', # Token 인증
    'Authorization': f'JWT {JWT_TOKEN}',  # JWT 인증
}

res = requests.get(HOST, headers=headers)
print(res.json())
