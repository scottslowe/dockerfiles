FROM node:6.14.3-alpine

LABEL maintainer "Scott Lowe <scott.lowe@scottlowe.org>"

RUN apk add --no-cache git && \
    rm -rf /var/cache/apk/*

RUN npm install -qg raml2html && \
    npm cache clean

RUN mkdir -p /data
VOLUME /data
WORKDIR /data

ENTRYPOINT ["raml2html"]

CMD ["-h"]
