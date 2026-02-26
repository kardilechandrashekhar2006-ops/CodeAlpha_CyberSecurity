# Task 3: Secure Coding Review

## 📌 Overview

This task audits insecure code and demonstrates secure coding practices.

---

## 🔍 Findings

- **SQL Injection Risk:** Vulnerable code concatenates user input directly into SQL query.
- **No Input Validation:** User input not sanitized.
- **Hardcoded Query:** No use of parameterized queries.

---

## ✅ Recommendations

- Use parameterized queries (Prepared Statements).
- Validate and sanitize user input.
- Apply secure coding best practices (e.g., ORM frameworks).

---

## 🎯 Conclusion

The vulnerable code shows how SQL Injection can bypass authentication.  
The secure version fixes this by using parameterized queries, preventing injection attacks.
