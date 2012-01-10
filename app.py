import os
import discogs_client as d
from discogs_client import Search, Artist, Release, MasterRelease

def master(versions):
    for version in versions:
        print release(version)

def release(release):
    data = release.data
    return release.title, data['year']

if __name__ == '__main__':
    d.user_agent = 'discogs-metadata-whore'

    artist_title = os.getcwd().split('/')[-2:]
    results = Search(' '.join(artist_title)).results()

    for i, result in enumerate(results):
        result_type = result.__class__.__name__
        if result_type == 'MasterRelease':
            master(result.versions)
            break
        else:
            release(result)
