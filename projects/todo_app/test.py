with open("test.txt", "r") as f:
    print(f.read())
    
tasks = ["task1", "task2", "task3"]
with open("test.txt", "w") as f:
    f.write(f"{tasks}")