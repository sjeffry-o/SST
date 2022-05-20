from flask import request, Flask, Response

app = Flask(__name__)

@app.route('/search')
def data():
    query = request.args.get('query')
    resp = Response(query)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run()
