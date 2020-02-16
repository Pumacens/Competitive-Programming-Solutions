import re

def validate_usr(username):
    if 4 <= len(username) <= 16:
        return not bool(re.search(r'[^0-9a-z_]', username))
        
    return False
    


# def validate_usr(username):
#     return bool(re.match(r'^[a-z0-9_]{4,16}$', username))