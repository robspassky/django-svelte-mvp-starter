from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField(User, through='GroupMember')

class GroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Model(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Prompt(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    version = models.IntegerField()

class SharedPrompt(models.Model):
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_prompts')
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    version = models.IntegerField()
    shared_with_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shared_with_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    version = models.IntegerField()
    rating = models.IntegerField()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

