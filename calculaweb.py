import os
from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/calculaform', methods=['POST'])
def form():
    numero1 = request.form['v1']
    newNum1 = int(numero1)
    numero2 = request.form['v2']
    newNum2 = int(numero2)
    operacao = request.form['operacao']
    print(operacao)

    if(operacao == 'soma'):
        resultado = int(newNum1 + newNum2)
    elif (operacao == 'subtracao'):
        resultado = int(newNum1 - newNum2)
    elif (operacao == 'divisao'):
        resultado = int(newNum1 / newNum2)
    elif (operacao == 'multiplicacao'):
        resultado = int(newNum1 * newNum2)
    return str(resultado)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
