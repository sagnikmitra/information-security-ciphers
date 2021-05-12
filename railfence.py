# Column & Diagonal Transposition of a text input using Railfence Cipher
# Language: Python | Version: 3.8.5
# Program done by Sagnik Mitra | CSBS | 3rd Year | 6th Semester | Roll: 2027
def main():
    layers = int(input("Enter the number of layers: "))
    plain_text = input("Enter the plain text: ")
    cipher_text = encrypt(layers, plain_text)
    print("Encrypted text after Column Transposition: " + cipher_text)
    diagonal(cipher_text)


def encrypt(layers, plain_text):
    plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.upper()
    rail = [""] * layers
    layer = 0
    for character in plain_text:
        rail[layer] += character
        if layer >= layers - 1:
            layer = 0
        else:
            layer += 1

    cipher = "".join(rail)
    return cipher


def diagonal(cipher):
    new_text1 = []
    new_text2 = []
    for j in range(0, len(cipher)):
        if j % 2 == 0:
            new_text1.append(cipher[j])
        else:
            new_text2.append(cipher[j])
    print("Diagonal Transposition divided the Cipher into Two Different lists \nwith respoect to their even and odd indexes that would be joined later =\n{}\n{}".format(
        new_text1, new_text2))
    result = ""
    result = new_text1 + new_text2
    str1 = ""
    for ele in result:
        str1 += ele
    print("Encrypted text after both Column & Diagonal Transposition: " + str1)


if __name__ == '__main__':
    main()
