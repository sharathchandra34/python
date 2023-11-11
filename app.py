from flask import Flask

app=Flask(__name__)

@app.route('/home')
def hello():
    return"hello sharath"


@app.route('/hello')
def hi():
    return 'this is 6th days'

if __name__ == '__main__':
    app.run(debug=True)