import requests


header={
    "Content_Type":"application/json",
    'Authorization': f'Bearer {token1}',
}

#获取登录验证码
def SmsCode(phone):
    code_url = "http://124.220.33.63:8705/sms/login/send"
    code_params = {
        "to": phone
    }
    code_resp = requests.post(url=code_url,headers=header,json=code_params)
    phone_code = code_resp.json().get('data').get('code')
    print(phone_code)
    return phone_code


def Login(phone):
    code = SmsCode(phone)
    login_url = "http://124.220.33.63:8705/login/phone"
    login_params = {
        "Phone": phone,
        "PhoneCode": code
    }
    resp_login = requests.post(url=login_url,headers=header,json=login_params)
    global token1
    token1 = resp_login.json().get('data')[0].get('token')
    print(token1)
    return token1

def CreatePlan():
    plan_url = "http://124.220.33.63:8705/api/plan"
    plan_params = {
      "cover": "https://cdn.codeffect.top/hebao/cover/5.png",#存钱计划背景
      "end_time": "2024-12-04",
      "method": "daily",
      "name": "看电影计划",
      "ret": 1389,
      "start_time": "2025-01-09",
      "target": 50000,
      "unit": 1389
    }
    plan_resp = requests.post(url=plan_url,headers=header,json=plan_params)
    plan_id = plan_resp.json().get('data').get('id')
    print(plan_id)
    return plan_id

def AcceptPlan():
    id = CreatePlan()
    confirm_url = "http://124.220.33.63:8705/api/plan/confirm/{id}"
    confirm_resp = requests.put(url=confirm_url,headers=header)
    print(confirm_resp)

if __name__ == '__main__':
    Login('+8617725048787')

    #SmsCode("+8619987434954")