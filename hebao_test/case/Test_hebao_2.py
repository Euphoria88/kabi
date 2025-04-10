import requests
from case.Test_hebao_1 import SmsCode

token = SmsCode("+8616688889999")

header = {
    "Content_Type":"application/json",
    "Authorization": f'Bearer {token}'
}

def create_flows():
    url = 'http://124.220.33.63:8705/api/flows'
    data = {
	    "date": "2024-11-21",
	    "amount": 2500,
	    "amount_user": 318,
	    "amount_type": "书籍",
	    "remark": 'null',
	    "flow_type": "expense",
	    "auto": 'false',
	    "id": 'null'
    }
    create_resp = requests.post(url=url,data=data,headers=header)
    return create_resp.json()




if __name__ == '__main_-':
    create_flows()