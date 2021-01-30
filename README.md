# applicationsDB

## Motivation
While utilizing a variety of job board websites to submit my applications for work, I realized that I was double applying to the same positions from different sites!  I decided to build myself a solution to document my applications as I've submitted them.

I'd never combined SQLite with Python so I decided to give it a shot. It ended up being extremely simple!

## Future enhancements
* I'd like to add a GUI to make it more user friendly.
* Expand on the RDBMS and include some notes in another table. 
* Make main an executable.
* Encrypt the db as to not worry about pushing it.


## To run in your Terminal
Navigate to the working directory and type:

  `./main.py ` or `python3 main.py` 

And you should be greeted with the following (note that the color of your terminal may vary)
<p>
  <img src="https://github.com/frgalvan/applicationsDB/blob/main/venv/img.png" width="570px" align="middle"/>
</p>

#### A note about the committed 'applied.db'
It's just got two dummy entries in it, but you can clear it and build it yourself! (see schema at the head of 'main.py')
