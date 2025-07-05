from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory user storage (for demo purposes)
users = {"yafai": "123456"}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"success": False, "message": "User already exists"}), 400
    users[username] = password
    return jsonify({"success": True, "message": "Registration successful"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
