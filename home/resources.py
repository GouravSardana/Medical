from import_export import resources
from .models import Medical_Library


class PersonResource(resources.ModelResource):
    class Meta:
        model = Medical_Library