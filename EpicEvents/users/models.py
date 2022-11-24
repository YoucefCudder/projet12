from django.contrib.auth.models import Group
from django.db import models


class WorkingTeam(Group):
    team = (("SALES", "SALES"), ("SUPPORT", "SUPPORT"), ("MANAGEMENT", "MANAGEMENT"))

    group = models.CharField(max_length=20, choices=team, default="MANAGEMENT")
    if group == "MANAGEMENT":
        is_staff = True
