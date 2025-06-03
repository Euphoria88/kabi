import requests
from RegistLogin import EnrollLogin

token, user_id = EnrollLogin('+8619980684952')
header ={
    "Content_Type": "application/json",
    "Authorization": f'Bearer {token}',
}
#获取用户匹配码
def GetMatchCode(phone):
    """
    :param user_id: 登录成功后返回的user_id
    :param token: 登录成功后返回的token
    :return: match_code
    """
    match_url = 'http://124.220.33.63:8705/api/user/profile'
    header = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '
    }
    header['Authorization'] += token
    print(token)
    match_res = requests.get(url=match_url, headers=header)
    # print(match_res.json())
    match_code = match_res.json()['data']['me']['match_code']
    print(match_code)
    return match_code

if __name__ == '__main__':
    GetMatchCode('+8619980684952')
