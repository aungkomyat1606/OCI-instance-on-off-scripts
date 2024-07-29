# OCI server on off scripts
The scripts and features that I use on oracle cloud infrastructure to automate processes.

# Set up Oracle CLI

# install OCI CLI for linux

<!-- log into linux terminal -->

```bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"```

<!-- press enter to set everything default -->

# Configuration of oci

```oci -v```

```oci os ns get ```

Yes to creating a new config file

```oci setup config```

1   user ocid

2   tenancy ocid

3   Region 

4   create new api signing rsa key pair >>> Yes

Press enter to destination and name .
Now go and copy that public key. 

Go to OCI console.
At User Page > Resources > API Keys
Add API Key.
Copy and paste public key.
Check fingerprint if they match or not.


```oci os ns get```


You shoud get an data output

Now I have Two scripts, one turn instance on and the other one turn the instance off with the file name of serveroff.py and serveron.py

Dont forget to Setup Python and pip env.

<!-- Please change the instance_ocid according to your need. -->

<!-- Run those scripts with crontab -->
<!-- copy and paste this  -->

# 6 AM server on & 8 PM server off

Run This with Crontab

```30 23 * * * /usr/bin/python3 /path/to/file/serveron.py >> /path/to/file/serveron.log ```

```30 02 * * * /usr/bin/python3 /path/to/file/serveroff.py >> /path/to/file/serveroff.log```
