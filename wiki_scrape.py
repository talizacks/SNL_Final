#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents


# In[2]:


SNL_Cast_Members_Full_Titles_dict = {}


# In[3]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Fred_Armisen_filmography"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable sortable"})

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Fred_Armisten_tv = []
for title in df['Title']:
    if '[' in title:
        print(title)
        sep = '['
        title = title.split(sep, 1)[0]
        print(title)
    Fred_Armisten_tv.append(title)
Fred_Armisten_tv

soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Fred_Armisten_film = []
for title in df['Title']:
    if '[' in title:
        print(title)
        sep = '['
        title = title.split(sep, 1)[0]
        print(title)

    Fred_Armisten_film.append(title)
Fred_Armisten_film

Fred_Armisten_dict = {'Titles':Fred_Armisten_film + Fred_Armisten_tv}

SNL_Cast_Members_Full_Titles_dict['Fred Armisen'] = Fred_Armisten_dict

Fred_Armisten_dict


# In[4]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Aristotle_Athari"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
# # print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Aristotle_Athari_films = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Aristotle_Athari_films.append(title)
Aristotle_Athari_films

soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Aristotle_Athari_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Aristotle_Athari_tv.append(title)
Aristotle_Athari_tv
Aristotle_Athari_dict = {'Titles':Aristotle_Athari_films + Aristotle_Athari_tv}

SNL_Cast_Members_Full_Titles_dict['Aristotle Athari']=Aristotle_Athari_dict
Aristotle_Athari_dict


# In[5]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Dan_Aykroyd#Filmography"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable sortable"})

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Dan_Aykroyd_film = []
for title in df['Title']:
    if '[' in title:
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Dan_Aykroyd_film.append(title)
Dan_Aykroyd_film

# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Dan_Aykroyd#Filmography"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Dan_Aykroyd_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Dan_Aykroyd_tv.append(title)
Dan_Aykroyd_tv


Dan_Aykroyd_dict = {'Titles':Dan_Aykroyd_film + Dan_Aykroyd_tv}
SNL_Cast_Members_Full_Titles_dict['Dan Aykroyd']= Dan_Aykroyd_dict
Dan_Aykroyd_dict


# In[6]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Peter_Aykroyd#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Peter_Aykroyd_film = []
for title in df['Title']:
    if '[' in title:
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Peter_Aykroyd_film.append(title)
Peter_Aykroyd_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Peter_Aykroyd_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Peter_Aykroyd_tv.append(title)
Peter_Aykroyd_tv

Peter_Aykroyd_dict = {'Titles':Peter_Aykroyd_film + Peter_Aykroyd_tv}
SNL_Cast_Members_Full_Titles_dict['Peter Aykroyd']= Peter_Aykroyd_dict
Peter_Aykroyd_dict


# In[7]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Vanessa_Bayer#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Vanessa_Bayer_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Vanessa_Bayer_film.append(title)
Vanessa_Bayer_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Vanessa_Bayer_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Vanessa_Bayer_tv.append(title)
Vanessa_Bayer_tv

Vanessa_Bayer_dict = {'Titles':Vanessa_Bayer_film+Vanessa_Bayer_tv}
SNL_Cast_Members_Full_Titles_dict['Vanessa Bayer'] = Vanessa_Bayer_dict


# In[8]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jim_Belushi#Film"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jim_Belushi_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jim_Belushi_film.append(title)
Jim_Belushi_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jim_Belushi_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jim_Belushi_tv.append(title)
Jim_Belushi_tv

Jim_Belushi_dict = {'Titles':Jim_Belushi_film + Jim_Belushi_tv}
SNL_Cast_Members_Full_Titles_dict['Jim Belushi']= Jim_Belushi_dict


# In[9]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/John_Belushi#Film"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
John_Belushi_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    John_Belushi_film.append(title)
John_Belushi_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
John_Belushi_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    John_Belushi_tv.append(title)
John_Belushi_tv

John_Belushi_dict = {'Titles':John_Belushi_film + John_Belushi_tv}
SNL_Cast_Members_Full_Titles_dict['John Belushi']= John_Belushi_dict


# In[10]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Beck_Bennett#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Beck_Bennett_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Beck_Bennett_film.append(title)
Beck_Bennett_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Beck_Bennett_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Beck_Bennett_tv.append(title)
Beck_Bennett_tv

Beck_Bennett_dict = {'Titles':Beck_Bennett_film + Beck_Bennett_tv}
SNL_Cast_Members_Full_Titles_dict['Beck Bennett']=Beck_Bennett_dict


# In[11]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jim_Breuer#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jim_Breuer_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jim_Breuer_tv.append(title)
Jim_Breuer_tv


Jim_Breuer_dict = {'Titles':Jim_Breuer_tv}
SNL_Cast_Members_Full_Titles_dict['Jim Breuer'] = Jim_Breuer_dict


# In[12]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Paul_Brittain#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Paul_Brittain_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Paul_Brittain_film.append(title)
Paul_Brittain_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Paul_Brittain_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Paul_Brittain_tv.append(title)
Paul_Brittain_tv

Paul_Brittain_dict = {'Titles':Paul_Brittain_film + Paul_Brittain_tv}
SNL_Cast_Members_Full_Titles_dict['Paul Brittain'] = Paul_Brittain_dict


# In[13]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Aidy_Bryant#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Aidy_Bryant_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Aidy_Bryant_film.append(title)
Aidy_Bryant_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Aidy_Bryant_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Aidy_Bryant_tv.append(title)
Aidy_Bryant_tv

Aidy_Bryant_dict = {'Titles':Aidy_Bryant_film + Aidy_Bryant_tv}
SNL_Cast_Members_Full_Titles_dict['Aidy Bryant']=Aidy_Bryant_dict


# In[14]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Dana_Carvey#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Dana_Carvey_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Dana_Carvey_film.append(title)
Dana_Carvey_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Dana_Carvey_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Dana_Carvey_tv.append(title)
Dana_Carvey_tv

Dana_Carvey_dict = {'Titles':Dana_Carvey_film + Dana_Carvey_tv}
SNL_Cast_Members_Full_Titles_dict['Dana Carvey']=Dana_Carvey_dict


# In[15]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Chevy_Chase#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chevy_Chase_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chevy_Chase_film.append(title)
Chevy_Chase_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chevy_Chase_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chevy_Chase_tv.append(title)
Chevy_Chase_tv

Chevy_Chase_dict = {'Titles':Chevy_Chase_film + Chevy_Chase_tv}
SNL_Cast_Members_Full_Titles_dict['Chevy Chase'] = Chevy_Chase_dict


# In[16]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Michael_Che#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Michael_Che_film = []
for title in df['Film']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Michael_Che_film.append(title)
Michael_Che_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Michael_Che_tv = []
for title in df['Series']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Michael_Che_tv.append(title)
Michael_Che_tv

Michael_Che_dict = {'Titles':Michael_Che_film + Michael_Che_tv}
SNL_Cast_Members_Full_Titles_dict['Michael Che'] = Michael_Che_dict


# In[17]:


SNL_Cast_Members_Full_Titles_dict


# In[18]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/George_Coe#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
George_Coe_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    George_Coe_film.append(title)
George_Coe_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
George_Coe_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    George_Coe_tv.append(title)
George_Coe_tv

George_Coe_dict = {'Titles':George_Coe_film+George_Coe_tv}
SNL_Cast_Members_Full_Titles_dict['George Coe']=George_Coe_dict


# In[19]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Billy_Crystal_filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Billy_Crystal_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Billy_Crystal_film.append(title)
Billy_Crystal_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Billy_Crystal_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Billy_Crystal_tv.append(title)
Billy_Crystal_tv

Billy_Crystal_dict = {'Titles':Billy_Crystal_film + Billy_Crystal_tv}
SNL_Cast_Members_Full_Titles_dict['Billy Crystal']=Billy_Crystal_dict


# In[20]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jane_Curtin#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jane_Curtin_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jane_Curtin_film.append(title)
Jane_Curtin_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jane_Curtin_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jane_Curtin_tv.append(title)
Jane_Curtin_tv

Jane_Curtin_dict = {'Titles':Jane_Curtin_film+Jane_Curtin_tv}
SNL_Cast_Members_Full_Titles_dict['Jane Curtin']=Jane_Curtin_dict


# In[21]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Joan_Cusack#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Joan_Cusack_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Joan_Cusack_film.append(title)
Joan_Cusack_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Joan_Cusack_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Joan_Cusack_tv.append(title)
Joan_Cusack_tv

Joan_Cusack_dict = {'Titles':Joan_Cusack_film+Joan_Cusack_tv}
SNL_Cast_Members_Full_Titles_dict['Joan Cusack']=Joan_Cusack_dict


# In[22]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Pete_Davidson#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Pete_Davidson_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Pete_Davidson_film.append(title)
Pete_Davidson_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Pete_Davidson_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Pete_Davidson_tv.append(title)
Pete_Davidson_tv

Pete_Davidson_dict = {'Titles':Pete_Davidson_film+Pete_Davidson_tv}
SNL_Cast_Members_Full_Titles_dict['Pete Davidson']=Pete_Davidson_dict
Pete_Davidson_dict


# In[23]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Tom_Davis_(comedian)#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tom_Davis_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tom_Davis_film.append(title)
Tom_Davis_film

# # parse data from the html into a beautifulsoup object
# soup = BeautifulSoup(response.text, 'html.parser')
# indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tom_Davis_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tom_Davis_tv.append(title)
Tom_Davis_tv

Tom_Davis_dict = {'Titles':Tom_Davis_film+Tom_Davis_tv}
SNL_Cast_Members_Full_Titles_dict['Tom Davis']=Tom_Davis_dict
Tom_Davis_dict


# In[24]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Mikey_Day#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Mikey_Day_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Mikey_Day_film.append(title)
Mikey_Day_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Mikey_Day_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Mikey_Day_tv.append(title)
Mikey_Day_tv

Mikey_Day_dict = {'Film':Mikey_Day_film+Mikey_Day_tv}
SNL_Cast_Members_Full_Titles_dict['Mikey Day']=Mikey_Day_dict


# In[25]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jim_Downey_(comedian)#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jim_Downey_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jim_Downey_film.append(title)
Jim_Downey_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jim_Downey_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jim_Downey_tv.append(title)
Jim_Downey_tv

Jim_Downey_dict = {'Film':Jim_Downey_film+Jim_Downey_tv}
SNL_Cast_Members_Full_Titles_dict['Jim Downey']=Jim_Downey_dict


# In[26]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Robert_Downey_Jr._filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Robert_Downey_Jr_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Robert_Downey_Jr_film.append(title)
Robert_Downey_Jr_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Robert_Downey_Jr_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Robert_Downey_Jr_tv.append(title)
Robert_Downey_Jr_tv

Robert_Downey_Jr_dict = {'Film':Robert_Downey_Jr_film+Robert_Downey_Jr_tv}
SNL_Cast_Members_Full_Titles_dict['Robert Downey Jr.']=Robert_Downey_Jr_dict


# In[27]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Brian_Doyle_Murray#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Brian_Doyle_Murray_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Brian_Doyle_Murray_film.append(title)
Brian_Doyle_Murray_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Brian_Doyle_Murray_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Brian_Doyle_Murray_tv.append(title)
Brian_Doyle_Murray_tv

Brian_Doyle_Murray_dict = {'Film':Brian_Doyle_Murray_film + Brian_Doyle_Murray_tv}
SNL_Cast_Members_Full_Titles_dict['Brian Doyle-Murray']=Brian_Doyle_Murray_dict


# In[28]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Rachel_Dratch#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Rachel_Dratch_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Rachel_Dratch_film.append(title)
Rachel_Dratch_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Rachel_Dratch_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Rachel_Dratch_tv.append(title)
Rachel_Dratch_tv

Rachel_Dratch_dict = {'Film':Rachel_Dratch_film + Rachel_Dratch_tv}
SNL_Cast_Members_Full_Titles_dict['Rachel Dratch']=Rachel_Dratch_dict


# In[29]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Robin_Duke#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Robin_Duke_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Robin_Duke_film.append(title)
Robin_Duke_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Robin_Duke_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Robin_Duke_tv.append(title)
Robin_Duke_tv

Robin_Duke_dict = {'Film':Robin_Duke_film+Robin_Duke_tv}
SNL_Cast_Members_Full_Titles_dict['Robin Duke']=Robin_Duke_dict


# In[30]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Nora_Dunn#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Nora_Dunn_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Nora_Dunn_film.append(title)
Nora_Dunn_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Nora_Dunn_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Nora_Dunn_tv.append(title)
Nora_Dunn_tv

Nora_Dunn_dict = {'Film':Nora_Dunn_film + Nora_Dunn_tv}
SNL_Cast_Members_Full_Titles_dict['Nora Dunn']=Nora_Dunn_dict


# In[31]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Christine_Ebersole#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Christine_Ebersole_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Christine_Ebersole_film.append(title)
Christine_Ebersole_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Christine_Ebersole_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Christine_Ebersole_tv.append(title)
Christine_Ebersole_tv

Christine_Ebersole_dict = {'Film':Christine_Ebersole_film + Christine_Ebersole_tv}
SNL_Cast_Members_Full_Titles_dict['Christine Ebersole']=Christine_Ebersole_dict


# In[32]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Dean_Edwards#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])

Dean_Edwards_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Dean_Edwards_film.append(title)
Dean_Edwards_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Dean_Edwards_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Dean_Edwards_tv.append(title)

Dean_Edwards_dict = {'Film':Dean_Edwards_film + Dean_Edwards_tv}
SNL_Cast_Members_Full_Titles_dict['Dean Edwards']=Dean_Edwards_dict
Dean_Edwards_dict


# In[33]:


Dean_Edwards_dict


# In[34]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Abby_Elliott#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Abby_Elliott_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Abby_Elliott_film.append(title)
Abby_Elliott_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Abby_Elliott_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Abby_Elliott_tv.append(title)
Abby_Elliott_tv

Abby_Elliott_dict = {'Film':Abby_Elliott_film+Abby_Elliott_tv}
SNL_Cast_Members_Full_Titles_dict['Abby Elliott']=Abby_Elliott_dict


# In[35]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Chris_Elliott#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chris_Elliott_film = []
for title in df['Film']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chris_Elliott_film.append(title)
Chris_Elliott_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chris_Elliott_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chris_Elliott_tv.append(title)
Chris_Elliott_tv

Chris_Elliott_dict = {'Film':Chris_Elliott_film+Chris_Elliott_tv}
SNL_Cast_Members_Full_Titles_dict['Chris Elliott']=Chris_Elliott_dict


# In[36]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jimmy_Fallon#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jimmy_Fallon_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jimmy_Fallon_film.append(title)
Jimmy_Fallon_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jimmy_Fallon_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jimmy_Fallon_tv.append(title)
Jimmy_Fallon_tv

Jimmy_Fallon_dict = {'Film':Jimmy_Fallon_film+Jimmy_Fallon_tv}
SNL_Cast_Members_Full_Titles_dict['Jimmy Fallon']=Jimmy_Fallon_dict


# In[37]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Siobhan_Fallon_Hogan#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Siobhan_Fallon_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Siobhan_Fallon_film.append(title)
Siobhan_Fallon_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Siobhan_Fallon_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Siobhan_Fallon_tv.append(title)
Siobhan_Fallon_tv

Siobhan_Fallon_dict = {'Film':Siobhan_Fallon_film+Siobhan_Fallon_tv}
SNL_Cast_Members_Full_Titles_dict['Siobhan Fallon']=Siobhan_Fallon_dict


# In[38]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Will_Ferrell_filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Will_Ferrell_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Will_Ferrell_film.append(title)
Will_Ferrell_film

indiatable=soup.find_all('table',{'class':"wikitable"})[2]

for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    if title not in Will_Ferrell_film:
        Will_Ferrell_film.append(title)
Will_Ferrell_film
# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[3]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Will_Ferrell_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Will_Ferrell_tv.append(title)
Will_Ferrell_tv
indiatable=soup.find_all('table',{'class':"wikitable"})[4]
df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])

for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    if title not in Will_Ferrell_tv:
        Will_Ferrell_tv.append(title)
Will_Ferrell_tv

Will_Ferrell_dict = {'Film':Will_Ferrell_film+Will_Ferrell_tv}
SNL_Cast_Members_Full_Titles_dict['Will Ferrell']=Will_Ferrell_dict
Will_Ferrell_dict


# In[39]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Tina_Fey_filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tina_Fey_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tina_Fey_film.append(title)
Tina_Fey_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tina_Fey_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tina_Fey_tv.append(title)
Tina_Fey_tv

Tina_Fey_dict = {'Film':Tina_Fey_film+Tina_Fey_tv}
SNL_Cast_Members_Full_Titles_dict['Tina Fey']=Tina_Fey_dict


# In[40]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Chloe_Fineman#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chloe_Fineman_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chloe_Fineman_film.append(title)
Chloe_Fineman_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chloe_Fineman_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chloe_Fineman_tv.append(title)
Chloe_Fineman_tv

Chloe_Fineman_dict = {'Film':Chloe_Fineman_film+Chloe_Fineman_tv}
SNL_Cast_Members_Full_Titles_dict['Chloe Fineman']=Chloe_Fineman_dict


# In[41]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Will_Forte#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Will_Forte_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Will_Forte_film.append(title)
Will_Forte_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Will_Forte_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Will_Forte_tv.append(title)
Will_Forte_tv

Will_Forte_dict = {'Film':Will_Forte_film+Will_Forte_tv}
SNL_Cast_Members_Full_Titles_dict['Will Forte']=Will_Forte_dict


# In[42]:


#WORK ON THIS ONE

# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Al_Franken#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Al_Franken_film = []
for title in df['Work']:
    Al_Franken_film.append(title)
Al_Franken_film
SNL_Cast_Members_Full_Titles_dict['Al Franken'] = {'Film':Al_Franken_film}
SNL_Cast_Members_Full_Titles_dict['Al Franken']


# In[43]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Heidi_Gardner#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Heidi_Gardner_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Heidi_Gardner_film.append(title)
Heidi_Gardner_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Heidi_Gardner_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Heidi_Gardner_tv.append(title)
Heidi_Gardner_tv

Heidi_Gardner_dict = {'Film':Heidi_Gardner_film+Heidi_Gardner_tv}
SNL_Cast_Members_Full_Titles_dict['Heidi Gardner']=Heidi_Gardner_dict


# In[44]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Janeane_Garofalo#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Janeane_Garofalo_film = []
for title in df['Title']:
#     print(title)
#     if '[' in title:         
#         print(title)         
#         sep = '['         
#         title = title.split(sep, 1)[0]         
#         print(title)
    Janeane_Garofalo_film.append(title)
Janeane_Garofalo_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Janeane_Garofalo_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Janeane_Garofalo_tv.append(title)
Janeane_Garofalo_tv

Janeane_Garofalo_dict = {'Film':Janeane_Garofalo_film+Janeane_Garofalo_tv}
SNL_Cast_Members_Full_Titles_dict['Janeane Garofalo']=Janeane_Garofalo_dict
Janeane_Garofalo_dict


# In[45]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Ana_Gasteyer#Film"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Ana_Gasteyer_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Ana_Gasteyer_film.append(title)
Ana_Gasteyer_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Ana_Gasteyer_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Ana_Gasteyer_tv.append(title)
Ana_Gasteyer_tv

Ana_Gasteyer_dict = {'Film':Ana_Gasteyer_film+Ana_Gasteyer_tv}
SNL_Cast_Members_Full_Titles_dict['Ana Gasteyer']=Ana_Gasteyer_dict
Ana_Gasteyer_dict


# In[46]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Gilbert_Gottfried#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Gilbert_Gottfried_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Gilbert_Gottfried_film.append(title)
Gilbert_Gottfried_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[2]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Gilbert_Gottfried_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Gilbert_Gottfried_tv.append(title)
Gilbert_Gottfried_tv

Gilbert_Gottfried_dict = {'Film':Gilbert_Gottfried_film+Gilbert_Gottfried_tv}
SNL_Cast_Members_Full_Titles_dict['Gilbert Gottfried']=Gilbert_Gottfried_dict


# In[47]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Mary_Gross#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Mary_Gross_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Mary_Gross_film.append(title)
Mary_Gross_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Mary_Gross_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Mary_Gross_tv.append(title)
Mary_Gross_tv

Mary_Gross_dict = {'Film':Mary_Gross_film+Mary_Gross_tv}
SNL_Cast_Members_Full_Titles_dict['Mary Gross']=Mary_Gross_dict


# In[49]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Christopher_Guest#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Christopher_Guest_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Christopher_Guest_film.append(title)
Christopher_Guest_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Christopher_Guest_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Christopher_Guest_tv.append(title)
Christopher_Guest_tv

Christopher_Guest_dict = {'Film':Christopher_Guest_film+Christopher_Guest_tv}
SNL_Cast_Members_Full_Titles_dict['Christopher Guest']=Christopher_Guest_dict
Christopher_Guest_dict


# In[50]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Bill_Hader_filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Bill_Hader_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Bill_Hader_film.append(title)
Bill_Hader_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Bill_Hader_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Bill_Hader_tv.append(title)
Bill_Hader_tv

Bill_Hader_dict = {'Film':Bill_Hader_film+Bill_Hader_tv}
SNL_Cast_Members_Full_Titles_dict['Bill Hader']=Bill_Hader_dict


# In[51]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Anthony_Michael_Hall#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Anthony_Michael_Hall_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Anthony_Michael_Hall_film.append(title)
Anthony_Michael_Hall_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Anthony_Michael_Hall_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Anthony_Michael_Hall_tv.append(title)
Anthony_Michael_Hall_tv

Anthony_Michael_Hall_dict = {'Film':Anthony_Michael_Hall_film + Anthony_Michael_Hall_tv}
SNL_Cast_Members_Full_Titles_dict['Anthony Michael Hall']=Anthony_Michael_Hall_dict


# In[52]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Brad_Hall#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Brad_Hall_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Brad_Hall_film.append(title)
Brad_Hall_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Brad_Hall_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Brad_Hall_tv.append(title)
Brad_Hall_tv

Brad_Hall_dict = {'Film':Brad_Hall_film + Brad_Hall_tv}
SNL_Cast_Members_Full_Titles_dict['Brad Hall']=Brad_Hall_dict


# In[53]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Darrell_Hammond#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Darrell_Hammond_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Darrell_Hammond_film.append(title)
Darrell_Hammond_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Darrell_Hammond_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Darrell_Hammond_tv.append(title)
Darrell_Hammond_tv

Darrell_Hammond_dict = {'Film':Darrell_Hammond_film+Darrell_Hammond_tv}
SNL_Cast_Members_Full_Titles_dict['Darrell Hammond']=Darrell_Hammond_dict


# In[54]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Phil_Hartman#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Phil_Hartman_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Phil_Hartman_film.append(title)
Phil_Hartman_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Phil_Hartman_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Phil_Hartman_tv.append(title)
Phil_Hartman_tv

Phil_Hartman_dict = {'Film':Phil_Hartman_film+Phil_Hartman_tv}
SNL_Cast_Members_Full_Titles_dict['Phil Hartman']=Phil_Hartman_dict


# In[55]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jan_Hooks#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jan_Hooks_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jan_Hooks_film.append(title)
Jan_Hooks_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jan_Hooks_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jan_Hooks_tv.append(title)
Jan_Hooks_tv

Jan_Hooks_dict = {'Film':Jan_Hooks_film+Jan_Hooks_tv}
SNL_Cast_Members_Full_Titles_dict['Jan Hooks']=Jan_Hooks_dict


# In[56]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/James_Austin_Johnson#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
James_Austin_Johnson_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    James_Austin_Johnson_film.append(title)
James_Austin_Johnson_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
James_Austin_Johnson_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    James_Austin_Johnson_tv.append(title)
James_Austin_Johnson_tv

James_Austin_Johnson_dict = {'Film':James_Austin_Johnson_film+James_Austin_Johnson_tv}
SNL_Cast_Members_Full_Titles_dict['James Austin Johnson']=James_Austin_Johnson_dict


# In[57]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Punkie_Johnson#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Punkie_Johnson_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Punkie_Johnson_film.append(title)
Punkie_Johnson_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Punkie_Johnson_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Punkie_Johnson_tv.append(title)
Punkie_Johnson_tv

Punkie_Johnson_dict = {'Film':Punkie_Johnson_film+Punkie_Johnson_tv}
SNL_Cast_Members_Full_Titles_dict['Punkie Johnson']=Punkie_Johnson_dict


# In[58]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Leslie_Jones_(comedian)#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Leslie_Jones_film = []
for title in df['Film title']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Leslie_Jones_film.append(title)
Leslie_Jones_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Leslie_Jones_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Leslie_Jones_tv.append(title)
Leslie_Jones_tv

Leslie_Jones_dict = {'Film':Leslie_Jones_film+Leslie_Jones_tv}
SNL_Cast_Members_Full_Titles_dict['Leslie Jones']=Leslie_Jones_dict


# In[59]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Colin_Jost#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Colin_Jost_film = []
for title in df['Film']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Colin_Jost_film.append(title)
Colin_Jost_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Colin_Jost_tv = []
for title in df['Series']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Colin_Jost_tv.append(title)
Colin_Jost_tv

Colin_Jost_dict = {'Film':Colin_Jost_film+Colin_Jost_tv}
SNL_Cast_Members_Full_Titles_dict['Colin Jost']=Colin_Jost_dict


# In[60]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Chris_Kattan#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chris_Kattan_film = []
for title in df['Film']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chris_Kattan_film.append(title)
Chris_Kattan_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chris_Kattan_tv = []
for title in df['Film']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chris_Kattan_tv.append(title)
Chris_Kattan_tv

Chris_Kattan_dict = {'Film':Chris_Kattan_film+Chris_Kattan_tv}
SNL_Cast_Members_Full_Titles_dict['Chris Kattan']=Chris_Kattan_dict


# In[61]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Taran_Killam#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Taran_Killam_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Taran_Killam_film.append(title)
Taran_Killam_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Taran_Killam_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Taran_Killam_tv.append(title)
Taran_Killam_tv

Taran_Killam_dict = {'Film':Taran_Killam_film+Taran_Killam_tv}
SNL_Cast_Members_Full_Titles_dict['Taran Killam']=Taran_Killam_dict


# In[62]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/David_Koechner#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
David_Koechner_film = []
for title in df['Film']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    David_Koechner_film.append(title)
David_Koechner_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
David_Koechner_tv = []
for title in df['Show']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    David_Koechner_tv.append(title)
David_Koechner_tv

David_Koechner_dict = {'Film':David_Koechner_film+David_Koechner_tv}
SNL_Cast_Members_Full_Titles_dict['David Koechner']=David_Koechner_dict


# In[63]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Julia_Louis-Dreyfus#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Julia_Louis_Dreyfus_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Julia_Louis_Dreyfus_film.append(title)
Julia_Louis_Dreyfus_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Julia_Louis_Dreyfus_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Julia_Louis_Dreyfus_tv.append(title)
Julia_Louis_Dreyfus_tv

Julia_Louis_Dreyfus_dict = {'Film':Julia_Louis_Dreyfus_film+Julia_Louis_Dreyfus_tv}
SNL_Cast_Members_Full_Titles_dict['Julia Louis-Dreyfus']=Julia_Louis_Dreyfus_dict


# In[64]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jon_Lovitz#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jon_Lovitz_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jon_Lovitz_film.append(title)
Jon_Lovitz_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jon_Lovitz_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jon_Lovitz_tv.append(title)
Jon_Lovitz_tv

Jon_Lovitz_dict = {'Film':Jon_Lovitz_film+Jon_Lovitz_tv}
SNL_Cast_Members_Full_Titles_dict['Jon Lovitz']=Jon_Lovitz_dict


# In[65]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Norm_Macdonald#Film"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[4]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Norm_Macdonald_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Norm_Macdonald_film.append(title)
Norm_Macdonald_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[5]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Norm_Macdonald_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Norm_Macdonald_tv.append(title)
Norm_Macdonald_tv

Norm_Macdonald_dict = {'Film':Norm_Macdonald_film+Norm_Macdonald_tv}
SNL_Cast_Members_Full_Titles_dict['Norm Macdonald']=Norm_Macdonald_dict


# In[66]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Michael_McKean#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Michael_McKean_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Michael_McKean_film.append(title)
Michael_McKean_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[2]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Michael_McKean_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Michael_McKean_tv.append(title)
Michael_McKean_tv

Michael_McKean_dict = {'Film':Michael_McKean_film+Michael_McKean_tv}
SNL_Cast_Members_Full_Titles_dict['Michael McKean']=Michael_McKean_dict


# In[71]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Mark_McKinney#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Mark_McKinney_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Mark_McKinney_film.append(title)
Mark_McKinney_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Mark_McKinney_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Mark_McKinney_tv.append(title)
Mark_McKinney_tv

Mark_McKinney_dict = {'Film':Mark_McKinney_film+Mark_McKinney_tv}
SNL_Cast_Members_Full_Titles_dict['Mark McKinney']=Mark_McKinney_dict
Mark_McKinney_dict


# In[72]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Kate_McKinnon#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Kate_McKinnon_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Kate_McKinnon_film.append(title)
Kate_McKinnon_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[2]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Kate_McKinnon_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Kate_McKinnon_tv.append(title)
Kate_McKinnon_tv

Kate_McKinnon_dict = {'Film':Kate_McKinnon_film+Kate_McKinnon_tv}
SNL_Cast_Members_Full_Titles_dict['Kate McKinnon']=Kate_McKinnon_dict


# In[73]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Tim_Meadows#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tim_Meadows_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tim_Meadows_film.append(title)
Tim_Meadows_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tim_Meadows_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tim_Meadows_tv.append(title)
Tim_Meadows_tv

Tim_Meadows_dict = {'Film':Tim_Meadows_film+Tim_Meadows_tv}
SNL_Cast_Members_Full_Titles_dict['Tim Meadows']=Tim_Meadows_dict


# In[74]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Seth_Meyers#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Seth_Meyers_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Seth_Meyers_film.append(title)
Seth_Meyers_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Seth_Meyers_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Seth_Meyers_tv.append(title)
Seth_Meyers_tv

Seth_Meyers_dict = {'Film':Seth_Meyers_film+Seth_Meyers_tv}
SNL_Cast_Members_Full_Titles_dict['Seth Meyers']=Seth_Meyers_dict


# In[75]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/John_Milhiser#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
John_Milhiser_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    John_Milhiser_film.append(title)
John_Milhiser_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
John_Milhiser_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    John_Milhiser_tv.append(title)
John_Milhiser_tv

John_Milhiser_dict = {'Film':John_Milhiser_film+John_Milhiser_tv}
SNL_Cast_Members_Full_Titles_dict['John Milhiser']=John_Milhiser_dict


# In[76]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Alex_Moffat#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Alex_Moffat_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Alex_Moffat_film.append(title)
Alex_Moffat_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Alex_Moffat_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Alex_Moffat_tv.append(title)
Alex_Moffat_tv

Alex_Moffat_dict = {'Film':Alex_Moffat_film+Alex_Moffat_tv}
SNL_Cast_Members_Full_Titles_dict['Alex Moffat']=Alex_Moffat_dict


# In[77]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jay_Mohr#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jay_Mohr_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jay_Mohr_film.append(title)
Jay_Mohr_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jay_Mohr_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jay_Mohr_tv.append(title)
Jay_Mohr_tv

Jay_Mohr_dict = {'Film':Jay_Mohr_film+Jay_Mohr_tv}
SNL_Cast_Members_Full_Titles_dict['Jay Mohr']=Jay_Mohr_dict


# In[78]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Kyle_Mooney#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Kyle_Mooney_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Kyle_Mooney_film.append(title)
Kyle_Mooney_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Kyle_Mooney_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Kyle_Mooney_tv.append(title)
Kyle_Mooney_tv

Kyle_Mooney_dict = {'Film':Kyle_Mooney_film+Kyle_Mooney_tv}
SNL_Cast_Members_Full_Titles_dict['Kyle Mooney']=Kyle_Mooney_dict


# In[79]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Tracy_Morgan#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tracy_Morgan_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tracy_Morgan_film.append(title)
Tracy_Morgan_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tracy_Morgan_tv = []
for title in df['Show']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tracy_Morgan_tv.append(title)
Tracy_Morgan_tv

Tracy_Morgan_dict = {'Film':Tracy_Morgan_film+Tracy_Morgan_tv}
SNL_Cast_Members_Full_Titles_dict['Tracy Morgan']=Tracy_Morgan_dict


# In[80]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Garrett_Morris#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Garrett_Morris_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Garrett_Morris_film.append(title)
Garrett_Morris_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Garrett_Morris_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Garrett_Morris_tv.append(title)
Garrett_Morris_tv

Garrett_Morris_dict = {'Film':Garrett_Morris_film+Garrett_Morris_tv}
SNL_Cast_Members_Full_Titles_dict['Garrett Morris']=Garrett_Morris_dict


# In[81]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Bobby_Moynihan#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Bobby_Moynihan_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Bobby_Moynihan_film.append(title)
Bobby_Moynihan_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Bobby_Moynihan_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Bobby_Moynihan_tv.append(title)
Bobby_Moynihan_tv

Bobby_Moynihan_dict = {'Film':Bobby_Moynihan_film+Bobby_Moynihan_tv}
SNL_Cast_Members_Full_Titles_dict['Bobby Moynihan']=Bobby_Moynihan_dict


# In[82]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Eddie_Murphy_filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Eddie_Murphy_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Eddie_Murphy_film.append(title)
Eddie_Murphy_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Eddie_Murphy_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Eddie_Murphy_tv.append(title)
Eddie_Murphy_tv

Eddie_Murphy_dict = {'Film':Eddie_Murphy_film+Eddie_Murphy_tv}
SNL_Cast_Members_Full_Titles_dict['Eddie Murphy']=Eddie_Murphy_dict


# In[83]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Bill_Murray#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Bill_Murray_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Bill_Murray_film.append(title)
Bill_Murray_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Bill_Murray_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Bill_Murray_tv.append(title)
Bill_Murray_tv

Bill_Murray_dict = {'Film':Bill_Murray_film+Bill_Murray_tv}
SNL_Cast_Members_Full_Titles_dict['Bill Murray']=Bill_Murray_dict


# In[84]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Mike_Myers#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Mike_Myers_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Mike_Myers_film.append(title)
Mike_Myers_film

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Mike_Myers_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Mike_Myers_tv.append(title)
Mike_Myers_tv

Mike_Myers_dict = {'Film':Mike_Myers_film+Mike_Myers_tv}
SNL_Cast_Members_Full_Titles_dict['Mike Myers']=Mike_Myers_dict


# In[85]:


SNL_Cast_Members_Full_Titles_dict


# In[86]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Kevin_Nealon#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# # print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Kevin_Nealon_film = []
for title in df['Work']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Kevin_Nealon_film.append(title)
Kevin_Nealon_film

Kevin_Nealon_dict = {'Film':Kevin_Nealon_film}

SNL_Cast_Members_Full_Titles_dict['Kevin Nealon']=Kevin_Nealon_dict


# In[87]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Laraine_Newman#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Laraine_Newman_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Laraine_Newman_film.append(title)
Laraine_Newman_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Laraine_Newman_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Laraine_Newman_tv.append(title)
Laraine_Newman_tv

Laraine_Newman_dict = {'Film':Laraine_Newman_film+Laraine_Newman_tv}
SNL_Cast_Members_Full_Titles_dict['Laraine Newman']=Laraine_Newman_dict


# In[88]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Ego_Nwodim#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Ego_Nwodim_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Ego_Nwodim_film.append(title)
Ego_Nwodim_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Ego_Nwodim_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Ego_Nwodim_tv.append(title)
Ego_Nwodim_tv

Ego_Nwodim_dict = {'Film':Ego_Nwodim_film+Ego_Nwodim_tv}
SNL_Cast_Members_Full_Titles_dict['Ego Nwodim']=Ego_Nwodim_dict


# In[89]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Michael_O%27Donoghue#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Michael_O_Donoghue_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Michael_O_Donoghue_film.append(title)
Michael_O_Donoghue_film

Michael_O_Donoghue_dict = {'Film':Michael_O_Donoghue_film}
SNL_Cast_Members_Full_Titles_dict["Michael O'Donoghue"]=Michael_O_Donoghue_dict
Michael_O_Donoghue_dict


# In[90]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Cheri_Oteri#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Cheri_Oteri_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Cheri_Oteri_film.append(title)
Cheri_Oteri_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Cheri_Oteri_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Cheri_Oteri_tv.append(title)
Cheri_Oteri_tv

Cheri_Oteri_dict = {'Film':Cheri_Oteri_film+Cheri_Oteri_tv}
SNL_Cast_Members_Full_Titles_dict['Cheri Oteri']=Cheri_Oteri_dict
Cheri_Oteri_dict


# In[91]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Chris_Parnell#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chris_Parnell_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chris_Parnell_film.append(title)
Chris_Parnell_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chris_Parnell_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chris_Parnell_tv.append(title)
Chris_Parnell_tv

Chris_Parnell_dict = {'Film':Chris_Parnell_film+Chris_Parnell_tv}
SNL_Cast_Members_Full_Titles_dict['Chris Parnell']=Chris_Parnell_dict


# In[92]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Nasim_Pedrad#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Nasim_Pedrad_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Nasim_Pedrad_film.append(title)
Nasim_Pedrad_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Nasim_Pedrad_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Nasim_Pedrad_tv.append(title)
Nasim_Pedrad_tv

Nasim_Pedrad_dict = {'Film':Nasim_Pedrad_film+Nasim_Pedrad_tv}
SNL_Cast_Members_Full_Titles_dict['Nasim Pedrad']=Nasim_Pedrad_dict


# In[93]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jay_Pharoah#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jay_Pharoah_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jay_Pharoah_film.append(title)
Jay_Pharoah_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jay_Pharoah_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jay_Pharoah_tv.append(title)
Jay_Pharoah_tv

Jay_Pharoah_dict = {'Film':Jay_Pharoah_film+Jay_Pharoah_tv}
SNL_Cast_Members_Full_Titles_dict['Jay Pharoah']=Jay_Pharoah_dict


# In[154]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Joe_Piscopo#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Joe_Piscopo_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Joe_Piscopo_film.append(title)
Joe_Piscopo_film.append('Saturday Night Live')


Joe_Piscopo_dict = {'Film':Joe_Piscopo_film}
SNL_Cast_Members_Full_Titles_dict['Joe Piscopo']=Joe_Piscopo_dict


# In[155]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Amy_Poehler_filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Amy_Poehler_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Amy_Poehler_film.append(title)
Amy_Poehler_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Amy_Poehler_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Amy_Poehler_tv.append(title)
Amy_Poehler_tv

indiatable=soup.find_all('table',{'class':"wikitable"})[2]
df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    if title not in Amy_Poehler_tv:
        Amy_Poehler_tv.append(title)

indiatable=soup.find_all('table',{'class':"wikitable"})[3]
df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    if title not in Amy_Poehler_tv:
        Amy_Poehler_tv.append(title)
indiatable=soup.find_all('table',{'class':"wikitable"})[4]
df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    if title not in Amy_Poehler_tv:
        Amy_Poehler_tv.append(title)    

Amy_Poehler_dict = {'Film':Amy_Poehler_film+Amy_Poehler_tv}
SNL_Cast_Members_Full_Titles_dict['Amy Poehler']=Amy_Poehler_dict
Amy_Poehler_dict


# In[100]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Randy_Quaid#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Randy_Quaid_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Randy_Quaid_film.append(title)
Randy_Quaid_film

Randy_Quaid_dict = {'Film':Randy_Quaid_film}
SNL_Cast_Members_Full_Titles_dict['Randy Quaid']=Randy_Quaid_dict


# In[101]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Colin_Quinn#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Colin_Quinn_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Colin_Quinn_film.append(title)
Colin_Quinn_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Colin_Quinn_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Colin_Quinn_tv.append(title)
Colin_Quinn_tv
indiatable=soup.find_all('table',{'class':"wikitable"})[2]
df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    if title not in Colin_Quinn_tv:
        Colin_Quinn_tv.append(title)

Colin_Quinn_dict = {'Film':Colin_Quinn_film+Colin_Quinn_tv}
SNL_Cast_Members_Full_Titles_dict['Colin Quinn']=Colin_Quinn_dict
Colin_Quinn_dict


# In[102]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Gilda_Radner#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Gilda_Radner_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Gilda_Radner_film.append(title)
Gilda_Radner_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Gilda_Radner_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Gilda_Radner_tv.append(title)
Gilda_Radner_tv

Gilda_Radner_dict = {'Film':Gilda_Radner_film+Gilda_Radner_tv}
SNL_Cast_Members_Full_Titles_dict['Gilda Radner']=Gilda_Radner_dict
Gilda_Radner_dict


# In[103]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Chris_Redd#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chris_Redd_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chris_Redd_film.append(title)
Chris_Redd_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chris_Redd_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chris_Redd_tv.append(title)
Chris_Redd_tv

Chris_Redd_dict = {'Film':Chris_Redd_film+Chris_Redd_tv}
SNL_Cast_Members_Full_Titles_dict['Chris Redd']=Chris_Redd_dict
Chris_Redd_dict


# In[104]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Rob_Riggle#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Rob_Riggle_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Rob_Riggle_film.append(title)
Rob_Riggle_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[2]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Rob_Riggle_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Rob_Riggle_tv.append(title)
Rob_Riggle_tv

Rob_Riggle_dict = {'Film':Rob_Riggle_film+Rob_Riggle_tv}
SNL_Cast_Members_Full_Titles_dict['Rob Riggle']=Rob_Riggle_dict
Rob_Riggle_dict


# In[105]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Tim_Robinson_(comedian)#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tim_Robinson_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tim_Robinson_film.append(title)
Tim_Robinson_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tim_Robinson_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tim_Robinson_tv.append(title)
Tim_Robinson_tv

Tim_Robinson_dict = {'Film':Tim_Robinson_film+Tim_Robinson_tv}
SNL_Cast_Members_Full_Titles_dict['Tim Robinson']=Tim_Robinson_dict


# In[106]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Chris_Rock_filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chris_Rock_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chris_Rock_film.append(title)
Chris_Rock_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Chris_Rock_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Chris_Rock_tv.append(title)
Chris_Rock_tv
indiatable=soup.find_all('table',{'class':"wikitable"})[2]
df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    if title not in Chris_Rock_tv:
        Chris_Rock_tv.append(title)
Chris_Rock_dict = {'Film':Chris_Rock_film+Chris_Rock_tv}
SNL_Cast_Members_Full_Titles_dict['Chris Rock']=Chris_Rock_dict
Chris_Rock_dict


# In[107]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Tony_Rosato#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tony_Rosato_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tony_Rosato_film.append(title)
Tony_Rosato_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Tony_Rosato_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Tony_Rosato_tv.append(title)
Tony_Rosato_tv

Tony_Rosato_dict = {'Film':Tony_Rosato_film+Tony_Rosato_tv}
SNL_Cast_Members_Full_Titles_dict['Tony Rosato']=Tony_Rosato_dict
Tony_Rosato_dict


# In[108]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jon_Rudnitsky#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jon_Rudnitsky_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jon_Rudnitsky_film.append(title)
Jon_Rudnitsky_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jon_Rudnitsky_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jon_Rudnitsky_tv.append(title)
Jon_Rudnitsky_tv

Jon_Rudnitsky_dict = {'Film':Jon_Rudnitsky_film+Jon_Rudnitsky_tv}
SNL_Cast_Members_Full_Titles_dict['Jon Rudnitsky']=Jon_Rudnitsky_dict
Jon_Rudnitsky_dict


# In[109]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Maya_Rudolph#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Maya_Rudolph_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Maya_Rudolph_film.append(title)
Maya_Rudolph_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Maya_Rudolph_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Maya_Rudolph_tv.append(title)
Maya_Rudolph_tv

Maya_Rudolph_dict = {'Film':Maya_Rudolph_film+Maya_Rudolph_tv}
SNL_Cast_Members_Full_Titles_dict['Maya Rudolph']=Maya_Rudolph_dict
Maya_Rudolph_dict


# In[110]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Andy_Samberg#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Andy_Samberg_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Andy_Samberg_film.append(title)
Andy_Samberg_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Andy_Samberg_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Andy_Samberg_tv.append(title)
Andy_Samberg_tv

Andy_Samberg_dict = {'Film':Andy_Samberg_film+Andy_Samberg_tv}
SNL_Cast_Members_Full_Titles_dict['Andy Samberg']=Andy_Samberg_dict
Andy_Samberg_dict


# In[111]:


#get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Adam_Sandler_filmography"
table_class="wikitable sortable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable sortable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Adam_Sandler_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Adam_Sandler_film.append(title)
Adam_Sandler_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable sortable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Adam_Sandler_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Adam_Sandler_tv.append(title)
Adam_Sandler_tv

Adam_Sandler_dict = {'Film':Adam_Sandler_film+Adam_Sandler_tv}
SNL_Cast_Members_Full_Titles_dict['Adam Sandler']=Adam_Sandler_dict
Adam_Sandler_dict


# In[112]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Horatio_Sanz#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Horatio_Sanz_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Horatio_Sanz_film.append(title)
Horatio_Sanz_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Horatio_Sanz_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Horatio_Sanz_tv.append(title)
Horatio_Sanz_tv

Horatio_Sanz_dict = {'Film':Horatio_Sanz_film+Horatio_Sanz_tv}
SNL_Cast_Members_Full_Titles_dict['Horatio Sanz']=Horatio_Sanz_dict
Horatio_Sanz_dict


# In[114]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Rob_Schneider#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Rob_Schneider_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Rob_Schneider_film.append(title)
Rob_Schneider_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Rob_Schneider_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Rob_Schneider_tv.append(title)
Rob_Schneider_tv

Rob_Schneider_dict = {'Film':Rob_Schneider_film+Rob_Schneider_tv}
SNL_Cast_Members_Full_Titles_dict['Rob Schneider']=Rob_Schneider_dict
Rob_Schneider_dict


# In[115]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Molly_Shannon#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Molly_Shannon_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Molly_Shannon_film.append(title)
Molly_Shannon_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Molly_Shannon_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Molly_Shannon_tv.append(title)
Molly_Shannon_tv

Molly_Shannon_dict = {'Film':Molly_Shannon_film+Molly_Shannon_tv}
SNL_Cast_Members_Full_Titles_dict['Molly Shannon']=Molly_Shannon_dict
Molly_Shannon_dict


# In[116]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Harry_Shearer#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Harry_Shearer_film = []
for title in df['Film']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Harry_Shearer_film.append(title)
Harry_Shearer_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Harry_Shearer_tv = []
for title in df['Series']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Harry_Shearer_tv.append(title)
Harry_Shearer_tv

Harry_Shearer_dict = {'Film':Harry_Shearer_film+Harry_Shearer_tv}
SNL_Cast_Members_Full_Titles_dict['Harry Shearer']=Harry_Shearer_dict
Harry_Shearer_dict


# In[117]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Martin_Short#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Martin_Short_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Martin_Short_film.append(title)
indiatable=soup.find_all('table',{'class':"wikitable"})[2]
df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Martin_Short_film.append(title)
# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Martin_Short_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Martin_Short_tv.append(title)
Martin_Short_tv

Martin_Short_dict = {'Film':Martin_Short_film+Martin_Short_tv}
SNL_Cast_Members_Full_Titles_dict['Martin Short']=Martin_Short_dict
Martin_Short_dict


# In[118]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Sarah_Silverman_filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Sarah_Silverman_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Sarah_Silverman_film.append(title)
indiatable=soup.find_all('table',{'class':"wikitable"})[2]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    if title not in Sarah_Silverman_film:
        Sarah_Silverman_film.append(title)
Sarah_Silverman_film


# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Sarah_Silverman_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Sarah_Silverman_tv.append(title)
Sarah_Silverman_tv

Sarah_Silverman_dict = {'Film':Sarah_Silverman_film+Sarah_Silverman_tv}
SNL_Cast_Members_Full_Titles_dict['Sarah Silverman']=Sarah_Silverman_dict
Sarah_Silverman_dict


# In[119]:


import string
# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jenny_Slate#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]
df=pd.read_html(str(indiatable))

# convert list to dataframe
df=pd.DataFrame(df[0])
Jenny_Slate_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jenny_Slate_film.append(title)

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jenny_Slate_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jenny_Slate_tv.append(title)
Jenny_Slate_tv

Jenny_Slate_dict = {'Film':Jenny_Slate_film+Jenny_Slate_tv}
SNL_Cast_Members_Full_Titles_dict['Jenny Slate']=Jenny_Slate_dict
Jenny_Slate_dict


# In[120]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Robert_Smigel#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Robert_Smigel_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Robert_Smigel_film.append(title)
Robert_Smigel_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Robert_Smigel_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Robert_Smigel_tv.append(title)
Robert_Smigel_tv

Robert_Smigel_dict = {'Film':Robert_Smigel_film+Robert_Smigel_tv}
SNL_Cast_Members_Full_Titles_dict['Robert Smigel']=Robert_Smigel_dict
Robert_Smigel_dict


# In[121]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/David_Spade#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
David_Spade_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    David_Spade_film.append(title)
David_Spade_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
David_Spade_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    David_Spade_tv.append(title)
David_Spade_tv

David_Spade_dict = {'Film':David_Spade_film+David_Spade_tv}
SNL_Cast_Members_Full_Titles_dict['David Spade']=David_Spade_dict
David_Spade_dict


# In[122]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Ben_Stiller_filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Ben_Stiller_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Ben_Stiller_film.append(title)
Ben_Stiller_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[2]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Ben_Stiller_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Ben_Stiller_tv.append(title)
Ben_Stiller_tv

Ben_Stiller_dict = {'Film':Ben_Stiller_film+Ben_Stiller_tv}
SNL_Cast_Members_Full_Titles_dict['Ben Stiller']=Ben_Stiller_dict
Ben_Stiller_dict


# In[123]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Cecily_Strong#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Cecily_Strong_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Cecily_Strong_film.append(title)
Cecily_Strong_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Cecily_Strong_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Cecily_Strong_tv.append(title)
Cecily_Strong_tv

Cecily_Strong_dict = {'Film':Cecily_Strong_film+Cecily_Strong_tv}
SNL_Cast_Members_Full_Titles_dict['Cecily Strong']=Cecily_Strong_dict
Cecily_Strong_dict


# In[125]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Jason_Sudeikis#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jason_Sudeikis_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jason_Sudeikis_film.append(title)
Jason_Sudeikis_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Jason_Sudeikis_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Jason_Sudeikis_tv.append(title)
Jason_Sudeikis_tv

Jason_Sudeikis_dict = {'Film':Jason_Sudeikis_film+Jason_Sudeikis_tv}
SNL_Cast_Members_Full_Titles_dict['Jason Sudeikis']=Jason_Sudeikis_dict
Jason_Sudeikis_dict


# In[126]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Kenan_Thompson#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Kenan_Thompson_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Kenan_Thompson_film.append(title)
Kenan_Thompson_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Kenan_Thompson_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Kenan_Thompson_tv.append(title)
Kenan_Thompson_tv

Kenan_Thompson_dict = {'Film':Kenan_Thompson_film+Kenan_Thompson_tv}
SNL_Cast_Members_Full_Titles_dict['Kenan Thompson']=Kenan_Thompson_dict
Kenan_Thompson_dict


# In[127]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Danitra_Vance#Film"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Danitra_Vance_film = []
for title in df['Film']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Danitra_Vance_film.append(title)
Danitra_Vance_film


Danitra_Vance_dict = {'Film':Danitra_Vance_film}
SNL_Cast_Members_Full_Titles_dict['Danitra Vance']=Danitra_Vance_dict
Danitra_Vance_dict


# In[128]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Melissa_Villase%C3%B1or#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Melissa_Villaseñor_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Melissa_Villaseñor_film.append(title)
Melissa_Villaseñor_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Melissa_Villaseñor_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Melissa_Villaseñor_tv.append(title)
Melissa_Villaseñor_tv

Melissa_Villaseñor_dict = {'Film':Melissa_Villaseñor_film+Melissa_Villaseñor_tv}
SNL_Cast_Members_Full_Titles_dict['Melissa Villaseñor']=Melissa_Villaseñor_dict
Melissa_Villaseñor_dict


# In[130]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Michaela_Watkins#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Michaela_Watkins_film = []
for title in df['Film']:
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Michaela_Watkins_film.append(title)
Michaela_Watkins_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Michaela_Watkins_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Michaela_Watkins_tv.append(title)
Michaela_Watkins_tv

Michaela_Watkins_dict = {'Film':Michaela_Watkins_film+Michaela_Watkins_tv}
SNL_Cast_Members_Full_Titles_dict['Michaela Watkins']=Michaela_Watkins_dict
Michaela_Watkins_dict


# In[131]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Damon_Wayans#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Damon_Wayans_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Damon_Wayans_film.append(title)
Damon_Wayans_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Damon_Wayans_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Damon_Wayans_tv.append(title)
Damon_Wayans_tv

Damon_Wayans_dict = {'Film':Damon_Wayans_film+Damon_Wayans_tv}
SNL_Cast_Members_Full_Titles_dict['Damon Wayans']=Damon_Wayans_dict
Damon_Wayans_dict


# In[132]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/No%C3%ABl_Wells#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Noël_Wells_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Noël_Wells_film.append(title)
Noël_Wells_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Noël_Wells_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Noël_Wells_tv.append(title)
Noël_Wells_tv

Noël_Wells_dict = {'Film':Noël_Wells_film+Noël_Wells_tv}
SNL_Cast_Members_Full_Titles_dict['Noël Wells']=Noël_Wells_dict
Noël_Wells_dict


# In[133]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Brooks_Wheelan#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Brooks_Wheelan_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Brooks_Wheelan_film.append(title)
Brooks_Wheelan_film


Brooks_Wheelan_dict = {'Film':Brooks_Wheelan_film}
SNL_Cast_Members_Full_Titles_dict['Brooks Wheelan']=Brooks_Wheelan_dict
Brooks_Wheelan_dict


# In[134]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Kristen_Wiig#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Kristen_Wiig_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Kristen_Wiig_film.append(title)
Kristen_Wiig_film
indiatable=soup.find_all('table',{'class':"wikitable"})[3]
df=pd.read_html(str(indiatable))
df=pd.DataFrame(df[0])
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Kristen_Wiig_film.append(title)
# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Kristen_Wiig_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Kristen_Wiig_tv.append(title)
Kristen_Wiig_tv

Kristen_Wiig_dict = {'Film':Kristen_Wiig_film+Kristen_Wiig_tv}
SNL_Cast_Members_Full_Titles_dict['Kristen Wiig']=Kristen_Wiig_dict
Kristen_Wiig_dict


# In[137]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Casey_Wilson#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Casey_Wilson_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Casey_Wilson_film.append(title)
Casey_Wilson_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Casey_Wilson_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Casey_Wilson_tv.append(title)
Casey_Wilson_tv

Casey_Wilson_dict = {'Film':Casey_Wilson_film+Casey_Wilson_tv}
SNL_Cast_Members_Full_Titles_dict['Casey Wilson']=Casey_Wilson_dict
Casey_Wilson_dict


# In[138]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Fred_Wolf_(writer)#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Fred_Wolf_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Fred_Wolf_film.append(title)
Fred_Wolf_film


Fred_Wolf_tv = ['The Pat Sajak Show','The Chevy Chase Show','Saturday Night Live']

Fred_Wolf_dict = {'Film':Fred_Wolf_film+Fred_Wolf_tv}
SNL_Cast_Members_Full_Titles_dict['Fred Wolf']=Fred_Wolf_dict
Fred_Wolf_dict


# In[139]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Bowen_Yang#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Bowen_Yang_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Bowen_Yang_film.append(title)
Bowen_Yang_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Bowen_Yang_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Bowen_Yang_tv.append(title)
Bowen_Yang_tv.append("Schmigadoon!")

Bowen_Yang_dict = {'Film':Bowen_Yang_film+Bowen_Yang_tv}
SNL_Cast_Members_Full_Titles_dict['Bowen Yang']=Bowen_Yang_dict
Bowen_Yang_dict


# In[141]:


# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Sasheer_Zamata#Filmography"
table_class="wikitable"
response=requests.get(wikiurl)
# print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find_all('table',{'class':"wikitable"})[0]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Sasheer_Zamata_film = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Sasheer_Zamata_film.append(title)
Sasheer_Zamata_film

# parse data from the html into a beautifulsoup object
indiatable=soup.find_all('table',{'class':"wikitable"})[1]

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
Sasheer_Zamata_tv = []
for title in df['Title']:     
    if '[' in title:         
        print(title)         
        sep = '['         
        title = title.split(sep, 1)[0]         
        print(title)
    Sasheer_Zamata_tv.append(title)
Sasheer_Zamata_tv

Sasheer_Zamata_dict = {'Film':Sasheer_Zamata_film+Sasheer_Zamata_tv}
SNL_Cast_Members_Full_Titles_dict['Sasheer Zamata']=Sasheer_Zamata_dict
Sasheer_Zamata_dict


# In[142]:


SNL_Cast_Members_Full_Titles_dict


# In[160]:


# No wiki tables
Morwenna_Banks_dict = {'Film':['Absolutely','The Thick of It','Red Dwarf',"Ruddy Hell! It's Harry and Paul",'Saxondale','Skins','Shameless','Stressed Eric','Between the Lions','Peppa Pig','Hyperdrive','Meg and Mog','Rupert Bear',"King Arthur's Disasters","Ben and Holly's Little Kingdom",'Humf','Sabrina the Teenage Witch','The Announcement','Catterick','Crapston Villas','Miss You Already','Gloomsbury','Tales of the Riverbank','The Eichmann Show','Damned','Shush!','The Adventures of Paddington','Saturday Night Live',]}
SNL_Cast_Members_Full_Titles_dict['Morwenna Banks'] = Morwenna_Banks_dict

A_Whitney_Brown_dict = {'Film':['Saturday Night Live','Tales From the Crypt','The Big Picture: An American Commentary',"The Daily Show"]}
SNL_Cast_Members_Full_Titles_dict['A. Whitney Brown'] = A_Whitney_Brown_dict

Beth_Cahill_dict = {'Film':['Saturday Night Live']}
SNL_Cast_Members_Full_Titles_dict['Beth Cahill']= Beth_Cahill_dict

Ellen_Cleghorne_dict = {'Film':['Armageddon','Coyote Ugly','Little Nicky','Old School','Grown Ups 2','Second Act','Def Comedy Jam','In Living Color','Cleghorne!','The Adventures of Pete and Pete','Worst Cooks in America: Celebrity Edition','Saturday Night Live']}
SNL_Cast_Members_Full_Titles_dict['Ellen Cleghorne']=Ellen_Cleghorne_dict

Denny_Dillon_dict = {'Film':['Saturday Night Fever','Dream On','The Magic of Herself the Elf','Night Court','Dr. Science', 'Roseanne: An Unauthorized Biography','Ice Age','Saturday Night Live']}
SNL_Cast_Members_Full_Titles_dict['Denny Dillon']= Denny_Dillon_dict

Andrew_Dismukes_dict = {'Film':['Call Me Brother','Inside Joke at Moontower','Saturday Night Live']}
SNL_Cast_Members_Full_Titles_dict['Andrew Dismukes']= Andrew_Dismukes_dict

Chris_Farley_dict = {'Film':["Wayne's World","Coneheads","Airheads","Billy Madison","Tommy Boy","Black Sheet","Beverly Hill Ninja","Almost Heroes","Dirty Work",'Saturday Night Live']}
SNL_Cast_Members_Full_Titles_dict['Chris Farley'] = Chris_Farley_dict

Rich_Hall_dict = {'Film':["Police Academy 2: Their First Assignment","One Crazy Summer","Million Dollar Mystery","C.H.U.D. II: Bud the C.H.U.D.","The Lives of the Saints",
                          "Arthur Christmas",'Not Necessarily the News','Fridays',
                          'Saturday Night Live',"Vanishing America","Monsters","Rich Hall's Fishing Show","Rich Hall's Cattle Drive (2006)","Rich Hall's How the West Was Lost","Rich Hall's The Dirty South","Rich Hall's Continental Drifters","Rich Hall's Inventing the Indian","Rich Hall's You Can Go To Hell, I'm Going To Texas","Rich Hall's California Stars","Rich Hall's Presidential Grudge Match","Rich Hall's Countrier Than You,""Rich Hall's Working for the American Dream,""Rich Hall's Red Menace,"'Elliott From Earth']}
SNL_Cast_Members_Full_Titles_dict['Rich Hall']=Rich_Hall_dict

Lauren_Holt_dict = {'Film':['Los Paradise: Tell You How I Feel','Keep Calm and Tampon','Parent Teacher Conference','Strange Beverly','Hunky-Dory Soda Pop!','Hypocrite','Saturday Night Live','Open Houses','The Filth','It Listens from the Radio']}
SNL_Cast_Members_Full_Titles_dict['Lauren Holt'] = Lauren_Holt_dict

Yvonne_Hudson_dict = {'Film':['Saturday Night Live']}
SNL_Cast_Members_Full_Titles_dict['Yvonne Hudson']=Yvonne_Hudson_dict

Melanie_Hutsell_dict = {'Film':["Can't Stop Dancing","He's Such a Girl","Bridesmaids","Mother's Little Helpers",'Saturday Night Live',"Best Dishes with Paula Deen","Lady Dynamite","Transparent"]}
SNL_Cast_Members_Full_Titles_dict['Melanie Hutsell']=Melanie_Hutsell_dict


Victoria_Jackson_dict = {'Film': ['Bizarre','Stoogemania','Baby Boom','The Pick-up Artist','Casual Sex?','The Couch Trip','Dream a Little Dream','UHF','Family Business','I Love You to Death','Sesame Street','The Undercover Kid','In the Heat of the Night','The Weird Al Show','Nightmare Ned','No More Baths','Elmo Aardvark: Outer Space Detective','The Wheels on the Bus','Brother White','Fat Chance','The Matchbreaker','Altar Egos', "Saturday Night Live"]}
SNL_Cast_Members_Full_Titles_dict['Victoria Jackson']=Victoria_Jackson_dict

                         
Tim_Kazurinsky_dict ={'Film':['Somewhere in Time','Saturday Night Live','Neighbors','About Last Night...','Police Academy 2','Police Academy 3','Police Academy 4','Married... with Children','Early Edition','Police Academy: The Series','Curb Your Enthusiasm', 'What About Joan?', 'Still Standing','According to Jim','Strange Relations',"The Moleman of Belmont Avenue",'Chicago Justice','Easy']}
SNL_Cast_Members_Full_Titles_dict['Tim Kazurinsky']=Tim_Kazurinsky_dict

                         
Laura_Kightlinger_dict = {'Film':['Saturday Night Live','Tenacious D','he Minor Accomplishments of Jackie Woodman',"Who's the Caboose?",'Dependable People','Sixty Spins Around the Sun','Dysenchanted','The Lego Batman Movie','Cat Demon: Re-Exhumed','Daddy Day Care', 'Kicking and Screaming', 'Wake Up', 'Ron Burgundy: The Lost Movie', 'The Truth About Lies','The Outdoorsman']}
SNL_Cast_Members_Full_Titles_dict['Laura Kightlinger']=Laura_Kightlinger_dict

                         
Gary_Kroeger_dict = {'Film':['Saturday Night Live','The Big Picture','Archie: To Riverdale and Back Again','A Man Called Sarge','Murder She Wrote','The Newlywed Game', 'Beat the Clock','Card Sharks','Whammy! The All-New Press Your Luck','Hidden Hills','Curb Your Enthusiasm','Comic Strip Live','Columbo: Death Hits the Jackpot']}
SNL_Cast_Members_Full_Titles_dict['Gary Kroeger']=Gary_Kroeger_dict

                         
Matthew_Laurance_dict = {'Film':['Saturday Night Live','Eddie and the Cruisers','Eddie and the Cruisers II: Eddie Lives!','Streets of Fire','Duet','thirtysomething','Beverly Hills, 90210']}
SNL_Cast_Members_Full_Titles_dict['Matthew Laurance']=Matthew_Laurance_dict

                         
Mike_O_Brien_dict = {'Film':['Saturday Night Live',"7 Minutes in Heaven with Mike O'Brien",'A.P. Bio']}
SNL_Cast_Members_Full_Titles_dict["Mike O'Brien"]=Mike_O_Brien_dict

                         
Gail_Matthius_dict = {'Film':['Saturday Night Live','Assaulted Nuts','Laugh Trax',"Bobby's World",'Tiny Toon Adventures', 'Animaniacs', 'The Ren & Stimpy Show', 'Bump in the Night','The Tick']}
SNL_Cast_Members_Full_Titles_dict['Gail Matthius']=Gail_Matthius_dict

                         
Laurie_Metcalf_dict ={'Film':['Saturday Night Live','Roseanne','Duckman','King of the Hill','Life with Louie','Dharma and Greg',
                              '3rd Rock from the Sun','The Norm Show','Charlie Lawrence','Easy Money','Absolutely Fabulous', 'Malcolm in the Middle',
                              'My Boys', 'Frasier', 'Portlandia', 'Without a Trace',"Grey's Anatomy",'Monk','Desperate Housewives','The Big Bang Theory','Getting On','The McCarthys','Horace and Pete','The Connors','A Wedding',
                              'Desperately Seeking Susan','Making Mr. Right','Miles from Home','Stars and Bars','Uncle Buck','Pacific Heights','Mistress','A Dangerous Woman','Blink','Leaving Las Vegas','Bulworth','Runaway Bride','JFK','Toy Story','Toy Story 2','Toy Story 3','Toy Story 4','Scream 2','The Long Island Incident','Treasure Planet','Meet the Robinsons','Beer League','Fun with Dick and Jane','Georgia Rule','Stop Loss','Lady Bird']}
SNL_Cast_Members_Full_Titles_dict['Laurie Metcalf']=Laurie_Metcalf_dict

                         
Alan_Zweibel_dict = {'Film':['Saturday Night Live',"It's Garry Shandling's Show",'Curb Your Enthusiasm','Monk','The Last Laugh','The Zen Diaries of Garry Shandling','Gilbert','Love, Gilda','Here Today','Dragnet','The Story of Us','North']}                         
SNL_Cast_Members_Full_Titles_dict['Alan Zweibel']=Alan_Zweibel_dict

                         
Don_Novello_dict = {'Film':['Saturday Night Live','Chicken Little Comedy Show','The Smothers Brothers Show','SCTV','The Godfather Part III','Atlantis: The Lost Empire',"Atlantis: Milo's Return",'All in the Bunker','The Colbert Report',"Mr. Mike's Mondo Video",'Become an Artist','Head Office','Father Guido Sarducci Goes to College','Tucker: The Man and His Dream','Blossom','Teenage Bonnie and Klepto Clyde','Casper','One Night Stand','Married... with Children','Jack','Touch','Just the Ticket','The Adventures of Rocky and Bullwinkle','Just One Night','Nothing Sacred','Factory Girl','Twixt','Palo Alto']}
SNL_Cast_Members_Full_Titles_dict['Don Novello']=Don_Novello_dict

                         
Ann_Risley_dict = {'Film':['Saturday Night Live','Off Campus','Night After Night','The Doctors','The Young Riders','Telling Secrets','Annie Hall',"Oliver's Story",'Manhattan','Simon','Stardust Memories','Honky Tonk Freeway','Rich and Famous','Come Back to the Five and Dime, Jimmy Dean, Jimmy Dean','Desert Bloom','El Diablo','Sunstroke','Four Eyes and Six Guns']}
SNL_Cast_Members_Full_Titles_dict['Ann Risley']=Ann_Risley_dict

                         
Julia_Sweeney_dict = {'Film':["It's Pat",'Saturday Night Live','This American Life','Pulp Fiction','Gremlins 2: The New Batch', 'Coneheads', 'Vegas Vacation', 'Clockstoppers', 'Whatever It Takes','Stuart Little','Baby Blues','The Goode Family','Back at the Barnyard','Lloyd in Space','Monsters University','George and Leo',"Maybe It's Me",'3rd Rock from the Sun','Hope & Gloria', 'Mad About You', 'According to Jim','Frasier','Sex and the City','Desperate Housewives','Brooklyn Nine-Nine']}
SNL_Cast_Members_Full_Titles_dict['Julia Sweeney']=Julia_Sweeney_dict

                         
Nancy_Walls_dict = {'Film':['Saturday Night Live','The Daily Show','The Goode Family','The Office','Bridesmaids','Angie Tribeca','The 40-Year-Old Virgin','Anger Management','Seeking a Friend for the End of the World']}                         
SNL_Cast_Members_Full_Titles_dict['Nancy Walls']=Nancy_Walls_dict

                         
Terry_Sweeney_dict = {'Film':['Saturday Night Live','MADtv','Hype','Tripping the Rift','Shag']}
SNL_Cast_Members_Full_Titles_dict['Terry Sweeney']=Terry_Sweeney_dict

                         
Charles_Rocket_dict = {'Film':['The Outlaws','Saturday Night Live','Fraternity Vacation','Miracles','Down Twisted','Earth Girls Are Easy','How I Got Into College','Honeymoon Academy','Dances with Wolves','Delirious','Brainsmasher... A Love Story','Hocus Pocus','Short Cuts',"It's Pat",'Wagons East','Dumb and Dumber','Steal Big Steal Little',"Charlie's Ghost Story",'Tom and Huck','Murder at 1600',"Fathers' Day",'The Killing Grounds','Dry Martini',"Carlo's Wake",'Titan A.E.','Tex','New Suit','Bleach','Shade','Yu-Gi-Oh! The Movie: Pyramid of Light','Fly Me to the Moon',
                              'Law & Order: Criminal Intent','The King of Queens','Static Shock','Greg the Bunny','The Zeta Project','3rd Rock from the Sun','Normal, Ohio','Batman Beyond','The X-Files','Star Trek: Voyager','Superman: The Animated Series','Tracey Takes On...','Cybill','Jenny','The New Batman Adventures','Grace Under Fire','Men in Black: The Series','The Pretender','Picket Fences',
                               'The Adventures of Hyperman','The Home Court','Touched by an Angel','Lois & Clark: The New Adventures of Superman','Wings','Wild Palms','Flying Blind','Tequila and Bonetti',"Parker Lewis Can't Lose",'Quantum Leap','Murder, She Wrote','Doctor Doctor','thirtysomething',"Murphy's Law",'Max Headroom','Miami Vice','Moonlighting','Hardcastle and McCormick','California Girls','Remington Steele','Steel Collar Man','Hawaiian Heat','The Investigators',"I Do, I Don't",'TV Party']}                         
SNL_Cast_Members_Full_Titles_dict['Charles Rocket']=Charles_Rocket_dict

                         
Pamela_Stephenson_dict = {'Film': ['The Yeomen of the Guard','Ryan','Space: 1999','The Violins of Saint-Jacques','New Avengers','Tales of the Unexpected','Funny Man','The Comic Strip',"Not The Nine O'Clock News",'The Professionals','Saturday Night Live','Private Collection', 'Stand Up', 'Virgin Soldiers', 'The Comeback', 'Doctors and Nurses', "Mel Brooks's History of the World, Part 1", 'Superman III', 'Bloodbath at the House of Death', 'Finders Keepers' , 'Scandalous', 'Ghosts Can Do It', 'Les Patterson Saves the World']}
SNL_Cast_Members_Full_Titles_dict['Pamela Stephenson']=Pamela_Stephenson_dict

                         
Sarah_Sherman_dict = {'Film':['Saturday Night Live','Jackass Forever']}
SNL_Cast_Members_Full_Titles_dict['Sarah Sherman']=Sarah_Sherman_dict

                         
Paul_Shaffer_dict = {'Film':['This Is Spinal Tap','Blues Brothers 2000','Scrooged',"Look Who's Talking Too",'Hercules','Happy New Year, America','Cover Wars','Law & Order: Criminal Intent','How I Met Your Mother','A Very Murray Christmas',"Schitt's Creek",'The Masked Singer','Saturday Night Live']}                         
SNL_Cast_Members_Full_Titles_dict['Paul Shaffer']=Paul_Shaffer_dict

                         
Jeff_Richards_dict = {'Film':['MADtv','Saturday Night Live','Mind of Mencia','Comics Unleashed with Byron Allen',"'Til Death",'Where My Dogs At?','FlashForward','The Burr Effect','The Hand Job','Projectorhead','Sheep Man','Bad Mofos']}
SNL_Cast_Members_Full_Titles_dict['Jeff Richards']=Jeff_Richards_dict

                         
Tom_Schiller_dict = {'Film':['Saturday Night Live',"La Dolce Gilda", "Don't Look Back in Anger","Java Junkie","Love Is a Dream",'Nothing Lasts Forever']}                         
SNL_Cast_Members_Full_Titles_dict['Tom Schiller']=Tom_Schiller_dict

                         
Emily_Prager_dict = {'Film':['Arena Brains','The Edge of Night','Tarzoon: Shame of the Jungle',"Mr. Mike's Mondo Video",'The National Lampoon Radio Hour','Saturday Night Live']}
SNL_Cast_Members_Full_Titles_dict['Emily Prager']=Emily_Prager_dict

                         
Dennis_Miller_dict = {'Film':['The Dennis Miller Show','Saturday Night Live','Dennis Miller Live','Monday Night Football','Hannity & Colmes','CNBC','Space Ghost Coast to Coast','Grand Slam','Amne$ia','Dennis Miller + One']}                         
SNL_Cast_Members_Full_Titles_dict['Dennis Miller']=Dennis_Miller_dict

                         
Finesse_Mitchell_dict = {'Film':['Saturday Night Live','The Late Late Show with Craig Kilborn',"Late Night with Conan O'Brien","Who's Your Caddy?",'The Comebacks','Mad Money',"Nick Swardson's Pretend Time",'The Choice','A.N.T. Farm','Roadies','Barely Lethal','Outmatched','Is It Cake?']}                         
SNL_Cast_Members_Full_Titles_dict['Finesse Mitchell']=Finesse_Mitchell_dict

                         
Jerry_Minor_dict = {'Film':['Saturday Night Live','Mr. Show', 'Trigger Happy TV', 'Delocated', 'Brickleberry', 'Unbreakable Kimmy Schmidt', 'Crossballs', 'The Hotwives of Orlando', 'Carpoolers', 'Community', 'Lucky Louie','Dr. Ken','Cedric the Entertainer Presents','Arrested Development','The Daily Show',"Lewis Black's Root of All Evil",'I Love You, Man', 'Drillbit Taylor', 'Beer League', 'Melvin Goes to Dinner','Curb Your Enthusiasm', 'Funny or Die Presents', 'Drunk History', 'The League', "Nick Swardson's Pretend Time", 'Key & Peele', 'Jon Benjamin Has a Van', 'Last Man Standing', 'How I Met Your Mother', 'Brooklyn Nine-Nine','Eastbound & Down','The Hotwives',"Bob's Burgers"]}                         
SNL_Cast_Members_Full_Titles_dict['Jerry Minor']=Jerry_Minor_dict

                         
Luke_Null_dict = {'Film':['Saturday Night Live']}
SNL_Cast_Members_Full_Titles_dict['Luke Null']=Luke_Null_dict

Dan_Vitale_dict = {'Film':['Saturday Night Live']}
SNL_Cast_Members_Full_Titles_dict['Dan Vitale']=Dan_Vitale_dict
                         
Patrick_Weathers_dict = {'Film':['Saturday Night Live']}
SNL_Cast_Members_Full_Titles_dict['Patrick Weathers']=Patrick_Weathers_dict


# In[161]:


# # get the response in the form of html
# wikiurl="https://en.wikipedia.org/wiki/"
# table_class="wikitable"
# response=requests.get(wikiurl)
# # print(response.status_code)

# # parse data from the html into a beautifulsoup object
# soup = BeautifulSoup(response.text, 'html.parser')
# indiatable=soup.find_all('table',{'class':"wikitable"})[0]

# df=pd.read_html(str(indiatable))
# # convert list to dataframe
# df=pd.DataFrame(df[0])
# _film = []
# for title in df['Title']:     if '[' in title:         print(title)         sep = '['         title = title.split(sep, 1)[0]         print(title)
#     _film.append(title)
# _film

# # parse data from the html into a beautifulsoup object
# indiatable=soup.find_all('table',{'class':"wikitable"})[1]

# df=pd.read_html(str(indiatable))
# # convert list to dataframe
# df=pd.DataFrame(df[0])
# _tv = []
# for title in df['Title']:     if '[' in title:         print(title)         sep = '['         title = title.split(sep, 1)[0]         print(title)
#     _tv.append(title)
# _tv

# _dict = {'Film':_film+_tv}
# SNL_Cast_Members_Full_Titles_dict['']=_dict


# In[162]:


SNL_Cast_Members_Full_Titles_dict.keys()


# In[163]:


Final_dict = {}
for i in SNL_Cast_Members_Full_Titles_dict.items():
    flat_list = [num for sublist in i[1].values() for num in sublist]
#     print(flat_list)
#     print(i[0])
#     print(i[1].values())
    Final_dict[i[0]]=list(set(flat_list))
Final_dict


# In[ ]:




