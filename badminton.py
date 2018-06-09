from datetime import datetime
import time

#day = date.weekday()

def cancel(log, uId, date, startTime, lastTime):
	data = date + uId
	for i in range(1, lastTime+1):
		if data in log[int(startTime)+i-1]:
			print 'Success: the cancelling is accepted!\n'
			log[int(startTime)].remove(data)
		else:
			print 'Error: the cancelling is invalid!\n'

def book(log, uId, date, startTime, lastTime):
	for i in range(1, lastTime+1):
		for d in log[int(startTime)+i-1]:
			if date in d:
				print 'Error: the booking conflicts with existing bookings!\n'
				return
	print 'Success: the booking is accepted!\n'
	data = date + uId
	log[int(startTime)].append(data)

def Print():
	

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
		uId = str[0]
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
			book(logA, uId, date, startTime[0], lastTime)
		elif playgroundId == 'B':
			book(logB, uId, date, startTime[0], lastTime)
		elif playgroundId == 'C':
			book(logC, uId, date, startTime[0], lastTime)
		else:
			book(logD, uId, date, startTime[0], lastTime)

	elif len(str) == 5:
		#cancel
		uId = str[0]
		date = str[1]
		startTime = str[2].split('~')[0].split(':')#string befor :
		endTime = str[2].split('~')[1].split(':')
		lastTime = int(endTime[0]) - int(startTime[0])
		playgroundId = str[3]
		if playgroundId == 'A':
			cancel(logA, uId, date, startTime[0], lastTime)
		elif playgroundId == 'B':
			cancel(logB, uId, date, startTime[0], lastTime)
		elif playgroundId == 'C':
			cancel(logC, uId, date, startTime[0], lastTime)
		else:
			cancel(logD, uId, date, startTime[0], lastTime)

	elif len(str) == 1:
		#print
		print 'print'
	else:
		print 'error'
		
