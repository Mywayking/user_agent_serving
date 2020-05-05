"""
-------------------------------------------------
   Author :       galen
   date：          2018/3/14
-------------------------------------------------
   Description:
-------------------------------------------------
"""
from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def v_index():
    return '''
        <form action="/login" method="POST">
            <input type="text" name="system" placeholder="input your system id"> <br />
            <input type="text" name="uid" placeholder="input your user id"> <br />
            <input type="password" name="pwd" placeholder="input your password"> <br />
            <input type="submit" value="Login">
        </form>
    '''


@app.route('/login', methods=['POST'])
def v_login():
    uid = request.form['uid']
    pwd = request.form['pwd']
    system = request.form['system']
    if uid == 'admin' and pwd == 'admin' and system == 'CRM':
        return 'Authorized successfully!'
    else:
        return 'Un-Autorized!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
