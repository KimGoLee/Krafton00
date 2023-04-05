from flask import url_for,session, Flask, render_template, jsonify,request,redirect
from pymongo import MongoClient 
from bson import ObjectId
app = Flask(__name__)

app.secret_key="kraftonjongle_blue02"

client = MongoClient('localhost',27017)
db = client.krafton   

@app.route('/')
def home():
   return render_template('login.html')

# 회원가입
@app.route('/save',methods=['POST'])
def save():
   name = request.form['give_name']
   phnum = request.form['give_phnum']
   room = request.form['give_room']
   team = request.form['give_team']
   email = request.form['give_email']
   pw = request.form['give_pw']
   blog = request.form['give_blog']
   user_info = {
      'name':name,
      'phnum':phnum,
      'room':room,
      'team':team,
      'email':email,
      'pw':pw,
      'blog':blog
   }
   db.test.insert_one(user_info);
   return jsonify({'result': 'success'})

# 로그인
@app.route('/login',methods=['POST'])
def login():
   email = request.form['give_email']
   password = request.form['give_password']
   all_data = db.test.find();

   for data in all_data:
      if email == data['email'] and password == data['pw']:
          user_id = str(data['_id']);
          session[user_id] = user_id;
          return jsonify({'result': 'success','user_id':user_id})
   return jsonify({'result': 'fail'})

# main
@app.route('/main')
def main():
   return render_template("main.html")

# logout
@app.route('/logout',methods=['POST'])
def logout():
   session.pop(request.form['give_user_id'])
   return jsonify({'result':'success'})



if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)