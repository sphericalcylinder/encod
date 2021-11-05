import sys

#choice = input("Would you like to encode or decode? ")

def binencode(toencode):
    done = []
    array = bytearray(toencode, "utf8")
    for i in array:
        binary = bin(i)
        binary = binary.replace('0b', '')
        done.append(binary)
    done = " ".join([str(elm) for elm in done])
    done = done.replace(',', '')
    return done

def bindecode(todecode):
    values = todecode.split()
    ascii_str = ""
    for value in values:
        num = int(value, 2)
        ascii_chr = chr(num)
        ascii_str += ascii_chr
    return ascii_str

def noArgs():
    pass

if len(sys.argv) <= 2:
    noArgs()

if sys.argv[1] == '-e' or sys.argv[1] == '--encode':
    print(binencode(sys.argv[2]))

elif sys.argv[1] == '-d' or sys.argv[1] == '--decode':
    print(bindecode(sys.argv[2]))

elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("""Use:
    encode(-e or --encode) or decode(-d, --decode) binary.""")

else:
    print("Unknown first argument: %s" % sys.argv[1])
    print("-h or --help for more help")

if choice.lower() == "encode":
    en = input("Wthat would you like to encode? ")
    print(binencode(en))

elif choice.lower() == "decode":
    de = input("What would you like to decode? ")
    print(bindecode(de))

else:
    print("I can\'t do that")
