from datetime import datetime, timedelta
def fasn(date, n):
    dt = datetime.strptime(date, "%y-%m-%d")
    db = dt - timedelta(days=n)
    ans = db.strftime("%y-%m-%d")
    return ans

ans = fasn("16-12-10", 11)
print(ans)