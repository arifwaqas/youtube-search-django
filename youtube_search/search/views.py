from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from search.models import ResultModel
from search.serializers import ResultModelSerializer

from django.conf import settings
from django.shortcuts import render, redirect

@csrf_exempt
def postdata(request):
    if request.method=='POST':
        results_data=JSONParser().parse(request)
        print(results_data)
        results_serializer=ResultModelSerializer(data=results_data)
        if results_serializer.is_valid():
            results_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Failed", safe=False)

def index(request):
    videos = []

    
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    search_params = {
        'part' : 'snippet',
        'q' : 'official',
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'maxResults' : 9,
        'type' : 'video'
    }

    r = requests.get(search_url, params=search_params)

    results = r.json()['items']

    video_ids = []
    for result in results:
        video_ids.append(result['id']['videoId'])

    video_params = {
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'part' : 'snippet,contentDetails',
        'id' : ','.join(video_ids),
        'maxResults' : 9
    }

    r = requests.get(video_url, params=video_params)

    results = r.json()['items']

    for result in results:
        video_data = {
            'title' : result['snippet']['title'],
            'id' : result['id'],
            'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
            #'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'thumbnail' : result['snippet']['thumbnails']['high']['url']
        }

        videos.append(video_data)
        
        
    video_paginator = Paginator(videos, 3)

    page=request.GET.get('page')


    try:
        video_page=video_paginator.page(page)
    except PageNotAnInteger:
        video_page=video_paginator.page(1)
    except EmptyPage:
        video_page=video_paginator.page(video_paginator.num_pages)

    context = {
        'videos' : video_page
    }

    return render(request, 'search/index.html', context)