from basic import db, Puppy
from flask_sqlalchemy import SQLAlchemy


## CREATE A NEW ENTRY IN TABLE==================================
my_puppy = Puppy("Som", 4)
db.session.add(my_puppy)
db.session.commit()

## READ DATA====================================
all_puppies = Puppy.query.all()  # will return all puppies object
print(all_puppies)

# GET ONE ROW OBJECT
puppy_one = Puppy.query.get(1) 
print(puppy_one.name)

# GET BY FILTER:
pupy_franki = Puppy.query.filter_by(name='Frankie')
print(pupy_franki.all())    #  list of all the puppy having name: Frankie

# UPDATE OPERATION;...===================================
first_puppy  = Puppy.query.get(1)
first_puppy.age = 12
db.session.add(first_puppy)
db.session.commit()

# FOR DELETEING...=================================
second_pup = Puppy.query.get(3)
db.session.delete(second_pup)
db.session.commit()

# AFTER DELETEING ITEM
all_puppies = Puppy.query.all()  # will return all puppies object
print(all_puppies)




