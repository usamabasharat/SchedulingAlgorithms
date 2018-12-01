pro = []
total = int(raw_input("Enter Number of Processes:")
time_slice = int(raw_input("Time Slice:")
for index in xrange(int(total)):
	pro.append([])
	pro[index].append(raw_input("Process Name:"))
	pro[index].append(int(raw_input("Arrival Time:")))
	pro[index].append(int(raw_input("Burst Time:")))
run = []
pro.sort(key = lambda pro:pro[1])
tb = 0
import Queue
ready = Queue
ready = ready.Queue()
arr = 0
ready.put(pro[arr])
arr = arr + 1
while not ready.empty():
	run = ready.get()
	if run[2] >= time_slice:
		run[2] = run[2] - time_slice
		print run
		tb = tb + time_slice
		if arr <= total:
			while arr < total:
				if pro[arr][1] <= tb:
					ready.put(pro[arr])
				if (arr + 1) == total:
					arr = arr + 1
					break
				arr = arr + 1
		if run[2] != 0:
			ready.put(run)
	else:
		print run
		tb = tb + run[2]
		if arr <= total:
			while arr < total:
				if pro[arr][1] <= tb:
					ready.put(pro[arr])
				if (arr + 1) == total:
					arr = arr + 1
					break
				arr = arr + 1

print "Process\t\tArrival Time\t\tBurst Time"
for index in xrange(int(total)):
	print pro[index][0],"\t\t\t",pro[index][1],"\t\t\t",pro[index][2],'\n'
