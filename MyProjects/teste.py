import hashlib
import hmac




def generate_mac(params_string, user_secret):
    hashing_obj = hmac.new(user_secret.encode('utf-8'), digestmod=hashlib.sha512)
    hashing_obj.update(params_string.encode('utf-8'))
    return hashing_obj.hexdigest()

def get_request_body(request):
    return request.body.decode("utf-8")


def build_request_msg_string(request):
    request_msg_string = request.path
    request_msg_string += "?"
    request_msg_string += get_request_body(request)

    return request_msg_string

class Request:
    def __init__(self, path,body):
        self.path = path
        self.body = body



user_secret = "226c96e3f4ff2d5e46cd7d882bf2de7265c5dc1eb4c3fb6b747475d1f9a54f4d"
path = "/api/v1/marketplace/crypto/buy/estimate"
body = b'{"fiat_quantity": "1.00","coin_id": "BTC"}'

request = Request(path, body)
params_string = build_request_msg_string(request)

Tapi_mac = generate_mac(params_string, user_secret)

print(params_string,"\n",Tapi_mac)