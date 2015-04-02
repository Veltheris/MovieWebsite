Movie Website - Great Films
============================

This is a python program to generate a single page website that displays information and trailers for movies.

Table of Contents
 -Requirements
 -Installation/Setup
 -Changelog
 -Comments

Requirements
------------
Python [Required] - Designed for 2.7, though it may work on others. Requires some modules from the Python Standard Library.
Web Browser [Optional] - For viewing the generated website.
Web Server [Optional] - A Web Server is required to be able to view the website on another device.


Installation/Setup
------------------
 -Place the MovieWebsite Folder somewhere on the computer
 -Go into Movies.py within the MovieWebsite Folder
 -Add the movies you wish to display to Movies.py, following the format listed.
 -Once all movies are there, run Movies.py to generate great_films.htm. This will generate inside the MovieWebsite folder. 
  To generate it elsewhere, go into great_films.py and change the output_file line.
 -great_films.htm will open automatically. Congratulations, you now have a website!
 -To view on another device, you will need to host great_films.htm using a web server.

Changelog
---------
Version 1.0
-Added footer with copyright information. Great Films logo now links to the top of the page.
-Changed the color scheme and name of program and website
-Added an info modal to the generator that displays information about the movie. Trailer is now launched through it.
-Added a parent class Video in Media.py. Movie is now a child of Video. Added information such as duration and ratings of   
 movies.

Version 0.0
-Base version as completed during the course.

Comments
--------
This was a fun project. Making the info modal to hold the details was the hardest part. >.<
