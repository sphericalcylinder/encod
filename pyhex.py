import binascii as basc

choice = input("Would you like to encode or decode? ")

def hexencode(toencode):
    done = []
    done.append(basc.hexlify(bytes(toencode, 'utf_8')))
    return done

def hexdecode(todecode):
    done = []
    decoded = bytes.fromhex(todecode)
    decoded = decoded.decode("ascii")
    done.append(decoded)
    return done

if choice.lower() == "encode":
    en = input("What would you like to encode? ")
    print(hexencode(en))

elif choice.lower() == "decode":
    de = input("What would you like to decode? ")
    print(hexdecode(de))

else:
    print("I can't do that")
