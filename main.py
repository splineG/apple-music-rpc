import pypresence
import requests
import time

# Apple Music API key
api_key = 'here'

# Apple Music developer token
developer_token = 'here'

# Discord client ID
client_id = '3061952143122544550'

# Discord user token
user_token = 'OTM2NjA1NUTmdjkxMDgz0.GQs6hg.jqVBMxA6kdw0qnkdnerOlEA0vuDnaeoTGWo7Bj9nBw'

# set the Discord Rich Presence
rpc = pypresence.Presence(client_id, user_token=user_token)
rpc.connect()

# continuously update the Rich Presence as the song changes
while True:
    # make a GET request to the /me/player/currently-playing endpoint
    headers = {'Authorization': f'Bearer {developer_token}'}
    response = requests.get('https://api.music.apple.com/v1/me/player/currently-playing', headers=headers)

    # get the current track and artist, and the time elapsed in the song
    data = response.json()
    track = data['item']['name']
    artist = data['item']['artistName']
    progress = data['progress']['ms'] // 1000

    # update the Rich Presence
    rpc.update(state=track, details=artist, large_image='apple_music', large_text='Apple Music', start=progress)

    # wait 1 second before updating again
    time.sleep(1)
