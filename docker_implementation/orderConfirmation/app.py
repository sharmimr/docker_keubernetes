from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/orderConfirmation/<order_id>', methods=['POST'])
def confirm_delivery(order_id):
    # Simulate confirming delivery for order_id
    # In a real system, this would update the database status
    # For simulation purposes, just return a confirmation message
    response = {'message': 'Order Confirmed', 'order_id': order_id}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)