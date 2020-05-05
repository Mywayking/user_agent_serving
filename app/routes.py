from flask import render_template, request
from app import app
from app import models
from app import db
from app import identify

# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
# handler = logging.FileHandler("log.txt")
cu = identify.UaIdentify()
cu.load_data()


@app.route('/user_agent/')
@app.route('/user_agent/index')
def index():
    ua = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=ua)


@app.route('/user_agent/get_ua', methods=['GET', 'POST'])
def user_agent():
    if request.method == 'POST':
        device_ua = models.DeviceUa(user_agent=request.form['hidden_ua'],
                                    brand=request.form['brand'])
        db.session.add(device_ua)  # 添加到数据库
        # db.session.commit()  # 提交到数据库
        return render_template("user_agent.html")
    else:
        ua = request.headers.get('User-Agent')
        return render_template('index.html', title='Home', user_agent=ua)


@app.route('/user_agent/identify')
def device_identify():
    ua = request.headers.get('User-Agent')
    print(ua)
    # logger.info(ua)
    output_data = cu.identify(ua)
    if output_data is None:
        return
    return render_template('identify.html', user_agent=ua, output_data=output_data)

# @app.route('/login', methods=['POST'])
# def login():
#     uid = request.form['uid']
#     pwd = request.form['pwd']
#     system = request.form['system']
#     if uid == 'admin' and pwd == 'admin' and system == 'CRM':
#         return 'Authorized successfully!'
#     else:
#         return 'Un-Autorized!'
