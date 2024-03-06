FROM redis:7.2

WORKDIR /redis

COPY init.sh ./

RUN chmod +x ./init.sh

EXPOSE 6379

CMD ["./init.sh"]