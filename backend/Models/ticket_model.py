from django.db import models
from django.conf import settings
from .team_model import Team


class Ticket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    github_username = models.CharField(max_length=50)
    # A description for user's personal projects
    projects_desc = models.TextField(max_length=4000)
    # Known programming languages of the user
    prog_languages = models.CharField(max_length=150)
    # Programming experience
    prog_experience = models.TextField(max_length=2000)
    # URL to the user's facebook profile
    facebook = models.URLField(max_length=200)
    # Complete discord identifier name#xxxx
    discord = models.CharField(max_length=40)
    # Interests of the user
    interests = models.TextField(max_length=2000)
    # TODO add actual university choices
    university_choices = [
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
    university = models.CharField(max_length=30, choices=university_choices)
    # How did the user find out about GDSC
    find_out = models.TextField(max_length=500)
    # Status of the ticket, True=Accepted
    ticket_status = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
