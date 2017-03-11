FROM fedora:latest
RUN dnf -y update
RUN dnf -y install python-virtualenv gcc-c++ libxml2-devel libxslt-devel libjpeg-devel zlib-devel redhat-rpm-config libffi-devel openssl-devel
RUN useradd -ms /bin/bash plone
USER plone 
RUN virtualenv /tmp/plone
WORKDIR /tmp/plone
ADD buildout.cfg /tmp/plone/
#ADD setup-plone.py /tmp/plone/
USER root
run chown -R plone.plone /tmp/plone
USER plone

#RUN bin/python bootstrap.py --setuptools-version=18.2
RUN bin/pip install zc.buildout==2.5.2
RUN bin/buildout bootstrap
RUN bin/buildout
USER root
ADD setup-plone.py /tmp/plone/
ADD setup-smashdocs.py /tmp/plone/
run chown -R plone.plone /tmp/plone
ADD data /tmp/plone/data
USER plone
RUN bin/instance run setup-plone.py
RUN bin/instance run setup-smashdocs.py
CMD bin/instance fg

