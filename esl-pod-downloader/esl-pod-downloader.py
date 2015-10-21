import logging
import os.path
import urllib.parse
import urllib.request
import urllib.error

first_podcast = 164
last_podcast = 1148

for podcast_id in range(first_podcast, last_podcast):
    url = 'http://media.libsyn.com/media/eslpod/ESLPod{}.mp3'.format(podcast_id)
    file_name = os.path.basename(urllib.parse.urlparse(url).path)

    if os.path.exists(file_name):
        continue

    try:
        urllib.request.urlretrieve(url, file_name)
    except urllib.error.HTTPError:
        logging.exception('Failed to download file from {}'.format(url))
