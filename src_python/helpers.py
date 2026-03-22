# helpers.py

def get_quote(s):
    ''' get substr between first and last " '''
    return s[s.find("\"")+1:s.rfind("\"")]

def get_int_list(s):
    ''' get int list after : '''
    lst = list(map(int, s.split(":")[1].strip().split()))
    return lst 

def get_hex_list(s):
    ''' get hex list after : '''
    lst = list(map(lambda x: int(x, 16), s.split(":")[1].strip().split()))
    return lst 

def is_null_token(s):
    ''' ignore tokens that are all periods or spaces '''
    for c in s:
        if c != "." and c != " ":
            return False
    return True 

def get_token_key(pat, row, col):
    ''' for track.tokens lookup and insertion '''
    return "pat={}::row={}::col={}".format(pat, row, col)
