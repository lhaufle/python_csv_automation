import csv
import os.path

class AddUser:

    field_names = ['user_name', 'address', 'email']

    def __init__(self, name = None, address = None, email = None):
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