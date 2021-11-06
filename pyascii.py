import sys

def asciiencode(toencode):
    done = []
    for c in toencode:
        a = ord(c)
        done.append(a)
    done = " ".join([str(elm) for elm in done])
    done = done.replace(',', '')
    return done

def asciidecode(todecode):
        done = []
        todecode = todecode.split()
        for c in todecode:
            done.append(chr(int(c)))
        done = " ".join([str(elm) for elm in done])
        done = done.rstrip()
        return done

def noArgs():
    choice = input("Would you like to encode or decode? ")

    if choice.lower() == 'encode':
        en = input("What would you like to encode? ")
        print(asciiencode(en))
        sys.exit(0)

    elif choice.lower() == 'decode':
        de = input("What would you like to decode? ")
        print(asciidecode(de))
        sys.exit(0)

    else:
        print("I can't do that")
        sys.exit(0)

print(sys.argv)

if len(sys.argv) < 2:
    noArgs()

if sys.argv[1] == '-e' or sys.argv[1] == '--encode':
    print(asciiencode(sys.argv[2]))

elif sys.argv[1] == '-d' or sys.argv[1] == '--decode':
    print(asciidecode(sys.argv[2]))

elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("""Use:
    encode(-e, --encode) or decode(-d, --decode) ASCII.""")

else:
    print("Unknown first argument: %s" % sys.argv[1])
    print("Accepted arguments: -e, -d, -h or --help")