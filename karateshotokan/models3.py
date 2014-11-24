from django.db import models
from django.dispatch import receiver
from django.template.defaultfilters import slugify

# Create your models here.

class Team(models.Model):
    teamName = models.CharField(max_length=50)
    teamPlayedTimes = models.PositiveIntegerField() #ile razy drużyna brała udział
    teamTogetherWon = models.PositiveIntegerField() #wygrane konkurencje drużynowe
    teamTogetherLost = models.PositiveIntegerField() #przegrane konkurencje drużynowe
    teamDrawn = models.PositiveIntegerField() #remisy
    teamPointsFor = models.PositiveIntegerField() #przyznane przez sedziow punkty za
    teamPointsAgainst = models.PositiveIntegerField() #przyznane przez sedziow punkty przeciwko

    team = models.ForeignKey('', related_name='')
    slug = models.SlugField(editable=False, uniqe=True)

    def __unicode__(self):
        return self.teamName

@receiver(models.signals.pre_save, sender=Team)
def team_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.nameTeam)


class Player(models.Model):
    playerName = models.CharField(max_length=50)
    playerSurname = models.CharField(max_length=50)
    playerColor = models.CharField(max_length=20, choices = (
                                   ('AKA', 'Czerwony'),
                                   ('AO', 'Niebieski'),
    ))
#playerWeight = models.PositiveIntegerField()
    team = models.ForeignKey(Team, related_name='players')
    slug = models.SlugField(editable=False)

    def __unicode__(self):
        ret = self.playerSurname + ", " + self.playerName + " (" + self.team + ")"
        return return

@receiver(models.signals.pre_save, sender=Player)
def player_handler(sender, instance, *args, **kwargs):
    name = instance.playerSurname + ' ' + instance.playerName[0]
    instance.slug = slugify(name)


                                   

