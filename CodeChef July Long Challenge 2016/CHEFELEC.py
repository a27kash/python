T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	electricity = map(int, raw_input())
	x = map(int, raw_input().split())
	beg = 0
	#traversing from extreme left in rightwards direction; linking all 0's to the first 1
	while electricity[beg] == 0:
		beg += 1
	length = x[beg] - x[0]
	#skipping over all 1's till we get next 0 or reach end of array
	while electricity[beg] == 1:
		beg += 1
		if beg == N:
			break
	beg -= 1
	end = N - 1
	#traversing from extreme right in leftwards direction; linking all 0's to the last 1
	while electricity[end] == 0:
		end -= 1
	length += x[N - 1] - x[end]
	#skipping over all 1's till we get previous 0 or reach beginning of array
	while electricity[end] == 1:
		end -=1
		if end == -1:
			break
	end += 1
	while beg < end:
		left_x = x[beg]
		max_gap = x[beg + 1] - x[beg]
		beg += 1
		while electricity[beg] == 0:
			gap = x[beg + 1] - x[beg]
			if gap > max_gap:
				max_gap = gap
			beg += 1
		right_x = x[beg]
		length += right_x -left_x - max_gap
		while electricity[beg] == 1:
			beg +=1
			if beg == N:
				break
		beg -= 1
	print length