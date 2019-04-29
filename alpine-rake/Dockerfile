FROM ruby:2.6.3-alpine3.9

MAINTAINER Scott Lowe <scott.lowe@scottlowe.org>

RUN gem install rake && \
    gem cleanup

ENTRYPOINT ["rake"]
