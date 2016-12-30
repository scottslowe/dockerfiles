FROM ubuntu:latest
MAINTAINER Scott Lowe <scott.lowe@scottlowe.org>

RUN apt-get update && apt-get -y install firefox --no-install-recommends && \
    rm -rf /var/lib/apt/lists*

ENV LANG en-US
ENTRYPOINT [ "/usr/bin/firefox" ]
