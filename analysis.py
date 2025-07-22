import pandas as pd
import matplotlib.pyplot as plt

#load data
df = pd.read_csv(r"D:\analysis\newOne\matplotlib_file\Netflix_data_analysis\netflix_titles.csv")

#clean data
df = df.dropna(subset=['type','title','director','cast','country','rating'])

type_count = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index,type_count.values,color=['red','orange'])
plt.xlabel("Type of Content")
plt.ylabel("Number of Movies/Shows")
plt.title("number of Movies vs Shows on Netflix")
plt.tight_layout()
plt.savefig("movies_vs_shows.png")

rating_count = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_count, labels=rating_count.index, autopct="%1.1f%%",startangle=90)
plt.title("Rating count")
plt.tight_layout()
plt.savefig("content_rating.png")

movie_df = df[df['type'] == 'Movie'].copy()
movie_df = movie_df.dropna(subset=['duration'])  # Ensure no NaNs
movie_df['duration_int'] = movie_df['duration'].str.replace(' min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.title("Distribution of Movie Durations")
plt.tight_layout()
plt.savefig("movies_duration.png")

release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(8,6))
plt.scatter(release_count.index,release_count.values,color='purple')
plt.xlabel("Year of Release")
plt.ylabel("Number of shows")
plt.title("Shows per Year")
plt.tight_layout()
plt.savefig("shows Release year")

country_count = df['country'].value_counts().head(10)
plt.barh(country_count.index,country_count.values,color='blue')
plt.title("Top 10 countries by Number of shows")
plt.xlabel("Number of shows")
plt.ylabel("countries")
plt.tight_layout()
plt.savefig("top_10_countries.png")

content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2,figsize=(12,5))

ax[0].plot(content_by_year.index,content_by_year['Movie'],color='red')
ax[0].set_title("Movies released Per year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")

ax[1].plot(content_by_year.index,content_by_year['TV Show'],color='green')
ax[1].set_title("TV Shows released Per year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Number of TV Shows")

fig.suptitle("Comparison b/w Movies And TV Shows Released Per Year")
plt.tight_layout()
plt.savefig("Comparison.png")
plt.show()
