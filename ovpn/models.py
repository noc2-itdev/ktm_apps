from django.db import models

class Team(models.Model):
    # define
    opened = '0'
    closed = '1'
    status = [
        (opened, 'mở'),
        (closed, 'đóng'),
    ]
    # fields
    name = models.CharField(max_length=50,unique=True)
    desc = models.TextField()
    block = models.CharField(max_length=1,choices=status,default=opened)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField('Member', related_name='teams')
    routes = models.ManyToManyField('Route', related_name='teams')

    def __str__(self):
        return self.name

class Member(models.Model):
    # define
    opened = '0'
    closed = '1'
    status = [
        (opened, 'mở'),
        (closed, 'đóng'),
    ]
    # fields
    name = models.CharField(max_length=255,unique=True)
    mail = models.EmailField(max_length=255,unique=True)
    desc = models.CharField(max_length=255)
    block = models.CharField(max_length=1,choices=status,default=opened)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Route(models.Model):
    # define
    opened = '0'
    closed = '1'
    status = [
        (opened, 'mở'),
        (closed, 'đóng'),
    ]
    # fields
    subnet = models.CharField(max_length=60)
    desc = models.TextField()
    block = models.CharField(max_length=1,choices=status,default=opened)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subnet