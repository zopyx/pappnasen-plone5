FROM fedora:latest
RUN dnf -y update
RUN dnf -y install python-virtualenv gcc-c++ libxml2-devel libxslt-devel libjpeg-devel zlib-devel redhat-rpm-config libffi-devel openssl-devel file python-devel
RUN useradd -ms /bin/bash plone
RUN virtualenv --clear /tmp/plone
WORKDIR /tmp/plone
ADD bootstrap.py /tmp/plone/
ADD buildout.cfg /tmp/plone/
ADD requirements.txt /tmp/plone/
RUN chown -R plone /tmp/plone
USER plone 
RUN bin/pip install -r requirements.txt
#ADD setup-plone.py /tmp/plone/
USER root
run chown -R plone.plone /tmp/plone
USER plone
RUN bin/buildout
USER root
ADD setup-plone.py /tmp/plone/
#ADD setup-smashdocs.py /tmp/plone/
ADD data /tmp/plone/data
run chown -R plone.plone /tmp/plone
USER plone
RUN bin/instance run setup-plone.py
#RUN bin/instance run setup-smashdocs.py
CMD bin/instance fg

