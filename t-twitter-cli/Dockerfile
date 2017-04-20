FROM fedora:25

MAINTAINER Scott Lowe <scott.lowe@scottlowe.org>

ADD docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod a+x /docker-entrypoint.sh

RUN dnf makecache && \
    dnf -y install ruby-devel make gcc gcc-c++ redhat-rpm-config && \
    gem install t --no-rdoc --no-ri && \
    gem cleanup && \
    dnf -y remove make gcc gcc-c++ redhat-rpm-config && \
    dnf autoremove && \
    dnf clean all

EXPOSE 9001

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/local/bin/t"]
