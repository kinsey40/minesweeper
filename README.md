# Minesweeper
Minesweeper, written in python (3.6) using tkinter GUI

## Dependencies
* Python version 3.5 or later
* numpy==1.13.3
* Tlc/tk version 8.6

#### Installing tkinter
If using a linux machine, use:

> apt-get install python-tk

If not using a linux machine, see [here](http://www.tkdocs.com/tutorial/install.html) for the installation process. 

## Cloning and Set-up

In order to clone the repo run one of the following: 
> git clone git@github.com:kinsey40/minesweeper.git
> git clone https://github.com/kinsey40/minesweeper.git

Within the repository is a setup.sh file. Running this file will create a python virtual environment, from which the user 
can run the application. 
*NOTE: This will install tkinter locallly onto your machine.*  

Alternatively, the user can create their own virtual environment, manually installing numpy and tkinter. 
The application can be run by running the main.py script.

Hence, run the following in the command terminal (Assuming the python path defaults to python3):

> cd minesweeper

> python main.py
