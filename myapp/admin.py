from django.contrib import admin
from .models import News
from .models import Session, Branch, Course, Study  
# Register your models here.
admin.site.register(News)
admin.site.register(Session)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Study)
