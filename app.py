import os
import discogs_client as d
from discogs_client import Search, Artist, Release, MasterRelease

cwd = os.getcwd()
[(root, curdir, files) for root, curdir, files in os.walk(cwd)]

def master(versions):
    for version in versions:
        print release(version)

def release(release):
    data = release.data

    return 'Tracks: %d\t%s - %s (%d)' % (
            len(release.tracklist),
            release.artists,
            release.title,
            data['year'],
            )

if __name__ == '__main__':
    print ''
    d.user_agent = 'discogs-metadata-whore'

    if len(files) < 1:
        print "cd into an album directory"
        exit

    artist_title = cwd.split('/')[-2:]
    query = ' '.join(artist_title)
    print '-- Searching for "%s"' % query
    results = Search(query).results()

    print '-- Found %d result(s)' % len(results)

    for i, result in enumerate(results):
        result_type = result.__class__.__name__
        if result_type == 'MasterRelease':
            print '-- Found Master Release with %d versions' % len(result.versions)
            master(result.versions)
            break
        else:
            release(result)
