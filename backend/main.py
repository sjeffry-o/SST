from flask import request, Flask
from vectorizeSearch import vectorizeSearch
import ngtpy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
index = ngtpy.Index('test')

@app.route('/search')
def data():
    query = request.args.get('query')
    result = vectorizeSearch(query, index)
    result.headers['Access-Control-Allow-Origin'] = '*'
    return result

if __name__ == '__main__':
    app.run(port=3001, host='0.0.0.0')
