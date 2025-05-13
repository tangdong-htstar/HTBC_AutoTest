import pytest
import requests


# 封装请求类
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self,params=None, headers=None):
        url = self.base_url
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"请求出错: {e}")
            return None

    def post(self, data=None, json=None, headers=None):
        url = self.base_url
        try:
            response = requests.post(url, data=data, json=json, headers=headers)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"请求出错: {e}")
            return None

# 测试数据
BASE_URL = "http://172.18.11.231:8081/security-jwt-service/auth/login"
client = APIClient(BASE_URL)


# 测试用例
@pytest.mark.parametrize("endpoint, expected_status", [
    ("/posts", 200),
    ("/comments", 200)
])
def test_get_requests(endpoint, expected_status):
    response = client.get(endpoint)
    assert response is not None
    assert response.status_code == expected_status


@pytest.mark.parametrize("data, expected_status", [
    ({
            "loginName": "TDYY01",
            "password": "TI+s4iYRQTwcbYDrtLU5eLB36ZTaxC1f9hIo26EwyD1QnnAtJz7XM12hI4dBL2fE8XlWWYJJhOscc3/ja5ZeCO4W4boFsqLrSwaBm8RcX7KiH6e2PECwmO5Ib/P91OIzOqht09Yvo/RGdGWEShRWOoVLgAxBZWj2J5j0JNvsJCA",
            "uuId": "9839c143-6a34-4122-a34f-785fea672473",
            "code": "5055",
            "rememberMe": "0",
            "captchaEnabled": 0
        }, 200)
])
def test_post_requests(data, expected_status):
    response = client.post(json=data)
    assert response is not None
    assert response.status_code == expected_status

