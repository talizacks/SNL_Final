#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import sqlite3
import matplotlib
import ipywidgets
import matplotlib.pyplot as plt
import regex as re
import bqplot
import numpy as np
import seaborn as sb

import plotly.graph_objects as go
import networkx as nx


# In[4]:


principals = pd.read_csv('Imdb_data/title.principals.tsv',delimiter='\t')
basics = pd.read_csv('Imdb_data/title.basics.tsv',delimiter='\t')
imdb_names = pd.read_csv('Imdb_data/name.basics.tsv',delimiter='\t')


# In[5]:


wiki_cast_excel = pd.read_csv('wiki_cast_excel.csv')
wiki_cast_excel.iloc[29]
wiki_cast = wiki_cast_excel.fillna('No')
wiki_cast


# In[6]:


plt.style.use('ggplot')
ax = wiki_cast.plot(x= "Performer",y="No. of seasons", figsize = (20,10), kind = 'bar')
ax.set_ylabel('No. of Seasons')


# In[7]:


imdb_names_df = imdb_names
imdb_names_df


# In[8]:


imdb_name_list = imdb_names_df.values.tolist()
imdb_names_df.columns.tolist()


# In[ ]:


cross_imdb_wiki_list = []
for person in imdb_name_list:
    if person[1] in wiki_cast['Performer'].values:
        cross_imdb_wiki_list.append(person)


# In[ ]:


cross_name_list = (set([r[1] for r in cross_imdb_wiki_list]))
len(cross_name_list) # <- Missing 2 cast members


# In[ ]:


from collections import Counter

Counter([r[1] for r in cross_imdb_wiki_list]).most_common(10)


# In[ ]:


cross_imdb_wiki_list


# In[ ]:


def check_names(name):
    cross_name_list = (set([r[1] for r in cross_imdb_wiki_list]))
    result = False
    
    if name in cross_name_list:
        result = True
    return result
SNL_name_check = [r for r in cross_imdb_wiki_list if check_names(r[1])]
(SNL_name_check)


# In[ ]:


def check_creds(works):
    SNL_IDs = ['tt0715791', 'tt0715791', 'tt0971348', 'tt10809086', 'tt0072562', 'tt1372614', 'tt2173702']
    result = False
    for work in works.split(','):
        if work in SNL_IDs:
            result = True
    return result
SNL_cred_check = [r for r in cross_imdb_wiki_list if check_creds(r[5])]
(SNL_cred_check)


# In[ ]:


SNL_df = pd.DataFrame(SNL_cred_check, columns = imdb_names.columns.tolist()).set_index('primaryName')
SNL_df


# In[ ]:


wiki_cast = wiki_cast.set_index('Performer')
imdb_wiki_table = pd.concat([SNL_df, wiki_cast], axis=1, join="outer")
imdb_wiki_table


# In[ ]:


names_title_dict = {item[1]:item[5].split(',') for item in SNL_name_check}
names_title_dict


# In[ ]:


for i in SNL_name_check:
    for x in i:
        if str(x).startswith('tt'):
            titles = x.split(',')
    
    name = i[1]
    names_title_dict[name] += titles

for name, titles in names_title_dict.items():
    names_title_dict[name] = list(set(titles))
    
names_title_dict


# In[ ]:


import csv
headers = ['name', 'title']
rows = []
for name, titles in names_title_dict.items():
    for t in titles:
        rows.append([name, t])


with open('snl_name_title_nodes.csv', 'w', encoding = 'utf-8') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(rows)


# # Visualizations

# In[ ]:


import pygraphviz as pgv

G = pgv.AGraph(names_title_dict,
               strict=True,
               directed=True,
               rankdir="RL",
               ranksep="0.25",
               ordering="in")

G.layout('dot')

G.draw('name_to_titles.png')

G.draw('name_to_titles.svg')


# In[ ]:


from IPython import display
display.Image('name_to_titles.png')


# In[ ]:


same_title_dict = {}
unique_title_list = []
for x in names_title_dict:
#     print((x))
    for unique_title in names_title_dict[x]:
        if unique_title not in unique_title_list:
            unique_title_list.append(unique_title)
    per_title_name_list = []
    for i in unique_title_list:
        
        if names_title_dict[x] == i:
            
            per_title_name_list.append(name_titles_dict[x])
        same_title_dict[i] = per_title_name_list
name = names_title_dict.keys()
title = same_title_dict.keys()
for title in same_title_dict:
#     print(title)
    name_list = []
#     print(name)
    for name in names_title_dict:
        if str(title) in names_title_dict[name] and name not in name_list:
#             print(name,title)
            name_list.append(name)
    same_title_dict[title] = name_list
            #     same_title_dict[title] = list((name))
same_title_dict


# In[ ]:


G = pgv.AGraph(same_title_dict,
               strict=True,
               directed=False,
               rankdir="RL",
               ranksep="0.25",
               ordering="in")

G.layout('dot')

G.draw('title_to_names.png')

G.draw('title_to_names.svg')


# In[ ]:


display.Image('title_to_names.png')


# In[ ]:


values = list(set([x for y in names_title_dict.values() for x in y]))
data = {}
for key in names_title_dict.keys():
    data[key] = [True if value in names_title_dict[key] else False for value in values]
 
boolean_table_name_cols = pd.DataFrame(data, index=values)
pd.DataFrame(boolean_table_name_cols)


# In[ ]:


# https://stackoverflow.com/questions/41964618/boolean-matrix-form-pythons-dict-of-lists
values = list(set([x for y in same_title_dict.values() for x in y]))
data = {}
for key in same_title_dict.keys():
    data[key] = [ True if value in same_title_dict[key] else False for value in values ]
 
boolean_table_title_cols = pd.DataFrame(data, index=values)
pd.DataFrame(boolean_table_title_cols)


# In[ ]:


fig, ax = plt.subplots(figsize=(11, 9))
sb.heatmap(boolean_table_title_cols)
plt.show()


# In[ ]:


fig, ax = plt.subplots(figsize=(45, 25))
sb.heatmap(boolean_table_name_cols)
plt.show()


# In[ ]:


# ATTEMPT AT A NETWORK NODE GRAPH
# g = nx.DiGraph(same_title_dict)
# g.add_nodes_from(same_title_dict.keys())
# for k, v in same_title_dict.items():
#     g.add_edges_from(([(k, t) for t in v]))
#     node_trace = go.Scatter(
#     x=node_x, y=node_y,
#     mode='markers',
#     hoverinfo='text',
#     marker=dict(
#         showscale=True,
#         # colorscale options
#         #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
#         #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
#         #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
#         colorscale='YlGnBu',
#         reversescale=True,
#         color=[],
#         size=10,
#         colorbar=dict(
#             thickness=15,
#             title='Node Connections',
#             xanchor='left',
#             titleside='right'),
#         line_width=2))
# nx.draw(g,with_labels=True)

# node_adjacencies = []
# node_text = []
# for node, adjacencies in enumerate(g.adjacency()):
#     node_adjacencies.append(len(adjacencies[1]))
#     node_text.append('# of connections: '+str(len(adjacencies[1])))

# node_trace.marker.color = node_adjacencies
# node_trace.text = node_text
# # Create Network Graph
# fig = go.Figure(data=[edge_trace, node_trace],
#              layout=go.Layout(
#                 title='<br>Network graph made with Python',
#                 titlefont_size=24,
#                 showlegend=False,
#                 hovermode='closest',
#                 margin=dict(b=20,l=5,r=5,t=40),
#                 annotations=[ dict(
#                     text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
#                     showarrow=False,
#                     xref="paper", yref="paper",
#                     x=0.005, y=-0.002 ) ],
#                 xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#                 yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))                )
# fig.show()


# In[ ]:


for actor in names_title_dict:
    fig, ax = plt.subplots(figsize=(11, 9))
    # https://stackoverflow.com/questions/41964618/boolean-matrix-form-pythons-dict-of-lists
    values = names_title_dict[actor]
    print(actor,values)
    data = {}
    boolean_table_name_cols = pd.DataFrame(data, columns=values)

    for key in names_title_dict:
        print(key)
        data[actor] = [True if value in names_title_dict[key] else False for value in values]
        print(data[actor])
#         for index in boolean_table_name_cols:
#             boolean_table_name_cols.append(data[actor])
        boolean_table_name_cols
        
#         sb.heatmap(boolean_table_name_cols)
#     plt.GridSpec(boolean_table_title_cols,ncols=len(values))
#     plt.show()


# In[ ]:


data = {}
for actor in names_title_dict:
    # https://stackoverflow.com/questions/41964618/boolean-matrix-form-pythons-dict-of-lists
    values = names_title_dict[actor]
    headers = values[:]
    headers.insert(0,actor)
#     print(headers)
#     print(values)

#     print(actor,values)
    
    actor_dict_2d = [headers]

    for key in names_title_dict:
#         print(key)
#         data[actor] = [True if value in names_title_dict[key] else False for value in values]
#         print(data[actor])
        t_or_f = [1 if value in names_title_dict[key] else 0 for value in values]
        t_or_f.insert(0,key)
        actor_dict_2d.append(t_or_f)
    data[actor] = actor_dict_2d
# print(data)


# In[ ]:


# table = pd.DataFrame(data['Kate McKinnon']).set_index(0)

# header = table.iloc[0]
# table.columns = header
# table = pd.DataFrame(table[1:], columns=header)
# wiki_cast.index


# In[ ]:


def create_table(i):
    table = pd.DataFrame(data[wiki_cast.iloc[i].name]).set_index(0)
    header = table.iloc[0]
    table.columns = header
    table = pd.DataFrame(table[1:], columns=header)
    return table
table = create_table(1)


# In[ ]:


def on_selection(change):
    if (change['owner'].selected) is not None and len(change['owner'].selected)==1: # only allow user to select one grid
            i = change['owner'].selected[0]

            myLabel.value = wiki_cast.iloc[i].name + ': ' + str(wiki_cast.iloc[i]['No. of seasons']) + ' seasons on SNL'
            table = create_table(i)
            heat_map.color = table.values.astype('float')
            heat_map.row = table.index.values.astype(str),
            heat_map.column = table.columns.values.astype(str)
#how to ignore if NoneType selected?


# In[ ]:


myLabel = ipywidgets.Label()


# In[ ]:


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
                                 selected_style={"stroke": "green", 
                                                 "fill": "skyblue"})


margin = dict(top=0, bottom=50, left=140, right=0)


no_SNL_seasons_bar.observe(on_selection,'selected')

fig_bars = bqplot.Figure(marks=[no_SNL_seasons_bar],
                         axes=[x_axb, y_axb], fig_margin=margin)
fig_bars.axes[0].tick_style = {'text-anchor': 'end'}

fig_bars.layout.height = '1700px'
fig_bars.layout.width = '550px'
fig_bars


# In[ ]:


table.values.astype(int)


# In[ ]:


##GRID HEAT MAP##

# 2. scales
col_sc = bqplot.OrdinalColorScale(scheme="Pastel1")
x_sc = bqplot.OrdinalScale()
y_sc = bqplot.OrdinalScale()

# 3. axis
col_ax = bqplot.ColorAxis(scale=col_sc, orientation='vertical', side='right', label = 'Color Scale')
x_ax = bqplot.Axis(scale=x_sc, label='Title IDs',tick_rotate=-90, tick_style ={'font-size':'8px'},  label_offset ='50px')
y_ax = bqplot.Axis(scale=y_sc, orientation='vertical', label='Actors',tick_offset = '50px',tick_style ={'font-size':'8px'}, label_offset ='50px')

# 4. marks
heat_map = bqplot.GridHeatMap(color = table.values.astype('float'),
                             row = table.index.values.astype(str),
                             column = table.columns.values.astype(str),scales = {'color': col_sc})

fig = bqplot.Figure(marks=[heat_map], axes=[col_ax,x_ax, y_ax])
fig.layout.height = '1700px'
fig.layout.width = '550px'


# In[ ]:


Label_bar = ipywidgets.VBox([myLabel,fig_bars])
myDashboard = ipywidgets.HBox([Label_bar,fig])
myDashboard


# My dashboard is used to see the frequency of collaboration amongst SNL cast members. The left part of the graph is a bar chart, representing the length of tenure at SNL. When a user clicks on a cast member's bar, the heat map on the right gets updated. At the moment, the order is inconsistent between the two portions of the graph. This iteration of the heat map is more of a representation of the overlap between IMDb 'Known For Titles,' which are the group of four or five top titles on an actor's (or director, producer, etc.) resume/page. I've also opted not to include the titles since they are currently just IMDb unique title IDs and wouldn't mean anything to a viewer. I am in the process of compiling the complete list of titles for every SNL cast member by scraping their wikipedia filmography tables (the file in which I do that is included in the zipped submission file). The next iteration of my dashboard will hopefully include these complete lists for each actor. I also plan to include a hover interaction feature for the heat map where a label will be updated to show the comparative actor's name in addition to the project that each box represents. In the current iteration, the row which is filled in completely filled in green represents the row of the actor whose bar was just selected.

# In[ ]:


import wiki_scrape


# In[ ]:


from collections import OrderedDict

SNL_Cast_Members_Full_Titles_dict = wiki_scrape.Final_dict
for i in SNL_Cast_Members_Full_Titles_dict.items():
    if 'Saturday Night Live' not in i[1]:
        i[1].append('Saturday Night Live')


# In[ ]:


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


# In[ ]:


values = list(set([x for y in SNL_Cast_Members_Full_Titles_dict.values() for x in y]))
data = {}
for key in SNL_Cast_Members_Full_Titles_dict.keys():
    data[key] = [True if value in SNL_Cast_Members_Full_Titles_dict[key] else False for value in values]
 
boolean_table_name_cols = pd.DataFrame(data, index=values)
pd.DataFrame(boolean_table_name_cols)


# In[ ]:


for actor in SNL_Cast_Members_Full_Titles_dict:
    fig, ax = plt.subplots(figsize=(11, 9))
    # https://stackoverflow.com/questions/41964618/boolean-matrix-form-pythons-dict-of-lists
    values = SNL_Cast_Members_Full_Titles_dict[actor]
    print(actor,values)
    data = {}
    boolean_table_name_cols = pd.DataFrame(data, columns=values)

    for key in names_title_dict:
        print(key)
        data[actor] = [True if value in SNL_Cast_Members_Full_Titles_dict[key] else False for value in values]
        print(data[actor])
#         for index in boolean_table_name_cols:
#             boolean_table_name_cols.append(data[actor])
        boolean_table_name_cols
        
#         sb.heatmap(boolean_table_name_cols)
#     plt.GridSpec(boolean_table_title_cols,ncols=len(values))
#     plt.show()


# In[ ]:


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
    
pd.DataFrame(data['Fred Armisen'])
# print(data)


# In[ ]:


def create_table(i):
    table = pd.DataFrame(data[wiki_cast.iloc[i].name]).set_index(0)
    header = table.iloc[0]
    table.columns = header
    table = pd.DataFrame(table[1:], columns=header)
    return table
table = create_table(1)


# In[ ]:


def on_selection(change):
    if (change['owner'].selected) is not None and len(change['owner'].selected)==1: # only allow user to select one grid
            i = change['owner'].selected[0]

            myLabel.value = wiki_cast.iloc[i].name + ': ' + str(wiki_cast.iloc[i]['No. of seasons']) + ' seasons on SNL'
            table = create_table(i)
            heat_map.color = table.values.astype('float')
            heat_map.row = table.index.values.astype(str),
            heat_map.column = table.columns.values.astype(str)
#how to ignore if NoneType selected?


# In[ ]:


myLabel = ipywidgets.Label()


# In[ ]:


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
                                 selected_style={"stroke": "green", 
                                                 "fill": "skyblue"})


margin = dict(top=0, bottom=50, left=140, right=0)


no_SNL_seasons_bar.observe(on_selection,'selected')

fig_bars = bqplot.Figure(marks=[no_SNL_seasons_bar],
                         axes=[x_axb, y_axb], fig_margin=margin)
fig_bars.axes[0].tick_style = {'text-anchor': 'end'}

fig_bars.layout.height = '1700px'
fig_bars.layout.width = '500px'
fig_bars


# In[ ]:


table.values.astype(int)


# In[ ]:


def get_data_value(change):
    #print(change['owner'].selected) # so we have IDs, but we want to print state names
    if change['owner'].selected is not None:
        for i,s in enumerate(change['owner'].selected): # over all selected states
            print(state_names[s == ids])
        
heat_map.observe(get_data_value,'selected')


# In[ ]:


##GRID HEAT MAP##

# 2. scales
col_sc = bqplot.OrdinalColorScale(scheme="Pastel1")
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
                             selected_style={"stroke": "green", 
                                                 "fill": "skyblue"},
                             tooltip=def_tt)


# 4 interactions
heat_map.interactions = {'hover': 'tooltip'}
fig = bqplot.Figure(marks=[heat_map], axes=[col_ax,x_ax, y_ax])
fig.layout.height = '1700px'
fig.layout.width = '550px'


# In[ ]:


Label_bar = ipywidgets.VBox([myLabel,fig_bars])
myDashboard = ipywidgets.HBox([Label_bar,fig])
myDashboard


# In[ ]:


tt = bqplot.Tooltip(fields=['name', 'x', 'y'], 
                    labels=['Country Name', 
                            'Income per Capita', 'Life Expectancy'])


# In[ ]:




