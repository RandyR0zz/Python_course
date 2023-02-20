def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        if item.is_a_key():
            print("found the key")