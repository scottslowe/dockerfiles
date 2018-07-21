FROM node:6.14.3-alpine

LABEL maintainer "Scott Lowe <scott.lowe@scottlowe.org>"

RUN apk add --no-cache git

RUN npm install -qg raml-cli && \
    npm cache clean

RUN mkdir -p /data
VOLUME /data
WORKDIR /data

ENTRYPOINT ["raml"]

CMD ["--help"]
