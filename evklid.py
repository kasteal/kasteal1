def evk(chas, delit):
  if chas % delit == 0:
    return delit
  else:
    return evk(delit, chas % delit)

x = int(input())
y = int(input())

print(evk(x, y))