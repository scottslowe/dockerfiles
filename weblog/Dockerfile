FROM alpine:3.6

# Metadata for the image
MAINTAINER Scott Lowe <scott.lowe@scottlowe.org>
LABEL maintainer="Scott Lowe <scott.lowe@scottlowe.org>"
LABEL description="Container used for Hugo-based static sites in a CI pipeline"

# Set Hugo version and architecture
ENV HUGO_VERSION="0.25.1"

# Get Hugo
ADD https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz /hugo.tar.gz
RUN tar xzf /hugo.tar.gz && \
    rm /hugo.tar.gz

# Get s3deploy
ADD https://github.com/bep/s3deploy/releases/download/v1.1/s3deploy_1.1_Linux-64bit.tar.gz /s3deploy.tar.gz
RUN tar xzf /s3deploy.tar.gz && \
    rm /README.md && \
    rm /LICENSE && \
    rm /s3deploy.tar.gz

# Expose default Hugo port
EXPOSE 1313

# Set up work area for building site
RUN mkdir /weblog
WORKDIR /weblog
