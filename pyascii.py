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

if len(sys.argv) <= 2:
    pass

if sys.argv[1] == '-e':
    print(asciiencode(sys.argv[2]))

elif sys.argv[1] == '-d':
    print(asciidecode(sys.argv[2]))

elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("""Use:
    encode(-e) or decode(-d) ASCII.""")

if choice.lower() == 'encode':
    en = input("What would you like to encode? ")
    print(asciiencode(en))

elif choice.lower() == 'decode':
    de = input("What would you like to decode? ")
    print(asciidecode(de))

else:
    print("I can't do that")
