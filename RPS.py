import random 
import keyboard
spisok=[]
choise1=""
choise2=""
s=["камень","ножницы","бумага"]
print("Бумага побеждает камень")
print("Камень побеждает ножницы")
print("Ножницы побеждают бумагу")
while True:
	print("1-играть с ботом")
	print("2-играть с другом")
	print("3-правила игры")
	print("4-выйти")
	print("")
	choise=0
	if keyboard.read_key()==1:
		choise==1
	elif keyboard.read_key()==2:
		choise==2
	elif keyboard.read_key()==3:
		choise==3
	elif keyboard.read_key()==4:
		choise==4
			
	if choise==1:
		counter1=0
		counter2=0
		player=input("Введи действие: ")
		bot=random.choice(s)
		print("Бот выбрал:",bot)
		print("ты "+ player +",бот "+ bot)
		if player=="камень" and bot=="ножницы" or player=="ножницы" and bot=="бумага" or player=="бумага" and bot=="камень":
			print("Игрок победил")
			counter1+=1
			print(f"Счет игрока = {counter1}\nСчет бота = {counter2}")
		elif bot=="камень" and player=="ножницы" or bot=="ножницы" and player=="бумага" or bot=="бумага" and player=="камень":
			print("Бот победил")
			counter2+=1
			print(f"Счет игрока = {counter1}\nСчет бота = {counter2}")
		elif player=="камень" and bot=="камень" or player=="ножницы" and bot=="ножницы" or player=="бумага" and bot=="бумага":
			print("Ничья")

		print("")

	if choise==2:
		counter1=0
		counter2=0
		player1=["a,s,d"]
		player2=["q,w,e"]
		print("Игрок-1 выбирает действие: ")
		if keyboard.read_key()=="a":
			choise1=1
		elif keyboard.read_key()=="s":
			choise1=2
		elif keyboard.read_key()=="d":
			choise1=3
		print("Игрок-2 выбирает действие: ")
		if keyboard.read_key()=="q":
			choise2=1
		elif keyboard.read_key()=="w":
			choise2=2
		elif keyboard.read_key()=="e":
			choise2=3
		print(f"Игрок 1 выбрал {choise1}")
		print(f"Игрок 2 выбрал {choise2}")
		if choise1==1 and choise2==2 or choise1==2 and choise2==3 or choise1==3 and choise2==1:
			print("Игрок - 1 победил")
			counter1+=1
			print(f"Счет игрока 1 = {counter1}\nСчет игрока 2 = {counter2}")
		elif choise2==1 and choise1==2 or choise2==2 and choise1==3 or choise2==3 and choise1==1:
			print("Игрок - 2 победил")
			counter2+=1
			print(f"Счет игрока 1 = {counter1}\nСчет игрока 2 = {counter2}")
		elif choise1==1 and choise2==1 or choise1==2 and choise2==2 or choise1==3 and choise2==3:
			print("Ничья")
		if counter1==5:
			print("Игрок 1 выиграл игру, поздравляю!")
			break
		if counter2==5:
			print("Игрок 2 выиграл игру, поздравляю!")
			break
		choise=""
		print("")

	if choise==3:
		print("Вы должны выбрать один из вариантов: камень, ножницы или бумага.")
		print("Если вы играете с ботом, то бот рандомно выбирает себе действие.")
		print("Если вы играете с другом то вы по очереди выбираете действие и играете.")
		print("")

	if choise==4:
		print("До свидания!")
		break
