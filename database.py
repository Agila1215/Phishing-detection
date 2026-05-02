 
import sqlite3
from datetime import datetime

def init_database():
    conn = sqlite3.connect('qr_shield.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT,
            full_name TEXT,
            created_at TIMESTAMP,
            last_login TIMESTAMP,
            is_admin BOOLEAN DEFAULT 0,
            status TEXT DEFAULT 'active'
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scan_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            qr_data TEXT,
            qr_type TEXT,
            result TEXT,
            risk_score REAL,
            confidence REAL,
            scan_time TIMESTAMP,
            ip_address TEXT,
            device_info TEXT,
            location TEXT,
            share_count INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_id INTEGER,
            action TEXT,
            target_user TEXT,
            details TEXT,
            timestamp TIMESTAMP,
            FOREIGN KEY (admin_id) REFERENCES users (id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS model_performance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT,
            accuracy REAL,
            precision REAL,
            recall REAL,
            f1_score REAL,
            timestamp TIMESTAMP
        )
    ''')
    
    # Create default admin user if not exists
    cursor.execute("SELECT * FROM users WHERE email = 'qrcodeprojectphishing@gmail.com'")
    if not cursor.fetchone():
        import hashlib
        hashed_password = hashlib.sha256('Qrcode@123'.encode()).hexdigest()
        cursor.execute('''
            INSERT INTO users (username, email, password, full_name, created_at, is_admin)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('admin', 'qrcodeprojectphishing@gmail.com', hashed_password, 'Administrator', datetime.now(), 1))
    
    conn.commit()
    conn.close()