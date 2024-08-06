status = {
    "Robin" : "Online",
    "Rudraksh" : "Online",
    "Vyoom" : "Offline",
}


def online_count(status):
    online_user = 0
    for value in status.values():   
        if value == "Online":
            online_user += 1
    return online_user


print(f"Number of online users: {online_count(status)}")