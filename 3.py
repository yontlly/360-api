import requests
import json
from faker import Faker


fake = Faker()


url="http://10.206.83.74:8888/v1/message/send?access_token=1tpugosWHd1ye6z5mYjCP8TlMVyMxMBC"

headers={"Content-Type":"application/json"}
a=0
while a<1000:
    kk=fake.company()
    formdata = {
    "appid":"3360176254038201",
    "to_users":["3360176254038200"],
    "to_depts":[],
    "type":"text",
    "message":{
        "content":kk
    },
    "msg_status":"1"
}

    response = requests.post(url, data=json.dumps(formdata), headers=headers)

    print(response.json())
    a=a+1


# "accounts":[
#         "liucx1"
#     ],





