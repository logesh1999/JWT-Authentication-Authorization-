from functools import wraps
import jwt
from flask import request, jsonify

#to use in other program 
#from JwtDecodeAndAuthenticate import auth
#@auth.token_required


class auth:
    def token_required(f):

        @wraps(f)
        def decorator(*args, **kwargs):

            token = None

            if 'Authorization' in request.headers:
                data = request.headers['Authorization']
                token = str.replace(str(data), 'Bearer ', '')
            if not token:
                return jsonify({'message': 'a valid token is missing'})

            try:
                data = jwt.decode(token, options={"verify_signature": False})
                # print(data)
            except:
                return jsonify({'message': 'token is invalid'})
            return f(*args, **kwargs)

        return decorator
