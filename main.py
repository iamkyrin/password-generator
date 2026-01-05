import random



ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
hexdigits = "0123456789abcdefABCDEF"
punctuation = '!#$%&()*+,-.<=>?@[]^_{|}~'
total = punctuation + hexdigits + digits + ascii_lowercase + ascii_uppercase

length = 20

password = "".join(random.sample(total, length))

print("Password:")
print("<------------------------------>")
print(password)
print("\nSaved Password in password.txt")
try:
    with open("password.txt", "a") as file:
        file.write("\n" + password)

except Exception as e:
    print(f"An Error Occurred", e)
