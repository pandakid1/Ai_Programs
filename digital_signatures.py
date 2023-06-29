# The following program implements the Digital Signature Algorithm
# Hash Function
def new_hash(message):
    digest = 0
    for c in message:
        digest  +=  ord ( c )
        digest = digest % 256
    return digest


# Modular Inverse Function
def mod_inv(n, modulus):
    q = [0, 0]
    r = [modulus, n]
    a = [0, 1]
    index = 2
    while r[len(r) - 1] != 0:
        quotient = r[index - 2] // r[index - 1]
        q.append(quotient)
        remainder = r[index - 2] - q[index] * r[index - 1]
        r.append(remainder)
        aux = a[index - 2] - q[index] * a[index - 1]
        a . append ( aux )
        index += 1
    inverse  =  a [ len ( a ) -  2 ]
    if  inverse  <  0 :
        inverse += modulus
    return inverse


# Sign a Message
def sign_message(message):
    k = 48
    r = 0
    s = 0
    while r == 0 or s == 0:
        r = ((g ** k) % p) % q
        if  r  ==  0 :
            k += 1
            continue
        s = ((new_hash(message) + x * r) * mod_inv(k, q)) % q
        if s == 0:
            k += 1
            continue
    return [r, s]


# Verify a Message
def verify(message, signature):
    r = signature[0]
    s = signature[1]
    for  sig  in  signature :
        if sig < 0 or sig > q:
            print("Invalid signature")
    w = mod_inv(s, q)
    u1 = (new_hash(message) * w) % q
    u2 = (r * w) % q
    v = (((g ** u1) * (y ** u2)) % p) % q
    print ( v )
    if v == r:
        print("Signature is valid!")
    else:
        print("Message is compromised!")


# Set the Values
q = 191
p = 383
h = 2
g = int(h ** ((p - 1) / q)) % p
print(g)

# Private / Public Keys
x = 29
y = (g ** x) % p

# Signing a Message
message = "Hello World"
signature = sign_message(message)
print("Signature")
print("r: " + str(signature[0]))
print("s: " + str(signature[1]))

# Verifying a Message
message1 = "Hello world"
message2 = "Hello World"
message3 = "Hello World!"

print("Verify message 1")
verify(message1, signature)

print("Verify message 2")
verify(message2, signature)

print("Verify message 3")
verify(message3, signature)