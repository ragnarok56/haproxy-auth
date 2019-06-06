from flask import Flask, request, jsonify
import pprint

app = Flask(__name__)

@app.route("/auth", methods=["POST"])
def auth():
    d = request.get_data()
    import sys
    print(request.json, file=sys.stderr)
    #print(d, file=sys.stderr)

    return jsonify({
        'user_dn': request.json,
        'entitlements': [{
            'name': 'this',
            'owner': 'someone'
        },{
            'name': 'another one',
            'owner': 'some other dude'
        }]
    })

@app.route("/")
def home():
    return request.headers.get('X-ENTITLEMENTS', 'No Entitlements')


class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, environ, resp):
        errorlog = environ['wsgi.errors']
        pprint.pprint(('REQUEST', environ), stream=errorlog)

        def log_response(status, headers, *args):
            pprint.pprint(('RESPONSE', status, headers), stream=errorlog)
            return resp(status, headers, *args)

        return self._app(environ, log_response)

if __name__ == '__main__':
    app.wsgi_app = LoggingMiddleware(app.wsgi_app)
    app.run(debug=True, host='0.0.0.0', port='80')