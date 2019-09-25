
print ("read from file")
text_file = open("read_it.txt","r")
lines=text_file.readlines()
print (lines)
print (len(lines))
for line in lines:
    print ([line])

text_file.close()