from flask import Flask
app = Flask(__name__)


@app.route('/test')
def test(): 
    print('test---start')   
    return {'result': 'test'}


if __name__ == '__main__':
  app.run()