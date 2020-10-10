from flask import Flask,render_template,redirect,request, url_for
app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index1():
    if request.method == 'POST':
        return redirect(url_for('index2'))
    return render_template('index1.html')
@app.route('/info',methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        return redirect(url_for('index3'))
    return render_template('index2.html')

@app.route('/assesment')
def index3():
    return render_template('index3.html')

@app.route('/teachers')
def index4():
    return render_template('index4.html')


if __name__ == '__main__':
    app.run(debug=True)