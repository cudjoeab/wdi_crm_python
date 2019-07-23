

class Contact:
  
  contacts = []
  next_id = 1 
  

  def __init__(self, first_name, last_name, email, note):
    """This method should initialize the contact's attributes"""
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.note = note 
    self.id = Contact.next_id 
    Contact.next_id += 1



  @classmethod
  def create(cls, first_name, last_name, email, note):
    """This method should call the initializer,
    store the newly created contact, and then return it
    """
    new_contact = Contact(first_name, last_name, email, note)
    cls.contacts.append(new_contact) 
    return new_contact 
  

  def __str__(self): 
    return f''' First name: {self.first_name}\n Last name: {self.last_name}\n Email: {self.email}\n Note: {self.note}\n ID: {self.id}\n '''

  @classmethod
  def all(cls):
    """This method should return all of the existing contacts"""
    return Contact.contacts 


  @classmethod
  def find(cls, id):
    """ This method should accept an id as an argument
    and return the contact who has that id
    """
    for contact in Contact.contacts: 
      if contact.id == id:
        return contact 

  def update(self, attribute, value):
    """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """
    setattr(self, attribute, value)
    return self



  @classmethod
  def find_by(cls, attribute, value):
    """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    """
    for contact in Contact.contacts: 
      # if contact.id == id:
      if getattr(contact, attribute) == value:
        return contact 


  @classmethod
  def delete_all(cls, contacts):
    """This method should delete all of the contacts"""
    Contact.contacts.clear()
    return contacts 





  def full_name(self,first_name):
    """Returns the full (first and last) name of the contact"""
    full_name = self.first_name + ' ' + self.last_name
    return full_name 



  def delete(self) :
    """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here
    """
    Contact.contacts.remove(self) 
    return Contact.contacts 
    

  # Feel free to add other methods here, if you need them.


contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')

# print(len(Contact.contacts))
# print(contact1.id)
# print(contact2.id) 

# print(contact1)

# print("Find 2nd - Bot")
# print(Contact.find(2))

# print("Find by first_name")
# print(Contact.find_by("first_name", "Betty"))

# print('Update contact')
# print(contact1.update('first_name', 'Bob')) 

# print('Full name')
# print(contact1.full_name('first_name')) 

# # '''call find method to select which contact will be deleted'''
# # print('Remove Contact') 
# # print(contact1.delete(Contact.find(2))) 

# # print('Delete all contacts')
# # print(Contact.delete_all(Contact.contacts)) #WHY?!?!?!?!



