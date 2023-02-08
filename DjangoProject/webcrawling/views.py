from django.shortcuts import render
from .models import FiveKeyword
from django.db.models import Q
from .models import FiveKeyword2
from .models import FiveKeyword3
from .models import FiveKeyword4
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Create your views here.


def index(request):
    return render(request, 'webcrawling/home.html')
def first(request):
    return render(request, 'webcrawling/first.html')

def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = FiveKeyword4.objects.filter(Q(name__contains=query))

    return render(request, 'webcrawling/search.html', {'query': query,'products': products})

def my_view(request):
    if request.method == 'POST':
        selected = request.POST.getlist('selected')
        a=[]
        x=[]
        title = selected[0]
        print(selected[0])
        for i in range(1, len(selected)):
            a.append(selected[i])
        #print(a)
        for i in range(0, 2787):
            x.append(FiveKeyword4.objects.get(id=i))
        #print(x)
        output = []
        #latest_question_list = FiveKeyword.objects.order_by('-name')[:5]
        output = [q.name for q in x]
        #print(output)
        output2 = [q.five_keyword for q in x]
        for i in range(0, 2787):
            if output[i] == title:
                output2[i] = selected[1] + ',' + selected[2] + ',' + selected[3]
        print(output)
        print(output2)


        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(output2)
        #print(tfidf_matrix.shape)
        
        cosine_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
        #print(cosine_matrix)

        np.round(cosine_matrix, 4)

        book2id = {}
        for i, c in enumerate(output): book2id[i] = c

        # id와 book title를 매핑할 dictionary를 생성해줍니다.
        id2book = {}
        for i, c in book2id.items(): id2book[c] = i

        #print(book2id)
        #print(id2book)

        # Toy Story의 id 추출

        idx = id2book[title]  # post 받은 인덱스
        print(idx)
        sim_scores = [(i, c) for i, c in enumerate(cosine_matrix[idx]) if i != idx]  # 자기 자신을 제외한 책들의 유사도 및 인덱스를 추출
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # 유사도가 높은 순서대로 정렬
        sim_scores[0:5]  # 상위 10개의 인덱스와 유사도를 추출

        #sim_scores = [(book2id[i], score) for i, score in sim_scores[0:5]]
        sim_scores = [ book2id[i] for i, score in sim_scores[0:5]]
        #print(sim_scores)

    return render(request, 'webcrawling/cosine.html', {'selected' : selected, 'sim_scores' : sim_scores})