# kibana-selenium
Kibana testing framework which uses selenium webdriver and phantomjs.


## Pre-Setup
In order to ensure operation in headless mode you will need to install phantomJS
```
    apt-get install phantomjs
```

## Install

```bash
-Optional: Best practice is to setup a virtualenv before proceeding.
    pip install virtualenv
    virtualenv ~/venv/kib-sel
    . ~/venv/kib-sel/bin/activate

-Required: These steps are needed everytime you rebuild the project.
    cd /opt && git clone https://github.com/rcbops-qe/kibana-selenium.git   
    cd kibana-selenium
    mv ~/.pip/pip.conf ~/.pip/pip2.conf
    pip install -r requirements.txt
    mv ~/.pip/pip2.conf ~/.pip/pip.conf
    export PYTHONPATH=$(pwd)


-Configuration file generator: This will create the configuration file needed for test execution in iad3-2 and iad3-3
    python conf-gen.py
    
    
-Local configuration management:
    user:
        kibana
    password: on infra
        grep -R "kibana_password" /etc/openstack_deploy/user_rpco_secrets.yml
    external_vip: on infra
        IAD3-LAB02:
            grep -R "external_lb_vip_address" /etc/openstack_deploy/openstack_user_config.yml
        
        IAD3-LAB03L
            grep -R "external_lb_vip_address" /opt/rpc-openstack/jenkins-oa/inventory/group_vars/qe-iad3-lab03.yml
```

## Test execution

```
python /opt/kibana-selenium/testrepo/kibana/kibana.py
```


## Troubleshooting:

```
-Setup
    Most common issue is that the pip.conf file doesn't allow remote lookups. If you get a pip install error while performing step : pip install -r requirements.txt, the easiest solution is to move the ~/.pip/pip.conf file execute install and then move back the pip.conf file.
    
-Error reporting
    Currently errors are output to a file named kibana.log in the directory the test were run from.
    Screenshots are also created into the current working directory.
