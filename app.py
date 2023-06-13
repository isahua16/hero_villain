from dbhelpers import run_statement
from apihelpers import check_data
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)
@app.get('')
def new_function():
    return
app.run(debug=True)
