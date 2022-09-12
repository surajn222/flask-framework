from flask import Flask, render_template
from requests import get
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello_world():
  return get(f'http://www.google.com').content
  #return 'Test'

@app.route('/<path>')
def hello_world_2(path):
  path = path.replace("|","/")
  return get('http://' + path).content

@app.route('/test2/<path>')
def hello_world_3(path):
  from pywebcopy import save_webpage

  url = 'http://' + path
  download_folder = '/Users/snathani/PycharmProjects/flask-framework/flask-minimal/tmp/webpage/'

  kwargs = {'bypass_robots': True, 'project_name': 'webpages'}

  save_webpage(url, download_folder, **kwargs)
  return render_template('tmp/webpage/webpages/colormind.io/index.html')
  #return app.send_static_file("/tmp/webpage/webpages" + path)

  #return "True"
import stat
@app.route('/browser/<path:urlFilePath>')
def browser(urlFilePath):
    nestedFilePath = os.path.join("/", urlFilePath)
    nestedFilePath = nestedFilePath.replace("/", "\\")
    if os.path.realpath(nestedFilePath) != nestedFilePath:
        return "no directory traversal please."
    if os.path.isdir(nestedFilePath):
        itemList = os.listdir(nestedFilePath)
        fileProperties = {"filepath": nestedFilePath}
        if not urlFilePath.startswith("/"):
            urlFilePath = "/" + urlFilePath
        return render_template('browse.html', urlFilePath=urlFilePath, itemList=itemList)
    if os.path.isfile(nestedFilePath):
        fileProperties = {"filepath": nestedFilePath}
        sbuf = os.fstat(os.open(nestedFilePath, os.O_RDONLY)) #Opening the file and getting metadata
        fileProperties['type'] = stat.S_IFMT(sbuf.st_mode)
        fileProperties['mode'] = stat.S_IMODE(sbuf.st_mode)
        fileProperties['mtime'] = sbuf.st_mtime
        fileProperties['size'] = sbuf.st_size
        if not urlFilePath.startswith("/"):
            urlFilePath = "/" + urlFilePath
        return render_template('file.html', currentFile=nestedFilePath, fileProperties=fileProperties)
    return 'something bad happened'

@app.route('/test')
def test():
  dir = os.getcwd()
  path = '/tmp/webpage/webpages/colormind.io/index.html'
  print(dir + path)
  #return dir + path
  #return dir
  return render_template('/tmp/webpage/webpages/colormind.io/index.html')
  #return 'Test1'

if __name__ == '__main__':
  app.run(debug=True)