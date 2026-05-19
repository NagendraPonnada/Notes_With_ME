import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='root', port=3306)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS notes_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    conn.commit()
    cursor.close()
    conn.close()
    print("SUCCESS: Database 'notes_db' created or already exists.")
except Exception as e:
    print(f"FAILED: {e}")
