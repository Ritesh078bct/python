
import sqlite3

conn=sqlite3.connect("youtube_manager.db")

cursor=conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')



def list_all_videos():
    cursor.execute("SELECT *FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video():
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()


def update_video():
    video_id = input("Enter video ID to update: ")
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    cursor.execute("UPDATE videos SET name=?, time=? where id=?",(name,time,video_id))
    conn.commit()


def delete_video():
    video_id = input("Enter video ID to delete: ")
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()









# main function
def main():
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
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("Invalid Choice")


if __name__=="__main__":
    main()