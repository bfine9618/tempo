
# coding: utf-8

# http://www.last.fm/api/ is the URL for the api

# In[63]:

import urllib3
import json
from pandas.io.json import json_normalize
import numpy as np


# In[68]:

http = urllib3.PoolManager()


# **Possible Genres are: **
#     electronic, jazz, folk, indie, rock, pop, country, rap

# In[112]:

genre = 'country'
numSongs = '1000'
apiKey = '0c25476dba4df7cb7e8aa5b7f2d7e295'
url = 'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag='


r = http.request('GET', url+genre+'&limit='+numSongs+'&api_key='+apiKey+'&format=json')
data = json.loads(r.data.decode('utf-8'))
test = json_normalize(data['tracks']['track'])
test['duration'] = test['duration'].apply(lambda x: float(x))
test.drop(['artist.mbid', 'image', 'streamable.#text', 'streamable.fulltrack', 'url', 'artist.url'] , axis=1, inplace=True)
test = test.rename(columns = {'@attr.rank':'rank', 'artist.name':'artist'})
test = test[['name', 'artist', 'duration', 'rank', 'mbid']]


# In[113]:

test['name'] = test['name'].apply(lambda x: x.upper())
test['artist'] = test['artist'].apply(lambda x: x.upper())


# In[119]:

test.to_csv('country1000.csv')


# In[111]:




# In[ ]:



