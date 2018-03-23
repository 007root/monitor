# 监控：
    根据自己的需求可以添加不同的监控项，现在只监控了本机到其他服务的状态。服务分为server和agent；agent需要一个守护进程，  
这里使用的是forever，安装请看https://www.npmjs.com/package/forever  
也可以用supervisor，看你们了；
报警使用的是微信，可以观摩一下我自己写的微信接口https://github.com/007root/weixin_api，

# 部署：  
agent nc配置：  
```
$ cat conf.py
# 本机去需要去访问的IP和端口
SER_DICT = {
    "ser-01":{
        "host": "192.168.1.2", 
        "port": 22,
        "timeout": 3    # 超时时间默认1s
    },
    "ser-02":{
        "host": "192.168.1.3",
        "port": 9090
    }
}
```
agent 启动  
```
forever start -c python monitor_agent.py
```
server 配置：
```
$ cat config.py
agent_ip = {
    "group-01": "http://192.168.4.65:8888",
}
```
server 目前使用的crontab 定期去调用 monitor_server.py 

