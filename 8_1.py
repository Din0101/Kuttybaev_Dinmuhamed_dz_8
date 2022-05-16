import re

# не делал задания со *
def email_parse(email_address):
    parsed = re.findall(r'(^\w+)@((\w+).(\w{2,}))$', email_address)
    if not parsed:
        raise ValueError(f"wrong email: {email_address}")
    return dict(zip(["username", "domain"], parsed[0]))


print(email_parse("ffff@fglgf.ru"))
