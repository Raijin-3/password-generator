from random import choice, randint, shuffle, sample


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#']

#randomly accessing items from list
password_letters = [choice(letters) for _ in range(randint(8, 8))]
password_symbols = symbols
password_numbers = [choice(numbers) for _ in range(randint(2, 2))]


password_list = password_letters + password_symbols + password_numbers

#shuffling and converting them into one string
shuffle(password_list)
password = "".join(password_list)


numsymbols = numbers + symbols

for i in range(len(password)-1):
    if password[0] in numsymbols:
        shuffle(password_list)
        password = "".join(password_list)
    elif password[-1] in numsymbols:
        shuffle(password_list)
        password = "".join(password_list)


print(password)
print("Hello")
