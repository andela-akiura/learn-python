"""Code to populate sqlalchemy_example.db."""

from sqlalchemy.orm import sessionmaker
from alchemy import Address, Base, Person
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Insert a person in the person table
new_person = Person(name='Savage')
session.add(new_person)
session.commit()

# Insert an address in the address table
new_address = Address(post_code='00200', person=new_person)
session.add(new_address)
session.commit()
