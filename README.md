# hbrc_python
采用Tornado框架，安装Tornado包
pip install tornado

#进程监控程序  Supervisor
满足的需求是：我现在有一个进程需要每时每刻不断的跑，但是这个进程又有可能由于各种原因有可能中断。
当进程中断的时候我希望能自动重新启动它：Supervisor
#安装很简单
pip install supervisor

#2. 配置
可以用以下命令生成配置文件：
  echo_supervisord_conf > etc/supervisord.conf
配置文件生成之后，在最末尾加上这几行东西：


[program:hello]
command=python /root/nmapp2_venv/test.py --port=8888
directory=/root/nmapp2_venv/
autorestart=true
redirect_stderr=true
OK，完成配置。

#3. 启动 supervisor
启动 supervisor：
supervisord
如果报错，请检查报错信息，比如：
Error: No config file found at default paths (
/root/nmapp2_venv/etc/supervisord.conf,
/root/nmapp2_venv/supervisord.conf,
supervisord.conf,
etc/supervisord.conf,
/etc/supervisord.conf); use the -c option to specify a config file at a different path
For help, use /root/nmapp2_venv/bin/supervisord -h
在上面的默认目录中，丢一个 supervisord.conf 即可。

如果报 http://localhost:9001 refused connection 错误，那是因为 supervisord 没有启动的原因。只要放好 supervisord.conf 文件，即可解决问题。

supervisorctl start all 开启全部服务。

如果修改了配置文件，supervisorctl reload 重启。修改了 Supervisor 的配置，也可以用 supervisorctl reread 来重新载入，或用 supervisorctl reload 来载入新配置并重启所有子进程。直接运行 supervisorctl 的话，可以进入命令行模式操作。
