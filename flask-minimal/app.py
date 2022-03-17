from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Test'

@app.route('/test')
def test():
  return 'Test'

if __name__ == '__main__':
  app.run(debug=True)