"""
-------------------------------------------------
   Author :       galen
   date：          2018/3/14
-------------------------------------------------
   Description:chmod a+x run.py
-------------------------------------------------
"""
from app import app

app.run(host='0.0.0.0', debug=False)
# app.run(host='0.0.0.0', port=8082, debug=False)
