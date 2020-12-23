
N = int(input())

l = input().split()

new=[]
pos=[]

for num in l:
	if int(num) > 0:
		pos.append(True)
	else:
		pos.append(False)
		
	if num == num[::-1]:
		new.append(True)
	else:
		new.append(False)

print(any(new) and all(pos))