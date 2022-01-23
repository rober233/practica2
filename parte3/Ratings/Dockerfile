FROM node:12.18.1-slim
RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install python3-pip -y
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
WORKDIR practica_creativa2/bookinfo/src/productpage
RUN pip3 install -r requirements.txt
WORKDIR practica_creativa2/bookinfo/src/ratings
COPY package.json /opt/microservices/
COPY ratings.js /opt/microservices/

ENV SERVICE_VERSION v1
EXPOSE 9080


CMD ["python3","/opt/microservices/ratings.js","9080"]
