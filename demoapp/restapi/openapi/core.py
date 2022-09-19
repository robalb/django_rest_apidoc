from rest_framework import (
    RemovedInDRF314Warning, exceptions, renderers, serializers
)
from sys import api_version
from typing import TypedDict
from django.conf import settings
from rest_framework.schemas import get_schema_view as rest_get_schema_view
from rest_framework.schemas.inspectors import ViewInspector
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.views import APIView
import warnings
import inspect

class OpenApiConfig(TypedDict):
    title: str
    description: str
    version: str


def __parse_source_config(title="", description="", version="0.1.0") -> OpenApiConfig:
    """ Utility function used to convert untyped config dicts into an OpenApiConfig
    """
    return OpenApiConfig(
            title=title,
            description=description,
            version=version
            )


def get_config() -> OpenApiConfig:
    """ Returns the global openapi configuration, as set in django settings
    """
    try:
        settings_source = settings.OPENAPI
    except AttributeError:
        settings_source = {}

    return __parse_source_config(**settings_source)


def get_schema_view(**kwargs):
    """ Returns a schema view for the openapi docs.

    This is the same as rest_framework.schemas.get_schema_view
    But it's been configured to use the default openapi settings
    """
    merged_kwargs = get_config() | kwargs
    return rest_get_schema_view(**merged_kwargs)



# Local development testing:
# docker exec -it django_rest_apidoc_django_1 python manage.py shell
#   from rest_framework.schemas.openapi import SchemaGenerator
#   generator = SchemaGenerator(title='Inline test')
#   schema = generator.get_schema()
#
# docker exec -it django_rest_apidoc_django_1 python manage.py openapischema --file remove.yaml
class OpenApiSchema(AutoSchema):
    """ The Openapi per-view introspection logic, that extends the original DRF Autoschema

    Usage: configure Django Rest Framework to use this Class by default, by
           editing the Django global settings:
           REST_FRAMEWORK = {
                # ... YOUR SETTINGS
                'DEFAULT_SCHEMA_CLASS': 'restapi.openapi.core.AutoSchema',
            }
    """

    def get_operation(self, path, method):
        warnings.warn("------get_operation")
        # print(path, method)
        ret = super().get_operation(path, method)
        # print(ret)
        return ret

    def get_response_serializer(self, path, method):
        """ Attempts to detect the response serializer by inspecting method params


        if a parameter response_model is defined with default value set to a valid response model,
        it will be documented as the response serializer.
        Otherwise the default system is used.
        Introspection references: https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object

        Note: This is arguably a bad hack, and a bad idea. a @response_model(Model)
              could be more pythonic way to implement this.

        """
        view = self.view

        method_name = getattr(view, 'action', method.lower())
        method_reference = getattr(view, method_name, None)
        method_parameters = inspect.signature(method_reference).parameters

        if "response_model" not in method_parameters:
            # use the default system used by DRF AutoSchema
            return super().get_response_serializer(path, method)

        obj = method_parameters["response_model"].default

        try:
            return obj()
        except exceptions.APIException:
            warnings.warn('{}.get_serializer() raised an exception during '
                          'schema generation. Serializer fields will not be '
                          'generated for {} {}.'
                          .format(view.__class__.__name__, method, path))
            return None


    def get_request_serializer(self, path, method):
        """ Attempts to detect the request serializer by inspecting the "request" param type annotation


        if the request parameter "request" has the signature type of a serializerclass,
        it will be documented as the request serializer.
        Otherwise the default system is used.
        Introspection references: https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object

        Note: this will require tweaks for compatibility between types.
              a decorator in front of every request method could help
        """
        view = self.view

        method_name = getattr(view, 'action', method.lower())
        method_reference = getattr(view, method_name, None)
        method_parameters = inspect.signature(method_reference).parameters

        if "request" not in method_parameters:
            # use the default system used by DRF AutoSchema
            return super().get_request_serializer(path, method)

        obj = method_parameters["request"].annotation

        try:
            return obj()
        except exceptions.APIException:
            warnings.warn('{}.get_serializer() raised an exception during '
                          'schema generation. Serializer fields will not be '
                          'generated for {} {}.'
                          .format(view.__class__.__name__, method, path))
            return None


