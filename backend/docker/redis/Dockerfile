FROM redis:7.2

WORKDIR /redis

COPY redis.conf /usr/local/etc/redis/redis.conf

COPY init.sh ./

RUN chmod +x ./init.sh

EXPOSE 6379

CMD ["./init.sh"]