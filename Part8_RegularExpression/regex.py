import re

def checkEmail(email):
    regex = "[a-zA-Z0-9_-]+@[a-zA-Z0-9]+[.][a-zA-Z]{1,3}"
    result = re.findall(regex, email)
    return True if len(result) == 1 and len(result[0]) == len(email) else False