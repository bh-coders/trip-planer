FROM redis:7.2

WORKDIR /redis

COPY init.sh /init.sh
RUN sed -i 's/\r$//g' /init.sh && chmod +x /init.sh

EXPOSE 6379

ENTRYPOINT ["/init.sh"]