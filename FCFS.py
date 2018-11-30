f = open("processes.txt", "r")
count = 0
y = 0
arr = []
turnaround = 0
total_turnaround = 0
finish_time = 0

for i in f:
	data = i.split(" ")	
	count = count + 1
	arr.append([])
	arr[y].append(data[0])
	arr[y].append(int(data[1]))
	arr[y].append(int(data[2]))
	finish_time = finish_time + arr[y][2]
	turnaround = finish_time - arr[y][1]
	arr[y].append(int(turnaround))
	total_turnaround = total_turnaround + (finish_time - arr[y][1])	
	y = y + 1

print("\nProcess Name\t\tArrival Time\t\tBurst Time\t\tTurnaround Time")

for i in range(count):
	print arr[i][0],"\t\t\t",arr[i][1],"\t\t\t",arr[i][2],"\t\t\t",arr[i][3]

avg = (float(total_turnaround)/count)

print "\nTotal Turnaround Time: ", total_turnaround
print "Avg TurnAround Time: ", avg, '\n' 
