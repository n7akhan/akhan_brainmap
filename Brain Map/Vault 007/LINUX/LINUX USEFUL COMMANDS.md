Use LINUX config terminal by pressing **control alt and T**
In the terminal you can type commands

==**BASIC**==
**ls == shows a list of the current directory**
**ls - a == lists all files that are even hidden**
**cd /{pathway to a directory and then files} == change directory
control +a = moves to the left
control +e = moves to the right
!! = runs the last command
echo "hello" > filename{1..10} = makes 10 files 


**ln = <span style="color:rgb(0, 255, 4)">links</span>
```

```


**tail** == <span style="color:rgb(0, 255, 4)">cats out the end of a file</span>
```
tail /etc/passwd
```
**This will cat out a few end lines of the file passwd

**head** == <span style="color:rgb(0, 255, 4)">cats out the beginning of the file</span>
```
head /etc/passwd
```
**This will cat out the beginning few lines of the file and you can use -n {number} to specifically a number of times




**cat /etc/group == shows you the users OR ls -lahk /home**
**sudo adduser {username} == adds user with home directories and passwords**


# USERADD 
**How to add users and give them passwords**
```

sudo useradd -c "This is a comment" -e 2025-04-20 -d /home/{username} -m 
-s /bin/bash {username}

```
 **-e** sets the expiration date in YYYY-MM-DD format
 **-c** adds a comment 
 **-s** adds a shell with a path /bin/bash
 **-d** /home/username this gives a directory path
 **-m** actually creates the directory
# PASSWD
**Now to give the user passwords:**
```
sudo passwd {username}
new password:
retype password

```
This is gives you the ability to add a password to your new user.
 