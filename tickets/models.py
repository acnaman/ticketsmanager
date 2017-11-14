from django.db import models

# Create your models here.

PART_CHOICES = (
    (0, 'Top Tenor'),
    (1, 'Second Tenor'),
    (2, 'Baritone'),
    (3, 'Bass'),
)

CLASSCODE_CHOICES = (
    (0, '一般'),
    (1, '学生'),
    (2, '地方'),
    (3, '地方学生'),
)

PERMISSION_CHOICES = (
    (0, '一般'),
    (1, '管理者'),
    (2, 'システム管理者'),
)

class Member(models.Model):
    #member_id = models.AutoField()
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=60)
    nickname = models.CharField(max_length=30, blank=True)
    part = models.IntegerField(choices=PART_CHOICES)
    tel = models.CharField(max_length=20, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    class_code = models.IntegerField(choices=CLASSCODE_CHOICES)
    permission = models.IntegerField(choices=PERMISSION_CHOICES)
    status = models.IntegerField(default=0)

SEATSTATUS_CHOICES = (
    (0, '未割り当て'),
    (1, '割り当て済み'),
    (2, '販売済み'),
)

class Seat(models.Model):
    #seat_id = models.AutoField()
    status = models.IntegerField(choices=SEATSTATUS_CHOICES)
    owner_member = models.ForeignKey(Member, on_delete=models.CASCADE)
