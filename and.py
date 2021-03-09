def check(mail):
    pat = str(r' ,:;!#%*()=+{}[]:"' + r"'/\|")
    if mail.count('@') != 1:
        return False
    for i in mail:
        if i in  pat: 
            return False
        if not i.isalpha() and i != '@' and i != '.' and not i.isdigit():
            return False
    if not ('.' in mail.split('@')[-1]):
        return False
    if not (2<=len(mail.split('@')[-1].split('.')[-1])<=4 ):
        return False
    for i in mail.split('@')[-1].split('.')[-1]:
        if i.isdigit():
            return False
    if len(mail[mail.find("@"):mail.rfind(".")]) < 2:
        return False
    if len(mail.split('@')[0]) < 4:
        return False
    return True
