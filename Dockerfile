FROM python:3.7.7-slim
RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install python3-pip -y
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
WORKDIR practica_creativa2/bookinfo/src/productpage
RUN pip3 install -r requirements.txt
ENV GROUP_NUMBER 18
EXPOSE 9080
COPY modificarhtml.py .

CMD ["python3","modificarhtml.py"]
