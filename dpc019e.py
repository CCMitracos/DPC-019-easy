# DPC 019 [E]
# Alphanumeric Counter

dpcfo = open("dpc019easytext.txt","r")
S = dpcfo.read()

alpha1 = "QWERTYUIOPASDFGHJKLZXCVBNM"
alpha2 = "qwertyuiopasdfghjklzxcvbnm"
alpha3 = "0123456789"
alphanumerics = alpha1 + alpha2 + alpha3

count = 0

for k in S:
    if (k in alphanumerics):
        count += 1

print count

quitprogram = raw_input("enter to quit >> ")
