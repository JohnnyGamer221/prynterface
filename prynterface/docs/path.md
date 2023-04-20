The `PATH` is an important concept when working on the command line. It's a list
of directories that tell your operating system where to look for programs, so
that you can just write `script` instead of `/home/me/bin/script` or
`C:\Users\Me\bin\script`. But different operating systems have different ways to
add a new directory to it:

## Windows
### 1.
Press the Windows key and R at the same time to open the "Run" dialog. <br> Enter ```SystemPropertiesAdvanced.exe``` and click "OK". <br> If this brings you to the "System Properties" window, click "Advanced" and then "Environment Variables".
- If this worked, skip to step 5.
- Otherwise, continue with step 2.

2. Depending on your OS:
  * If you're using Windows 8 or 10, press the Windows key, then search for and
    select "System (Control Panel)".
  * If you're using Windows 7, right click the "Computer" icon on the desktop
    and click "Properties".
3. Click "Advanced system settings".
4. Click "Environment Variables".
5. Under "System Variables", find the `PATH` variable, select it, and click
   "Edit". If there is no `PATH` variable, click "New".
6. Depending on your OS:
  * If you see a list of values add yours to the end.
  * If you see a single value make sure to add a semicolon between the values.<br>
    e.g. `C:\Windows\System32` --> `C:\Windows\System32;C:\Users\Me\bin`
  
7. Click "OK".
8. Restart your terminal.

## Mac OS X

1. Open the `.bash_profile` file in your home directory (for example,
   `/Users/your-user-name/.bash_profile`) in a text editor.
2. Add `export PATH="$PATH:your-dir"` to the last line of the file, where
   *your-dir* is the directory you want to add.
3. Save the `.bash_profile` file.
4. Restart your terminal.

## Linux

1. Open the `.bashrc` file in your home directory (for example,
   `/home/your-user-name/.bashrc`) in a text editor.
2. Add `export PATH="$PATH:your-dir"` to the last line of the file, where
   *your-dir* is the directory you want to add.
3. Save the `.bashrc` file.
4. Restart your terminal.

[original by nex3](https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7)
