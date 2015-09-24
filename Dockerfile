FROM fedora:latest
RUN dnf -y update
RUN dnf -y install python-virtualenv
RUN virtualenv /tmp/plone
WORKDIR /tmp/plone
ADD bootstrap.py /tmp/plone
ADD buildout.cfg /tmp/plone

RUN bin/python bootstrap.py --setuptools-version=18.2
CMD ls -la
