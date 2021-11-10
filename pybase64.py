import sys
import base64
from signature import Signature

signature = Signature()
signature.sign()

err_msg = "You must provide an input after the argument"

def base64encode(toencode):
    done = []
    done.append(base64.b64encode(bytes(toencode, 'utf_8')))
    return done

def base64decode(todecode):
    done = []
    done.append(base64.b64decode(bytes(todecode, 'utf_8')))
    return done

def noArgs():
    choice = input("Would you like to encode or decode? ")
    if choice.lower() == 'encode':
        en = input("What would you like to encode? ")
        print(base64encode(en))
        sys.exit(0)

    elif choice.lower() == 'decode':
        de = input("What would you like to decode? Include the padding. ")
        print(base64decode(de))
        sys.exit(0)

    else:
        print("I can't do that")
        sys.exit(0)


if len(sys.argv) < 2:
    noArgs()

if sys.argv[1] == '-e' or sys.argv[1] == '--encode':
    try:
        print(base64encode(sys.argv[2]))
    except:
        print(err_msg)

elif sys.argv[1] == '-d' or sys.argv[1] == '--decode':
    try:
        print(base64decode(sys.argv[2]))
    except:
        print(err_msg)

elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("""Use:
    encode(-e, --encode) or decode(-d, --decode) base64.""")

else:
    print("Unknown first argument: %s" % sys.argv[1])
    print("-h or --help for more help")
