from django.shortcuts import render, HttpResponse
# from model import search 
import joblib
import pickle
import pandas as pd
import numpy as np
import time
from tqdm import tqdm
import seaborn as sns
from textblob import TextBlob
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
import gc #garbage collector
from pprint import pprint
from Home import form

model = SentenceTransformer('msmarco-distilbert-base-dot-prod-v3')

# with open('search-model.pkl', 'rb') as f:
#     d = pickle.load(f)

data = pd.read_csv('preprocess_dataset.csv')
data.info()
data.shape
data.head()


df = data[['heading','text','url']]
del data

encoded_data = model.encode(df.heading.tolist())
encoded_data = np.asarray(encoded_data.astype('float32'))
index = faiss.IndexIDMap(faiss.IndexFlatIP(768))
index1=faiss.IndexIDMap(faiss.IndexFlatIP(768))
index.add_with_ids(encoded_data, np.array(range(0, len(df))).astype(np.int64))
faiss.write_index(index, 'heading.index')
faiss.write_index(index1,'url.index')


# df.head()

def fetch_info(dataframe_idx):
    info = df.iloc[dataframe_idx]
    meta_dict = {}
    meta_dict['heading'] = info['heading']
    meta_dict['url']=info['url']
    return meta_dict
    
def search(query, top_k, index, model):
    t=time.time()
    query_vector = model.encode([query])
    top_k = index.search(query_vector, top_k)
    print('>>>> Results in Total Time: {}'.format(time.time()-t))
    top_k_ids = top_k[1].tolist()[0]
    top_k_ids = list(np.unique(top_k_ids))
    results =  [fetch_info(idx) for idx in top_k_ids]
    return results

def searchs (request):
    # title = request.GET.get("q", "")
    if q in request.GET:
        q=request.GET['q']
        print(q)
    results=search(title, top_k=5, index=index, model=model)
    d = []
    for r in results:
        d.append(r)
        
    # return(d)

def home_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    # logic of view will be implemented here
        # return render(request, "home.html")
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})
# query="health"
# results=search(query, top_k=5, index=index, model=model)

# for r in results:
#     print(r)

# def search_query(request):
#         title = request.GET.get("s","")
#         print(title)
# #         # results=search(query, top_k=5, index=index, model=model)

# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'myapp/index.html', {'posts': posts})
# # Create your views here.
def index(request):
    return render(request,"index.html")


def help(request):
    return render(request,"help.html")

def about(request):
    return render(request,"about.html")

# def search(query):


    
# class SearchView(ListView):
#     model = search_model
#     template_name = 'search.html'
#     context_object_name = 'all_search_results'

#     def get_queryset(self):
#        result = super(SearchView, self).get_queryset()
#        query = self.request.GET.get('search')
#        if query:
#           postresult = search_model.objects.filter(title__contains=query)
#           result = postresult
#        else:
#            result = None
#        return result