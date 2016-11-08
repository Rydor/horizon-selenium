import subprocess


def get_external_lb_vip():
    host = subprocess.check_output(["hostname"])
    if "qe-iad3-3" in host:
        h = "qe-iad3-lab03"
        fi = "/opt/rpc-openstack/jenkins-oa/inventory/group_vars/{0}.yml".format(h)
    elif "qe-iad3-2" in host:
        fi = "/etc/openstack_deploy/openstack_user_config.yml"
    else:
        raise Exception("conf-gen.py is for iad3-2 and iad3-3.")

    elva = subprocess.check_output([
        "grep", "-R", "external_lb_vip_address", fi])
    return elva


def get_password():
    password = subprocess.check_output([
        "grep", "-R", "kibana_password",
        "/etc/openstack_deploy/user_extras_secrets.yml"])
    return password

vip = get_external_lb_vip()
pas = get_password()

f = open('/opt/horizon-selenium/config/app.yaml', 'w')
f.write("horizon:\n")
f.close()
append = open('/opt/horizon-selenium/config/app.yaml', 'a')
append.write("  username: horizon\n")
append.write("  "+pas)
append.write(vip)
append.close()
print "Config file generated into config/app.yaml"
