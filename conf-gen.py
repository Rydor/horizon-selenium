import argparse
import subprocess


def get_external_lb_vip(file_location=None):
    file_location = (file_location
                     or "/etc/openstack_deploy/openstack_user_config.yml")
    elva_line = subprocess.check_output([
        "grep", "-R", "external_lb_vip_address", file_location])
    elva = elva_line.split(":", 1)[1].strip()
    return elva


def get_password(file_location=None):
    file_location = (file_location
                     or "/etc/openstack_deploy/user_osa_secrets.yml")
    password_line = subprocess.check_output([
        "grep", "-R", "keystone_auth_admin_password", file_location])
    password = password_line.split(":", 1)[1].strip()
    return password

if __name__ == '__main__':
    description = "Script to generate config file"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--password-file")
    parser.add_argument("--vip-file")
    parser.add_argument("--password")
    parser.add_argument("--vip")
    args = parser.parse_args()

    vip = args.vip or get_external_lb_vip(args.vip_file)
    pas = args.password or get_password(args.password_file)

    f = open('/opt/horizon-selenium/config/app.yaml', 'w+')
    f.write("horizon:\n")
    f.close()
    append = open('/opt/horizon-selenium/config/app.yaml', 'a')
    append.write("  username: admin\n")
    append.write("  horizon_password: {0}\n".format(pas))
    append.write("  external_lb_vip_address: {0}".format(vip))
    append.close()
    print "Config file generated into config/app.yaml"
