alphabet = "abcdefghijklmnopqrstuvwxyz"
pt = input("Enter the plaintext: ").lower()
key = input("Enter the key: ").lower()
def encrypt(p,k):
    ct,i,j = "",0,0
    for _ in range(len(k),len(p)):
        k+=k[i%len(k)]
        i = i + 1
    for _ in p:
        ct+=alphabet[(alphabet.find(p[j])+alphabet.find(k[j]))%26]
        j = j + 1
    return ct
print(encrypt(pt,key))

x=input("Enter the encrypted text: ")
def decrypt(c,k):
    nk,dt,i,j = [],"",0,0
    for _ in range(len(c)):
        nk+=(k[i%len(k)])
        i = i + 1
    for _ in c:
        dt+=alphabet[(alphabet.find(c[j])-alphabet.find(nk[j]))%26]
        j = j + 1
    return dt
print(key)
print (decrypt(x,key))
