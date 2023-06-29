# The following program creates a phone book database and uses hash functions to set up efficient lookup functions

def new_hash(message):
    digest = 0
    if message == "":
        digest = -1
    for c in message:
        digest  +=  ord(c)
    digest = digest % max_size
    return digest


# Unsorted Phonebook
phone_book = [
    ("Alice", 4082553555),
    ("", 0000000000),
    ("Diane", 9830978345),
    ("Bob", 6503879023),
    ("", 0000000000),
    ("Eve", 7642398541),
    ("Charlie", 5052358753)
]

max_size = 19
while len(phone_book) < max_size - 1:
    phone_book.append(("", 0000000000))
phone_book.append(("Steven", 1420573857))

# Make a search
search_name = input("Lookup which number: ")
search_count = 0

for  i  in  range ( len ( phone_book )):
    search_count += 1
    if search_name == phone_book[i][0]:
        print("Unsorted book search:")
        print(phone_book[i][1])
        print(search_count)
        break
    if search_count == max_size:
        print("Not found (unsorted)")

# ///////////////////////////////////////////////////////////////// #
# Sorted Phonebook
sorted_book = sorted(phone_book, key=lambda phone_book: phone_book[0])
while sorted_book[0][0] == "":
    del(sorted_book[0])

# Make a search
search_index = int(len(sorted_book) / 2)
search_max = len(sorted_book) - 1
search_min  =  0
search_count = 0
for  i  in  range ( len ( sorted_book )):
    search_count += 1
    if search_name == sorted_book[search_index][0]:
        print("Sorted book search:")
        print(sorted_book[search_index][1])
        print(search_count)
        break
    elif search_name < sorted_book[search_index][0]:
        search_max = search_index
        search_index -= int((search_index - search_min) / 2 + 0.5)
    elif search_name > sorted_book[search_index][0]:
        search_min = search_index
        search_index += int((search_max - search_index) / 2 + 0.5)
    if search_count == len(sorted_book):
        print("Not found (alphabetical)")

# ///////////////////////////////////////////////////////////////// #
# Hash Sort
phone_hash = []
hashed_book = [("", 0000000000) for _ in range(max_size)]
for  i  in  range ( len ( phone_book )):
    name = phone_book[i][0]
    digest = new_hash(name)
    if  digest  ==  - 1 :
        continue
    phone_hash.append(digest)
    new_index = digest
    while hashed_book[new_index] != ("", 0000000000):
        new_index = (new_index + 1) % max_size
    hashed_book[new_index] = phone_book[i]

# Make a search
hash_index = new_hash(search_name)
search_count = 0
for  i  in  range ( len ( hashed_book )):
    search_count += 1
    if hashed_book[hash_index][0] == search_name:
        print(hashed_book[hash_index][1])
        print(search_count)
        break
    hash_index = (hash_index + 1) % max_size
    if search_count == max_size:
        print("Not found (hashed)")