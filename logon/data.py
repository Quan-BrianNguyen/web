import sqlite3

def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Tạo bảng users nếu chưa có
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )''')

    # Thêm một người dùng ví dụ (nếu bạn muốn có sẵn tài khoản để đăng nhập thử)
    c.execute("INSERT INTO users (username, password) VALUES ('admin','123')")
    c.execute("INSERT INTO users (username, password) VALUES ('quan','123' )" )


    

    conn.commit()
    conn.close()

create_db()
