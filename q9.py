from datetime import datetime

def ans(fd, td, d):

    fd = datetime.strptime(fd, "%y-%m-%d")
    td = datetime.strptime(td, "%y-%m-%d")
    delta = abs(fd - td).days
    if delta < d:
        return True
    else:
        return False
    
fans = ans("21-01-01", "21-01-05", 7)
print(fans)