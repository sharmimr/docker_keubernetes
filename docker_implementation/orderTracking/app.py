from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/orderTracking/<order_id>', methods=['GET'])
def track_order(order_id):
    # Simulate order tracking based on order_id
    # In a real system, this would fetch data from a database or cache
    if order_id == '12345':
        status = 'Processing'
    elif order_id == '67890':
        status = 'Out for Delivery'
    else:
        status = 'Delivered'

    response = {'order_id': order_id, 'status': status}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)