import string, random

def generatePassword():
    passwordLen = 13
    
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(passwordLen))

    
