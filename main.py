from flask import Flask, jsonify, request
from jwt import exceptions
import time
import uuid
import jwt

app = Flask(__name__)

config = {
    'algorithm': 'HS256',
    'token_type': 'Bearer',
    'expires_in': 60 * 60 * 24,
    'grant_type': 'client_credentials',
    'audience': 'https://sandbox.api.advantest.com/',
    'client_id': 'mPUx2ON7xbTM647dEItS4bAGLGV1nrRp',
    'client_secret': '1SuftRaGynwEbbb0GzGRQdz8AhHW-f1nG4HACAhWE7iCjcj-70xVXMa9dh6Epc3V'
}


def init_token(cfg=None):
    result = {}
    try:
        stamp = time.time()
        key_id = uuid.uuid4().hex
        cfg = config if cfg is None else cfg
        payload = {
            'iat': stamp,
            'jti': key_id,
            'iss': cfg.get('audience'),
            'aud': cfg.get('audience'),
            'azp': cfg.get('client_id'),
            'gyp': cfg.get('grant_type'),
            'exp': stamp + cfg.get('expires_in'),
            'sub': f'{cfg.get("client_id")}@TECloud'
        }
        headers = {
            'kid': key_id,
            'alg': cfg.get('algorithm'),
            'typ': cfg.get('token_type')
        }
        access_token = jwt.encode(payload=payload, key=cfg['client_secret'], algorithm=cfg.get('algorithm'),
                                  headers=headers)
        result = {
            'access_token': access_token,
            'expires_in': cfg.get('expires_in'),
            'token_type': cfg.get('token_type')
        }

    except Exception as e:
        print(f'Init JWT token fail:{e}')

    return result


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/user/info', methods=['GET'])
def user_info():
    result = {
        'username': 'jerry',
        'password': '123456'
    }
    return jsonify(result), 200


@app.route('/api/oauth/token', methods=['POST'])
def oauth_token():
    info = request.values.to_dict()
    jwt_token = init_token()
    return jsonify(jwt_token), 200


def decode_token(token, cfg=None):
    result = {}
    try:
        cfg = config if cfg is None else cfg
        result['payload '] = jwt.decode(token, cfg['client_secret'], algorithms=[cfg.get('algorithm')], verify=True)

    except exceptions.ExpiredSignatureError:
        result['message'] = 'token已失效'

    except jwt.DecodeError:
        result['message'] = 'token认证失败'

    except jwt.InvalidTokenError:
        result['message'] = '非法的token'

    print(result)


if __name__ == '__main__':
    PORT = 5000
    # app.run(port=PORT)
    jwt_token = init_token()
    access_token = jwt_token.get('access_token')
    decode_token(access_token)
    print(access_token)
