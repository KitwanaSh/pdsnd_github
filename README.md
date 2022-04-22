# Bike Share Project
This is a data science **project** created to analyze how users rent bicycle on a very short-term basis for a price.
This allows people to borrow a bike from one point and return it to another point, though they can also return it to the same location if they’d like to just go for a ride. Regardless, each bike can serve several users per day.
I have written code to import the data and answer interesting questions about it by computing descriptive statistics. I have also written a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

#### List of Files
In this project we concentrated on 3 major cities in the United States and each one of them has its own file in csv format as follow:
- chicago.csv -> City: Chicago
- new-york-city.csv -> City: New-York-City
- washington.csv -> City: Washington DC
The main (*python*) file that contains the code in order to do the analysis is named **bikeshare_2.py**

### What Software do you need?
The following open source software are required to work on this project:
- You must have Python3 that includes Numpy and pandas libraries installed using anaconda
- A text editor eg.(VsCode, Atom or Sublime)
- A terminal (in my case, i use Git Bash)

### Computation
In this project, I have written code to provide the following *descriptive statistics*:

##### Most common times of travel (i.e., occurs most often in the start time)
- most common month
- most common day of week
- most common hour of day
##### Most common stations and trip
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)
##### Trip duration
- total travel time
- average travel time
##### User info
- counts of each user type
- counts of each gender (only available for New-York-City and Chicago data)
- earliest, most recent, most common year of birth (only available for New-York-City and Chicago data)
