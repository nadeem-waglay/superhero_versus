from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from django.conf import settings
from .models import Superhero


class superheroView(APIView):
    def get(self, request):
        r = requests.get(settings.SUPERHERO_API + '1/powerstats')
        print(r.status_code)
        print(r.json()['name'])
        return Response({'test': 'working'})


class superheroVersusView(APIView):
    def get(self, request, name_a, name_b, stat='average'):
        superhero_a = Superhero.objects.filter(name__iexact=name_a)

        if not superhero_a:
            print(name_a+' not in db')
            try:
                superhero_a_results = requests.get(settings.SUPERHERO_API + 'search/' + name_a).json()['results']
                print('adding '+name_a+' to db')
                for result in superhero_a_results:
                    superhero_a, _ = Superhero.objects.get_or_create(
                        id=result['id'],
                        name=result['name'],
                        full_name=result['biography']['full-name'],
                        intelligence=result['powerstats']['intelligence'],
                        strength=result['powerstats']['strength'],
                        speed=result['powerstats']['speed'],
                        durability=result['powerstats']['durability'],
                        power=result['powerstats']['power'],
                        combat=result['powerstats']['combat'],
                    )

            except Exception:
                return Response({'response' : 'error', 'error' : 'superhero '+name_a+' does not exist'})
        else:
            superhero_a = superhero_a[0]

        superhero_b = Superhero.objects.filter(name__iexact=name_b)
        if not superhero_b:
            print(name_b+' not in db')
            try:
                superhero_b_results = requests.get(settings.SUPERHERO_API + 'search/' + name_b).json()['results']
                print('adding '+name_b+' to db')
                for result in superhero_b_results:
                    superhero_b, _ = Superhero.objects.get_or_create(
                        id=result['id'],
                        name=result['name'],
                        full_name=result['biography']['full-name'],
                        intelligence=result['powerstats']['intelligence'],
                        strength=result['powerstats']['strength'],
                        speed=result['powerstats']['speed'],
                        durability=result['powerstats']['durability'],
                        power=result['powerstats']['power'],
                        combat=result['powerstats']['combat'],
                    )
            except Exception:
                return Response({'response' : 'error', 'error' : 'superhero '+name_b+' does not exist'})
        else:
            superhero_b = superhero_b[0]

        stat_adjective_map = {
            'strength': 'stronger',
            'intelligence': 'smarter',
            'speed': 'faster',
            'durability': 'more durable',
            'power': 'more powerful',
            'combat': 'a better fighter',
            'average': 'better overall',
        }

        if getattr(superhero_a, stat) > getattr(superhero_b, stat):
            return Response({
                'result': superhero_a.name + ' is ' + stat_adjective_map[stat] + ' than ' + superhero_b.name, # noqa: 501
                superhero_b.name: getattr(superhero_b, stat),
                superhero_a.name: getattr(superhero_a, stat),
                })
        else:
            return Response({
                'result': superhero_b.name + ' is ' + stat_adjective_map[stat] + ' than ' + superhero_a.name, # noqa: 501
                superhero_b.name: getattr(superhero_b, stat),
                superhero_a.name: getattr(superhero_a, stat),
                })
