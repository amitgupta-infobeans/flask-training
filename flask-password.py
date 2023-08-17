from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


password = "superadminpassword"
hashed_password = bcrypt.generate_password_hash(password = password)
# print(hashed_password)
chekk = bcrypt.check_password_hash(hashed_password, 'superadminpassword')
# print(chekk)




