
#def Cancel(date, startTime, playgroundId):

def book(log, date, startTime, lastTime):
	for i in range(1, lastTime+1):
		if date in log[int(startTime)+i-1]:
			print 'Error: the booking conflicts with existing bookings!\n'
			return
	print 'Success: the booking is accepted!\n'
	log[int(startTime)].append(date)



#def Print():


log = []
logA = dict()
logB = dict()
logC = dict()
logD = dict()

#init log
for i in range(9, 22):
	logA[i] = []
	logB[i] = []
	logC[i] = []
	logD[i] = []

while True:
	str = raw_input();
	#str = 'U123 2016-01-01 12:00~13:00 A C'
	str = str.split(' ')

	#userID = str[0]
	#year = str[1]

	if len(str) == 4:
		#book
		date = str[1]
		startTime = str[2].split('~')[0].split(':')#string befor :
		endTime = str[2].split('~')[1].split(':')
		lastTime = int(endTime[0]) - int(startTime[0])
		playgroundId = str[3]

		if startTime[1] != '00':
			print 'the booking is invalid, not int'
			break
		if playgroundId is not 'A' and not 'B' and not 'C' and not 'D':
			print 'the booking is invalid, playgroundId'
			continue
		if playgroundId == 'A':
			book(logA, date, startTime[0], lastTime)
		elif playgroundId == 'B':
			book(logB, date, startTime[0], lastTime)
		elif playgroundId == 'C':
			book(logC, date, startTime[0], lastTime)
		else:
			book(logD, date, startTime[0], lastTime)

	elif len(str) == 5:
		#cancel
		print 'cancel'
	elif len(str) == 1:
		#print
		print 'print'
	else:
		print 'error'
		
