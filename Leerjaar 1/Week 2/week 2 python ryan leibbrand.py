#opdrachten week 2 ryan leibbrand 10-9-2025

# opdracht 1.1 met for loops figuren maken
for i in range(5): #print 5 keer ******
    print("*****")

print("\n")

for i in range(6): # print 1x * tot 5x * door te vermendigvuldigen door de i 
    print("*" * i) 
 
print("\n")

for i in range(6): # range 6 want dan doet hij het 5x extra getall voor de -1
    print("******"[0:(5-i)])

print("\n")

for i in range(5): #print 5 keer 12345
    print("12345")

print("\n")

for i in range(5): 
    print("12345"[0:(1+i)]) #eerst alleen de eerste dan + de i, 1,2,3,4,5

print("\n")

for i in range(5):#!
   print("...."[0:(4-i)] + "12345"[0:1+i])

print("\n","\n","\n"+"opdracht 1.2","\n")
#opdracht 1.2 met while loops figuren maken

# eerst **
amount = 0
while amount <= 5:# doed 1 amount erbij tot 5 dan stopt met printen
    print("*****")
    amount += 1

print("\n")

amount = 1# sets amount back to 1
while amount <= 5:
    print("*" * amount)
    amount += 1

print("\n")

amount = 1
while amount <= 5:
    print("*****"[0:(6-amount)])
    amount += 1

print("\n")

# 12345

amount = 1
while amount <= 5:# while amount is minder of gelijk aan 5 doorgaan
    print("12345")
    amount += 1 # amount = amount + 1

print("\n")

amount = 1
while amount <= 5:
    print("12345"[0:(1*amount)])
    amount += 1

print("\n")

amount = 1
while amount <= 5:
  print("...."[0:(5-amount)] + "12345"[0:amount])
  amount +=1

print("\n")

#opdracht 2 

amount = int(input("Hoe groot is de vierkant"))
symbool_randd = str(input("Welk symbool heeft de rand"))
symbool_inhoud = str(input("Welk symbool moet de inhoud zijn"))

print(symbool_randd * amount)
for i in range(amount-2):
    print(symbool_randd + symbool_inhoud*(amount - 2) + symbool_randd) 

print(symbool_randd * amount)
