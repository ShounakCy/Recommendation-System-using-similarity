#Import libraries
# encoding: utf-8
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import pandas as pd
from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
#import sys
from flask import Flask
#from flask import jsonify
import json
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('engine.html')

@app.route('/recommendations/<sku>')
def recommendations(sku):
    
    df = pd.read_excel("output2.xlsx").fillna("")
    df = df[['SKU','Title','Design','Performance','Finish','Blades','Sweep size',
             'Color','Price','Air Delivery','Gallery_Image','BuyNowURL','UnderLight']]
      
    
    class Product:
        def __init__(self,sku,title,price,image,link):
            self.sku = sku
            self.title = title
            self.price = price
            self.image = image
            self.link = link     
            
    
###############################################################################
            
    df_SKU =df.copy()
    df_SKU = df_SKU[['SKU']] 
    
    df_Image =df.copy()
    df_Image = df_Image[['Gallery_Image']]
    
    df_Link =df.copy()
    df_Link = df_Link[['BuyNowURL']]
        
###############################################################################

    df_Title = df.copy()
    df_Title = df_Title[['Title']]
    df_Title['Title'] = df_Title['Title'].map(lambda x: x.split(' '))
    
    df_Title['bag_of_words'] = ''
    columns = df_Title.columns
    for index, row in df_Title.iterrows():
        words = ''
        for col in columns:
            words = words + ' '.join(row[col])+ ' '
        row['bag_of_words'] = words
        
    df_Title.drop([col for col in df_Title.columns if col!= 'bag_of_words'], 
                  axis=1,inplace = True)
    
    count = CountVectorizer()
    count_matrix_Title = count.fit_transform(df_Title['bag_of_words'])
    
    cosine_sim_Title = cosine_similarity(count_matrix_Title, count_matrix_Title)
    cosine_sim_Title = cosine_sim_Title* 0.216666667




    
###############################################################################
    df_Design = df.copy()
    df_Design = df_Design[['Design']]
    
    df_Design['design'] = ""
    for index, row in df_Design.iterrows():
        Design = row['Design']
        r = Rake()
        r.extract_keywords_from_text(Design)
        key_words_dict_scores = r.get_word_degrees()
        row['design'] = list(key_words_dict_scores.keys())
    df_Design.drop(['Design'], axis=1,inplace = True)  
    
    df_Design['bag_of_words'] = ''
    columns = df_Design.columns
    for index, row in df_Design.iterrows():
        words = ''
        for col in columns:
            words = words + ' '.join(row[col])+ ' '
        row['bag_of_words'] = words
        
    df_Design.drop([col for col in df_Design.columns if col!= 'bag_of_words'], 
                   axis=1,inplace = True)
    
    count_matrix_Design = count.fit_transform(df_Design['bag_of_words'])
    
    cosine_sim_Design = cosine_similarity(count_matrix_Design, count_matrix_Design)
    cosine_sim_Design = cosine_sim_Design* 0.116666667




    
###############################################################################
    df_Performance = df.copy()
    df_Performance = df_Performance[['Performance']]
    
    df_Performance['performance'] = ""
    for index, row in df_Performance.iterrows():
        Performance = row['Performance']
        r = Rake()
        r.extract_keywords_from_text(Performance)
        key_words_dict_scores = r.get_word_degrees()
        row['performance'] = list(key_words_dict_scores.keys())
    df_Performance.drop(['Performance'], axis=1,inplace = True)  
    
    df_Performance['bag_of_words'] = ''
    columns = df_Performance.columns
    for index, row in df_Performance.iterrows():
        words = ''
        for col in columns:
            words = words + ' '.join(row[col])+ ' '
        row['bag_of_words'] = words
        
    df_Performance.drop([col for col in df_Performance.columns if col!= 'bag_of_words'],
                        axis=1,inplace = True)
    
    count_matrix_Performance = count.fit_transform(df_Performance['bag_of_words'])
    
    cosine_sim_Performance= cosine_similarity(count_matrix_Performance, count_matrix_Performance)
    cosine_sim_Performance = cosine_sim_Performance* 0.083333333



    
###############################################################################
    df_Finish = df.copy()
    df_Finish = df_Finish[['Finish']]
    
    df_Finish['finish'] = ""
    for index, row in df_Finish.iterrows():
        Finish = row['Finish']
        r = Rake()
        r.extract_keywords_from_text(Finish)
        key_words_dict_scores = r.get_word_degrees()
        row['finish'] = list(key_words_dict_scores.keys())
    df_Finish.drop(['Finish'], axis=1,inplace = True)  
    
    df_Finish['bag_of_words'] = ''
    columns = df_Finish.columns
    for index, row in df_Finish.iterrows():
        words = ''
        for col in columns:
            words = words + ' '.join(row[col])+ ' '
        row['bag_of_words'] = words
        
    df_Finish.drop([col for col in df_Finish.columns if col!= 'bag_of_words'],
                   axis=1,inplace = True)
    
    count_matrix_Finish = count.fit_transform(df_Finish['bag_of_words'])
    
    cosine_sim_Finish= cosine_similarity(count_matrix_Finish, count_matrix_Finish)
    cosine_sim_Finish = cosine_sim_Finish* 0.1




    
###############################################################################
    df_Blades =df.copy()
    df_Blades = df_Blades[['Blades']]
    
    tmpBlades = df_Blades['Blades'].values.reshape(-1,1)
    from scipy.spatial.distance import cdist
    cosine_dist_Blades= cdist(tmpBlades, tmpBlades, metric= 'euclidean')
    cosine_dist_Blades = (1-(cosine_dist_Blades/cosine_dist_Blades.max()))*0.1




    
###############################################################################
    df['Sweep size'] =  df['Sweep size'].map(lambda x: x.replace('mm',''))
    df_Sweep = df.copy()
    df_Sweep = df_Sweep[['Sweep size']]
    
    tmpSweep = df_Sweep['Sweep size'].values.reshape(-1,1)
    from scipy.spatial.distance import cdist
    cosine_dist_Sweep= cdist(tmpSweep, tmpSweep, metric= 'euclidean')
    cosine_dist_Sweep = (1-(cosine_dist_Sweep/cosine_dist_Sweep.max()))*0.033333333




    
###############################################################################
    
    df_Color = df.copy()
    df_Color = df_Color[['Color']]
    df_Color['Color'] =  df_Color['Color'].map(lambda x: x.replace('-',''))
    df_Color['Color'] = df_Color['Color'].map(lambda x: x.split(' '))
    
    df_Color['bag_of_words'] = ''
    columns = df_Color.columns
    for index, row in df_Color.iterrows():
        words = ''
        for col in columns:
            words = words + ' '.join(row[col])+ ' '
        row['bag_of_words'] = words
        
    df_Color.drop([col for col in df_Color.columns if col!= 'bag_of_words'], 
                  axis=1,inplace = True)
    
    count = CountVectorizer()
    count_matrix_Color = count.fit_transform(df_Color['bag_of_words'])
    
    cosine_sim_Color = cosine_similarity(count_matrix_Color, count_matrix_Color)
    cosine_sim_Color = cosine_sim_Color* 0.1




    
###############################################################################
    df_Price =df.copy()
    df_Price = df_Price[['Price']]
    
    tmpPrice = df_Price['Price'].values.reshape(-1,1)
    from scipy.spatial.distance import cdist
    cosine_dist_Price = cdist(tmpPrice, tmpPrice, metric='euclidean')
    cosine_dist_Price = (1-(cosine_dist_Price/cosine_dist_Price.max()))*0.183333333






   
    
###############################################################################
# encoding: utf-8
    df_Air_Delivery = df.copy()
    df_Air_Delivery = df_Air_Delivery[['Air Delivery']]
    
    df_Air_Delivery['Air Delivery'] = df_Air_Delivery['Air Delivery'].map(lambda x: x.replace('m³/min',''))
    
    tmpAir_Delivery = df_Air_Delivery['Air Delivery'].values.reshape(-1,1)
    
    from scipy.spatial.distance import cdist
    
    cosine_dist_Air_Delivery = cdist(tmpAir_Delivery, tmpAir_Delivery, metric='euclidean')
    cosine_dist_Air_Delivery = (1-(cosine_dist_Air_Delivery/cosine_dist_Air_Delivery.max()))*0.033333333






###############################################################################
    df_UnderLight = df.copy()
    df_UnderLight = df_UnderLight[['UnderLight']].replace('No',0)
    df_UnderLight = df_UnderLight[['UnderLight']].replace('YES',1)
    
    tmpUnderLight = df_UnderLight['UnderLight'].values.reshape(-1,1)
    from scipy.spatial.distance import cdist
    
    cosine_dist_UnderLight = cdist(tmpUnderLight, tmpUnderLight, metric='euclidean')
    cosine_dist_UnderLight = (1-(cosine_dist_UnderLight/cosine_dist_UnderLight.max()))*0.033333333




   
    
###############################################################################    
    
    
    df.set_index('SKU', inplace = True)
    df_Title.set_index('bag_of_words', inplace = True)
    df_Price.set_index('Price', inplace = True)
    df_SKU.set_index('SKU', inplace =True)
    df_Image.set_index('Gallery_Image', inplace=True)
    df_Link.set_index('BuyNowURL', inplace=True)
    
###############################################################################
    
    Similarity_Matrix =  cosine_sim_Title+ cosine_sim_Design + cosine_sim_Performance + cosine_sim_Finish + cosine_dist_Blades + cosine_dist_Sweep + cosine_sim_Color + cosine_dist_Price + cosine_dist_Air_Delivery + cosine_dist_UnderLight
   
    indices = pd.Series(df.index)
        # initializing the empty list of recommended fans
    recommended_fans = []
        # gettin the index of the fan that matches the sku
    idx = indices[indices == sku].index[0]
    #print(idx)
      # creating a Series with the similarity scores in descending order
    score_series = pd.Series(Similarity_Matrix[idx]).sort_values(ascending = False)
    #print(score_series)
     # getting the indexes of the 10 most similar fans
    top_10_indexes = list(score_series.iloc[0:6].index)
    top_10_indexes.remove(idx)
    #print(top_10_indexes)

    p = {'sku':df_SKU.index[idx],'price':str(df_Price.index[idx]),
         'title':df_Title.index[idx],'image' : df_Image.index[idx],
         'link': df_Link.index[idx]}
    recommended_fans.append(p)
    
    for i in top_10_indexes:
                p = {'sku':df_SKU.index[i],'price':str(df_Price.index[i]),
                     'title':df_Title.index[i],'image' : df_Image.index[i],
                     'link': df_Link.index[i]}
                recommended_fans.append(p)
    
    return json.dumps(recommended_fans)

if __name__ == '__main__':
    
    app.run(host="0.0.0.0",port=3000,debug = True)
