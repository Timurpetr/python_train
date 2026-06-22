def dir_reduc(arr):
    way = []
    for send in arr:
        if way:
            last = way[-1]
            if (last == "NORTH" and send == "SOUTH") or \
               (last == "SOUTH" and send == "NORTH") or \
               (last == "EAST" and send == "WEST") or \
               (last == "WEST" and send == "EAST"):
                way.pop()
            else:
                way.append(send)
        else:
            way.append(send)
    return way

print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))