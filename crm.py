from contact import Contact
from sys import exit 

class CRM:
  def main_menu(self):
    while True: # repeat indefinitely
      self.print_main_menu()
      user_selected = int(input()) 
      self.call_option(user_selected)

  def print_main_menu(self):
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

    print('Please enter their first name: ')
    first_name = input().lower()
    print('Please enter their last name: ')
    last_name = input().lower()
    print('Please enter their email: ')
    email = input().lower()
    print('Any notes? ')
    note = input().lower()

    Contact.create(first_name , last_name, email, note)
  
  # def modify_existing_contact(self):
  #   print("Please enter ")
  
  def delete_contact(self):
    print("\nDelete Contact\n")
    print("Please enter their ID:")
    contact_to_delete = int(input())
    print(Contact.find(contact_to_delete))
    Contact.delete(Contact.find(contact_to_delete)) 
    # print(f'{contact_to_delete}, is now deleted.')
  

  def display_all_contacts(self):
    print('All contacts:')
    for contact in Contact.contacts:
      print(contact)
  #exit()
  # def search_by_attribute(self):

a_crm_app= CRM()
a_crm_app.main_menu()
