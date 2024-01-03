from django.contrib import admin
from project_app import models as project_models
from ems_app import models as core_models
# Register your models here.

admin.site.register(project_models.ProjectModel)
