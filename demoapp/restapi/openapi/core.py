from typing import TypedDict
from django.conf import settings


class OpenApiConfig(TypedDict):
    title: str
    description: str
    version: str


def __parse_source_config(title="", description="", version="1.0.0") -> OpenApiConfig:
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



