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
    if any(("viewer.html" in f.name.lower()) for f in os.scandir(url)):
        return
    if not any(f.name.lower().endswith((".jpg", ".png", ".jpeg", ".webp")) for f in os.scandir(url)):
        return
    files = filter(lambda x: x.lower().endswith((".jpg", ".png", ".jpeg", ".webp")), os.listdir(url))

    def extract_name(name):
        f = filter(lambda x: True if x else False, re.split("([0-9]+)|([^0-9]+)", name))
        m = map(lambda x: int(x) if x.isdigit() else x, f)
        return list(m)
    
    files = sorted(files, key=extract_name)

    if url[-1] != '/':
        url += '/'

    debugCount = 0
    printNum = 5
    contentStr = ""
    for file in files:
        if debugCount < printNum:
            print(file)
        elif debugCount == printNum:
            print("...", end=" ")
        debugCount += 1
        contentStr += content.format(file, url + file)
        #contentStr += "<img src=\"" + file + "\" alt=\"" + file + "\" width=800px>\n"
    if len(files) >= printNum:
        print(len(files) - printNum, "more pics.")

    html = open(url + outputName, "w", encoding="UTF-8")
    html.write(header + contentStr + tail)
    html.close()
    print("Add Viewer.html for" + url)

def walkDir(dir, newName):
    # try:
    gen_html(dir, newName)
    # # except:
    #     pass
    subfolders = [f.path for f in os.scandir(dir) if f.is_dir()]
    for f in subfolders:
        # print(f)
        walkDir(f, newName)

def main():
    parser = argparse.ArgumentParser(description="Generate HTML for pictures.")
    parser.add_argument("-d", dest="dir", metavar="src_directory", default=".", help="path to source pictures' directory (default: current working directory \".\")")
    parser.add_argument("-o", dest="newName", metavar="output's_name", default="Viewer.html", help="the name of the output pdf (default: \"viewer.html\")")

    args = parser.parse_args()
    walkDir(args.dir, args.newName)


if __name__ == "__main__":
    main()
