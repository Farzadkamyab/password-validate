import re

def passwd_validate(password:str):
    password = str(password)

    pattern = re.compile("^(?=.*[a-z])(?=.*[a-z])(?=.*/d)[A-Zz-z\d@$!#%*?&]{8,}$")
    return bool(pattern.match(password))

if __name__ == '__main__':
    passwd = "Farzad021"
    print(passwd_validate(passwd))