FROM debian:latest

RUN apt-get update && apt-get -y install firefox-esr

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/slowe && \
    echo "slowe:x:${uid}:${gid}:Scott Lowe,,,:/home/slowe:/bin/bash" >> /etc/passwd && \
    echo "slowe:x:${uid}:" >> /etc/group && \
    mkdir -p /etc/sudoers.d && \
    echo "slowe ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/slowe && \
    chmod 0440 /etc/sudoers.d/slowe && \
    chown ${uid}:${gid} -R /home/slowe

USER slowe
ENV HOME /home/slowe
CMD /usr/bin/firefox
