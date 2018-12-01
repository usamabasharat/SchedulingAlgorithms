pro = []
total = raw_input("Enter Number of Processes:")
bt = 0
for index in xrange(int(total)):
	pro.append([])
	pro[index].append(raw_input("Process Name: "))
	pro[index].append(int(raw_input("Arrival Time:")))
	pro[index].append(int(raw_input("Priority: ")))
	pro.[index].append(int(raw_input("Burst Time:")))
	bt = bt + pro[index][3]
pro.sort(key = lambda pro:pro[1])
pro.sort(key = lambda pro:pro[2])
index = 0
print "Process Name\t\tArrival Time\t\tPriority\t\tBurst Time\n"
for index in xrange(int(total)):
	print pro[index][0],'\t\t\t',pro[index][2],'\t\t\t',pro[index][3],'\n'
print "Burst Time: ", bt
