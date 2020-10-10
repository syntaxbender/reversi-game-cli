from termcolor import colored
import time
def table_printer(table,possible_moves):
	for j in range (0,8):
		for i in range(0,8):
			if(j==0 and i==0):
				print("  0 1 2 3 4 5 6 7")
			if(i==0):
				print(j, end=" ")
			try:
				if(isinstance(possible_moves.index([i,j]),int)):
					print("{}".format(colored("X ", 'red', 'on_green'),i,j), end="")
			except:
				print("{}".format(get_player_color(table[i][j]),i,j), end="")
		print("")
def get_player_color(player,call_type="color"):
	if(call_type=="color"):
		if player == 1:
			player_color = colored("◉ ", 'white', 'on_green')
		elif player == 0:
			player_color = colored("  ", 'grey', 'on_green')
		else:
			player_color = colored("◉ ", 'grey', 'on_green')
	else:
		if player == 1:
			player_color = "Beyaz"
		elif player == 0:
			player_color = "Boş"
		else:
			player_color = "Siyah"
	return player_color		

def make_arr():
	arr = [[0 for x in range(8)] for y in range(8)]
	return arr
def get_directional_coordinate(direction,x,y,k):
    if direction == "upleft":
        x = x - k
        y = y - k
        return [x, y]
    elif direction == "up":
        x = x
        y = y - k
        return [x, y]
    elif direction == "upright":
        x = x + k
        y = y - k
        return [x, y]
    elif direction == "left":
        x = x - k
        y = y
        return [x, y]
    elif direction == "right":
        x = x + k
        y = y
        return [x, y]
    elif direction == "downleft":
        x = x - k
        y = y + k
        return [x, y]
    elif direction == "down":
        x = x
        y = y + k
        return [x, y]
    elif direction == "downright":
        x = x + k
        y = y + k
        return [x, y]
def toggle_player(player):
	if player == 1:
		return 2
	else:
		return 1
def update_score(score,player,reverse_count):
	if player == 1:
		score[0] = score[0]+reverse_count+1
		score[1] = score[1]-reverse_count
	else:
		score[1] = score[1]+reverse_count+1
		score[0] = score[0]-reverse_count
	return score
def reverse(table,reverse_list):
	table[reverse_list[1]][reverse_list[2]] = reverse_list[3]
	for reverse_coordinate in reverse_list[4]:
		table[reverse_coordinate[0]][reverse_coordinate[1]] = reverse_list[3]
	return table
def check_possible_moves(table,player): # taş konacak yerleri hesaplar
	directions = ["upleft", "up", "upright", "left", "right", "downleft", "down", "downright"]
	possible_moves = []
	for x in range(0,8):
		for y in range(0,8):
			if table[x][y] == player:
				for direction in directions:
					for direction_step in range(1,8):
						directional_coordinate = get_directional_coordinate(direction,x,y,direction_step)
						if directional_coordinate[0] < 0 or directional_coordinate[1] < 0 or directional_coordinate[0] > 7 or directional_coordinate[1] > 7:
							break
						elif table[directional_coordinate[0]][directional_coordinate[1]] == 0:
							if direction_step == 1:
								break
							else:
								possible_moves.append([directional_coordinate[0],directional_coordinate[1]]) #fanilist bir liste önyüze mevlanadanfeyzalanlar yollanır önyüzde arrayda for ile işlenir mevlanadanfeyzalanlar'ın her iterasyonunda 
								break
						elif table[directional_coordinate[0]][directional_coordinate[1]] == table[x][y]:
							break
						#elif reversi_masasi[mevladanreturnaldim[0]][mevladanreturnaldim[1]] != reversi_masasi[x][y]:
							#fanilist = [mevladanreturnaldim[0],mevladanreturnaldim[1]]
							#print("taraniyor4: "+str(x)+", "+str(y)+" - "+tavafistikameti+str(istikametartiran)+" - "+str(mevladanreturnaldim[0])+","+str(mevladanreturnaldim[1])+" - deger : "+str(reversi_masasi[mevladanreturnaldim[0]][mevladanreturnaldim[1]])+" - player : "+str(player))
	if(len(possible_moves)<1):
		return [False,"Hamle kalmadı!"]
	return [True,possible_moves]	
def check_reverses(table,x,y,player):
	if(table[x][y] != 0):
		return [False,"Oynamak istediğiniz koordinatta zaten bir taş var."]
	directions = ["upleft", "up", "upright", "left", "right", "downleft", "down", "downright"]
	reverse_list = []
	for direction in directions:
		templist = []
		for direction_step in range(1,8):
			directional_coordinate = get_directional_coordinate(direction,x,y,direction_step)
			if directional_coordinate[0] < 0 or directional_coordinate[1] < 0 or directional_coordinate[0] > 7 or directional_coordinate[1] > 7:
				break
			elif table[directional_coordinate[0]][directional_coordinate[1]] == 0:
				break
			elif table[directional_coordinate[0]][directional_coordinate[1]] == player:
				if direction_step == 1:
					break
				else:
					reverse_list += templist #fanilist bir liste önyüze mevlanadanfeyzalanlar yollanır önyüzde arrayda for ile işlenir mevlanadanfeyzalanlar'ın her iterasyonunda 
					break
			elif table[directional_coordinate[0]][directional_coordinate[1]] != player:
				templist.append([directional_coordinate[0],directional_coordinate[1]])
	if(len(reverse_list)<1):
		return [False,"Geçersiz Hamle"]
	return [True,x,y,player,reverse_list]


table = make_arr()
table[3][3] = 1
table[4][4] = 1
table[3][4] = 2
table[4][3] = 2
player = 2
check_game_is_over = 0
score = [2,2]

while(True):
	print("Beyaz : "+str(score[0])+" - Siyah : "+str(score[1]))
	print(get_player_color(player,"text")+" oyuncu oynuyor")
	possible_moves = check_possible_moves(table,player)
	if(possible_moves[0] == True):
		check_game_is_over=0
	else:
		check_game_is_over=check_game_is_over+1
		print(get_player_color(player,"text")+" oyuncu için oynanabilir yer yok, el rakibe devredildi.")
		player = toggle_player(player)
		continue
	if check_game_is_over==2:
		print("Rakibinizin ve sizin oyunda oynayabileceğiniz bir yeriniz kalmadı, oyun bitti!")
		break
	remove_duplicates_possible_moves = [list(t) for t in set(tuple(element) for element in possible_moves[1])]
	table_printer(table,remove_duplicates_possible_moves)
	x = int(input("x = "))
	y = int(input("y = "))
	start = time.time()
	reverse_list = check_reverses(table,x,y,player)
	if(reverse_list[0] == False):
		print(reverse_list[1])
	else: 
		table = reverse(table,reverse_list)
		score = update_score(score,player,len(reverse_list[4]))
		player = toggle_player(player)
	end = time.time()
	print("Exec time : "+str(end - start)+"\n\n\n\n")