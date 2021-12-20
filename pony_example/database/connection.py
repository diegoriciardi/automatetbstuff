from pony.orm import *   

db = Database(
        provider='mysql',
        user='example',     
        host='example',       
        passwd='example',    
        db='example'  
     )

class Person(db.Entity):
        name = Required(str)
        age = Required(int)
        cars = Set('Car')

class Car(db.Entity):
        make = Required(str)
        model = Required(str)
        owner = Required('Person')

set_sql_debug(False)

db.generate_mapping(create_tables=False)
