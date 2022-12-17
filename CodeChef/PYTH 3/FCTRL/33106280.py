# cook your dish here
for _ in range(int(input())):
	n=int(input())
	s=0
	while(n!=0):
		s+=n//5
		n=n//5
	print(s)