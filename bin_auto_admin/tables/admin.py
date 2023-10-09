from .models import File
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# @admin.register(File)
# class FileAdmin(admin.ModelAdmin):
#     list_display = ('file_name', 'description', 'file_link', 'price', 'created_at', 'updated_at')
#     search_fields = ('file_name', 'description')
#     list_filter = ('created_at', 'updated_at')
#     ordering = ('-created_at',)

# класс обработки данных
class FileResource(resources.ModelResource):

    class Meta:
        model = File
        exclude = ('id', 'created_at, ')

# вывод данных на странице
class FileAdmin(ImportExportModelAdmin):
    resource_classes = [FileResource]
    list_display = ('file_name', 'description', 'file_link', 'price', 'created_at', 'updated_at')
    search_fields = ('file_name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(File, FileAdmin)