import time
user = {                           #存储用户名和密码
    "luozeng":'123',
    "xuemanfei":'456',
    "xutian":'789'
}

def yanzheng(hello):
    def func(*args,**kwargs):
        start = time.time()
        username = input("请输入用户：").strip()     #用户输入
        password = input("请输入密码：").strip()
        if username in user and password == user[username]:        #用户名和密码验证
            print("登陆成功")
            hello(*args,**kwargs)
        else:
            exit("用户名或密码错误！")
        end = time.time()
        print("运行时间：%s"%(end - start))
    return func
@yanzheng
def hello():
    print("你好！")
hello()