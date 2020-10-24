from flask import Flask, render_template, request, jsonify

red_wool_price = 100
green_wool_price = 10
blue_wool_price = 1

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/request_price', methods=['POST'])
def request_price():
    num_red_wool = int(request.form.get('num_red_wool'))
    num_green_wool = int(request.form.get('num_green_wool'))
    num_blue_wool = int(request.form.get('num_blue_wool'))
    price = red_wool_price * num_red_wool + green_wool_price * num_green_wool + blue_wool_price * num_blue_wool
    return jsonify({ 'price': price })

if __name__ == '__main__':
    application.run()