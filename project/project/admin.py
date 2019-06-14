from django.contrib import admin
from .models import Organisation, WikiPage, Task, Review, Profile
  
admin.site.register(Organisation)
admin.site.register(WikiPage)
admin.site.register(Task)
admin.site.register(Review)
admin.site.register(Profile)

print("test")
