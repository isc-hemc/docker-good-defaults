FROM redis:5.0

RUN mkdir /data/redis-volume/ \
    && chown -R redis:redis /data/redis-volume/

COPY ./redis.conf /etc/redis/redis.conf
