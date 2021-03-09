import re
def check(mail):  return True if re.fullmatch('[a-zA-Z09.]{4,}@(([a-zA-Z09]{2,}\.)+)[a-zA-Z]{2,4}', mail) else False