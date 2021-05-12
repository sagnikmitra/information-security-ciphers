//Information Security - Caesar Cipher (Alphanumeric version)
//Language : C
//Program done by Sagnik Mitra | CSBS | 3rd Year | 6th Semester | Roll : 2027

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main()
{

    char plain[10], cipher[10];
    int key, i, length;

    printf("\nEnter the plain text:");
    scanf("%s", plain);
    printf("\nEnter the key value (0-9):");
    scanf("%d", &key);
    printf("\nPLAIN TEXT: %s", plain);
    printf("\nENCRYPTED TEXT: ");

    for (i = 0, length = strlen(plain); i < length; i++)
    {

        cipher[i] = (plain[i] + key);

        if (isupper(plain[i]) && (cipher[i] > 'Z'))
            cipher[i] = cipher[i] - 26;
        if (islower(plain[i]) && (cipher[i] > 'z'))
            cipher[i] = cipher[i] - 26;

        printf("%c", cipher[i]);
    }

    printf("\nAFTER DECRYPTION : ");

    for (i = 0; i < length; i++)
    {

        plain[i] = cipher[i] - key;
        if (isupper(cipher[i]) && (plain[i] < 'A'))
            plain[i] = plain[i] + 26;
        if (islower(cipher[i]) && (plain[i] < 'a'))
            plain[i] = plain[i] + 26;

        printf("%c", plain[i]);
    }

    return 0;
}