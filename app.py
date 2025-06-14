from flask import Flask, request, jsonify
from google_sheets import get_all_projects, save_project

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Material Estimator API is running."

@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(get_all_projects())

@app.route('/save_project', methods=['POST'])
def post_project():
    data = request.get_json()
    result = save_project(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
