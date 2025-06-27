from flask import Flask, request, jsonify 
app = Flask(__name__)

users = {
    1:{"name": "abcd", "age": 23, "country": "India"},
    2:{"name": "wxyz", "age": 12, "country": "japan"},
    3: {"name": "pqrs", "age": 53, "country": "Australia"}
}

@app.route("/users", methods = ["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users/<int:user_id>", methods = ["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "users not found"}), 400

@app.route("/users", methods = ["GET"])
def new_user():
    data = request.get_json()
    user_id = max(users.key()) + 1
    users[user_id] = data
    return jsonify({"message": "new user created", "user": users[user_id]}), 201

@app.route("/users/<int:user_id>", methods = ["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "users not found"}), 404
    else:
        data = request.get_json()
        users[user_id].update(data)
        return jsonify({"message": "user updated succesfully", "user": users[user_id]}), 200
    
@app.route("/users/<int:user_id>", methods = ["DELETE"])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"message": "user deleted", "user": users[user_id]}, 200)
    return jsonify({"error": "users not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)