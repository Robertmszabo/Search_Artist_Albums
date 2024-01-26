import requests

def search_artist_albums(artist_name, access_token):
    base_url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Search for the artist
    params = {
        "q": artist_name,
        "type": "artist",
    }
    response = requests.get(base_url, params=params, headers=headers)
    artist_data = response.json()

    # Get the artist's ID
    artist_id = artist_data["artists"]["items"][0]["id"]

    # Get the artist's albums
    albums_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    response = requests.get(albums_url, headers=headers)
    albums_data = response.json()

    # Display the list of albums
    print(f"Albums by {artist_name}:")
    for album in albums_data["items"]:
        print(album["name"])

# Replace 'your_client_id' and 'your_client_secret' with your Spotify API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Get access token
token_url = "https://accounts.spotify.com/api/token"
token_params = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
}

token_response = requests.post(token_url, data=token_params)
access_token = token_response.json()["access_token"]

# Get user input for the artist's name
artist_name = input("Enter the artist's name: ")

# Search for the artist's albums
search_artist_albums(artist_name, access_token)
