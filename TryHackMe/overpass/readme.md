# tryhackme ctf overpass
my machine ip: 10.9.234.242
target: 10.10.7.77

#### procedure
- perform nmap scan `nmap -sC -sV 10.10.7.77`
    ![nmap scan](images/nmap_scan.png)

- since we know port 80 is open lets perform gobuster scan `gobuster dir -w <path to wordlist> -u http://10.10.7.77:80`
    ![gobuster](images/gobuster.png)

- lets go to `10.10.7.77/admin`
    ![login page](images/loginpage.png)

- go to page source and look into the login.js asset.
    ![login page](images/loginjs.png)
    - the login method sets a cookie "SessionToken" lets try to set it into any string using the browser console and reload the page `Cookies.set('SessionToken', 'anything')`

- we were able to login just by creating a cookie. now let's copy the private ssh keys from james into our local machine
    ![login page](images/adminpage.png)

- lets try to crack the passphrase of the priv ssh key using john the ripper. first is to use ssh2john.py to turn it into a readble format. Dont forget for private keys you have to set the permission to 600.
    ![login page](images/ssh2john.png)

- lets crack it using john and rockyou.txt
    ![login page](images/john.png)

- lets ssh in using james and the cracked passphrase.

- lets create a directory in our local machine `mkdir -p downloads/src`
    ![create dir](images/createdir.png)

- move the buildscript.sh file from the overpass website to the directory that we just created and `downloads/src` and replace the content with a reverse shell code.
    ![rev shell](images/revshell.png)

- spawn a python web server `python3 -m http.server 80` and spawn a netcat listener `nc -lvnp <port>`
    ![rev shell](images/webserver.png)
    ![rev shell](images/netcat.png)

- change the ip address for overpass.thm from the target machine to your ip
    ![rev shell](images/hosts.png)

- wait for the netcat listner to get the root shell.
