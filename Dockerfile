FROM haproxy:1.9

RUN apt-get update && apt-get install -y lua-socket