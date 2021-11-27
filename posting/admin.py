from django.contrib import admin
from .models import Post, Category, Comment,Reliability

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ReliabilityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Reliability, ReliabilityAdmin)