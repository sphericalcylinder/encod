import sys
import base64


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
    if choice.lower().startswith == 'e':
        en = input("What would you like to encode? ")
        print(base64encode(en))
        sys.exit(0)

    elif choice.lower().startswith == 'd':
        de = input("What would you like to decode? Include the padding. ")
        print(base64decode(de))
        sys.exit(0)

    else:
        print("I can't do that")
        sys.exit(0)


print(sys.argv)

if len(sys.argv) < 2:
    noArgs()

if sys.argv[1] == '-e':
    print(base64encode(sys.argv[2]))

elif sys.argv[1] == '-d':
    print(base64decode(sys.argv[2]))

elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("""Use:
    encode(-e), or decode(-d) base64.""")

else:
    print("Unknown first argument: %s" % sys.argv[1])
    print("Accepted arguments: -e, -d, -h or --help")