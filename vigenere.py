import sys
import cs50

if len(sys.argv) != 2:
    print("Usage: ./python viginere.py k")
    exit(1)

key = sys.argv[1]

if key.isalpha() == False:
    print("Usage: ./python viginere.py k")
    exit(2)

print("plaintext: ", end="")
ptext = cs50.get_string()

cipher = []
m = 0
for c in ptext:
    if c.isalpha():
        tmp_chr = chr(ord(c) + (ord(key[m % len(key)].lower()) - 97))
        if not tmp_chr.isalpha():
            # check cases
            if ord(c) > 64 and ord(c) < 91:
                cipher.append(chr(65 + (ord(tmp_chr) - 91)))
            else:
                cipher.append(chr(97 + (ord(tmp_chr) - 123)))
        else:
            cipher.append(tmp_chr)

        m = m + 1
    else:
        cipher.append(c)

s = ""
print("ciphertext: {}".format(s.join(cipher)))