# The following program demonstrates the number conversion
# in decimals, hexadecimals, and binary numbers.
A = 0x5f
print(A)
print(hex(A))
print(bin(A))

B = 0b1000_0010_0100_0000_1010_0111_1001_1100
C = 0x82_40_a7_9c
if B == C:
    print("They’re the same!")
    print("Value of B - " + str(B))
    print("Value of C - " + str(C))
else:
    print("They’re different")
    print("Value of B - " + str(B))
    print("Value of C - " + str(C))