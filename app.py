from dbhelpers import run_statement
from apihelpers import check_data
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)

@app.post('/api/hero')
def new_hero():
    error = check_data(request.json, ['name', 'description', 'image_url'])
    if (error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call new_hero(?,?,?)', [request.json.get('name'), request.json.get('description'), request.json.get('image_url')])
    if(type(results) == list and results != []):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify('Something went wrong'), 500)

@app.post('/api/villain')
def new_villan():
    error = check_data(request.json, ['name', 'description', 'image_url', 'hero_id'])
    if (error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call new_villain(?,?,?,?)', [request.json.get('name'), request.json.get('description'), request.json.get('image_url'), request.json.get('hero_id')])
    if(type(results) == list and results != []):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify('Something went wrong'), 500)

@app.get('/api/hero')
def get_heroes():
    results = run_statement('call get_heroes()')
    if(type(results) == list and results != []):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify('Something went wrong'), 500)

@app.get('/api/villain')
def get_villain():
    error = check_data(request.args, ['hero_id'])
    if(type(error) == None):
        return make_response(jsonify(error), 400)
    results = run_statement('call get_villain(?)', [request.args.get('hero_id')])
    if(type(results) == list and results != []):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify('Something went wrong'), 500)

app.run(debug=True)
