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
