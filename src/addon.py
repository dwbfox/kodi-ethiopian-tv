
import xbmcaddon
import xbmcgui
import xbmcplugin
import sys
import re
import urllib2


regex = re.compile('file:\s*"(.+)"')

def get_stream_urls():
    
    stream_sources = {
        'EBS TV': 'http://www.vixtream.net/vcdn/playerf.php?chan=ebstv',
        'EBC 1': 'http://www.vixtream.net/vcdn/ebctv.php',
        'EBC 2': 'http://www.vixtream.net/vcdn/ebctv.php?chan=ebc2',
        'EBC 3': 'http://www.vixtream.net/vcdn/ebctv.php?chan=ebc3'
    }

    """Retrieves actual streamable URLs from the sources provided"""
    streams = {}
    for stream_source in stream_sources:
        source = urllib2.urlopen(stream_sources[stream_source]).read()
        try:
            streams[stream_source] = regex.search(source).group(1)
        except:
            streams[stream_source + '(Unavailable)'] = ''
    return streams


def main():
    proc_handle = int(sys.argv[1]);
    for stream_url in stream_urls:
        listItem = xbmcgui.ListItem(get_stream_urls())
        listItem.setIconImage('icon.png')
        xbmcplugin.addDirectoryItem(handle=proc_handle, url=stream_urls[stream_url], listitem=listItem)
    xbmcplugin.endOfDirectory(proc_handle)

main()