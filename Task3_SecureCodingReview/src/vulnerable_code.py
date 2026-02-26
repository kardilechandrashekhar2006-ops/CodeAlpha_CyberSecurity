import sqlite3

def login(username, password):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create demo table
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin','admin123')")

    # ❌ Vulnerable query (SQL Injection possible)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Executing:", query)

    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    # Normal login
    print("Normal:", login("admin", "admin123"))

    # Malicious input
    print("Injection:", login("admin", "' OR '1'='1"))