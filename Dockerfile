FROM fedora:latest
RUN dnf -y update
RUN dnf -y install python-virtualenv gcc-c++ libxml2-devel libxslt-devel
RUN useradd -ms /bin/bash plone
USER plone 
RUN virtualenv /tmp/plone
WORKDIR /tmp/plone
ADD bootstrap.py /tmp/plone/
ADD buildout.cfg /tmp/plone/

RUN bin/python bootstrap.py --setuptools-version=18.2
RUN bin/buildout
CMD bin/instance fg
