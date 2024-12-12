
name1 = input("Enter the name of the first runner: ")
time1 = float(input("Enter the time of the first runner (in seconds): "))

name2 = input("Enter the name of the second runner: ")
time2 = float(input("Enter the time of the second runner (in seconds): "))


if time1 < time2:
    print(f"{name1} is the faster runner.")
elif time2 < time1:
    print(f"{name2} is the faster runner.")
else:
    print("Both runners finished at the same time.")
