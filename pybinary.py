choice = input("Would you like to encode or decode? ")

def binencode(toencode):
    done = []
    array = bytearray(toencode, "utf8")
    for i in array:
        binary = bin(i)
        binary = binary.replace('0b', '')
        done.append(binary)
    return done

def bindecode(todecode):
    values = todecode.split()
    ascii_str = ""
    for value in values:
        num = int(value, 2)
        ascii_chr = chr(num)
        ascii_str += ascii_chr
    return ascii_str

if choice.lower() == "encode":
    en = input("Wthat would you like to encode? ")
    print(binencode(en))

elif choice.lower() == "decode":
    de = input("What would you like to decode? ")
    print(bindecode(de))

else:
    print("I can\'t do that")
