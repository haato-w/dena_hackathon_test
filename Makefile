THIS_DIR:=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))

setup-django-in-host: ## pythonは既に入っているものとする 開発をする分にはいらない？（初期化以外）
	pip3 install django
	pip3 install djangorestframework
setup-docker:
	docker build ./ -t django-image
up:
	docker run -v $(THIS_DIR)/systems/web/:/usr/src/app/  --name django-system -it django-image /bin/bash
