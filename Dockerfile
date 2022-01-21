FROM python:3.7.7-slim
  
RUN apt-get update -y
RUN apt-get install git -y
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
COPY edithtml.py bookinfo/src/productpage

WORKDIR bookinfo/src/productpage

RUN pip3 install -r requirements.txt

ENV GROUP_NAME valor_a_pasar_en_run

EXPOSE 9080

CMD ["python3", "edithtml.py"]
