.PHONY: build
collect_static:
	rm -rf static
	docker-compose run --rm app sh -c "python manage.py collectstatic"

.PHONY: local
local:
	#echo "####################################################"
	#echo ">>>> To start local server with local PostgreSQL, do the followings:"
	#echo ">>>> Define env variable in Dockerfile: ENV USE_LOCAL_POSTGRESQL true"
	#echo ">>>> Undefine env variable in Dockerfile: #ENV USE_GCLOUD_SQL true"
	#echo ">>>> Delete all the containers in Docker dashboard"
	#echo "####################################################"
	docker-compose -f docker-compose-local.yml up --build --remove-orphans

.PHONY: gcsql
gcsql:
	echo "####################################################"
	echo ">>>> To start local server with Cloud SQL, do the followings:"
	echo ">>>> Define env variable in Dockerfile: USE_GCLOUD_SQL true"
	echo ">>>> Undefine env variable in Dockerfile: #ENV USE_LOCAL_POSTGRESQL true"
	echo ">>>> Delete all the containers in Docker dashboard"
	echo "####################################################"
	echo ">>>> USE_LOCAL_POSTGRESQL in Dockerfile must be defined..."
	docker-compose up --build --remove-orphans

.PHONY: deploy
deploy: collect_static
	docker-compose -f docker-compose-deploy.yml run --rm gcloud sh -c "gcloud app deploy --project kakaocall-0929" --build --remove-orphans
