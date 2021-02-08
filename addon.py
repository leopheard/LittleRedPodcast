from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon
plugin = Plugin()
url1 = "https://www.omnycontent.com/d/playlist/a7b4f8fe-59d9-4afc-a79a-a90101378abf/bf2c1d80-3656-4449-9d00-a903004e8f84/efbff746-e7c1-463a-9d80-a903004e8f8f/podcast.rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://podcastaddict.com/cache/artwork/thumb/2187472"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://podcastaddict.com/cache/artwork/thumb/2187472"},
    ]
    return items
@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items
if __name__ == '__main__':
    plugin.run()
