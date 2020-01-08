from django.shortcuts import render
from django.http import JsonResponse
import requests
import random


def index(request):
    # r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=897")
    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=7")
    print(r.status_code)
    result = r.json()
    

    for element in result['results']:
        idsplit = element['url'].split("/")
        id = idsplit[-2]
        element['id'] = id
        element['name'] = element['name'].upper()
        if 'teamPokemon' not in request.session:
            print("efface tout")
            request.session['teamPokemon'] = []
    context = {'contenu' : result,
    'teamPokemon': request.session['teamPokemon']}
     
    return render(request, "myapp/index.html", context)

def pokemon(request, number):
    # Retourne les valeurs du pokemon depuis l'api
    r = requests.get("https://pokeapi.co/api/v2/pokemon/%d" % number)
    print(r.status_code)
    result = r.json()
    context = {'contenu': result}
    # Va chercher les attaques du pokémon

    ListeAttaques = []
    for attaques in result['moves']:
        ListeAttaques.append(attaques)
        idsplit = attaques['move']['url'].split("/")
        id = idsplit[-2]
        attaques['move']['id'] = id
    AttaqueAffiche = random.sample(ListeAttaques, 4)
    
    attaqueeeee = []
    for element in AttaqueAffiche:
        # Va chercher les carateristiques des attaques des pokémons
        r = requests.get("https://pokeapi.co/api/v2/move/%s" % element['move']['id'])
        attaqueeeee.append(r.json()) 

    context = {'contenu': result,
                'attaques': attaqueeeee,
                 }
    return render(request, "myapp/pokemon.html", context)

def AddPokemon(request, id):
   r = requests.get("https://pokeapi.co/api/v2/pokemon/%d" % id)
   save_session = request.session['teamPokemon']
   save_session.append(r.json())
#   request.session['teamPokemon'].append(r.json())
   request.session['teamPokemon'] = save_session
   print("_________________________________________________________")
   print(request.session['teamPokemon'])
   print("_________________________________________________________")

   return JsonResponse({
       'success': request.session['teamPokemon']
   }, safe=False)