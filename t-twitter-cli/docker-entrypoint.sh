#!/bin/sh

#adduser --disabled-password --gecos "" ${HOST_USER}
#chown -R ${HOST_USER}:${HOST_USER} /home/${HOST_USER}
#su - ${HOST_USER} -c "export LANG=en_US.UTF-8; export LANGUAGE=en_US.UTF-8; export LC_ALL=en_US.UTF-8; $@"
exec "$@"

