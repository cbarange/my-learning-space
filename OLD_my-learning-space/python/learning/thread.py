#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading
import multiprocessing
import os
from math import sqrt
import platform

# Ecrire un programme qui attend 10 secondes et affiche 'Bonjour', exécuter la commande pstree avec le pid et l'option ap, utilise la commande ./thread.py &
def exercise_1():
	time.sleep(10)
	print('Bonjour')

# Ecrire un programme qui lance un Thread qui attend 10 secondes et affiche 'Bonjour', et utiliser la commande pstree
def exercise_2():
	t1 = threading.Thread(target=exercise_1)
	t1.start()
	t1.join() # Avec et sans join
	print("exercise_2")

# Ecrire un programme qui lance un processus qui attend 10 secondes et affiche 'Bonjour', utiliser la commande pstree
def exercise_3():
	p1 = multiprocessing.Process(target=exercise_1)
	p1.start()
	#p1.join()
	print("exercise_3")

# Ecrire un programme qui lance un fork qui attend 10 secondes et affiche 'Bonjour', utiliser la commande pstree
def exercise_4():
	p = os.fork() # Uniquement dans un env UNIX
	if(p==0):
		exercise_1()
	else:
		print("exercise_4")
	#os.getpid()
	#os.getppid()

def exercise_5():
	print(platform.machine())
	print(platform.version())
	print(platform.platform())
	print(platform.uname())
	print(platform.system())
	print(platform.processor())
	print()
	print(multiprocessing.cpu_count())

# ps aux
if __name__ == "__main__":
	#multiprocessing.freeze_support() # For windows compatibility
	exercise_5()


# https://docs.python.org/fr/3/library/multiprocessing.html


"""
cbr17@LP5-CBR17-CEM:~$ pstree 6432 -ap
python3,6432 ./thread.py
cbr17@LP5-CBR17-CEM:~$ pstree 6434 -ap
python3,6434 ./thread.py
  └─{python3},6435
cbr17@LP5-CBR17-CEM:~$ pstree 6437 -ap
python3,6437 ./thread.py
  └─python3,6438 ./thread.py
cbr17@LP5-CBR17-CEM:~$

"""


