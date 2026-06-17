
user ={
    "name": "John",
    "password": "1234",
    "email": "john@example.com",
    "address": "123 Main St",
    "country": "USA"
}
senitive_keys = input("Enter sensitive keys (comma-separated): ").split(",")
    
for i in senitive_keys:
    if i in user:
        print(f"{i} is a sensitive key and its value is: {user[i]}")
        user.pop(i)
    else:
        print(f"{i} is not a sensitive key")
print(user)

