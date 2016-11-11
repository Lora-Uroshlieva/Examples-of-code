def f(x, l = 1):
    for i in x:
         if type(i)== list:
             f(i, l + 1)
             print('level = ', l)
         else:
             print(i)

(f([1, 2, 3, 4, 5, [11, 12, [21, 22, ['a1', 'b2', 'c3', []], 23], 13], 6, 7]))