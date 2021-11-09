import sys
from signature import Signature
import binascii as basc

signature = Signature()
signature.sign()

err_msg = "You must provide an input after the argument"


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

def noArgs():
    choice = input("Would you like to encode or decode? ")

    if choice.lower() == "encode":
        en = input("What would you like to encode? ")
        print(hexencode(en))
        sys.exit(0)

    elif choice.lower() == "decode":
        de = input("What would you like to decode? ")
        print(hexdecode(de))
        sys.exit(0)

    else:
        print("I can't do that")
        sys.exit(0)

if len(sys.argv) < 2:
    noArgs()

if sys.argv[1] == '-e' or sys.argv[1] == '--encode':
    try:
        print(hexencode(sys.argv[2]))
    except:
        print(err_msg)

elif sys.argv[1] == '-d' or sys.argv[1] == '--encode':
    try:
        print(hexdecode(sys.argv[2]))
    except:
        print(err_msg)

elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("""Use:
    encode(-e, --encode) or decode(-d, --decode) hexadecimal.""")

else:
    print("Unknown first argument: %s" % sys.argv[1])
    print("-h or --help for more help")

