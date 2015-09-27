all: build push

build:
	docker build -t zopyx/plone-50-demo .

push:
	docker push zopyx/plone-50-demo
