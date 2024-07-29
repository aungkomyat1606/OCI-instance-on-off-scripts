# OCIscripts
the scripts and features that i use on oracle cloud infrastructure

# Set up Oracle CLI

# install oci cli for linux

<!-- log into linux terminal -->

bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

<!-- press enter to set everything default -->

# configuration of oci

oci -v
oci os ns get 

# Y to creating a new config file

oci setup config

<!-- 
1   user ocid
2   tenancy ocid
3   Region 
4   create new api signing rsa key pair Y
press enter to destination and name 
now go and copy that public key  
-->

<!-- Go to OCI console 
at User Page > Resources > API Keys
add API Key
Copy and paste public key
Check fingerprint if they match or not 
 -->

oci os ns get 

<!-- You shoud get an data output -->

# Now I have Two scripts, one turn instance on and the other one turn the instance off

<!-- Please change the instance_ocid according to your need. -->
Example:     instance_ocid = 'ocid1.instance.oc1.ap-tokyo-1.anxhiljrrf6sm3ycg6r73m5rnteeo6mccshpmqqvz7gk6zjbzwtmbnzcbczq'

<!-- Run those scripts with crontab -->