# 5 points, 2 for effort. Maximum attempts: 1.
# open admission.csv, read it line by line

file_dir = 'admission.csv'

fileContent = open(file_dir)

for line in fileContent:
	line = line.strip()
	print(line)

