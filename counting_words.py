# 5 points, 2 for effort. Maximum attempts: 1.

sentence = 'this is is a very long string'
# freq of i is 4.

# input: a string
# output: a dict
def freq(s):
	pass

	freq = {}

	for c in s:
		#print(c)
		if c in freq:
			freq[c] += 1
		else:
			freq[c] = 1

	return freq


print(freq(sentence))

