from django.contrib import admin


from vbb_backend.users.models import User, Mentor, Student, HeadMaster

admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(HeadMaster)