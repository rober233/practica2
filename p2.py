#! /usr/bin/python
from subprocess import call
import os
import sys

#Descarga de la aplicacion 

call(['git clone https://github.com/CDPS-ETSIT/practica_creativa2.git'], shell=True)

#Instalamos el gestor de paquetes PIP
call(["sudo apt-get -y update "], shell=True)
call(["sudo apt-get -y install python3-pip "], shell=True)

#Instalamos la lista de dependencias 
call(["sudo pip3 install -r p2/bookinfo/src/productpage/requirements.txt"], shell=True)

#Creamos la variable del entorno
os.environ['GROUP_NUMBER']="18"
num_grupo= str(os.environ.get('GROUP_NUMBER'))

#Modificamos el titulo
fin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'r') # in file
fout = open("productpage1.html", 'w') # out file
for line in fin:
    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
        fout.write("{% block title %} Equipo: "+num_grupo+"{% endblock %}")
    else :
        fout.write(line)
fin.close()
fout.close()

call(["mv","productpage1.html","practica_creativa2/bookinfo/src/productpage/templates/productpage.html"], shell=True)

#Cambiamos el puerto para lanzar la aplicacion


#Lanzamos la aplicacion
call(["sudo python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9088"], shell=True)
