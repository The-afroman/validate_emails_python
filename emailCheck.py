from validate_email import validate_email
import csv

valid_email_list = []
invalid_email_list = []

with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i in readCSV:
        email = i[0]
        #print(email)
        is_valid = validate_email(email , verify=True)
        if is_valid is None:
            print(email + " VALID!")
            valid_email_list.append(email)
        else:
            print (email + " INVALID!")
            invalid_email_list.append(email)

with open('valid.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['VALID_EMAILS'])
    for i in valid_email_list:
        writer.writerow([i])

with open('invalid.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['INVALID_EMAILS'])
    for i in invalid_email_list:
        writer.writerow([i])







