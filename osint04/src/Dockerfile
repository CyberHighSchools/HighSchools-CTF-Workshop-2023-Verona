FROM debian:bookworm-slim as base

RUN apt-get update -qqy && \
    apt-get install -qqy \
    tor \
    curl \
    git \
    net-tools \
    python3 \
    vim \
    ruby-full \
    build-essential


RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/*

COPY ./entrypoint.sh /entrypoint.sh

# setup tor
ARG HOSTNAME
ENV HOSTNAME=${HOSTNAME}
COPY ./${HOSTNAME}/ /var/lib/tor/${HOSTNAME}/
RUN chmod 700 /var/lib/tor/${HOSTNAME}/
RUN chown -R root:root /var/lib/tor/
RUN sed -i 's|#HiddenServiceDir /var/lib/tor/hidden_service/|HiddenServiceDir /var/lib/tor/'"$HOSTNAME"'|' /etc/tor/torrc
RUN sed -i 's|#HiddenServicePort 80 127.0.0.1:80|HiddenServicePort 80 127.0.0.1:4000|' /etc/tor/torrc
RUN sed -i '1s/^/SocksPort 0.0.0.0:8050\n/' /etc/tor/torrc

COPY ./src/ /var/www/html/
WORKDIR /var/www/html/
RUN gem install jekyll bundler
RUN bundle install

ENTRYPOINT [ "/entrypoint.sh" ]