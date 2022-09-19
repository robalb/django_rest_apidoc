from typing import TypedDict
from django.conf import settings
from rest_framework.schemas import get_schema_view as rest_get_schema_view


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
    """
    merged_kwargs = get_config() | kwargs
    return rest_get_schema_view(**merged_kwargs)



