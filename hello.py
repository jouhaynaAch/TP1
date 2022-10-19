from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return 'welcome to my website made with flask!'

if __name__=='__main__':
    app.run()

    