from contact import Contact

class CRM:
  # def main_menu(self):
  #
  #
  # def print_main_menu(self):
  #
  #
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
  # def display_all_contacts(self):
  #
  # def search_by_attribute(self):

test_crm = CRM()

test_crm.add_new_contact()
