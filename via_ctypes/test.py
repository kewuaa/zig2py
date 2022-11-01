from ctypes import windll
import subprocess

subprocess.call(['zig', 'build-lib', 'test.zig', '-dynamic'])


mylib = windll.LoadLibrary('./test.dll')
mylib.hello()

