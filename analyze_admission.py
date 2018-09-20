# 5 points, 2 for effort. Maximum attempts: 1.
# Questions:
# (1) How many applicants have gpa > 3.5?
# - How many are accepted?
# - What's lowest GRE of an accepted application?

INPUT = 'admission.csv'
f = open(INPUT)
f.readline()
Gcount = 0
for line in f:
	line = line.strip()
	#print(line)

	admit,gre,gpa,rank = line.split(',')

	if float(gpa) > 3.5:
		Gcount += 1

f.close()

print(Gcount)









