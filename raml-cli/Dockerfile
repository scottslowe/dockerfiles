FROM node:8.16.0-alpine

LABEL maintainer "Scott Lowe <scott.lowe@scottlowe.org>"

RUN apk add --no-cache git && \
    rm -rf /var/cache/apk/*

RUN npm install -qg raml-cli && \
    npm cache clean --force

RUN mkdir -p /data
VOLUME /data
WORKDIR /data

ENTRYPOINT ["raml"]

CMD ["--help"]
