from django.contrib import admin
from moodlog.models import Mood, Action, MoodLog
# Register your models here.
admin.site.register(Mood)
admin.site.register(Action)
admin.site.register(MoodLog)