all: build push

build:
	docker build -t zopyx/plone-52-demo .

build-clean:
	docker build --no-cache=true -t zopyx/plone-52-demo .

push:
	docker push zopyx/plone-52-demo
