
import json

# to load the data from the file
def load_video():
    try:
        with open('youtube_manager.txt','r') as file:
            test=json.load(file)
            return test
    except FileNotFoundError:
        return []
    
# to save the data to the file
def save_data_helper(videos):
    with open('youtube_manager.txt','w') as file:
        json.dump(videos,file)


# to list all the videos
def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index,video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration : {video['time']}")
    # print(enumerate(videos))
    print("\n")
    print("*"*70)


# to add a video
def add_video(videos):  
    name=input("Enter video name: ")
    time=input("Enter video duration: ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)
    # print(videos)

# to update a video
def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video index to be updated"))
    if 1<=index<=len(videos):
        name=input("enter the new video name: ")
        time=input("enter the new duration: ")
        videos[index-1]={"name":name, "time":time}
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

        


# to delete a video
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))

    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")


# main function
def main():
    videos=load_video()
    while True:
        print("Youtube Manager App | Choose an option:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube videos")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit")
        # print(videos)
        choice=input("Enter Your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")


if __name__=="__main__":
    main()