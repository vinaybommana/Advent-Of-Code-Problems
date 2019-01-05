>>> first_claim
'@ 3, 2: 5x4'
>>> elf_1_fabric_starting_coordinates = (0, 0)
>>> starting_coordinate = first_claim.split(':')[0].strip("@")
>>> starting_coordinate
' 3, 2'
>>> s = starting_coordinate.strip()
>>> y, x = tuple(s.split(', '))
>>> x, y
('2', '3')
>>> x, y = int(x), int(y)
>>> x, y
(2, 3)
>>> square_size = first_claim.split(':')[1]
>>> square_size = square_size.strip()
>>> q = tuple(square_size.split('x'))
>>> q
('5', '4')
>>> y_f, x_f = int(q[0]), int(q[1])
>>> x_f, y_f
(4, 5)
>>> x + x_f, y + y_f
(6, 8)
>>> final_x, final_y = x + x_f, y + y_f
>>> final_x - x, finay_y -y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'finay_y' is not defined
>>> final_x - x, final_y - y
(4, 5)
>>> final_x, final_y
(6, 8)
>>> x, y
(2, 3)
>>> x + 1, y + 1
(3, 4)
>>> start_x, start_y = x + 1, y + 1
>>> final_x, final_y
(6, 8)
>>> start_x, start_y
(3, 4)
>>> for i in range(start_x, start_x + int(q[1])):
...     print(i)
...
3
4
5
6
>>> for i in range(start_x, start_x + int(q[1])):
...     for j in range(start_y, start_y + int(q[0])):
...         print((i, j))
...
(3, 4)
(3, 5)
(3, 6)
(3, 7)
(3, 8)
(4, 4)
(4, 5)
(4, 6)
(4, 7)
(4, 8)
(5, 4)
(5, 5)
(5, 6)
(5, 7)
(5, 8)
(6, 4)
(6, 5)
(6, 6)
(6, 7)
(6, 8)
>>>
