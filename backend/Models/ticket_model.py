from django.db import models
from django.conf import settings


class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    github_username = models.CharField(max_length=50)
    projects_desc = models.TextField(max_length=4000)
    prog_languages = models.CharField(max_length=150)
    prog_experience = models.TextField(max_length=2000)
    # TODO mkae facebook a URL field
    facebook = models.CharField(max_length=200)
    discord = models.CharField(max_length=40)
    interests = models.TextField(max_length=2000)
    # TODO
    gdsc_teams = [
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
         ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
         ),
        ('unknown', 'Unknown'),
    ]
    teams = models.CharField(max_length=30, choices=gdsc_teams)
    faculta_profil = [
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
         ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
         ),
        ('unknown', 'Unknown'),
    ]
    facultate = models.CharField(max_length=30, choices=faculta_profil)
    # HOW DID YOU FIND OUT ABOUT GDSC ?
    find_out = models.TextField(max_length=500)
    ticket_status = models.BooleanField(default=False)
    # TODO Implement dunder methods
