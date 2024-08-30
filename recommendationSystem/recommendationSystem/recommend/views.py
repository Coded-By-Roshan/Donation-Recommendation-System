from django.shortcuts import render
from django.db import connection
from .models import *
from django.http import JsonResponse
import json
import pandas as pd
from math import sqrt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.db.models import Count

# [7,1] , [5,0]


global sorted_paragraphs


def get_recommend_data(request,pk):
    latest_post_id = []
    latest_post = Posts.objects.all().order_by('-pk').values_list('id')
    for lp in latest_post:
        print(lp[0])
        latest_post_id.append(lp[0])

    try:
        final_data = check_similar_para(pk)
        # we get this data 
        #  [(7, 1.0000000000000007), (1, 0.35269337134192436), (2, 0.28613169175965075), (8, 0.14580296087995107), (9, 0.0)]
        converted_list = [item[0] for item in final_data]
        return JsonResponse((converted_list), safe=False)
    except:
        return JsonResponse(list(latest_post_id), safe=False)


    




def check_similar_para(pk):
    all_para = []
    likes = Likes.objects.filter(uid=pk)
    posts = Posts.objects.all()
    for i in posts:
        all_para.append((i.id,i.description))
    
    liked_postDesc_array = []
    for like in likes:
        if(like.likes == 1):
            pid = like.postid
            liked_post = Posts.objects.filter(id=pid)
            for i in liked_post:
                liked_postDesc_array.append((i.description)) 
    print("likedpost",liked_postDesc_array)
    for j in liked_postDesc_array:  
        similarity_scores = [(id, calculate_similarity(j.lower(), para.lower())) for id,para in all_para]
        sorted_paragraphs = sorted(similarity_scores,key=lambda x: x[1], reverse=True)
    
    return sorted_paragraphs        


def calculate_similarity(paragraph1, paragraph2):
    vectorizer = CountVectorizer().fit_transform([paragraph1, paragraph2])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity(vectors)
    print("similar")
    print(similarity)
    
    return similarity[0][1]


# 11 = [(7, 1.0000000000000007), (1, 0.35269337134192436), (2, 0.28613169175965075), (8, 0.14580296087995107), (9, 0.0)]



















# 8 = [[7, 1.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [8, 0.0]]
 

# 10 = [[3, 1.0], [4, 1.0], [5, 1.0], [1, 0.0], [2, 0.0], [7, 0.0], [8, 0.0]]


# [7,1,2,3,4,5,8]