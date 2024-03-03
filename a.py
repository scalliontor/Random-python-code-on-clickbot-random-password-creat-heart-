#row = 9 
#column = 13
for i in range(9):
	for j in range(13):
		if i==2 or i == 6 or i + j  == 6 or j - i == 6 or i - j == 2 or i + j == 14:
			if (j==6 or j==5 or j==7 ) and (i == 2 or i == 6) :
				print("đ",end =" ")
			else:
				print("*",end=" ")
		else:
			print(" ", end = " ")
	print()
			