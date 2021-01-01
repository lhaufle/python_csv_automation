'''
The AddUser class takes zero to three arguments in the custructor. 
A dictionary is added to a list. Prior values from the csv document, 
if any, will also be appended to list as dictionaries to be used by
the read_from_csv() method that is meant to be used to pass the values
to the Word_Gen class as an argument. 
'''
import csv
import os.path

class AddUser:

    field_names = ['user_name', 'address', 'email']

    #defaults sent to None in constructor to allow for zero parameters args
    def __init__(self, name = None, address = None, email = None):
        if name == None and address == None and email == None:
            self.users = []
        else:
            self.users = [{'user_name': name, 'address': address, 'email': email}]

    def read_from_csv(self):
        user_list = []
        with open('C:/Users/lhaufle/Desktop/MassDocs/user.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_list += [{'user_name': row['user_name'], 'address': row['address'], 'email': row['email']}]
        return user_list

    def write_to_csv(self):
        path = 'C:/Users/lhaufle/Desktop/MassDocs/user.csv'
        #check if file exists
        empty = os.stat(path).st_size == 0
        #open file and write or append as needed
        with open('C:/Users/lhaufle/Desktop/MassDocs/user.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.field_names)
            #if file is not showing data, then add headers to file
            if empty:
                writer.writeheader()
            writer.writerows(self.users)
