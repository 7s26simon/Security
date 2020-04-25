from base64 import b64encode

# Location of filepath
filepath = '/home/si/Desktop/numbers.txt'

# Open file, then read line by line & encode each number on each line to Base64
with open(filepath) as fp:
	file = open("converted.txt", "w")
	for line in fp:
			#print (b64encode(fp.readline()))
			a = (b64encode(line))
			print (a)
			file.write(a)
			file.write('\n')

# Close numbers.txt file
fp.close()

# Close the converted.txt file
file.close()

