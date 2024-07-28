from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/deliveryConfirmation', methods=['GET'])
def delivery_confirmation():
    return jsonify(message="Delivery Complete"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
