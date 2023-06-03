from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Group, GroupMember, Model, Prompt, SharedPrompt, Rating, Message

admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Model)
admin.site.register(Prompt)
admin.site.register(SharedPrompt)
admin.site.register(Rating)
admin.site.register(Message)

class UserAdmin(DefaultUserAdmin):
    search_fields = ('name',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')
    search_fields = ('name',)

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
