from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='thumuc')


# Kết nối cơ sở dữ liệu
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Trang chủ hiển thị form đăng nhập
@app.route('/')
def home():
    return render_template('login.html')

# Xử lý đăng nhập
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    user = conn.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'").fetchone()


    if user:
        return redirect(url_for('dashboard'))
    else:
        return 'Tên đăng nhập hoặc mật khẩu không chính xác', 401

# Trang dashboard sau khi đăng nhập thành công
@app.route('/dashboard')
def dashboard():
    return 'Chào mừng bạn đến với trang web của nhóm 8!'

if __name__ == '__main__':
    app.run(debug=True)

