import codecs
import sys
from signature import Signature

signature = Signature()
signature.sign()

err_msg = "You must provide an input after the argument"

def rotencode(stuffToEncode):
    res = codecs.encode(stuffToEncode, 'rot_13')
    return res

def rotdecode(encodedStuff):
    res = codecs.decode(encodedStuff, 'rot_13')
    return res

def noArgs():

    choice = input("Do you want to encrypt or decode? ")

    if choice.lower() == "encode":
        en = input("What would you like to encrypt? ")
        print(rotencode(en))
        sys.exit(0)

    elif choice.lower() == "decrypt":
        de = input("What would you like to decrypt? ")
        print(rotdecode(de))
        sys.exit(0)

    else:
        print("Sorry, I can't do that")
        sys.exit(0)

if len(sys.argv) < 2:
    noArgs()

if sys.argv[1] == '-e' or sys.argv[1] == '--encrypt':
    try:
        print(rotencode(sys.argv[2]))
    except:
        print(err_msg)

elif sys.argv[1] == '-d' or sys.argv[1] == '--decrypt':
    try:
        print(rotdecode(sys.argv[2]))
    except:
        print(err_msg)

elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("""Use:
    encode(-e, --encrypt) or decode(-d, --decrypt) ROT13.""")

else:
    print("Unknown first argument: %s" % sys.argv[1])
    print("-h or --help for more help")
