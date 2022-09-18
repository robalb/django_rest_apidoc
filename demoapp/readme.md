# built-in openapi schema generation
https://www.django-rest-framework.org/api-guide/schemas/

./manage.py generateschema --file openapi-schema.yml

## caveats

https://www.django-rest-framework.org/api-guide/schemas/#autoschema

Note: The automatic introspection of components, and many operation parameters 
relies on the relevant attributes and methods of GenericAPIView: get_serializer(),
pagination_class, filter_backends, etc. For basic APIView subclasses, default 
introspection is essentially limited to the URL kwarg path parameters for this reason.

https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview


 docker exec -it django_rest_apidoc_django_1 python manage.py shell


# custom schema class

https://www.django-rest-framework.org/community/3.10-announcement/
https://github.com/peeringdb/peeringdb/blob/master/peeringdb_server/api_schema.py

For customizations that you want to apply across the entire API, you can subclass rest_framework.schemas.openapi.SchemaGenerator and provide it as an argument to the generateschema command or get_schema_view() helper function.

https://github.com/tfranzel/drf-spectacular





# usage

## migrations

docker-compose run django python manage.py makemigrations restapi
docker-compose run django python manage.py makemigrations
docker-compose run django python manage.py migrate


## install dependencies

docker-compose run django pip install <depname>


