import requests
def get_auth(login,password):

    url = "https://mapi.itstep.org/v1/mystat/auth/login"

    headers = {"accept": "application/json"}
    data = {"login": login, "password": password}
    
    response = requests.post(url, headers=headers, data = data)
    if(response.status_code == 200):
        return True,response.text
    else:
        return False,None
        
def get_marks(login,password):
    result = get_auth(login,password)
    if(result[0] == False):
        return False
    else:
        url = "https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks"
        headers = {"authorization":f"Bearer {result[1]}"}
        response = requests.get(url,headers=headers)
        if(response.status_code == 200):
            return response.text
        else:
            return False
    
