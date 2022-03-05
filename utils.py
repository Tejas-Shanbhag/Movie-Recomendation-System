import numpy as np
import ast
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def convert_genres(x):
    my_list = []
    x = ast.literal_eval(x)
    for i in x:
        my_list.append(i['name'])
    return my_list
        
def convert_cast(x):
    my_list = []
    x = ast.literal_eval(x)
    for i in x:
        my_list.append(i['name'])
    return my_list[:3]

def get_director(x):
    my_list = []
    x = ast.literal_eval(x)
    for i in x:
        if i['job'] == 'Director':
            my_list.append(i['name'])
            break
    return my_list

def stem_text(x):
    my_list = []
    
    for i in x.split():
        my_list.append(ps.stem(i))
        
    return " ".join(my_list)
    