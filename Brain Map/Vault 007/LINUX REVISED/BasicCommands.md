# Linux Commands

## Navigation
| Command | Description             | Syntax              | Output                                                  |     |
| ------- | ----------------------- | ------------------- | ------------------------------------------------------- | --- |
| ls      | list structure          | `ls -l {directory}` | `drwxr-xr-x. 1 user group  98 Feb 21 09:03 {directory}` |     |
| pwd     | print working directory | `pwd`               | `/home/student/`                                        |     |
| cd      | change directory        | `cd {directory}`    | *none*                                                  |     |


## File Manipulation
| Command | Description | Syntax | Output |
| --- | --- |  --- | --- |
| touch | create a file | `touch {filename}` |  |
| mkdir | make a directory | `mkdir {directory}` | |
| cp | copy a file | `cp {source} {destination}` | 
| mv | move or rename a file | `mv {source} {destination}` |
| rm | remove a file | `rm [flags] {files}` | |
| cat | output contents of the file | `cat {filename}` | `...file output` |
| nano | start nano file editor | `nano {filename}` | \<nano editor> |

## Symbols
| Command | Description | Syntax |
| --- | --- |  --- |
| $ | Prompt (Standard User)| |
| # | Prompt (Super User)| |
| ~ | User's home directory | `cd ~` <br> see this with: `echo ~` |
| / | File system room| `cd /` | |
| .. | relative return| `ls ..` | |
| . | present directory | `cp ~/Downloads/somefile.txt .` |
| - | directory queue | `cd -` <br> see this with: `echo $OLDPWD` |

## Filepaths
**Absolute:**
`/home/student/Documents`

**Relative:**
`./Documents/dir1`
`../Desktop/temp`

