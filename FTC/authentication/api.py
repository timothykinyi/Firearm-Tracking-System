from flask import Flask, jsonify, request
from flask_cors import CORS
import feedapi as FA

app = Flask(__name__)
CORS(app)

@app.route('/policedata', methods=['GET'])
def get_police_data():
    return jsonify(FA.policedata())

@app.route('/gundata', methods=['GET'])
def get_gun_data():
    return jsonify(FA.gundata())

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if FA.login(username,password):
        return jsonify(FA.logininfo(username)), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

@app.route('/getlocation', methods=['POST'])
def location_getter():
    data = request.get_json()
    email = data.get('email')
    time = data.get('time')
    date = data.get('date')

    return jsonify(FA.get_location(email , time , date)), 200

@app.route('/register_gun', methods=['POST'])
def gun_reg():
    data = request.get_json()
    guntype = guntype
    gunserialnumber = data.get('gunserialnumber')
    manufacturedate = data.get('manufacturedate')
    trackercode = data.get('trackercode')
    gunstatus = data.get('gunstatus')
    asigned = data.get('asigned')
    
    

    return jsonify(FA.register_gun(guntype, gunserialnumber, manufacturedate, trackercode, gunstatus, asigned)), 200

@app.route('/register_police', methods=['POST'])
def police_reg():
    data = request.get_json()
    firstname = data.get('firstname')
    secondname = data.get('secondname')
    policeID = data.get('policeID')
    rank = data.get('rank')
    email = data.get('email')
    phoneno = data.get('phoneno')

    return jsonify(FA.register_police(firstname, secondname, policeID, rank, email, phoneno)), 200

@app.route('/register_user', methods=['POST'])
def user_reg():
    data = request.get_json()
    policeID = data.get('policeID')
    rank = data.get('rank')
    email = data.get('email')

    return jsonify(FA.register_police(policeID, rank, email)), 200

@app.route('/checkin_gun', methods=['POST'])
def gun_checkin():
    data = request.get_json()
    policeID = data.get('policeID')
    First_name = data.get('First_name')
    Last_name = data.get('Last_name')
    serial_number = data.get('serial_number')
    Number_of_bullets = data.get('Number_of_bullets')
    time = data.get('time')

    return jsonify(FA.checkin(policeID, First_name, Last_name, serial_number, Number_of_bullets, time)), 200

@app.route('/checkout_gun', methods=['POST'])
def gun_checkout():
    data = request.get_json()
    policeID = data.get('policeID')
    First_name = data.get('First_name')
    Last_name = data.get('Last_name')
    serial_number = data.get('serial_number')
    Number_of_bullets = data.get('Number_of_bullets')
    time = data.get('time')

    return jsonify(FA.checkout(policeID, First_name, Last_name, serial_number, Number_of_bullets, time)), 200

@app.route('deletegun', methods=['DELETE'])
def delete_gun():
    data = request.get_json()
    serial_number = data.get('serial_number')
    return jsonify(FA.remove_gun(serial_number))

@app.route('deletepolice', methods=['DELETE'])
def delete_police():
    data = request.get_json()
    policeID = data.get('policeID')
    return jsonify(FA.remove_police(policeID))

@app.route('/users_update', methods=['PATCH'])
def update_user():
    data = request.get_json()
    user_rank = data.get('user_rank')
    return jsonify(FA.user_update(user_rank))
    
@app.route('/police_rank_update', methods=['PATCH'])
def update_police_rank():
    data = request.get_json()
    police_new_rank = data.get('police_new_rank')
    return jsonify(FA.police_rank_update(police_new_rank))

if __name__ == '__main__':
    app.run(debug=True , port=80)
