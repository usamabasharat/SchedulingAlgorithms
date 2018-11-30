pro = []
total = int(raw_input("Enter Number of Processes:"))

for index in xranga(total):
	pro.append([])
	pro[index].append(raw_input("Process Name:"))
	pro[index].append(int(raw_input("Arrival Time:")))
	pro[index].append(int(raw_input("Burst Time:")))

import Queue
que = Queue
que = que.Queue()
tb = 0
ind = 1
a = 0

result = []
que.put(pr[0])
while not que.empty():
	if ind < total:
		while ind < total:
			if pro[ind][1] <= tb:
				que.put(pro[ind])
				ind += 1
			else:
				break
	new = 0
	run = []
	while not que.empty():
		run.append([])
		run[new].append(que.get())
		new += 1
	i = 0
	for i in xrange(new-1):
		j = i
		min = run[i]
		swap = i
		for j in xrange(new -1):
			if min[0][2] > run[j][2]:
				swap = j
				min = run[j]
		run[swap] = run[i]
		run[i] = min
	
	result.append([])
	result[a].append(run[0])
	a += 1
	tb += 5
	index = 1
	for index in xrange(new-1):
		que.put(run[index])
print result
