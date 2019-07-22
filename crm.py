from contact import Contact

class CRM:
  # def main_menu(self):
  #   while True: # repeat indefinitely
  #     self.print_main_menu()
  #     user_selected = int(input())
  #     self.call_option(user_selected)

  # def print_main_menu(self):
  #   print('[1] Add a new contact')
  #   print('[2] Modify an existing contact')
  #   print('[3] Delete a contact')
  #   print('[4] Display all the contacts')
  #   print('[5] Search by attribute')
  #   print('[6] Exit')
  #   print('Enter a number: ')

  # def call_option(self):
  #
  #

   def add_new_contact(self):

     print('Please enter their first name: ')
     new_first_name = 'Abigail'
     print('Please enter their last name: ')
     new_last_name = 'Cudjoe'
     print('Please enter their email: ')
     new_email = 'cudjoeab@gmail.com'
     print('Any notes?')
     new_note = 'the most confused right now '

     
     new_contact = new_first_name , new_last_name, new_email, new_note 
     Contact.create(new_first_name , new_last_name, new_email, new_note)
     print(new_contact)
     return new_contact 
     
  
  # def modify_existing_contact(self):
  #
  #
  # def delete_contact(self):
  #
  #
   def display_all_contacts(self):
    print('All contacts:')
    for contact in Contact.contacts:
      print(contact)
  #
  # def search_by_attribute(self):

test_crm = CRM()

test_crm.add_new_contact()
