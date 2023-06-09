import os
from flask import url_for,session, Flask, render_template, jsonify,request,redirect,send_from_directory
from pymongo import MongoClient 
from bson import ObjectId
app = Flask(__name__)

app.secret_key="kraftonjongle_blue02"

client = MongoClient('localhost',27017)
db = client.krafton   


 
@app.route('/')
def home():
   return render_template('login.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

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
   time = 0;
   user_info = {
      'name':name,
      'phnum':phnum,
      'room':room,
      'team':team,
      'email':email,
      'pw':pw,
      'blog':blog,
      'time': time
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
          print('user_id : ' + user_id)
          print('session[user_id] : '+session[user_id])
                
          return jsonify({'result': 'success','user_id':user_id})
   return jsonify({'result': 'fail'})

# main
@app.route('/main')
def main():
   user_id = request.args['user_id'];
   if user_id not in session:
      print("Login first!")
      return redirect(url_for('home'))



   color_list=[]
   all_users = db.test.find({})
   user_info = db.test.find_one({'_id':ObjectId(user_id)});
   name = user_info['name']
   email = user_info['email']
   phnum=user_info['phnum']
   room = user_info['room']
   team = user_info['team']
   blog = user_info['blog']
   hour = int(user_info['time'])//3600
   minute = int(user_info['time'])//60
   second = int(user_info['time'])%60

   if hour < 10:
      hour = '0'+str(hour)
   if minute < 10:
      minute = '0'+str(minute)
   if second < 10:
      second = '0'+str(second)

   for user in all_users :
      if user['team'] == team:
         color_list.append(user)

   color_list.sort(key=lambda x:-int(x['time']))

   total = len(color_list)
   ranking = 0;

   for i in range(len(color_list)):
      if user_id == str(color_list[i]['_id']):
         ranking = i+1;
         break
         
   img_url = './static/images/'+email+'.jpg';
   

   return render_template("main.html",name=name,email=email,phnum=phnum,room=room,team=team,blog=blog,hour=hour,minute=minute,second=second,total=total,ranking=ranking,img_url=img_url)

# logout
@app.route('/logout',methods=['POST','GET'])
def logout():
   session.pop(request.form['give_user_id'])
   return jsonify({'result':'success'})

# get : 사용자의 정보 가져오기
@app.route('/user_info',methods=['POST'])
def user_info():
   id = request.form['give_user_id']
   user_info = db.test.find_one({'_id':ObjectId(id)});
   return jsonify({'result':'success','name':user_info['name'],'phnum':user_info['phnum'], 'room': user_info['room'],'team':user_info['team'],'email':user_info['email'],'blog':user_info['blog'],'time':user_info['time'],'hour':int(user_info['time'])//3600,'min':int(user_info['time'])//60})

# open_rank : 랭크페이지로 이동
@app.route('/rank')
def rank():

   user_id = request.args['user_id'];
   if user_id not in session:
      print("Login first!")
      return redirect(url_for('home'))
   
   print("user_id : " + user_id)
   for i in session:
      print(i)
   if user_id not in session:
      print("Login!")
      return redirect(url_for('home'))
   

   redList=[];
   greenList=[];
   blueList=[];
   all_user_data=db.test.find({});

   for user in all_user_data :
      hour = int(user['time'])//3600
      minute = int(user['time'])//60
      second = int(user['time'])%60
      if hour < 10:
         hour = '0'+str(hour)
      if minute < 10:
         minute = '0'+str(minute)
      if second < 10:
         second = '0'+str(second)
      
      if user['team'] == 'red':
         user['time']=int(user['time']);
         redList.append({'user_id':str(user['_id']),'name': user['name'],'hour':hour,'min':minute,'time':user['time'],'second':second});
      elif user['team'] == 'green':
         user['time']=int(user['time']);
         greenList.append({'user_id':str(user['_id']),'name': user['name'],'hour':hour,'min':minute,'time':user['time'],'second':second});
         #greenList.append({'user_id':str(user['_id']),'name': user['name'],'hour':user['time']//3600,'min':user['time']//60,'time':user['time']});
      elif user['team']=='blue':
         user['time']=int(user['time']);
         blueList.append({'user_id':str(user['_id']),'name': user['name'],'hour':hour,'min':minute,'time':user['time'],'second':second});
         #blueList.append({'user_id':str(user['_id']),'name': user['name'],'hour':user['time']//3600,'min':user['time']//60,'time':user['time']});
   
   redList.sort(key=lambda x:-x['time'])
   greenList.sort(key=lambda x:-x['time'])
   blueList.sort(key=lambda x:-x['time'])
   return render_template('rank.html',redList=redList,greenList=greenList,blueList=blueList)

# update_time : 시간을 업데이트
@app.route('/update_time',methods=['POST'])
def update_time():
   id = request.form['give_user_id']
   time = request.form['give_time']
   new_time = int(db.test.find_one({'_id':ObjectId(id)})['time'])+int(time);
   db.test.update_one({'_id':ObjectId(id)},{'$set':{'time':new_time}})
   
   return jsonify({'result':'success'})


@app.route('/upload', methods=['POST'])
def upload():
    # Get the file from the request
    file = request.files['image']
    # Save the file to the images folder
    file.save('./static/images/' + file.filename)

    return 'File uploaded successfully'


# main session 종료와 시간 저장
@app.route('/main_close', methods=['POST'])
def main_close():
   id = request.form['give_user_id']
   time = request.form['give_time']
   login = request.form['give_login']
   new_time = int(db.test.find_one({'_id':ObjectId(id)})['time'])+int(time);
   db.test.update_one({'_id':ObjectId(id)},{'$set':{'time':new_time}})


   return 'close'




   


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)