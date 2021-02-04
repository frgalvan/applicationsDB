# applicationsDB

## Motivation
While I was utilizing a variety of job board websites to submit my applications for work, I realized that I was double applying to positions from different sites!  I decided to build myself a small program to document my applications as I'm submitting them to prevent this from happening again.

## Brief Overview
I started out with a simple python terminal interface with 2 options: 
  1.  Search for the name of a company to compare against the DB. 
  2.  Submit a new entry from the user's input
  
I've since added a few more features.
#### [You can see more here](https://github.com/frgalvan/applicationsDB/wiki)
  

## System requirements
I'd never combined SQLite with Python so I decided to give it a shot. It ended up being very simple! This project was built in Pycharm on macOS Big Sur.
* SQLite 3.32
* Python 3.8


## To run in your Terminal
Navigate to the working directory and type:

```
python3 main.py
```
or 	
```
./main.py 
```

And you should be greeted with the following (note that the color of your terminal may vary):
<p>
  <img src="https://github.com/frgalvan/applicationsDB/blob/main/venv/img.png" width="570px" align="middle"/>
</p>

## Future enhancements
* I'd like to add a GUI to make it more user friendly.
* Expand on the RDBMS and include some notes in another table. 
* Make main an executable.
* Encrypt the db as to not worry about pushing it.

***A note about the committed 'applied.db'***
*It's just got two dummy entries in it, but you can clear it and build it yourself! (see schema at the head of 'main.py')*
