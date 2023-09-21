# Linux Commands
## 1. Files and Directories
- `ls`: List all files and directories (Option `-l` long format, `-a` include all hidden files, `h` Human readable file size)
- `cd /path/to/directory`: change directory
- `pwd`: print current working directory
- `mkdir`: create a new directory
- `rm`: remove files and directories (option `-r` remove directories recursively, `-f` force removal without confirmation)
- `cp`: copy files and directories (option `-r` copy directories recursively)
- `mv`: remove/rename files and directories
- `touch`: create an empty file and upload file timestamp
- `cat`: concatenate files to the standard output 
- `head` and `tail`: display the first and the last few line
- `find` search for files and directories (option `-name` by name and `-type` by type)
## 2. File permission commands
- `chmod`: change file permission (Option `u` user/owner permission, `g` group permission, `x` execute permission, `+` add permision, `-` Remove permission)
- `chown`: change file ownership
- `chgrp`: change the group ownership
- `umask`: set default file permission
## 3. Network commands
- `ifconfig`: display network interface information
- `ping`: send ICMP echo request to a host
- `ssh`: recurely connect to a remote server
- `scp`: securely copy files between hosts
- `wget`: download files from a website
- `curl`: transfer data to or from a server
## 4. Other commands
- `uname`: unix name command (option `-a` all information, `-s` kernel name)
- `history`: list up to 500 previously executed commands
- `man`: user manual of any commands 
- `echo`: display text or string in the standard output
- `zip archive.zip note.text`: compress into .zip file
- `unzip archive.zip`: unzip a file
- `hostname`: system hostname (option `-a` hostname alias, `-i` machine IP address)
- `useradd`, `userdel` and `passwd`: add, delete and password
# References
1. [Linux commands cheat sheet](https://www.geeksforgeeks.org/linux-commands-cheat-sheet/)
2. [Linux commands](https://www.hostinger.com/tutorials/linux-commands)
