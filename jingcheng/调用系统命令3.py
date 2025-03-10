import subprocess

popen = subprocess.Popen('python3',encoding='utf-8', stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)

popen.stdin.write('print("hello") \n')
popen.stdin.write('import os \n')
popen.stdin.write('print(os.environ) \n')

out, err = popen.communicate()
print(out)
popen.stdin.close()
popen.stdout.close()
