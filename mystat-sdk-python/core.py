import requests

class MyStat:
    def __init__(self,login,password):
        self.login = login
        self.password = password
    
    def get_auth(self):
        url = "https://mapi.itstep.org/v1/mystat/auth/login"
        headers = {"accept": "application/json"}
        data = {"login": self.login, "password": self.password}
         
        response = requests.post(url, headers=headers, data = data)
        if(response.status_code == 200):
            return True,response.text
        else:
            return False,None
        
    def get_marks(self):
        result = self.get_auth()
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
            

    
