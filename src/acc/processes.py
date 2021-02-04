# Note: this package is called "processes" and not "supervisor"
# to prevent collision with # the supervisor package.
# Might not be needed actually. TODO: check this.

from .util import system
from .config import HOME

CONF = """
[unix_http_server]
file={HOME}/supervisor.sock   ; (the path to the socket file)

[supervisord]
logfile={HOME}/supervisord.log ; (main log file;default $CWD/supervisord.log)
logfile_maxbytes=50MB       ; (max main logfile bytes b4 rotation;default 50MB)
logfile_backups=10          ; (num of main logfile rotation backups;default 10)
loglevel=info               ; (log level;default info; others: debug,warn,trace)
pidfile={HOME}/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
nodaemon=false              ; (start in foreground if true;default false)
minfds=1024                 ; (min. avail startup file descriptors;default 1024)
minprocs=200                ; (min. avail process descriptors;default 200)

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix://{HOME}/supervisor.sock ; use a unix:// URL  for a unix socket

[program:nginx]
command=nginx -c {HOME}/nginx/nginx.conf
autostart=true

"""


class Supervisor:
    def start(self):
        system(f"supervisord -c {HOME}/supervisor.conf")

    def stop(self):
        system(f"supervisorctl -c {HOME}/supervisor.conf shutdown", ignore_err=True)

    def start_service(self, name):
        system(f"supervisorctl -c {HOME}/supervisor.conf start {name}")

    def stop_service(self, name):
        system(f"supervisorctl -c {HOME}/supervisor.conf stop {name}")

    def restart_service(self, name):
        system(f"supervisorctl -c {HOME}/supervisor.conf restart {name}")

    def reload(self):
        system(f"supervisorctl -c {HOME}/supervisor.conf update")

    def gen_conf(self):
        print("!!! GENERATING SUPERVISOR CONF !!!")
        conf = CONF.format(HOME=HOME)

        from .model import session, Instance, RUNNING, READY

        instances = session.query(Instance).all()
        for instance in instances:
            if instance.state in (RUNNING, READY):
                conf += f"[program:{instance.name}]\n"
                conf += "command=nuxeowrapper %d\n" % instance.iid
                conf += "autostart=false\n"
                conf += "stopsignal=INT\n"
                conf += "\n"

        with open(f"{HOME}/supervisor.conf", "w") as fd:
            fd.write(conf)


supervisor = Supervisor()
