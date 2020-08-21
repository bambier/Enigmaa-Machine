import pickle


#If you added operator in today_hash.py first go to @0 and add r5,... to and of r4 like r3, r4, 45, r6, ... , rn then go to @3 and ad cn = rn[alphabets.find(c(n-1))] at last of c4 then add cn = alphabets[rn.find(reflected)] and change c4 to alphabets[rn.find(rn)]] ((next steps are optimal))   then go to @0 and define some varable for your operator after t =	0 and set it to 0 now go to @5 and at last of it addcyour varabels like them then go to @2 and add it at last of it behind other varabels.


# @0
# Load hash file
file = open("today_hash.enigma", "rb")
alphabets, r1, r2, r3, r4 = pickle.load(file)
file.close()

x = 0
y = 0
z = 0
t = 0



# @4
def reflector(char):
	
	return alphabets[len(alphabets) - alphabets.find(char) - 1]




# @3
def machine(char):
	
	c1 = r1[alphabets.find(char)]
	c2 = r2[alphabets.find(c1)]
	c3 =  r3[alphabets.find(c2)]
	c4 = r4[alphabets.find(c3)]
	
	reflected = reflector(c4)
	
	c4 = alphabets[r4.find(reflected)]
	c3 =  alphabets[r3.find(c4)]
	c2 =  alphabets[r2.find(c3)]
	c1 =  alphabets[r1.find(c2)]
	
	return c1





# @5
def turn(r1, r2, r3, r4, x, y, z, t):
	if x == 63:
		r1 = r1[1:] + r1[0]
		y += 1
		x = 0
	if y == 63:
		r2 = r2[1:] + r2[0]
		z += 1
		y = 0
	if z == 63:
		r3 = r3[1:] + r3[0]
		t += 1
		z = 0
	if t == 63:
		r4 = r4[1:] + r4[0]
	
	
	return r1, r2, r3, r4, x, y, z, t


# @2
def enigma(word):
	hash_text = ""
	
	for character in word:
		x += 1
		hash_text += machine(character)
		r1, r2, r3, r4, x, y, z, t = turn(r1, r2, r3, r4, x, y, z, t)
	
	return hash_text



# @1
if __name__ == "__main__":
	while True:
		text = input("Enter text to hash or unhash>> ")
		coded_text = enigma(text)
		print("|{0}|".format(coded_text))
		
