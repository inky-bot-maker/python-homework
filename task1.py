users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30, "email": "charlie@example.com"},
    {"name": "David", "email": "david@example.com"},
]

adults = [u["name"] for u in users if u.get("age", 0) >= 18 and "email" in u]
print(adults)  # ['Alice', 'Charlie']
