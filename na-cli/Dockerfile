FROM ruby:3.4.8-alpine
RUN apk --no-cache add vim fzf less shadow
RUN gem install na
RUN groupadd -g 1000 slowe
RUN useradd -d /home/slowe -g 1000 -m -u 1000 slowe
COPY entrypoint.sh /usr/local/bin/
RUN chmod a+x /usr/local/bin/entrypoint.sh
USER slowe
WORKDIR /home/slowe
ENV EDITOR=vim
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
