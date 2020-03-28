import os, random


# def search_file(filename, search_path, pathsep=os.pathsep):
#     for path in search_path.split(pathsep):
#         candidate = os.path.join(path, filename)
#         if os.path.isfile(candidate):
#             return os.path.abspath(candidate)


def random_play(dir):
    music = []
    found = False
    for dirpath, dirnames, filenames in os.walk(dir):  # 输入文件夹路径
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.mp3':
                filepath = os.path.join(dirpath, filename)
                if os.path.getsize(filepath) > 1048576:# 去掉太小的音乐文件(太小可能是铃声音乐等)
                    music.append(filepath)
                    found = True
    random_music = random.choice(music)
    os.startfile(random_music)

def run(sentiment):
    random_play('./music/'+sentiment)

