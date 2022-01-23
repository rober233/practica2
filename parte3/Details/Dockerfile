FROM ruby:2.7.1-slim
RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install python3-pip -y
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
WORKDIR practica_creativa2/bookinfo/src/details
ENV SERVICE_VERSION v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE true
EXPOSE 9080
COPY details.rb /opt/microservices/

CMD ["ruby","/opt/microservices/details.rb","9080"]
