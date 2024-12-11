'''
Signup for website using username and password

USERNAME REQUIREMENTS

Start with a lowercase, only contain letters, numbers, & underscores
Not be in provided taken usernames list
taken usernames are  'admin', 'admin123', 'user', 'superuser'

if requirements not met print either "Invalid username", or "username taken", 
based on the context & continue looping.

PASSWORD REQUIREMENTS
8 characters long
One Uppercase
One lowercase
One digit
Contain at least one special character !,@,#,$,^,&,*,_,-,
NO spaces

If the password doesn't meet the requirement print "Invalid Password"
contnue looping

Project requirements
NO Functions 
No AI generated code
Done in One While Loop
No extra error messages
code must be clean & readable, remove print stmts used during development and testing

if username and password meet requirements print"Sign up successful"
Now have user sign into website using username and password they created

If username and password are valid print "Login successful"
If either oe doesn't match print "Incorrect username or password" and continue looping

'''

# initalize variable
username = ''
password = ''
taken_usernames = ['admin', 'admin123', 'user', 'superuser']


# error messages
msgs = ('Login succesful', 'Sign up successful','Invalid username', 'username taken', 'Invalid Password','Incorrect username or password')
login_successful = msgs[0]
sign_up_successful = msgs[1]
invalid_username = msgs[2]
username_taken = msgs[3]
invalid_pw = msgs[4]
both_incorrect = msgs[5]

# user instructions
print(''' Please create a username and password for your account.  The username must meet the following requirement: 
      - Start with a lowercase, only contain letters, numbers, & underscores. PASSWORD REQUIREMENTS
8 characters long
One Uppercase
One lowercase
One digit
Contain at least one special character !,@,#,$,^,&,*,_,-,
NO spaces''')


# start loop 
while True:
    
    # Get username
    username = input("Please create a username for your account: ")
    
       
    # Check if username is in taken list
    if username in taken_usernames:
        print(username_taken)
        break    
    #Check if username has only letters,numbers, and or underscores
    if username.isidentifier():
        # Get password
        password = input("Please create a password: ")
        
    else:
        print(invalid_username)
        continue
    # check if pw len=8, 1 uppercase, 1 lowercase,1 number,1 symbol
    
    # check length of password
    length = len(password) == 8
    
    # check for alphanumberic
    alphanumeric = password.isalnum() == False
        
    # check for at leaast one uppercase letter
    uppercase = password != password.lower()
    
    # check for whitespace
    contain_spaces = password.count(' ') == 0 
    
    # check for password requirements
    valid_password = (length and alphanumeric and uppercase and contain_spaces) 
          
    if valid_password == False:
        print(invalid_pw)
                        
    else:
        print(sign_up_successful)
        print("Please log in using your username and password")
        login_username = input("Please enter your username: ")
        login_password = input("Please enter your password: ")
        if login_username == username and login_password == password:
            print(login_successful)
            break
        else:
            print("Incorrect username and password") 





