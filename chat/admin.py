from django.contrib import admin
from .models import Profile, Question, ProfileQuestionMapping, Job, Option
# Register your models here.

admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(ProfileQuestionMapping)
admin.site.register(Job)
admin.site.register(Option)

