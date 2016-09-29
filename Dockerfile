FROM fedora:latest
RUN dnf -y update
RUN dnf -y install python-virtualenv gcc-c++ libxml2-devel libxslt-devel libjpeg-devel zlib-devel redhat-rpm-config
RUN useradd -ms /bin/bash plone
USER plone 
RUN virtualenv /tmp/plone
WORKDIR /tmp/plone
ADD bootstrap.py /tmp/plone/
ADD buildout.cfg /tmp/plone/
#ADD setup-plone.py /tmp/plone/
USER root
run chown -R plone.plone /tmp/plone
USER plone

RUN bin/python bootstrap.py --setuptools-version=18.2
RUN bin/buildout
USER root
ADD setup-plone.py /tmp/plone/
run chown -R plone.plone /tmp/plone
ADD data /tmp/plone/data
USER plone
RUN bin/instance run setup-plone.py
CMD bin/instance fg

