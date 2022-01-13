# Debian-Based-Auto-Updater
**Debian Based Auto-Updater** (**DBAU**) is a tool developed with the aim of simplifying the automation of the ***update procedure*** of Debian based systems by making it ***totally automatic***, **without modifying system files for its operation**. It just needs four main packages (Two of them are usually out-of-box packages).

# Installation
DBAU has only 2 main requirements:
1. A system based on Debian (take a look at: [Debian based distros](https://en.wikipedia.org/wiki/Category:Debian-based_distributions)) or which supports the package managers 'dpkg' and 'apt'
2. Four packages:
   - sudo (usually self-installed in many distributions), to elevate privileges during updating process. Run `apt-get install sudo` to install it;
   - cron (usually self-installed in many distributions), to automate the execution of the tool. This package can be installed automatically by DBAU or run `apt-get install cron` if you prefer to do it by yourself;
   - python3 and python3-pip, required to run the tool and download/install the required python modules. Run `apt-get install python3 python3-pip` to install them;

Once the necessary packages are installed. We can proceed to download and make DBAU operational. Run the following **line-by-line** terminal commands ***without root priviliges***:
1. `cd /home/username` Suggest: If you prefer you can also use folders contained in it, the important thing is that they are accessible and editable without root permissions.
2. `git clone INSERISCI QUI LINK`
3. `cd DBAU`
4. `pip3 install -r requirements.txt`
5. `python3 DBAU.py`

And It's done.

# Troubleshooting
Please, for any problem don't hesitate to let me know via the issue section of the repository. The only thing you need to do is go to the 'logs' folder inside the DBAU folder, find the file with the error output and attach the file or paste its contents. I apologize from now on for any problems.

# A great contribution
If you are familiar with python and/or if the tool was helpful and you want to improve it or fix bugs or errors, please feel free to do so using the 'testing' branch and commit your changes. Thanks in advance to all of you. :)

# To infinity and beyond
In the future, I would like to implement this tool and make it compatible with most package managers for linux and freebsd. It will take time but DBAU is just the beginning.
