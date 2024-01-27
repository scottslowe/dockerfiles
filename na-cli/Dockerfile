FROM ruby:3.3.0-slim-bookworm
RUN apt-get -y update && apt-get -y install vim less && apt-get clean
RUN gem install na
RUN groupadd -g 1000 slowe
RUN useradd -d /home/slowe -g 1000 -m -u 1000 slowe
COPY entrypoint.sh /usr/local/bin/
RUN chmod a+x /usr/local/bin/entrypoint.sh
USER slowe
WORKDIR /home/slowe
ENV EDITOR vim
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
