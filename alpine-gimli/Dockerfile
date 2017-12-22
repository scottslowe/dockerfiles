FROM ruby:2.4.3-alpine3.6

MAINTAINER Scott Lowe <scott.lowe@scottlowe.org>
LABEL maintainer="Scott Lowe <scott.lowe@scottlowe.org>"

ENV VERSION=0.6.0.pre

RUN apk --no-cache update && \
    apk --no-cache add build-base libc-dev libxml2-dev libxslt-dev libxslt && \
    gem install gimli --version ${VERSION} --no-format-exec && \
    apk --no-cache del build-base libc-dev libxml2-dev libxslt-dev

wORKDIR /tmp

ENTRYPOINT ["gimli"]
CMD ["--help"]
