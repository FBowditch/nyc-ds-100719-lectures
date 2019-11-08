

def find_by_name(album):
    for x in data_list:
            if x['album'] == album:
                   return x
    
    
def find_by_rank(rank):
    for x in data_list:
            if int(x['number']) == rank:
                   return x['album']


def find_by_year(year):
    yearly_albums = []
    for x in data_list:
            if int(x['year']) == year:
                   yearly_albums.append(x['album'])
    return yearly_albums
    

def find_by_years(year1, year2):
    yearly_albums = []
    for x in data_list:
        if int(x['year']) >= year1 and int(x['year']) <= year2:
                yearly_albums.append(x['album'])
    return yearly_albums


def find_by_ranks(rank1, rank2):
    ranked_albums = []
    for x in data_list:
        if int(x['number']) >= rank1 and int(x['number']) <= rank2:
                ranked_albums.append(x['album'])
        else:
            pass
    return ranked_albums


def all_titles(data):
    titles =[]
    for x in data:
        titles.append(x['album'])
    return titles

def all_artist(data):
    artist =[]
    for x in data:
        artist.append(x['artist'])
    return artist




def most_albums(data):
    
    data2 = []
    for x in data:
        data2.append(x['artist'])
    
    frequency_dict = {}
    
    for x in data2:
        if x not in frequency_dict:
            frequency_dict[x] = 1
        else:
            frequency_dict[x] += 1
            
    Most_albums_list = []

    highest_freq = max(frequency_dict.values())
    for key, val in frequency_dict.items():
        if val == highest_freq:
            Most_albums_list.append(key)
    
    return Most_albums_list



def most_words_title(data):
    
    data2 = []
    for x in data:
        data2.append(x['album'])
    
    words = []
    for title in data2:
        words.extend(title.split())
    
    frequency_dict = {}
    
    for word in words:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1
            
    Most_Popular_Word = []

    highest_freq = max(frequency_dict.values())
    for key, val in frequency_dict.items():
        if val == highest_freq:
            Most_Popular_Word.append(key)
    
    return Most_Popular_Word


#HISTOGRAM ALBUMS

import pandas as pd
df = pd.read_csv('data.csv')
years = list(df['year'])
df.head()

import matplotlib.pyplot as plt
plt.hist(years, bins=[1950,1960,1970,1980,1990,2000,2010,2020])

plt.xlabel('Years')
plt.ylabel('#Albums')
plt.title('Albums Per Decade')

#HISTOGRAM GENRES :::::: STILL WORKING

def get_genres(data): 
    
    genres_list = []
    for x in data:
        genres_list.append(x['genre'])
    return set(genres_list)

print(get_genres(data_list))


####NEXT STEPS

text_file = open('top-500-songs.txt', 'r')
   
lines = text_file.readlines()

def separate_string(data):
    
    strings_list = []
   
    for item in data:
        strings1 = item.strip()
        string2 = strings1.split('\t')
        strings_list.append(string2)


    return strings_list
                  
lines_dict = separate_string(lines)


#DICTIONARY FOR LIST OF 500 SONGS
#STILL WORKING

text_file = open('top-500-songs.txt', 'r')
   
lines = text_file.readlines()

def separate_string(data):
    
    strings_list = []
   
    for item in data:
        strings1 = item.strip()
        string2 = strings1.split('\t')
        strings_list.append(string2)


    return strings_list
                  
lines3 = separate_string(lines)


lines_dict = {}

for song in lines3:
    lines_dict["RANK"] = lines3[0][0]
    lines_dict["NAME"] = lines3[0][1]
    lines_dict["ARTIST"] = lines3[0][2]
    lines_dict["YEAR"] = lines3[0][3]

lines_dict


