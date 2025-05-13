#请求处理模块，封装了发送 HTTP 请求的方法，方便在测试用例中调用
import requests

class RequestHandler:
    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, url, **kwargs):
        return self.session.request(method, url, **kwargs)

    def close_session(self):
        self.session.close()