import pickle
from random import shuffle
import string

# Define characters and digits
alphabets = string.ascii_letters + string.digits + " "


# If you want more operator first go to @1 and copy one of them and paste in last of them and just rename it to r5 , r6 ... then Go to @2 and add it to last of pickle.dump() as like this pickle.dump((r1,r2,...,r5,r6,...),file) then change settings in enigma_machin.py


# Define some operartor
# @1
r1 = list(alphabets)
shuffle(r1)
r1 = "".join(r1)

r2 = list(alphabets)
shuffle(r2)
r2 = "".join(r2)

r3 = list(alphabets)
shuffle(r3)
r3 = "".join(r3)



r4 = list(alphabets)
random.shuffle(r4)
r4 = "".join(r4)


# Write operators to today_hash.enigma
#@2
with open("today_hash.enigma", "wb") as file:
	pickle.dump((alphabets, r1, r2, r3, r4), file)
	file.close()

print(r1)
print(r2)
print(r3)
print(r4)
print(alphabets)
