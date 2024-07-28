from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webOrder', methods=['POST'])
def receive_order():
    # Assuming a JSON payload with order details
    order_data = request.get_json()

    # Store the order data (in real scenario, this would save to a database)
    order_id = order_data.get('order_id')  # Assuming order_id is part of payload
    # Save order data logic would go here

    # Respond with a confirmation
    response = {'message': 'Order Received', 'order_id': order_id}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
