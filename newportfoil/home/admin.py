from django.contrib import admin

from home import models

# Register your models here.
@admin.register(models.Commit_visit)
class CommitAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'email',
    ordering = '-id',
    list_per_page = 10
    list_max_show_all = 50
    