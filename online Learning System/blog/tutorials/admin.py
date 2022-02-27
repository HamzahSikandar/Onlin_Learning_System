from django.contrib import admin
from tutorials.models import Course,Topics
# Register your models here.
admin.site.register(Course)


@admin.register(Topics)
class PostTopics(admin.ModelAdmin):
    class Media:
        js=('js/tiny_blog.js',)