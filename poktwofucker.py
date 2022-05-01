import requests
isGrkbGay = True
with open("fucking.txt", "r") as filestream:
    for line in filestream:
        fuck = {
            'field_command': 'signup_submit',
            'field_signup_email': str(line.strip()) + '@gmail.com',
            'field_signup_username': str(line.strip()),
            'field_signup_password_1': 'aaaaaa' + str(line.strip()),
            'field_signup_password_2': 'aaaaaa' + str(line.strip()),
        }
        response = requests.post('https://pok.byteemail.com/signup.php', data=fuck)
        print(response.text)
