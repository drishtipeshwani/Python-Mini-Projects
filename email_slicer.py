email = input("Enter your email address").strip()

user_name = email[:email.index('@')]
domain_name = email[email.index('@')+1:]

print('Your username is' + " " + user_name)

print('Your domain name is' + " "+ domain_name)