from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect

from karatekyokushin.forms import *

# Create your views here.

def KarateKyokushinMain(request):
    template = loader.get_template('main.html')
#    latest_seasons = Season.objects.order_by('-id')[:10]
#    latest_rounds = Round.objects.order_by('-id')[:10]
#    latest_matchday = Matchday.objects.order_by('-id')[:10]
#    latest_matches = Match.objects.order_by('-id')[:10]
    context = RequestContext(request, {
#       'latest_matches': latest_matches,
#       'latest_seasons': latest_seasons,
#       'latest_rounds': latest_rounds,
#        'latest_matchday': latest_matchday,
    })
    return HttpResponse(template.render(context))

def KarateKyokushinCreate(request):
    
    #    if request.method == 'POST':
    #        form = CreateTournamentForm(request.POST)
    #        if form.is_valid():
    #            form.save()
    #    else:
    #        form = CreateTournamentForm()
    #    return render(request, 'createtournament.html', {
    #        'form': form, 
    #    })
    if 'user' in request.session:
        template = loader.get_template('createtournament.html')
        
        if request.method == 'POST':
            form = CreateTournamentForm(request.POST)
            if form.is_valid():
                user = User.objects.get(id=request.session['user'])
                instance=form.save()#instance zawiera zapisany obiekt, takze z jego id
                Manager.objects.create(user_id=user, tournament = instance)
                return redirect('/user/')
        else:
           form = CreateTournamentForm()
        
    #    latest_seasons = Season.objects.order_by('-id')[:10]
    #    latest_rounds = Round.objects.order_by('-id')[:10]
    #    latest_matchday = Matchday.objects.order_by('-id')[:10]
    #    latest_matches = Match.objects.order_by('-id')[:10]
        context = RequestContext(request, {
            'form': form,
    #       'latest_matches': latest_matches,
    #       'latest_seasons': latest_seasons,
    #       'latest_rounds': latest_rounds,
    #        'latest_matchday': latest_matchday,
        })
        return HttpResponse(template.render(context))
    else: 
        return redirect('/signIn/')

def tournament(request, tournament_id):
    template = loader.get_template('tournament.html')
    tournament = Tournament.objects.get(id=tournament_id)
    manager = Manager.objects.get(tournament=tournament)
    teams = list()
    players = list()
    playersT = PlayerTournament.objects.filter(tournament_id=tournament, acceptedbymanager=True, acceptedbycoach=True)
    for playerT in playersT:
        player = playerT.player_id
        players.append(player)
        teams.append(Team.objects.get(id=player.team_id.id))
    context = RequestContext(request, {'tournament': tournament, 'teams': teams, 'players':players, 'manager':manager })
    return HttpResponse(template.render(context))

def player(request, player_id):
    template = loader.get_template('player.html')
    player = Player.objects.get(id=player_id)
    team = Team.objects.get(id=player.team_id.id)
    coach = Coach.objects.get(id=team.coach.id)
    playersT = PlayerTournament.objects.get(player_id=player)
    context = RequestContext(request, {'playersT': playersT, 'team': team, 'player':player, 'coach': coach,})
    return HttpResponse(template.render(context))

def addPlayersToTournament(request, tournament_id):
    if 'user' in request.session:
        template = loader.get_template('addPlayerToTournament.html')
        tournament = Tournament.objects.get(id=tournament_id)
        players = Player.objects.filter(acceptedbycoachteam=True, acceptedbyplayer=True)
        for playerT in PlayerTournament.objects.filter(tournament_id=tournament):
            players = players.exclude(id=playerT.player_id.id)
        context = RequestContext(request, {'tournament': tournament, 'players':players })
        return HttpResponse(template.render(context))
    else: 
        return redirect('/signIn/')

def playerToAdd(request, player_id, tournament_id):
    player = Player.objects.get(id=player_id)
    tournament = Tournament.objects.get(id=tournament_id)
    p=PlayerTournament.objects.create(player_id=player, tournament_id=tournament, acceptedbymanager=True, acceptedbycoach=False)
    return redirect('addPlayersToTournament', tournament_id = tournament.id)

def playerToTournamentAccept(request, playerT_id):
    PlayerTournament.objects.filter(id=playerT_id).update(acceptedbycoach = True)
    p = PlayerTournament.objects.get(id=playerT_id)
    p.tournament_id.coaches.add(Coach.objects.get(id = Team.objects.get(id= p.player_id.team_id.id).coach.id))
    return redirect('/user/')

def deletePlayerTour(request, player_id, tournament_id):
    player = Player.objects.get(id = player_id)
    tournament = Tournament.objects.get(id = tournament_id)
    coach = Coach.objects.get(id = Team.objects.get(id = player.team_id.id).coach.id)
    tournament.coaches.remove(coach)
    playerT = PlayerTournament.objects.get(player_id = player, tournament_id=tournament).delete()
    return redirect('tournament', tournament_id = tournament.id)
    
    