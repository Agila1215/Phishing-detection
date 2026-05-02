 
import sqlite3
import hashlib
from datetime import datetime
from backend.email_service import send_email_notification, notify_admin

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed):
    return hash_password(password) == hashed

def create_user(username, email, password, full_name):
    conn = sqlite3.connect('qr_shield.db')
    cursor = conn.cursor()
    try:
        hashed = hash_password(password)
        cursor.execute('''
            INSERT INTO users (username, email, password, full_name, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, email, hashed, full_name, datetime.now()))
        conn.commit()
        
        user_message = f"""Hello {full_name},

🎉 Thank you for registering with AI QR Shield!

Your account has been created successfully.
You can now log in and start scanning QR codes securely.

Account Details:
- Username: {username}
- Email: {email}
- Registered: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Stay safe from phishing attacks!

Best regards,
AI QR Shield Team
"""
        send_email_notification(email, "🎉 Welcome to AI QR Shield!", user_message)
        notify_admin("REGISTERED", email, full_name)
        
        return True, "Registration successful!"
    except sqlite3.IntegrityError:
        return False, "Username or email already exists!"
    finally:
        conn.close()

def authenticate_user(email, password):
    conn = sqlite3.connect('qr_shield.db')
    cursor = conn.cursor()
    hashed = hash_password(password)
    cursor.execute('''
        SELECT * FROM users WHERE email = ? AND password = ?
    ''', (email, hashed))
    user = cursor.fetchone()
    if user:
        cursor.execute('''
            UPDATE users SET last_login = ? WHERE id = ?
        ''', (datetime.now(), user[0]))
        conn.commit()
        
        user_message = f"""Hello {user[4]},

🔐 You have successfully logged into your AI QR Shield account.

Login Details:
- Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- Email: {email}

If this wasn't you, please contact support immediately.

Stay safe!
AI QR Shield Team
"""
        send_email_notification(email, "🔐 New Login to AI QR Shield", user_message)
        notify_admin("LOGGED IN", email, user[4])
        
        user_dict = {
            'id': user[0],
            'username': user[1],
            'email': user[2],
            'full_name': user[4],
            'created_at': user[5],
            'last_login': user[6],
            'is_admin': user[7],
            'status': user[8]
        }
        conn.close()
        return True, user_dict
    conn.close()
    return False, None