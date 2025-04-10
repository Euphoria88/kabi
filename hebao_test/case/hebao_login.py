import requests


header = {
    "Content-Type": "application/json"
}

# proxies = { "http": None, "https": None}

#获取短信验证码
def SmsSend(phone):
    sms_url = "http://124.220.33.63:8705/sms/login/send"
    sms_data = {
        # "biz": "hebao",
        # "message_type": "login",
        "to": phone
    }
    code_resp = requests.post(url= sms_url, headers=header, json=sms_data)
    code = code_resp.json().get('data').get('code')
    print(code)
    return code

#登录账号
def Login(phone):
    code = SmsSend(phone)
    login_url = "http://124.220.33.63:8705/login/phone"
    login_data = {
        "Phone": phone,
        "PhoneCode": code
    }
    login_resp = requests.post(url=login_url,headers=header,json=login_data)
    token = login_resp.json().get('data')[0].get('Token')
    print(token)
    return token

if __name__ == "__mian__":
    Login("+8618716202139")
    # SmsSend()