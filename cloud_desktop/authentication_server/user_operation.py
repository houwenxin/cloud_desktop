import encryptionAES
import os

def check_valid(string):
    for letter in string:
        if letter == ":":
            return False
    return True

def find_current_user(username):
    f = open("user", "r+")
    allLine = f.readlines()
    for eachline in allLine:
        user = eachline.split(":")[0]
        if(user == username):
            f.close()
            return False
    f.close()
    return True

def create_new_user(username, iv, ciphertext):
    if(check_valid(username)==False or check_valid(iv)==False or check_valid(ciphertext)==False):
        return "Invalid"
    if(find_current_user(username) == False):
        return False
    f = open("user", 'r+')
    f.seek(0, 2)
    f.write(username + ":" + iv + ":" + ciphertext + os.linesep)
    f.close()
    return True

def delete_user(username, password):
    if(find_current_user(username) == True):
        return False
    identity = encryptionAES.certificate(username, password)
    if(identity[0] == False):
        return False
    else:
        f = open('user', 'r+')
        allLine = f.readlines()
        f.close()
        f = open('user', 'w+')
        current_line = 1
        for eachline in allLine:
            if(current_line != identity[1]):
                f.write(eachline)
            current_line += 1
        f.close()
        return True    
