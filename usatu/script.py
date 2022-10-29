import math


def solve(a,b,stops = None):

	if stops is not None:

		if a not in stops or b not in stops:
			return 'NO'
		else:
			i = []
			j = []
			for index,val in enumerate(stops):
				if val == a:
					i.append(index)
				if val == b:
					j.append(index)

			i.sort()
			j.sort()
			if i[0] < j[-1] :
				return'YES'
			return 'NO'

t = int(input())
result = []

for _ in range(t):
	input()
	n,k = map(int,input().split())
	stops = [int(x) for x in input().split()]
	for _ in range(k):
		a,b = map(int,input().split())
		result.append(solve(a,b,stops))

for r in result:
	print(r)

"""
3


6 3
3 7 1 5 1 4
3 5
1 7
3 10

YES
NO
NO


3 3
1 2 1
2 1
1 2
4 5
YES
YES
NO

7 5
2 1 1 1 2 4 4
1 3
1 4
2 1
4 1
1 2


NO
YES
YES
NO
YES

"""