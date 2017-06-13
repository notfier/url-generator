MANAGE := python manage.py


# python
run:
	( \
		source .env/bin/activate; \
		$(MANAGE) runserver; \
	)
makemigrations:
	( \
		source .env/bin/activate; \
		$(MANAGE) makemigrations; \
	)
migrate:
	( \
		source .env/bin/activate; \
		$(MANAGE) migrate; \
	)
test:
	( \
		source .env/bin/activate; \
		$(MANAGE) test; \
	)
shell:
	$(MANAGE) shell
createsuperuser:
	echo "from django.contrib.auth.models import User; " \
		 "User.objects.create_superuser('admin', 'admin@admin.com', 'admin');" | make shell
install:
	( \
		rm -r .env; \
		virtualenv .env -p python3 --no-site-packages; \
		source .env/bin/activate; \
		pip install -r requirements_dev.txt; \
		make makemigrations; \
		make migrate; \
		make createsuperuser; \
	)
install_and_run:
	make install
	make run

