def ticket() :
    A = 15 * a
    return A
def bseat() :
    B = 12 * b
    return B
def cseat() :
    C = 9 * c
    return C
def total() :
    D = A + B + C
    return D

a = int(input("Enter count of A seat: "))
b = int(input("Enter count of B seat: "))
c = int(input("Enter count of C seat: "))

A = ticket()
B = bseat()
C = cseat()
D = total()

print("Income from class A seats: $",A)
print("Income from class B seats: $",B)
print("Income from class C seats: $",C)
print("Total income: $",D)


