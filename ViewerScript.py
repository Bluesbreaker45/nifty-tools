import os
import re
import argparse

header = """\
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>viewer</title>
</head>

<style>
    .content {
        text-align: center;
    }
    .content img {
        width: 800px;
    }
</style>

<body>
"""

tail = """
</body>

</html>
"""

content =  """\
    <div class="content">
        <img src="{}" alt="{}">
    </div>
"""

def gen_html(url, outputName):
    files = filter(lambda x: x.endswith((".jpg", ".png", ".jpeg")), os.listdir(url))

    def extract_name(name):
        f = filter(lambda x: True if x else False, re.split("([0-9]+)|([^0-9]+)", name))
        m = map(lambda x: int(x) if x.isdigit() else x, f)
        return list(m)
    
    files = sorted(files, key=extract_name)

    if url[-1] != '/':
        url += '/'

    contentStr = ""
    for file in files:
        print(file)
        contentStr += content.format(url + file, url + file)
        #contentStr += "<img src=\"" + file + "\" alt=\"" + file + "\" width=800px>\n"

    html = open(outputName, "w", encoding="UTF-8")
    html.write(header + contentStr + tail)
    html.close()


def main():
    parser = argparse.ArgumentParser(description="Generate HTML for pictures.")
    parser.add_argument("-d", dest="dir", metavar="src_directory", default=".", help="path to source pictures' directory (default: current working directory \".\")")
    parser.add_argument("-o", dest="newName", metavar="output's_name", default="Viewer.html", help="the name of the output pdf (default: \"viewer.html\")")

    args = parser.parse_args()
    gen_html(args.dir, args.newName)


if __name__ == "__main__":
    main()
