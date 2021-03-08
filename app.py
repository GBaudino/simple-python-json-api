from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data ={
        "persons": [
            {"name" : "martin diaz",
            "age" : 18,
            "nationality" : 'Argentinian'
            },
            
            {"name":"cecilia lopez",
            "age" : 20,
            "nationality" : 'Colombian'},
            
            {"name":"gerardo gomez",
            "age" : 78,
            "nationality" : 'Brasilian'}
        ]
    }
    return jsonify(data)