from datetime import datetime
import time

#day = date.weekday()


def cancel(log, uId, date, startTime, lastTime):
	data = date + '@' + uId
	for i in range(1, lastTime+1):
		if not log[int(startTime)+i-1]:
			print 'Error: the booking being cancelled does not exist!\n'
			return
		for d in log[int(startTime)+i-1]:
			if date in d:
				log[int(startTime)].remove(data)
				#print 'Success: the cancelling is accepted!\n'
				#return True

			else:
				print 'Error: the cancelling is invalid!\n'
				#return False
	print 'Success: the cancelling is accepted!\n'
	#return True

def book(log, uId, date, startTime, lastTime, playgroundId):
	format = '%Y-%m-%d'
	day = datetime.strptime(date, format).weekday()
	rent = 0
	for i in range(1, lastTime+1):
		for d in log[int(startTime)+i-1]:
			if date in d:
				print 'Error: the booking conflicts with existing bookings!\n'
				return
	
	#calculate rent
	for i in range(1, lastTime+1):
		if day > 5:
			if int(startTime)+i-1 < 12:
				rent = 40
			elif int(startTime)+i-1 < 18:
				rent = 50
			else:
				rent = 60
		else:
			if int(startTime)+i-1 < 12:
				rent = 30
			elif int(startTime)+i-1 < 18:
				rent = 50
			elif int(startTime)+i-1 < 20:
				rent = 80
			else:
				rent = 60

		moneyLog = playgroundId + '@' + date + '@' + str(int(startTime)+i-1)
		if not money:
			money.append(moneyLog + '@' + str(rent) + '@0')
		else:
			for m in money:
				if moneyLog in m:
					m.split('@')[4] = str(rent + int(m.split('@')[4]))
				else:
				#money.append(playgroundId + '@' + date + '@' + str(int(startTime)+i-1) + '@' + str(rent) + '@0')
					money.append(moneyLog + '@' + str(rent) + '@0')

	data = date + '@' + uId
	log[int(startTime)].append(data)
	print 'Success: the booking is accepted!\n'



def printMoney():
	'''
	mindate = '2018-06-10'
	print 'playground A:\n'
	for i in logA:
		if min(i) > mindate:
			mindate = min(i)
	mindate = mindate.split('@')[0]
	for i in logA:
		for j in i:
			if mindate in j:
	'''
	print money


fine = []
money = []

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
	inputString = raw_input();
	#str = 'U123 2016-01-01 12:00~13:00 A C'
	inputString = inputString.split(' ')

	#userID = str[0]
	#year = str[1]

	if len(inputString) == 4:
		#book
		uId = inputString[0]
		date = inputString[1]
		startTime = inputString[2].split('~')[0].split(':')#string befor :
		endTime = inputString[2].split('~')[1].split(':')
		lastTime = int(endTime[0]) - int(startTime[0])
		playgroundId = inputString[3]

		if lastTime == 0:
			print 'Error: the booking is invalid!\n'
			continue

		if startTime[1] != '00':
			print 'the booking is invalid, not int'
			continue
		if playgroundId is not 'A' and not 'B' and not 'C' and not 'D':
			print 'the booking is invalid, playgroundId'
			continue
		if playgroundId == 'A':
			book(logA, uId, date, startTime[0], lastTime, playgroundId)
		elif playgroundId == 'B':
			book(logB, uId, date, startTime[0], lastTime, playgroundId)
		elif playgroundId == 'C':
			book(logC, uId, date, startTime[0], lastTime, playgroundId)
		else:
			book(logD, uId, date, startTime[0], lastTime, playgroundId)

	elif len(inputString) == 5:
		#cancel
		uId = inputString[0]
		date = inputString[1]
		startTime = inputString[2].split('~')[0].split(':')#string befor :
		endTime = inputString[2].split('~')[1].split(':')
		lastTime = int(endTime[0]) - int(startTime[0])
		playgroundId = inputString[3]
		if playgroundId == 'A':
			cancel(logA, uId, date, startTime[0], lastTime)
			#if cancel(logA, uId, date, startTime[0], lastTime):
				#money
				#fine.append('A@'+date+str[2]+'fine:'+money)

		elif playgroundId == 'B':
			cancel(logB, uId, date, startTime[0], lastTime)
		elif playgroundId == 'C':
			cancel(logC, uId, date, startTime[0], lastTime)
		else:
			cancel(logD, uId, date, startTime[0], lastTime)

		fineRecord = ''
		fine.append(fineRecord)

	elif len(inputString) == 1:
		#print
		printMoney()
	else:
		print 'error'
		
