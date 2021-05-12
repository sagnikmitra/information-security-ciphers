#Information Security - Playfair Cipher
#Language: Python | Version: 3.8.5
#Program done by Sagnik Mitra | CSBS | 3rd Year | 6th Semester | Roll: 2027
def find(matrix, ch):

    if ch == 'J':
        return [0, 0]

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return [i, j]

    return [-1, -1]


print('Enter the text to be encrypted: ', end=' ')
pt = [i for i in input().split()]

plaintext = ''.join(i for i in pt)

if len(plaintext) % 2 != 0:
    plaintext += 'Z'

print('Enter the key to be used for encryption: ', end=' ')
key = input()
cyphertext = ''

table = [['' for i in range(5)] for j in range(5)]
used = [i for i in key]
pos = 0

ch = 'A'

# Building the matrix

for i in range(5):
    for j in range(5):
        if pos < len(key):
            table[i][j] = key[pos]
            pos += 1
        else:
            flag = False

            while flag == False:
                if ch not in used and ch != 'J':
                    table[i][j] = ch
                    used.append(ch)
                    flag = True
                    ch = chr(ord(ch)+1)
                else:
                    ch = chr(ord(ch)+1)


# Encryption
for i in range(0, len(plaintext), 2):
    first = find(table, plaintext[i])
    second = find(table, plaintext[i+1])

    if first[0] < second[0]:
        cyphertext += table[first[0]][second[1]]
        cyphertext += table[second[0]][first[1]]

    elif first[0] > second[0]:
        cyphertext += table[second[0]][first[1]]
        cyphertext += table[first[0]][second[1]]

    elif first[0] == second[0] and first[1] != second[1]:
        cyphertext += table[first[0]][(first[1]+1) % 5]
        cyphertext += table[second[0]][(second[1]+1) % 5]

    elif first[0] != second[0] and first[1] == second[1]:
        cyphertext += table[(first[0]+1) % 5][first[1]]
        cyphertext += table[(second[0]+1) % 5][second[1]]


print('\n\'Z\' is added at the end of the string is length is odd.\n')
print('\nPlaintext given: ', ' '.join(i for i in pt))
print('\nKey used for encryption: ', key)

print('\nTable used for encryption: \n')
print('-------------')
for i in table:
    print('| ', end='')
    for j in i:
        print(j, end=' ')

    print('|')
print('-------------')
print('\nEncrypted text:', cyphertext)
