
N, M = input().split()
N = int(N)
M = int(M)

l = []
for num in range(N):
	l.append(input().split())
	for i in range(M):
		l[num][i] = int(l[num][i])

k = int(input())
'''
print("N, M are {},{}".format(N,M))
for i in l:
	print(i)
print(k)
'''
if k < M and k >= 0:
	arrange=[]
	for players in l:
	#players[k] = int(players[k])
		arrange.append(players[k])
	arrange.sort()

	for elem in arrange:
		for players in l:
			if elem == players[k]:
				print(*players)
				break
		l.remove(players)