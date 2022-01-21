#! /usr/bin/python
from subprocess import call
import os
import sys

cwd = str(os.getcwd())
#Descarga de la aplicacion 

call(['git clone https://github.com/CDPS-ETSIT/practica_creativa2.git'], shell=True)

#Instalamos el gestor de paquetes PIP
call(["sudo apt-get -y update "], shell=True)
call(["sudo apt-get -y install python3-pip "], shell=True)

#Instalamos la lista de dependencias 
call(["sudo pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt"], shell=True)

#Creamos la variable del entorno
os.environ['GROUP_NUMBER']="18"
num_grupo= str(os.environ.get('GROUP_NUMBER'))

#Modificamos el titulo
call(['cp /practica_creativa2/bookinfo/src/productpage/templates/productpage.html '+cwd+'/practica_creativa2/bookinfo/src/productpage/templates/productpage1.html'], shell=True)
copia = open('/practica_creativa2/bookinfo/src/productpage/templates/productpage1.html', 'r')
f = open('/practica_creativa2/bookinfo/src/productpage/templates/productpage.html', 'w')
for line in copia:
    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
        f.write("{% block title %}" + num_grupo + "{% endblock %}")
    else:
        f.write(line)
f.close()

#Lanzamos la aplicacion
call(["sudo python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9088"], shell=True)
