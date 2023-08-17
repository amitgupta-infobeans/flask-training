from werkzeug.security import generate_password_hash, check_password_hash


hashed_pwd = generate_password_hash('mynewpassword')
print(hashed_pwd)
check = check_password_hash(hashed_pwd, 'mynewpassword')
print(check)