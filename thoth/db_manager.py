# db_manager.py

import os
import sqlite3
from .constants import THOTH_DIR

DB_PATH = os.path.join(THOTH_DIR, 'thoth_storage.db')

def ensure_db_exists():
    if not os.path.exists(DB_PATH):
        create_db()

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Creating Files table
    cursor.execute('''
    CREATE TABLE Files (
        file_id TEXT PRIMARY KEY, 
        original_name TEXT, 
        backup_time TIMESTAMP, 
        user TEXT, 
        sha256_sum TEXT, 
        backup_path TEXT, 
        file_size INTEGER, 
        compression_algo TEXT, 
        encryption_algo TEXT
    )
    ''')

    # Creating Chunks table
    cursor.execute('''
    CREATE TABLE Chunks (
        chunk_id TEXT PRIMARY KEY, 
        file_id TEXT, 
        chunk_path TEXT, 
        FOREIGN KEY (file_id) REFERENCES Files(file_id)
    )
    ''')

    conn.commit()
    conn.close()

ensure_db_exists()
