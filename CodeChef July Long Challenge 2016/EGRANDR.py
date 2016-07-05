T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	a, c, processing  = 0, 0, True
	for x in map(int, raw_input().split()):
		N -= 1
		if x == 2:
			processing = False
		elif x == 3:
			a += 1
			#if the count of 3's exceeds that of 5's; the GPA can't be >= 4.0
			if a - c > N:
				processing = False
		elif x == 5:
			c += 1
		if not processing:
			break
	#it's mandatory to obtain atleast one 5's
	if processing and c > 0:
		print "Yes"
	else:
		print "No"