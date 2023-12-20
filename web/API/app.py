from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Python!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)
