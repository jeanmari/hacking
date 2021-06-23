# Rootme
my machine ip: 10.9.234.242
target ip: 10.10.225.185

#### Process
1. Perform an NMAP scan `nmap -sC -sV 10.10.225.185`
    - This woud provide you answers to the questions:
        - How many ports are open?
        - What version is Apache running?
        - What service is running on port 22
    <nmap scan image>
2. Since we know port 80 is open, we should take a look at their website.
    <home page image>
    - It's best practice to view the page source of the website for possible vectors for exploitation, however in this case, there are no interesting code to look into.
3. Perform gobuster scan `gobuster dir -w <wordlist directory path> -u http://10.10.225.185:80`
    - It looks like we have 2 interesting directories to look into: /panel and /uploads
    <gobuster image>
4. Go to /panel and you'll see file uploads page. This would be our vector to upload a file for remote code execution and get a reverse shell.
    </panel image>
    - Download the reverse shell code from this link https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php and edit the file with your listening port and IP
    - Upload the file and let's see how it would behave. It looks like it won't accept the typical .php extension based from the message.
        <denied upload image>
    - What we can do is fire-up burpsuite and create our wordlist of extensions: php, php3, php4, php5, phtml
    - set intercept to "On" and and upload the reverse shell again. Once request is captured, send it to the intruder and set the position to "php" extension, without the period. Don't forget to set the payload which would be the wordlist for extension
        <position set burp>
    - Start the attack and bingo we can send phtml extensions.
        <success upload burp>
5. in your terminal, run the command `nc -lvnp <port from reverse shell file>`
    <netcat image>
    - go to /uploads and click on the phtml extension. Congrats! We got a shell.
        <uploads directory image>
        <reverse shell image>
    - get the 1st flag at /var/www/user.txt

6. We need to get root access to the machine because www-data is a low level user that doesn't have much permissions.
    - 1st thing is find SUID perms using this command: `find / -perm /4000 2</dev/null`
        <suid perm image>
    - python is unusual to have an suid perm for it. lets look for python suid in this link https://gtfobins.github.io/
        <gtfobins image python>
    - bingo we can perform this command to get root access.
    - get the flag located at /root
