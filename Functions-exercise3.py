def primo(inteiro):
    co = 0
    for v in range(2,inteiro):
        if(inteiro%v == 0):
           co = co + 1
        if(co == 0):
          return True
        else:
            return False

num = primo(10)
print(num)

