**Standard input** = stdin is a text stream that acts like a source of command input
**Standard output** = stout is a text stream that acts as the destination for command output
**Standard error** = stderr is a text stream that is used as the destination for error messages

**TO MAKE USE STD**
```
ls ~ -al > listing.txt
What this does is with the > symbol we took the output and redirected into a file
```

**Here we can redirect data streams***
```
echo "Meow" > text.txt
Here we took standard output and used redirector > to redict the output
echo "woof" >> text.txt
This appends meow and woof! This >> appends it and does not override it
```

**EXAMPLE OF REDIRECTION**
***I wanna see the last ten accounts made into a accounts.log file***
```
tail /etc/passwd > accounts.log
or if i want only my name files
tail /etc/passwd | grep arslan > accounts.log
```