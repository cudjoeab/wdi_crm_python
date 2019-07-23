from contact import Contact
from sys import exit 

class CRM:
  def main_menu(self):
    while True: # repeat indefinitely
      self.print_main_menu()
      user_selected = int(input()) 
      self.call_option(user_selected)

  def print_main_menu(self):
    print('\n --MAIN MENU-- \n')
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')

  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4: 
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6: 
      sys.exit() 
  
  def add_new_contact(self):
    print('\n--ADD A NEW CONTACT--')
    print('Please enter their first name: ')
    first_name = input().lower()
    print('Please enter their last name: ')
    last_name = input().lower()
    print('Please enter their email: ')
    email = input().lower()
    print('Any notes? ')
    note = input().lower()


    # Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')

    Contact.create(first_name=first_name, last_name=last_name, email=email, note=note)
  
  def modify_existing_contact(self):
    print('\n--EDIT AN EXISTING CONTACT--')
    print('Enter the ID of the user you wish to modify:')
    user_id = int(input())

    print('\nSelect from the options below:')
    print('- first_name -')
    print('- last_name -')
    print('- email -')
    print('- note -')
    

    edit_attribute = input()

    print('What are your changes?')
    edit_value = str(input())
    print('\n')
    
    if edit_attribute == 'first_name':
      query = Contact.update(first_name = edit_value).where(Contact.id == user_id)
    elif edit_attribute == 'last_name':
      query = Contact.update(last_name = edit_value).where(Contact.id == user_id)
    elif edit_attribute == 'email':
      query = Contact.update(email = edit_value).where(Contact.id == user_id)
    elif edit_attribute == 'note':
      query = Contact.update(note = edit_value).where(Contact.id == user_id)


    
    query.execute() 
    # print(Contact.update(Contact.find(user_id), edit_attribute, modify_value))
    print('\nYour changes have been made.')

  
  def delete_contact(self):
    print("\n--DELETE CONTACT--\n")
    print("Please enter their ID:")
    id = int(input())
    print(Contact.select(id))
    Contact.delete(Contact.find(id)) 
    print(f'{id}, is now deleted.')
  

  def display_all_contacts(self):
    print('\n --ALL CONTACTS--\n')
    for contact in Contact.select():
      print(f'{contact.id}: {contact.first_name} | {contact.last_name} | {contact.email} | {contact.note} ')
  
  def search_by_attribute(self):
    print('\n--SEARCH BY ATTRIBUTE--\n')
    print('\nSelect from the options below:')
    print('- first_name -')
    print('- last_name -')
    print('- email -')
    print('- note -')

    search_attribute = input()

    print('\n Enter search:\n')
    search_value = input().lower()

    print(Contact.find_by(search_attribute, search_value)) 


a_crm_app= CRM()
a_crm_app.main_menu()
