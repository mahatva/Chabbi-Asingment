def cl(list1, list2):

    ce = list(set(list1) & set(list2))
    nce = list(set(list1) ^ set(list2))

    return ce, nce

Mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z",
              "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!",
              "One Piece", "Attack On Titan"]

ce, nce = cl(Mainstream, must_watch)
print("Common elements:", ce)
print("Non-common elements:", nce)
