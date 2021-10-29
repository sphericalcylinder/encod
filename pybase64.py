import base64

choice = input("Would you like to encode or decode? ")

def base64encode(toencode):
    done = []
    done.append(base64.b64encode(bytes(toencode, 'utf_8')))
    return done

def base64decode(todecode):
    done = []
    done.append(base64.b64decode(bytes(todecode, 'utf_8')))
    return done

if choice.lower() == 'encode':
    en = input("What would you like to encode? ")
    print(base64encode(en))

elif choice.lower() == 'decode':
    de = input("What would you like to decode? Include the padding. ")
    print(base64decode(de))

else:
    print("I can't do that")
