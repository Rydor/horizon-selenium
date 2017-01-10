# horizon-selenium
Horizon testing framework which uses selenium webdriver and phantomjs.


## Pre-Setup
In order to ensure operation in headless mode you will need to install phantomJS
```
    apt-get install phantomjs
```

In order to use Firefox instead of phantomjs you will need to install firefox.
Install instructions - http://kb.mozillazine.org//Installing_Firefox#Linux
Ensure you use a version older than 46.0.1 to avoid ghostdriver issues.

## Install

```bash
-Optional: Best practice is to setup a virtualenv before proceeding.
    pip install virtualenv
    virtualenv ~/venv/horizon-sel
    . ~/venv/horizon-sel/bin/activate

-Required: These steps are needed everytime you rebuild the project.
    cd /opt && git clone https://github.com/Rydor/horizon-selenium.git
    cd horizon-selenium
    mv ~/.pip/pip.conf ~/.pip/pip2.conf
    pip install -r requirements.txt
    mv ~/.pip/pip2.conf ~/.pip/pip.conf
    export PYTHONPATH=$(pwd)


-Configuration file generator: This will create the configuration file.
Tested in iad3-2 and iad3-3.
    python conf-gen.py
    
    
-Local configuration management:
    user:
        admin
    password: on infra
        grep -R "keystone_auth_admin_password" /etc/openstack_deploy/user_osa_secrets.yml
    external_vip: on infra
        grep -R "external_lb_vip_address" /etc/openstack_deploy/openstack_user_config.yml

```

## Test execution

```
nosetests -sv --with-xunit /opt/horizon-selenium/testrepo/horizon/base.py
```


## Troubleshooting:

```
-Setup
    Most common issue is that the pip.conf file doesn't allow remote lookups.
    If you get a pip install error while performing step :
    pip install -r requirements.txt, the easiest solution is to move the
    ~/.pip/pip.conf file execute install and then move back the pip.conf file.
    
-Error reporting
    Currently errors are output to a file named horizon.log in the directory the test were run from.
    Screenshots are also created into the current working directory.
