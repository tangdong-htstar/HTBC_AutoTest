import requests

# 定义请求的 URL
url = 'http://172.18.11.231:8081/security-jwt-service/auth/login'
data = {
            "loginName": "TDYY01",
            "password": "TI+s4iYRQTwcbYDrtLU5eLB36ZTaxC1f9hIo26EwyD1QnnAtJz7XM12hI4dBL2fE8XlWWYJJhOscc3/ja5ZeCO4W4boFsqLrSwaBm8RcX7KiH6e2PECwmO5Ib/P91OIzOqht09Yvo/RGdGWEShRWOoVLgAxBZWj2J5j0JNvsJCA",
            "uuId": "9839c143-6a34-4122-a34f-785fea672473",
            "code": "5055",
            "rememberMe": "0",
            "captchaEnabled": 0
        }
def login():
    response = requests.post(url, json=data).json()
    print('--------------------------------------------')
    print(response)
    status = response['status']

    if status == 0:
        # 打印响应的 JSON 数据
        print(response)
    else:
        print(f"请求失败，状态码: {response.status_code}")

if __name__ == '__main__':
    login()