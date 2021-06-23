# Rootme CTF Challenge
my machine ip: 10.9.234.242

target ip: 10.10.225.185

#### Process
1. Perform an NMAP scan `nmap -sC -sV 10.10.225.185`
    - This woud provide you answers to the questions:
        - How many ports are open?
        - What version is Apache running?
        - What service is running on port 22
    ![Nmap Scan](./images/nmap%20scan.PNG)
2. Since we know port 80 is open, we should take a look at their website.
    ![Home Page](./images/home%20web%20page.PNG)
    - It's best practice to view the page source of the website for possible vectors for exploitation, however in this case, there are no interesting code to look into.


3. Perform gobuster scan `gobuster dir -w <wordlist directory path> -u http://10.10.225.185:80`
    - It looks like we have 2 interesting directories to look into: /panel and /uploads
    ![Nmap Scan](./images/gobuster%20scan.PNG)
    
4. Go to /panel and you'll see file uploads page. This would be our vector to upload a file for remote code execution and get a reverse shell.
    ![Nmap Scan](./images/home%20panel%20page.PNG)
    - Download the reverse shell code from this link https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php and edit the file with your listening port and IP
    - Upload the file and let's see how it would behave. It looks like it won't accept the typical .php extension based from the message.
        ![Nmap Scan](./images/denied%20upload.PNG)
    - What we can do is fire-up burpsuite and create our wordlist of extensions: php, php3, php4, php5, phtml
    - set intercept to "On" and and upload the reverse shell again. Once request is captured, send it to the intruder and set the position to "php" extension, without the period. Don't forget to set the payload which would be the wordlist for extension
        ![Nmap Scan](./images/burpsuite%20set%20position.PNG)
    - Start the attack and bingo we can send phtml extensions.
        ![Nmap Scan](./images/burpsuite%20success%20upload.PNG)
    
5. in your terminal, run the command `nc -lvnp <port from reverse shell file>`
    
    ![Nmap Scan](./images/netcat%20comman.PNG)
    - go to /uploads and click on the phtml extension. Congrats! We got a shell.
        ![Nmap Scan](./images/uploads%20dir.PNG)
        ![Nmap Scan](./images/reverse%20shell.PNG)
    - get the 1st flag at /var/www/user.txt

6. We need to get root access to the machine because www-data is a low level user that doesn't have much permissions.
    - 1st thing is find SUID perms using this command: `find / -perm /4000 2</dev/null`
        ![Nmap Scan](./images/find%20suid%20perm.PNG)
    - python is unusual to have an suid perm for it. lets look for python suid in this link https://gtfobins.github.io/
        ![Nmap Scan](./images/suid%20python.PNG)
    - bingo we can perform this command to get root access.
    - get the flag located at /root
