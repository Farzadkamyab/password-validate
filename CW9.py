import re

def passwd_validate(password:str):
    password = str(password)

    pattern = re.compile("^(?=.*[a-z])(?=.*[a-z])(?=.*/d)[A-Zz-z\d@$!#%*?&]{8,}$")
    
    if re.match(pattern, password):
        print('valid')
    else:
        print('invalid')

if __name__ == '__main__':
    passwd = "Farzad021"
    print(passwd_validate(passwd))