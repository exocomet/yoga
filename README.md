# Ye Olde Graph App 🧘

## Contents

- [Prerequisites](#yoga-prereq)
- [Docs](#yoga-docs)
- [Proof of concept](#yoga-proofconcept)

<a id="yoga-prereq"></a>

## Prerequisites - Ubuntu system setup

### Linux users and groups

This will create the three users and add them to the developers group.

```bash
sudo groupadd developers
sudo useradd -G developers -d /home/john -m -s /bin/bash john
sudo useradd -G developers -d /home/andrew -m -s /bin/bash andrew
```

Go ahead and set some initial passwords for your team mates:

```bash
sudo passwd john
sudo passwd andrew
sudo passwd robert
```


### Python and virtual environment

- Python version - fabric might be picky?
- Virtual environment - place it to `/usr/local/bin/venv`
 [link](https://unix.stackexchange.com/questions/8656/usr-bin-vs-usr-local-bin-on-linux)


### Git

    cd WOHIN??
    git clone https://github.com/exocomet/yoga.git

### SSH

There is some [doc](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1604)
on Digital Ocean.

    ssh-keygen

Append public key to the file ~/.ssh/authorized_keys


### Fabric

Used for deployment automation. Example fabfile:

    https://github.com/sloria/flask-template/blob/master/fabfile.py

#### Issues

Throws lots of `CryptographyDeprecationWarnings`, see: https://github.com/paramiko/paramiko/issues/1369. Temporary solution is a downgrade to a previous version of cryptography.

    pip install cryptography==2.4.2


### Firewall

Instructions on DO [https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-16-04]

    sudo apt-get install ufw
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw allow ssh
    ## is the same as the following command, see /etc/services for a port number mapping
    #sudo ufw allow 22

    sudo ufw enable

    sudo ufw status verbose

    sudo ufw allow http #80
    sudo ufw allow https #443

Database connections need their own rules, see the link above.

    sudo ufw enable
    sudo ufw disable
    sudo shutdown -r now
    sudo service apache2 restart


### Apache and mod_wsgi

This is fucking important.

    https://modwsgi.readthedocs.io/en/develop/user-guides/virtual-environments.html#virtual-environment-and-python-version

To install / reinstall mod_wsgi for python3 use this command:

    sudo apt-get install libapache2-mod-wsgi-py3


### Jupyter

How to use an existing virtual environment as kernel for your local jupyter notebooks [link][jupyter_venv]

    $ python -m venv projectname
    $ source projectname/bin/activate
    (venv) $ pip install ipykernel
    (venv) $ ipython kernel install --user --name=projectname

[jupyter_venv]: https://anbasile.github.io/programming/2017/06/25/jupyter-venv/




<a id="yoga-docs"></a>

## Docs

https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04
https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
https://modwsgi.readthedocs.io/en/develop/user-guides/virtual-environments.html#virtual-environment-and-python-version
http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/
http://www.fabfile.org/



<a id="yoga-proofconcept"></a>

## Proof of concept

Installed a minimal working example on a Digital Ocean droplet.

Server address

    http://46.101.128.223/


### Paths on ubuntu

This is only relevant for this working minimal example.

 - /etc/apache2/sites-available/YogaApp.conf
 - /var/www/YogaApp
 - /var/www/YogaApp/YogaApp
 - /var/www/YogaApp/yogaapp.wsgi
 - /var/www/YogaApp/YogaApp/__init__.py
 - /var/www/YogaApp/YogaApp/static

