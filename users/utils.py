from .models import Profile, Skill
from django.db.models import Q


def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    skills = Skill.objects.filter(name__icontains=search_query)
    

    #profiles = Profile.objects.filter(name__icontains = search_query) #no se usan multiples icontains con varios campos porque funciona como un AND no como un OR
    profiles = Profile.objects.distinct().filter(          #el distinct porque sino imprime una instancia del mismo profile por cada tag q tenga el user
        Q(name__icontains = search_query) | 
        Q(short_intro__icontains = search_query) |
        Q(skill__in = skills)
        )
    return profiles, search_query
    
