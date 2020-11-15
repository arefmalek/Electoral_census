# Electoral_census
Berkeley DSS Datathon Project

## Project Description

### Intro
![density plot](https://github.com/arefmalek/Electoral_census/blob/main/aref/images/Electoral_capita.png)
![Electoral College per Capita plot](https://github.com/arefmalek/Electoral_census/blob/main/aref/images/Density.png)

We've all heard the concept that the Electoral college and have heard the stats about other stats (pictures above) but this weekend we wanted to explore who is really benefitting from this that was designed "for the people".

### Methodology
I'll spare the charts for now, but our tactic was to essentially get the proportion of an electoral vote that a person represents in each state.

Found complete dataset breaking down number of people that fall within each demographic for every state. Multiply the electoral votes allocation with the total number of citizens over 18 - aka all eligible voters per state - to get the number of electoral votes that each demographic in each state represents.

Finally, we take the sum of all the rows to find the total number of electoral votes represented by each demographic nationwide

### Results
Honestly, they are pretty damning. We tried to match demographics like race, gender, and age and we see that the electoral college has some pretty heavy favorites

![race chart](https://github.com/arefmalek/Electoral_census/blob/main/aref/images/Electoral_capita.png)
![poverty](https://github.com/arefmalek/Electoral_census/blob/main/aref/images/Density.png)

### Impact

The value of votes is not only tied to population density 
Low density vs. high density -> voter disenfranchisement

The electoral college is just a modern version of the original "white, landowning males" that we heard of at the country's origin. The times may be different, but the spirit seems to be the same.