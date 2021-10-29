choice = input("Would you like to encode or decode? ")

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

if choice.lower() == 'encode':
    en = input("What would you like to encode? ")
    print(asciiencode(en))

elif choice.lower() == 'decode':
    de = input("What would you like to decode? ")
    print(asciidecode(de))

else:
    print("I can't do that")
