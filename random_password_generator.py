import random
import string

digit_passsword = string.digits
str_password = string.ascii_letters

punc_password= string.punctuation

password_length = 12

char_value = digit_passsword + str_password + punc_password

latest_pass = ""
for i in range(password_length):
    latest_pass += random.choice(char_value)

print("My password is:", latest_pass)
# print(digit_passsword)
# print(str_password)
# print(punc_password)

# print(char_value)
