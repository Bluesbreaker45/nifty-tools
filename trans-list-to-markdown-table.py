#! /usr/bin/env python3
"""
Playlist to txt: https://www.tunemymusic.com/zh-cn/Spotify-to-File.php
Link to txt: in playlist in Spotify, ctrl-c and paste the result in a file.
"""

def zipListAndLink(listPath, linkPath): 
    def join(pair):
        authorAndName = pair[0]
        delim = authorAndName.find('-')
        author = authorAndName[0:delim].strip()
        name = authorAndName[delim + 1:].strip()
        link = pair[1].strip()

        skeleton = "| [{name}]({link}) | {author} |"
        return skeleton.format(name=name, link=link, author=author)

    with open(listPath, "r", encoding="utf-8") as playlist,\
         open(linkPath, "r", encoding="utf-8") as link:
        z = zip(playlist, link)
        m = map(join, z)
        for e in m:
            print(e)

def main():
    zipListAndLink("./My-Spotify-Playlist.txt", "./link.txt")

if __name__ == "__main__":
    main()