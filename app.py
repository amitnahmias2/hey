from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def check_string():
    input_string = request.args.get('input_string', '')
    if len(input_string) == 5:
        return 'happy'
    else:
        return 'unhappy'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
