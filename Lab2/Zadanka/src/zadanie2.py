def validate_email(email):
    malpa = 0
    miejsce = email.find("@") + 1
    domeny = ["wp.pl", "interia.pl", "gmail.com"]
    for i in email:
        if i == "@":
            malpa = 1 + malpa
    if malpa == 1:
        for i in domeny:
            if email[miejsce:len(email)] == i:
                return True
    return False