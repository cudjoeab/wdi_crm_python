from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')

class Contact(Model):
  first_name = CharField()
  last_name = CharField()
  email = CharField()
  note = TextField()

  def full_name(self,first_name):
    """Returns the full (first and last) name of the contact"""
    full_name = self.first_name + ' ' + self.last_name
    return full_name 

db.connect()
db.create_tables([Contact])  
