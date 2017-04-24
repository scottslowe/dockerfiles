FROM ruby:2.4.1-alpine

MAINTAINER Scott Lowe <scott.lowe@scottlowe.org>

RUN gem install rake && \
    gem cleanup

ENTRYPOINT ["rake"]
