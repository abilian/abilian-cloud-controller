Abilian Cloud Controller
========================

The project currently provides a "acc" command-line tool that allows to
create, start, stop and destroy Abilian instances on a single dedicated server
(or VM). 

Note: this command-line tool is supposed to be used on the server,
so it's really useful for a sysadmin or to experiment with the system.
It is not a command-line tools for developers (a la 'bees' or 'vmc').

What it does
------------

- Manage instances (creates them from a "model", setup the config file,
  wire them behind nginx)
- Stop them after some inactivity (via a script launched from cron)
- When an instance is stopped, point nginx to a small webserver that
  will restart the instance when a web request is made to it

Install
-------

You need Python and pip.

Simply running `python setup.py install` should be enough, if you have installed
all the dependencies (run `pip install -r deps.txt` first).

You can also use `make env` to create a virtualenv, then activate it
with `source env/bin/activate`.

To test, you need to create an `abiliancloud` directory in your home directory with a
certain structure. You can use `sh setup.sh` for this.

You would need a wildcard DNS for the system to work.

Since that's not practical, you can add to your `/etc/hosts` file something like:

```text
127.0.0.1 abilian1 abilian2 abilian3 abilian4 abilian5
```

(Assuming you will never test more than 5 instances).

Postgresql needs to be started.

You also need to be sudoer (on Linux). (Of course this will be relaxed in the future).

Using
-----

The config is hardcoded in `config.py`. However, this is easy to fix.

Typical scenario is:

```
- acc boot # starts nginx, mostly
- acc create 
- acc stop *iid*
- acc destroy *iid*
```

Currently, instance with iid (instance id) *iid* will be mapped to host
"abilian*iid*". This can be changed in model.py.

Run `acc help` for more info.

I parallel, you need to start the web server (`acc server`) and from
time to time (i.e. using a crontab) to run `acc monitor`.

Architecture
------------

We currently have:

- A small database (currently Sqlite, could be moved transparently to Postgres) that
  stores information about the instances
- A common Postgres database for the instances (currently needs to be started manually)
- A supervisord daemon that is responsible for starting / stopping the instances (and nginx)
- Nginx that acts as the proxy
- A small webserver to process requests to sleeping instances


TODO
----

Lots of things:

- Pass parameters to acc create (like: admin email, hostname, etc.) and manage more finely
  - Instance names, database names, passwords, admin password
  - Port
- Better state control for instances
- One possibility is to move all the current scripts (only useful for
  testing) to the web server, an add a small command line tool that calls
  the web server via REST/JSON
- Make a nice admin interface using the web server
- Make an end-user interface using the web server ?
- Create a command-line tool for the users (a la vmc) ? (Probably not, at least not for customers)

Cleanup:

- Ensure that everything is rock-solid.


History
-------

This project was initially developped (by Nuxeo) for the [Compatible One project](https://www.lemagit.fr/actualites/2240197626/Portabilite-des-clouds-le-projet-Compatible-One-met-daccord-le-Libre-francais)
