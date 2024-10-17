
# file=open('youtube_manager.txt','r')
# print(file.read())
videos = [
    {'name': 'Intro to Python', 'time': '15:30'},
    {'name': 'OOP in Python', 'time': '25:45'},
    {'name': 'Data Structures', 'time': '30:10'}
]


# print(videos[0]["name"], end="\n")

for video in videos:
    for item in video:
        print(f"{item}:{video[item]}" ,end=", ")
    print(end="\n")