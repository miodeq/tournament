from django.contrib import admin
from main.models1 import *
from karatekyokushin.models2 import *

# Register your models here.

admin.site.register(Team)
admin.site.register(User)
admin.site.register(Coach)
admin.site.register(Player)
admin.site.register(PlayerTournament)
admin.site.register(Manager)
admin.site.register(Tournament)
