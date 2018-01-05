import cs50
import math

def main():
    print("Number: ", end="")
    card_number = cs50.get_string()
    luhnChecksum(card_number)

def luhnChecksum(card_no):
    # In C, tried to convert numbers into arrays, should have just used char * + atoi, I am not a smart person
    uncheckedSum = 0
    checkedSum = 0

    for i in range(len(card_no)):
        if i % 2 == 0:
            uncheckedSum = uncheckedSum + int(card_no[i])
        else:
            digit = int(card_no[i]) * 2
            if digit > 9:
                checkedSum = checkedSum + ((math.floor(digit / 10)) + (digit % 10))
            else:
                checkedSum = checkedSum + digit

    if (uncheckedSum + checkedSum) % 10 == 0:
        checkVendor(card_no[:2])
    else:
        print("INVALID")

def checkVendor(code):
    if code[0] == '4':
        print("VISA")
    else:
        if code == '35':
            print("JCB")
        elif code in ['34', '37']:
            print("AMEX")
        elif code in ['51', '52', '53', '54', '55']:
            print("MASTERCARD")
        elif code == '56':
            print("Bankcard")
        elif code in ['30', '38']:
            print("Diners Club")
        elif code == '60':
            print("Discover")
        else:
            print("VENDOR NOT FOUND, INVALID")

if __name__ == "__main__":
    main()