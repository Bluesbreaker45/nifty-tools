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
    .content video {
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

video_content = """\
    <div class="content">
        <video src="{}" controls>
            <p>Your browser doesn't support HTML5 video. Here is a <a href="{}">link to the video</a> instead.</p>
        </video>
    </div>
"""

def gen_html(url, outputName):
    if any(("viewer.html" in f.name.lower()) for f in os.scandir(url)):
        return
    
    # 检查是否有图片或视频文件
    has_images = any(f.name.lower().endswith((".jpg", ".png", ".jpeg", ".webp")) for f in os.scandir(url))
    has_videos = any(f.name.lower().endswith((".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm")) for f in os.scandir(url))
    
    if not has_images and not has_videos:
        return
    
    # 获取视频文件
    video_files = []
    if has_videos:
        video_files = list(filter(lambda x: x.lower().endswith((".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm")), os.listdir(url)))
    
    # 获取图片文件
    image_files = []
    if has_images:
        image_files = list(filter(lambda x: x.lower().endswith((".jpg", ".png", ".jpeg", ".webp")), os.listdir(url)))

    def extract_name(name):
        f = filter(lambda x: True if x else False, re.split("([0-9]+)|([^0-9]+)", name))
        m = map(lambda x: int(x) if x.isdigit() else x, f)
        return list(m)
    
    # 分别排序视频和图片文件
    video_files = sorted(video_files)
    image_files = sorted(image_files, key=extract_name)

    if url[-1] != '/':
        url += '/'

    debugCount = 0
    printNum = 5
    contentStr = ""
    
    # 首先添加视频文件
    for file in video_files:
        if debugCount < printNum:
            print(f"Video: {file}")
        elif debugCount == printNum:
            print("...", end=" ")
        debugCount += 1
        contentStr += video_content.format(file, url + file)
    
    # 然后添加图片文件
    for file in image_files:
        if debugCount < printNum:
            print(f"Image: {file}")
        elif debugCount == printNum:
            print("...", end=" ")
        debugCount += 1
        contentStr += content.format(file, url + file)
    
    total_files = len(video_files) + len(image_files)
    if total_files >= printNum:
        print(f"{total_files - printNum} more files.")

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
    parser.add_argument("-o", dest="newName", metavar="output's_name", default="Viewer.html", help="the name of the output html file (default: \"Viewer.html\")")

    args = parser.parse_args()
    walkDir(args.dir, args.newName)


if __name__ == "__main__":
    main()
