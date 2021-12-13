def evk(chas, delit, a):
  if chas % delit == 0:
    lokomotiv = []
    for i in a:
      if i[0] == delit:
        lokomotiv = i[:]
    return lokomotiv
  else:
    a.append([chas % delit, 0, 0])
    for i in a:
      if i[0] == chas:
        a[-1][1] += i[1]
        a[-1][2] += i[2]
      if i[0] == delit:
        a[-1][1] -= i[1] * (chas// delit)
        a[-1][2] -= i[2] * (chas// delit)
    return evk(delit, chas % delit, a)

x = int(input())
y = int(input())
a = [[x, 1,0],[y, 0,1]]
n = evk(x, y, a)
print(n[0], "=", n[1], "*", x, "+", n[2], "*", y)