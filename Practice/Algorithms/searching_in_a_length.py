from collections import deque

graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["tom", "mike", "alex"]
graph["bob"] = ["anuj", "clay", "morris"]
graph["claire"] = ["robert", "mohammed", "sadio"]
graph["tom"] = []
graph["mike"] = []
graph["alex"] = ["lens_killer"]
graph["anuj"] = ["kate_drugdealer"]
graph["clay"] = []
graph["morris"] = []
graph["robert"] = []
graph["mohammed"] = []
graph["sadio"] = []
graph["lens_killer"] = []
graph["kate_drugdealer"] = []

def person_is_a_killer(name):
    if "killer" in name:
        return name

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_a_killer(person):
                print(person + " is a killer")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False