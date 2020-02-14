# Ubuntu AD.

# echo /etc/sysctl.conf >> "net.ipv4.ip_forward = 1"
# sysctl -p /etc/sysctl.conf
or
# echo 1 > /proc/sys/net/ipv4/ip_forward

echo /etc/hosts >> "127.0.0.1 aadds.contoso.com ubuntu"

sudo apt-get update
sudo apt-get install krb5-user samba sssd sssd-tools libnss-sss libpam-sss ntp ntpdate realmd adcli

sudo vi /etc/ntp.conf
#
#server aadds.contoso.com
#

sudo systemctl stop ntp
sudo ntpdate aadds.contoso.com
sudo systemctl start ntp

sudo realm discover AADDS.CONTOSO.COM
kinit contosoadmin@AADDS.CONTOSO.COM
sudo realm join --verbose AADDS.CONTOSO.COM -U 'contosoadmin@AADDS.CONTOSO.COM' --install=/
