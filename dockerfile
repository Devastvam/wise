FROM ubuntu:latest  

WORKDIR /app  

COPY wisecow.sh .  

RUN chmod +x wisecow.sh  

CMD ["/app/wisecow.sh"]  
