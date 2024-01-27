FROM ruby:3.3.0-slim-bookworm
RUN apt-get -y update && apt-get -y install vim less && apt-get clean
RUN gem install na
ENV EDITOR vim
WORKDIR /tasks
COPY entrypoint.sh /usr/local/bin/
RUN chmod a+x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
