import os
#!pip install numpy==1.26.4
import pandas as pd
#import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

# Load the .env file variables
load_dotenv("/workspaces/interacting-with-api-python-project-tutorial/keys.env")

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")


credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
connection = spotipy.Spotify(client_credentials_manager=credentials)

artist = connection.artist_top_tracks("28gNT5KBp7IjEOQoevXf9N")

top_10_tracks = [(d["name"],d["popularity"],d["duration_ms"]) for d in artist["tracks"][0:10]]

df = pd.DataFrame(top_10_tracks ,columns=["Track", "Popularity", "Duration"])

print("Top 3 songs for Camilo: \n",df.head(3))

x_values = df.Popularity
y_values = df.Duration

plt.scatter(x_values,y_values)
plt.show()
plt.savefig("ScatterPlot Popularity vs Duration.jpg",dpi = 300)


print("\nCorrelations for Popularity vs Duration \n \n", df.corr())