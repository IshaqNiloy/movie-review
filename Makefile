run:
	python3 manage.py runserver 8080

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

freeze:
	pip3 freeze > requirements.txt

install-requirements:
	pip3 install -r requirements.txt

create-super-user:
	python3 manage.py runscript create_super_user

