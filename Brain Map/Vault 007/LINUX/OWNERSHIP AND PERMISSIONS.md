
# OWNERSHIP STEPS 

**chown == change ownership of directories or files**

**EXERCISE**
```
arslan@astrocomp:/$ sudo mkdir GroupDir/ (makes a new directory)
arslan@astrocomp:/$ ll GroupDir/
	total 8
	drwxr-xr-x  2 root root 4096 Mar 19 18:05 ./
	drwxr-xr-x 24 root root 4096 Mar 19 18:05 ../
	(This shows that the ownership is root since we used sudo)
	
arslan@astrocomp:/GroupDir$ sudo chown -Rv  arslan:devteam GroupDir/

(We -Recursivley change the permissions and verbosaly show whats happening)

arslan@astrocomp:/GroupDir$ ll
total 8
drwxr-xr-x  2 arslan devteam 4096 Mar 19 18:05 ./
drwxr-xr-x 24 root   root    4096 Mar 19 18:05 ../

(Now you can see that the user is Arslan and group devteam)
```

# PERMISSION STEPS

**chmod = to change or manage permission**

