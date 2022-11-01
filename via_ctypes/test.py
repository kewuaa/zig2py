from ctypes import windll
import timeit


mylib = windll.LoadLibrary('./zig_lib/zig-out/lib/zig_lib.dll')
print('zig say:', end='\n\t')
mylib.hello()
print('=' * 66)
zig_add = mylib.add
number = 10000
print(f'test how much time cost when add {number} times', end='\n\n')
zig_time = timeit.timeit(stmt=lambda: zig_add(100, 200), number=number)
py_time = timeit.timeit(stmt='100 + 200', number=number)
print(f'zig: {zig_time}\npython: {py_time}')

