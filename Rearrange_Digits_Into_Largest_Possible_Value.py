n=int(input("enter a digit greater than 9 \n"))
def super_size(n):
	if n < 10:
		return n
	else:
		n = str(n)
		l=list(n)
		s = sorted(l, reverse = True)
		final = int("".join(s))
		return final
print (super_size(n))
