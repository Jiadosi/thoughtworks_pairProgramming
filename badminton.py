
#def Cancel(date, startTime, pId):

def Book(date, startTime, lastTime, pId):
	if pId == 'A':
		for i in range(1, lastTime+1):
			if date in logA[int(startTime)+i-1]:
				print 'Error: the booking conflicts with existing bookings!\n'
				return
		print 'Success: the booking is accepted!\n'
		logA[int(startTime)].append(date)

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
		pId = str[3]

		if startTime[1] != '00':
			print 'the booking is invalid, not int'
			break
		if pId is not 'A' and 'B' and 'C' and 'D':
			print 'the booking is invalid, pId'
			break
		Book(date, startTime[0], lastTime, pId)

	elif len(str) == 5:
		#cancel
		print 'cancel'
	elif len(str) == 1:
		#print
		print 'print'
	else:
		print 'error'
		
