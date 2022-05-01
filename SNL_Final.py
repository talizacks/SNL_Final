#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib
import ipywidgets
import bqplot
import numpy as np


# In[2]:


# imdb_names_df = pd.read_csv('Imdb_data/name.basics.tsv',delimiter='\t')


# In[3]:


imdb_names_df = pd.read_csv('imdb_wiki_filter.csv')


# In[4]:


wiki_cast_excel = pd.read_csv('wiki_cast_excel.csv')
wiki_cast_excel.iloc[29]
wiki_cast = wiki_cast_excel.fillna('No')
wiki_cast


# In[5]:


imdb_name_list = imdb_names_df.values.tolist()

cross_imdb_wiki_list = []
for person in imdb_name_list:
    if person[1] in wiki_cast['Performer'].values:
        cross_imdb_wiki_list.append(person)


# In[6]:


imdb_names = imdb_names_df
def check_names(name):
    cross_name_list = (set([r[1] for r in cross_imdb_wiki_list]))
    result = False
    
    if name in cross_name_list:
        result = True
    return result
SNL_name_check = [r for r in cross_imdb_wiki_list if check_names(r[1])]

def check_creds(works):
    SNL_IDs = ['tt0715791', 'tt0715791', 'tt0971348', 'tt10809086', 'tt0072562', 'tt1372614', 'tt2173702']
    result = False
    for work in works.split(','):
        if work in SNL_IDs:
            result = True
    return result
SNL_cred_check = [r for r in cross_imdb_wiki_list if check_creds(r[5])]

SNL_df = pd.DataFrame(SNL_cred_check, columns = imdb_names.columns.tolist()).set_index('primaryName')


# In[7]:


wiki_cast = wiki_cast.set_index('Performer')
# print(wiki_cast.index)
imdb_wiki_table = pd.concat([SNL_df, wiki_cast], axis=1, join="outer")
imdb_wiki_table


# In[8]:


names_title_dict = {item[1]:item[5].split(',') for item in SNL_name_check}
names_title_dict


# In[9]:


for i in SNL_name_check:
    for x in i:
        if str(x).startswith('tt'):
            titles = x.split(',')
    
    name = i[1]
    names_title_dict[name] += titles

for name, titles in names_title_dict.items():
    names_title_dict[name] = list(set(titles))
    
names_title_dict


# In[10]:


import wiki_scrape


# In[11]:


order = list(wiki_cast.index)
SNL_Cast_Members_Full_Titles_dict = sorted((wiki_scrape.Final_dict).items(), key=lambda pair: order.index(pair[0]))
SNL_Cast_Members_Full_Titles_dict2 = {}
for i in SNL_Cast_Members_Full_Titles_dict:
    SNL_Cast_Members_Full_Titles_dict2[i[0]]=i[1]

SNL_Cast_Members_Full_Titles_dict2
SNL_Cast_Members_Full_Titles_dict = SNL_Cast_Members_Full_Titles_dict2


# In[12]:


same_title_dict = {}
unique_title_list = []
for x in SNL_Cast_Members_Full_Titles_dict:
#     print((x))
    for unique_title in SNL_Cast_Members_Full_Titles_dict[x]:
        if unique_title not in unique_title_list:
            unique_title_list.append(unique_title)
    per_title_name_list = []
    for i in unique_title_list:
        
        if SNL_Cast_Members_Full_Titles_dict[x] == i:
            
            per_title_name_list.append(SNL_Cast_Members_Full_Titles_dict[x])
        same_title_dict[i] = per_title_name_list
name = SNL_Cast_Members_Full_Titles_dict.keys()
title = same_title_dict.keys()
for title in same_title_dict:
#     print(title)
    name_list = []
#     print(name)
    for name in SNL_Cast_Members_Full_Titles_dict:
        if str(title) in SNL_Cast_Members_Full_Titles_dict[name] and name not in name_list:
#             print(name,title)
            name_list.append(name)
    same_title_dict[title] = name_list
            #     same_title_dict[title] = list((name))
same_title_dict


# In[13]:


for i in SNL_Cast_Members_Full_Titles_dict.items():
    if 'Saturday Night Live' not in i[1]:
        i[1].append('Saturday Night Live')


# In[14]:


values = list(set([x for y in SNL_Cast_Members_Full_Titles_dict.values() for x in y]))
data = {}
for key in SNL_Cast_Members_Full_Titles_dict.keys():
    data[key] = [True if value in SNL_Cast_Members_Full_Titles_dict[key] else False for value in values]
 
boolean_table_name_cols = pd.DataFrame(data, index=values)
pd.DataFrame(boolean_table_name_cols)


# In[15]:


for actor in SNL_Cast_Members_Full_Titles_dict:
    # https://stackoverflow.com/questions/41964618/boolean-matrix-form-pythons-dict-of-lists
    values = SNL_Cast_Members_Full_Titles_dict[actor]
#     print(actor,values)
    data = {}
    boolean_table_name_cols = pd.DataFrame(data, columns=values)

    for key in names_title_dict:
#         print(key)
        data[actor] = [True if value in SNL_Cast_Members_Full_Titles_dict[key] else False for value in values]
        print(data[actor])
#         for index in boolean_table_name_cols:
#             boolean_table_name_cols.append(data[actor])
        boolean_table_name_cols


# In[24]:


data = {}
for actor in SNL_Cast_Members_Full_Titles_dict:
    # https://stackoverflow.com/questions/41964618/boolean-matrix-form-pythons-dict-of-lists
    values = SNL_Cast_Members_Full_Titles_dict[actor]
    headers = values[:]
    headers.insert(0,actor)
#     print(headers)
#     print(values)

#     print(actor,values)
    
    actor_dict_2d = [headers]

    for key in SNL_Cast_Members_Full_Titles_dict:
#         print(key)
#         data[actor] = [True if value in names_title_dict[key] else False for value in values]
#         print(data[actor])
        t_or_f = [1 if value in SNL_Cast_Members_Full_Titles_dict[key] else 0 for value in values]
        t_or_f.insert(0,key)
        actor_dict_2d.append(t_or_f)
    data[actor] = actor_dict_2d
# print(data)    
pd.DataFrame(data['Fred Armisen'])
# print(data)


# In[17]:


def create_table(i):
    table = pd.DataFrame(data[wiki_cast.iloc[i].name]).set_index(0)
    header = table.iloc[0]
    table.columns = header
    table = pd.DataFrame(table[1:], columns=header)
    return table
table = create_table(0)


# In[18]:


myLabel = ipywidgets.Label()


# In[19]:


wiki_cast = wiki_cast[::-1]
def on_selection(change):
    if (change['owner'].selected) is not None and len(change['owner'].selected)==1: # only allow user to select one grid
            i = change['owner'].selected[0]

            myLabel.value = wiki_cast.iloc[i].name + ': ' + str(wiki_cast.iloc[i]['No. of seasons']) + ' seasons on SNL'
            table = create_table(i)
            heat_map.color = table.values.astype('float')
            heat_map.row = table.index.values.astype(str),
            heat_map.column = table.columns.values.astype(str)


# In[20]:


####### BAR PLOT ######
# 2. scales
x_scb = bqplot.OrdinalScale()
y_scb = bqplot.LinearScale()
# 3. axis 
x_axb = bqplot.Axis(label='SNL Cast Member', orientation = 'vertical',
                    scale=x_scb, label_offset = '115px',
                    tick_style={'font-size':'3px','text-anchor': 'end'},
                    padding = 0.25)
y_axb = bqplot.Axis(label='Number of Seasons on SNL',
                    scale=y_scb, label_offset = '40 px')

# 4. mark -- heatmap using out colors to map our data
no_SNL_seasons_bar = bqplot.Bars(orientation='horizontal',x=wiki_cast.index,
                                 y=wiki_cast['No. of seasons'],
                                 align='center',scales = {'x':x_scb,
                                                          'y':y_scb},
                                 interactions={"click": "select"},
                                 selected_style={"stroke": "#a6cee3", 
                                                 "fill": "#b2df8a"})


margin = dict(top=0, bottom=50, left=140, right=0)


no_SNL_seasons_bar.observe(on_selection,'selected')

fig_bars = bqplot.Figure(marks=[no_SNL_seasons_bar],
                         axes=[x_axb, y_axb], fig_margin=margin)
fig_bars.axes[0].tick_style = {'text-anchor': 'end'}

fig_bars.layout.height = '1700px'
fig_bars.layout.width = '500px'


# In[21]:


##GRID HEAT MAP##
# 2. scales

col_sc = bqplot.OrdinalColorScale(colors = ['#a6cee3','#1f78b4','#b2df8a'])
x_sc = bqplot.OrdinalScale()
y_sc = bqplot.OrdinalScale()

# 3. axis
col_ax = bqplot.ColorAxis(scale=col_sc, orientation='horizontal', side='top', label = 'Color Scale')
x_ax = bqplot.Axis(scale=x_sc, label='Title IDs',tick_rotate=-90, tick_style ={'font-size':'8px'},  label_offset ='50px')
y_ax = bqplot.Axis(scale=y_sc, orientation='vertical', label='Actors',tick_offset = '50px',tick_style ={'font-size':'8px'}, label_offset ='50px')

def_tt = bqplot.Tooltip(fields=["row", "column","color"])

# 4. marks
heat_map = bqplot.GridHeatMap(color = table.values.astype('float'),
                             row = table.index.values.astype(str),
                             column = table.columns.values.astype(str),scales = {'color': col_sc},
                             selected_style={"stroke": "#b2df8a", 
                                                 "fill": "skyblue"},
                             tooltip=def_tt)


# 4 interactions
heat_map.interactions = {'hover': 'tooltip'}
fig = bqplot.Figure(marks=[heat_map], axes=[col_ax,x_ax, y_ax])
fig.layout.height = '1700px'
fig.layout.width = '550px'


# In[23]:


Label_bar = ipywidgets.VBox([myLabel,fig_bars])
myDashboard = ipywidgets.HBox([Label_bar,fig])
myDashboard


# In[ ]:





# In[ ]:





# In[ ]:




