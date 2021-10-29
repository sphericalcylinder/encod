import codecs
choice = input("Do you want to encode or decode? ")

def rotencode(stuffToEncode):
    res = codecs.encode(stuffToEncode, 'rot_13')
    return res

def rotdecode(encodedStuff):
    res = codecs.decode(encodedStuff, 'rot_13')
    return res

if choice.lower() == "encode":
    en = input("What would you like to encode? ")
    print(rotencode(en))

elif choice.lower() == "decode":
    de = input("What would you like to decode? ")
    print(rotdecode(de))

else:
    print("Sorry, I can't do that")
