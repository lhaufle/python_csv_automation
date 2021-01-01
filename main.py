from add_user import AddUser
from word_gen import Word_Gen

def menu():
    ##check if user wants to add to the user list
    print('A)Add a User \n' +
          'G)Generate Messages \n' +
          'Q)Quit'
          '---------------------')
    ##get user input
    response = input('Please Select an option:').upper()

    return response

users = AddUser()

#word_gen.gen_messages("The only thing you contribute to your salvation is the sin that made it necessary J.E.")

response = menu()

#get new user info
if response == 'A':
    user_name = input("Please enter the users first and last name:")
    address = input("please enter the user's address")
    email = input("Please enter the user's email")

    #add validation later
    users = AddUser(user_name, address, email)
    users.write_to_csv()
elif response == 'G':
    word_gen = Word_Gen(users.read_from_csv())
    message = input("What message would you like to send:")
    word_gen.gen_messages(message)
else:
    print("BYE")

































