# Electoral_census
Big shoutout to UC Berkeley Datathon picking this as the second winner! 

## Project Description

### Intro
We've all heard the concept that the Electoral college may be biased towards certain people. You might have even heard the statistic about Wyoming votes per Capita are the most valuable (which is very true, if you look at the graphs below), but you never really hear about how the American people may be inherently preferred by the sytem. This weekend, we started to dig deep into who the electoral college prefers, and the results are . . . surprising. 
![density plot](https://github.com/arefmalek/Electoral_census/blob/main/geoplots/images/electoral_v1.png)
![Electoral College per Capita plot](https://github.com/arefmalek/Electoral_census/blob/main/geoplots/images/Electoral_capita.png)

### Methodology
I'll spare the charts for now, but our tactic was to essentially get the proportion of an electoral vote that a person represents in each state.

We found the complete dataset breaking down number of people that fall within each demographic for every state and multiplied the electoral votes allocation with the total number of citizens over 18 - aka all eligible voters per state - to get the number of electoral votes that each demographic in each state represents.

Finally, we take the sum of all the rows to find the total number of electoral votes represented by each demographic nationwide

### Results
Honestly, they are pretty damning. We tried to match demographics like race and income and we see that the electoral college has some pretty heavy favorites. We can see that the differential in Electoral College values for White voters outweighs other demographics. We also see that those above the poverty line tend to have the vote count more in the electoral college than those who are below the poverty line.

![Disparities](https://github.com/arefmalek/Electoral_census/blob/main/geoplots/images/Disparities.PNG)

### Impact

When many of us heard that at the country's inception, only "White, Landowning males" were allowed to vote, we were appalled that the US was so inherently biased towards one demographic determining the countries future. With these findings, however, it seems that the statement we heard at the country's inception still remains true, it's just hidden in data most don't have the time to find.
