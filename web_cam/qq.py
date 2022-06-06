from flask import Flask, render_template, request

app = Flask(__name__)

def gauss(a, b):
    a = a.copy()
    b = b.copy()
    zxczhuk = len(b)

    def forward():
        for i in range(zxczhuk-1):
            if a[i][i] == 0:
                for j in range(i+1, zxczhuk):
                    if a[j][i] != 0:
                        a[i], a[j] = a[j], a[i]
            for j in range(i+1, zxczhuk):
                zxczilba = -(a[j][i]/a[i][i])
                for k in range(i, zxczhuk):
                    a[j][k] += a[i][k]*zxczilba
                b[j] += b[i] * zxczilba

    def backward():
        for i in range(zxczhuk-1, -1, -1):
            for j in range(i-1, -1, -1):
                zxczilba = -(a[j][i] / a[i][i])
                a[j][i] = 0
                b[j] += b[i]*zxczilba
            b[i] /= a[i][i]

    forward()
    backward()

    return b


@app.route('/')
def index(name='1', age='1'):
    if request.method == 'GET':
        name = request.args.get('name')
        age = request.args.get('age')

    if name is None:
        name = "Ноунейм"
    if age is None:
        age = 'hz'
    else:
        age = int(age)+10
    return render_template('index.html', name=name, age=age)


@app.route('/gaus')
def gaus(ans= 'РЕШЕНИЙ НЕТ'):
    a = [[0 for j in range(3)] for i in range(3)]
    b = [0 for i in range(3)]
    if request.method == 'GET':
        for i in range(3):
            b[i] = request.args.get('{}_{}'.format(i, 3))
            for j in range(3):
                a[i][j] = request.args.get('{}_{}'.format(i, j))
    if no_mt(a[0]) and no_mt(a[1]) and no_mt(a[2]) and b:
        for i in range(3):
            for j in range(3):
                a[i][j] = int(a[i][j])
            b[i] = int(b[i])
        ans = gauss(a, b)
    return render_template('gaus.html', ans=ans)


def no_mt(a):
    for i in a:
        if i == '' or i is None:
            return 0
    return 1



app.run(debug=True)
