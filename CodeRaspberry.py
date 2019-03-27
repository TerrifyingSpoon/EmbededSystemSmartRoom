import sys     # pour la gestion des parametres
import serial  # bibliotheque permettant la communication serie
import datetime

#On ecrit dans l'interface /dev/ttyUSB0 a 9600 bauds
ser = serial.Serial('/dev/ttyACM0', 9600)

#on  ecrit dans la console serie de l'Arduino la lettre passee en parametre lors de l'execution de la commande :
#ser.write(sys.argv[1])
while 1:
	date = datetime.datetime.now()
	info = ser.readline();
	fichier = open("/var/www/html/temp.csv", "a")
	fichier.write(str(date) + "," + info)
	fichier.close()
	print info;
