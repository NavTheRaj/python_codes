## Middle-Character
def MC():
  mc = input('Enter String: ')
  if len(mc) % 2 == 0:
#even  
    print(mc[len(mc) // 2 - 1] + mc[len(mc) // 2])
  else: 
#odd
    print(mc[len(mc) // 2])
