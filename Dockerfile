FROM fedora:latest
MAINTAINER Andreas Jung <info@zopyx.com>
RUN dnf -y update
RUN dnf -y install python-virtualenv
RUN virtualenv plone
WORKDIR plone
ADD bootstrap.py plone 
COPY buildout.cfg plone 
CMD ls -la
