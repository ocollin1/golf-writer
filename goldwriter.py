playerfile = open('playerfile.txt' , 'w')
finsih = 'No'
while finsih == 'No' :
	newPlayer = input('Enter player Name')
	newScore = input('Enter player Score')

	playerfile.write(newPlayer)
	playerfile.write(newScore)

	finsih = input('More Players? Yes/No: ')
 	pass 
