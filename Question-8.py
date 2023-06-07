#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
import matplotlib.pyplot as plt

# Send a GET request to retrieve the data from the API
url = 'http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'
response = requests.get(url)
data = response.json()

# Extract the episodes data
episodes = data['_embedded']['episodes']

# Convert the episodes data into a pandas DataFrame
df = pd.DataFrame(episodes)

# Get all the overall ratings for each season
season_ratings = df.groupby('season')['rating'].mean()

# Plotting the ratings for each season
plt.figure(figsize=(10, 6))
season_ratings.plot(kind='bar')
plt.xlabel('Season')
plt.ylabel('Average Rating')
plt.title('Overall Ratings for Each Season of Westworld')
plt.xticks(rotation=0)
plt.show()

# Get all the episode names whose average rating is more than 8 for every season
high_rated_episodes = df.groupby(['season', 'name']).filter(lambda x: x['rating'].mean() > 8)['name']

# Get all the episode names that aired before May 2019
air_date_threshold = '2019-05'
episodes_before_2019 = df[df['airdate'] < air_date_threshold]['name']

# Get the episode name from each season with the highest and lowest rating
highest_rated_episodes = df.groupby('season')['rating'].idxmax().apply(lambda idx: df.loc[idx, 'name'])
lowest_rated_episodes = df.groupby('season')['rating'].idxmin().apply(lambda idx: df.loc[idx, 'name'])

# Get the summary for the most popular (highest ratings) episode in every season
most_popular_episodes = df.groupby('season').apply(lambda x: x.loc[x['rating'].idxmax(), 'summary'])

# Print the results
print('Overall Ratings for Each Season:')
print(season_ratings)
print('\nEpisode Names with Average Rating > 8:')
print(high_rated_episodes)
print('\nEpisode Names Aired Before May 2019:')
print(episodes_before_2019)
print('\nEpisode with Highest Rating in Each Season:')
print(highest_rated_episodes)
print('\nEpisode with Lowest Rating in Each Season:')
print(lowest_rated_episodes)
print('\nSummary of the Most Popular Episode in Each Season:')
print(most_popular_episodes)


# In[ ]:




