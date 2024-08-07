from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webOrderAccept', methods=['POST'])
def accept_order():
    try:
        order_data = request.get_json()
        if order_data is None:
            return jsonify({'error': 'Invalid JSON format'}), 400

        # Process order_data here
        return jsonify({'message': 'Order accepted', 'data': order_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
