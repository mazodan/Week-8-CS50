import sys
import cs50

def main():
    if len(sys.argv) != 2:
        print("Usage: ./python caesar.py k")
        exit(1)

    k = int(sys.argv[1]) % 26
    print("plaintext: ", end="")
    ptext = cs50.get_string()
    print("ciphertext: {}".format(caesarCipher(ptext, k)))
    exit(0)

def caesarCipher(plaintext, k):
    ctext = []
    for c in plaintext:
        if c.isalpha():
            # This is going to be a bit tricky, must preserve casing
            s = chr(ord(c) + k)
            if s.isalpha():
                ctext.append(s)
            else:
                # check if lower or upper case to apply the proper modulo
                if ord(c) >= ord('a') and ord(c) <= ord('z'):
                    n = (ord(c) + k) % 123
                    ctext.append(chr(97 + n))
                else:
                    n = (ord(c) + k) % 91
                    ctext.append(chr(65 + n))
        else:
            ctext.append(c)

    s = ""
    return s.join(ctext)

if __name__ == "__main__":
    main()