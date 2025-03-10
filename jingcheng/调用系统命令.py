# encoding:utf-8

import subprocess

runcmd = subprocess.run(" ls /",encoding="utf-8",shell=True) #shell=True表示使用shell执行命令

print(runcmd)

def run_cmd(cmd):
    """
    执行命令
    :param cmd:
    :return:
    """
    try:
        # PIPE 表示将命令的输出和错误信息保存到变量中
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        if result.returncode != 0:
            print("命令执行失败")
            return None
        if result.stdout:
            print(result.stdout)
    except Exception as e:
        print(e)
        return None
if __name__ == '__main__':
    run_cmd("lss /")