from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views
from karatekyokushin import views2
from karateshotokan import views3
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^karatekyokushin/', views2.KarateKyokushinMain, name='KarateKyokushinMain'),
    url(r'^karateshotokan/', views3.KarateShotokanMain, name='KarateShotokanMain'),
    url(r'^createShotokan/', views3.KarateShotokanCreate, name='KarateShotokanCreate'),
    url(r'^create/', views2.KarateKyokushinCreate, name='KarateKyokushinCreate'),
    url(r'^createTeam/', views.createTeam, name='CreateTeam'),
    url(r'^signUp/', views.signUp, name='signUp'),
    url(r'^signIn/', views.signIn, name='signIn'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^updateProfile/', views.updateProfile, name='updateProfile'),
    url(r'^tournament/(?P<tournament_id>\d+)/', views2.tournament, name='tournament'),
    url(r'^team/(?P<team_id>\d+)/', views.team, name='team'),
    url(r'^userToAdd/(?P<user_id>\d+) (?P<team_id>\d+)/', views.userToAdd, name='userToAdd'),
    url(r'^playerToAdd/(?P<player_id>\d+) (?P<tournament_id>\d+)/', views2.playerToAdd, name='playerToAdd'),
    url(r'^deletePlayerTour/(?P<player_id>\d+) (?P<tournament_id>\d+)/', views2.deletePlayerTour, name='deletePlayerTour'),
    url(r'^addPlayers/(?P<team_id>\d+)/', views.addPlayers, name='addPlayers'),
    url(r'^addPlayersToTournament/(?P<tournament_id>\d+)/', views2.addPlayersToTournament, name='addPlayersToTournament'),
    url(r'^playerToTeamAccept/(?P<player_id>\d+)/', views.playerToTeamAccept, name='playerToTeamAccept'),
    url(r'^playerToTournamentAccept/(?P<playerT_id>\d+)/', views2.playerToTournamentAccept, name='playerToTournamentAccept'),
    url(r'^user/', views.user, name='user'),
    url(r'^player/(?P<player_id>\d+)/', views2.player, name='player'),
    
)
