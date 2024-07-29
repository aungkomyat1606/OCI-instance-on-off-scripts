# OCIscripts
The scripts and features that I use on oracle cloud infrastructure to automate processes.

# Set up Oracle CLI

# install OCI CLI for linux

<!-- log into linux terminal -->

``` bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```
<!-- press enter to set everything default -->

# Configuration of oci

oci -v
oci os ns get 
Y to creating a new config file

oci setup config

<!-- 1   user ocid
2   tenancy ocid
3   Region 
4   create new api signing rsa key pair Y
press enter to destination and name 
now go and copy that public key   -->


<!-- Go to OCI console 
at User Page > Resources > API Keys
add API Key
Copy and paste public key
Check fingerprint if they match or not 
 -->

oci os ns get 

<!-- You shoud get an data output -->

Now I have Two scripts, one turn instance on and the other one turn the instance off

<!-- Setup Python and pip env -->

<!-- Please change the instance_ocid according to your need. -->
Example:     instance_ocid = 'ocid1.instance.oc1.ap-tokyo-1.anxhiljrrf6sm3ycg6r73m5rnteeo6mccshpmqqvz7gk6zjbzwtmbnzcbczq'

<!-- Run those scripts with crontab -->
<!-- copy and paste this  -->

# 6 AM server on /// 8 PM server off

30 23 * * * /usr/bin/python3 /home/akm/server/serveron.py >> /home/akm/server/logs/serveron.log

30 02 * * * /usr/bin/python3 /home/akm/server/serveroff.py >> /home/akm/server/logs/serveroff.log
