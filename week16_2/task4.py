import time


width = 70


def run_chr(s):
    for i in range(width-len(s), -1, -1):
        print(s[:-1] + ' '*i + s[-1] + ' ', end='\r', flush=True)
        time.sleep(0.01)


word = 'Привет!!!'
for i in range(len(word)):
    run_chr(word[:i+1])
