from basic import db, Puppy

# create all the tables in the database

db.create_all()


sam = Puppy('Sammy', 3)
frak = Puppy('Frankie', 5)


print(sam.id)
print(frak.id)

db.session.add_all([sam, frak])
# or you can add like this:  
# db.session.add(sam)
# db.session.add(frak)

db.session.commit()

print(sam.id)
print(frak.id)
