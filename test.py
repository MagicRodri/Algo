
s = {1,2,3,4,5}
j = {9,10,11,12}
k = {5,6,7,8,9}
data = []
for _ in range(3):
	a = [int(x) for x in input().split()]
	a.pop(0)
	data.append(set(a))
print(sorted(data[0]|data[1]|data[2]))
# s = 0
# with open('input.txt','r') as f:
# 	content = f.readlines()
# 	for line in content:
# 		line = [int(x) for x in line.split()]
# 		s += sum(line)

# with open('output.txt','w') as f:
# 	f.write(str(s))