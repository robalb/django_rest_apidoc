from django.core.management.base import BaseCommand
from django.utils.module_loading import import_string

from rest_framework import renderers
from rest_framework.schemas.openapi import SchemaGenerator
from restapi.openapi.core import get_config


class Command(BaseCommand):
    """
    This management command is a copy of DRF generateschema
    https://github.com/encode/django-rest-framework/rest_framework/management/commands/generateschema.py

    The legacy coreapi options have been removed, and support for specifying the api version
    has been added via the --apiversion argument

    """
    help = "A fine-tuned version of DRF generateschema"


    def add_arguments(self, parser):
        config = get_config()
        parser.add_argument('--title', dest="title", default=config["title"], type=str)
        parser.add_argument('--url', dest="url", default=None, type=str)
        parser.add_argument('--description', dest="description", default=config['description'], type=str)
        parser.add_argument('--apiversion', dest="version", default=config['version'], type=str)
        parser.add_argument('--format', dest="format", choices=['openapi', 'openapi-json'], default='openapi', type=str)
        parser.add_argument('--urlconf', dest="urlconf", default=None, type=str)
        parser.add_argument('--generator_class', dest="generator_class", default=None, type=str)
        parser.add_argument('--file', dest="file", default=None, type=str)

    def handle(self, *args, **options):
        if options['generator_class']:
            generator_class = import_string(options['generator_class'])
        else:
            generator_class = self.get_generator_class()
        generator = generator_class(
            url=options['url'],
            title=options['title'],
            description=options['description'],
            urlconf=options['urlconf'],
            version=options['version']
        )
        schema = generator.get_schema(request=None, public=True)
        renderer = self.get_renderer(options['format'])
        output = renderer.render(schema, renderer_context={})

        if options['file']:
            with open(options['file'], 'wb') as f:
                f.write(output)
        else:
            self.stdout.write(output.decode())

    def get_renderer(self, format):
        renderer_cls = {
            'openapi': renderers.OpenAPIRenderer,
            'openapi-json': renderers.JSONOpenAPIRenderer,
        }[format]
        return renderer_cls()

    def get_generator_class(self):
        return SchemaGenerator