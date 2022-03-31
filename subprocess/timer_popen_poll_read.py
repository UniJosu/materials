import subprocess
from time import sleep

with subprocess.Popen("python timer.py 5") as process:

    print(process.poll())  # returns None because process not yet finished
    sleep(3)
    print(process.poll())  # None
    sleep(3)
    print(process.poll())  # 0

with subprocess.Popen("python timer.py 5", stdout=subprocess.PIPE) as process:

    print(process.poll())
    print(process.stdout.read())  # reads everything and blocks until EOF
    sleep(3)
    print(process.poll())  # returns 0 because that is exit code
    print(process.stdout.read())  # b''
    sleep(3)
    print(process.poll())  # 0
    print(process.stdout.read())  # b''


with subprocess.Popen("python timer.py 5", stdout=subprocess.PIPE) as process:

    # https://stackoverflow.com/questions/57726771/what-the-difference-between-read-and-read1-in-python
    # https://docs.python.org/3/library/io.html?highlight=read1#io.BufferedIOBase.read1
    # https://docs.python.org/3/library/io.html?highlight=read1#io.BufferedIOBase.read

    print(process.poll())
    print(process.stdout.read1())
    sleep(3)
    print(process.poll())
    print(process.stdout.read1())
    sleep(3)
    print(process.poll())
    print(process.stdout.read1())