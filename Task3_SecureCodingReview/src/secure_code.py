import sqlite3

def login(username, password):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create demo table
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin','admin123')")

    # ✅ Secure query using parameterized statements
    query = "SELECT * FROM users WHERE username=? AND password=?"
    print("Executing securely:", query)

    cursor.execute(query, (username, password))
    result = cursor.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    # Normal login
    print("Normal:", login("admin", "admin123"))

    # Malicious input (will fail safely)
    print("Injection attempt:", login("admin", "' OR '1'='1"))