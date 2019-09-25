from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def serve_index():
    return "Index"

@app.route('/Hello')
def sever_Hello():
    return "Hello to flask tutorials:"

@app.route('/hello1')
def server_hello():
    return render_template('hello.html') 

#@app.route('/post/<post_id>')
#def  server_post(post_id):
 #   return "This is post: "+ post_id

@app.route('/post/<post_id>')
def  server_post(post_id):
    return render_template('post.html',id= post_id)

@app.route('/login')
def server_login():
    return render_template('login.html') 

@app.route('/auth',methods = ['POST'])
def login_check():
    username =request.form['username']
    password =request.form['password']

    if username=='abc' and password =='1234':
        return render_template('auth.html',action = True)
    else:
        return render_template('auth.html',action =False)

if __name__=='__main__':
     app.run(port =8070,debug= True) 
 