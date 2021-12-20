# 2021 Submissions
<details>
  <summary>The Story So Far...</summary>

You're minding your own business on a ship at sea when the overboard alarm goes off! You rush to see if you can help. Apparently, one of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for situations like this. It's covered in Christmas lights (because of course it is), and it even has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough; there's a little meter that indicates the antenna's signal strength by displaying 0-50 stars.

Your instincts tell you that in order to save Christmas, you'll need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

</details>


## Day 1: Sonar Sweep
<details>
  <summary>Instructions:</summary>
  face of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:
```
199
200
208
210
200
207
240
269
260
263
```

This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

```
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
```
In this example, there are 7 measurements that are larger than the previous measurement.

</details>

>How many measurements are larger than the previous measurement?

Not particularly tricky. Greater than of two numbers, starting at 1 instead of 0.

Of course I put the < the wrong way and calculate it backwards by accident. Then when my answer was still wrong, I realised that I'm comparing strings not integers. After casting them to int, my result was 1 more than before and this was the correct answer.

Time: **20 mins**


### Part 2
<details>
<summary>Instructions:</summary>
Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

```
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
```

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:
```
A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
```

In this example, there are 5 sums that are larger than the previous sum.
</details>

> Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

OK so same problem but now comparing the last 3 numbers with the current 3 numbers. Shouldn't be too difficult to mod my code to do this. I do think I'm going to extract a method to calculate the rolling total from an index.

I was smart enough to add a sanity check for an index less than 2, and then also that if I'm comparing the current 3 with the previous 3, I need to start even one higher, so my loop starts at 3. Worked first time, although I took the time to step through the code line by line and make sure.

Time: **7 mins**

## Day 2: Dive!
<details>
  <summary>Instructions:</summary>
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

* `forward X` increases the horizontal position by X units.
* `down X` increases the depth by X units.
* `up X` decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

```
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

* `forward 5` adds 5 to your horizontal position, a total of 5.
* `down 5` adds 5 to your depth, resulting in a value of 5.
* `forward 8` adds 8 to your horizontal position, a total of 13.
* `up 3` decreases your depth by 3, resulting in a value of 2.
* `down 8` adds 8 to your depth, resulting in a value of 10.
* `forward 2` adds 2 to your horizontal position, a total of 15.

After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. 
</details>

> What do you get if you multiply your final horizontal position by your final depth?
So we're writing a function that reads commands with a word and a number, and then returns the delta of the two. That I can do.

OK so tuples get weird when there's typing involved, so we're going with a list of 2 ints to represent position. My main function is taking the delta from the function and applying it to my running position. 

Time: **20 mins** (it seems the first part of the challenge is usually the big change and the slower part)

### Part 2
<details>
  <summary>Instructions:</summary>
  Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

* `down X` increases your aim by X units.
* `up X` decreases your aim by X units.
* `forward X` does two things:
  1. It increases your horizontal position by X units.
  2. It increases your depth by your aim multiplied by X.
Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

Now, the above example does something different:

* `forward 5` adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
* `down 5` adds 5 to your aim, resulting in a value of 5.
* `forward 8` adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
* `up 3` decreases your aim by 3, resulting in a value of 2.
* `down 8` adds 8 to your aim, resulting in a value of 10.
* `forward 2` adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. 
</details>

> What do you get if you multiply your final horizontal position by your final depth?

OK so we need to pass in the current aim to encapsulate, or we need to do the actual adjustment of the course directly. It's already in a function, so the easiest and safest would be to pass the current aim in. Good thing I used a list instead of tuples...

After making the necessary changes I ran the code and it worked first time. It helps if your instructions are clear. The answer that came out looked ridiculous but it was correct so yay me!

Time: **5 mins**, probably because the infrastructure was already there.

## Day 3: Binary Diagnostic
<details>
  <summary>Instructions:</summary>
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

```
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
```

Considering only the first bit of each number, there are five `0` bits and seven `1` bits. Since the most common bit is `1`, the first bit of the gamma rate is `1`.

The most common second bit of the numbers in the diagnostic report is `0`, so the second bit of the gamma rate is `0`.

The most common value of the third, fourth, and fifth bits are `1`, `1`, and `0`, respectively, and so the final three bits of the gamma rate are `110`.

So, the gamma rate is the binary number `10110`, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is `01001`, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
</details>

> What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

Oh no we're doing bit manipulation‽ I have no experience with bits! For now at least it's not that difficult to handle, but it might be a problem later...
OK time to write a gamma and epsilon function.

First useful thing would be to write a pivot function that puts all the first characters in index 1 of a list, then I can just count the characters in the string for each index.

Time: **27 mins**

  ### Part 2
<details>
  <summary>Instructions:</summary>
Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

* Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
* If you only have one number left, stop; this is the rating value for which you are searching.
* Otherwise, repeat the process, considering the next bit to the right.

The bit criteria depends on which type of rating value you want to find:

* To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
* To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.

For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

* Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
* Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
* In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
* In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
* In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
* As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.

Then, to determine the CO2 scrubber rating value from the same example above:

* Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
* Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
* In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
* As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.

Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)
  </details>

> What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

OK we need a function that filters out the data based on the gamma number, then by the epsilon number, until only one value remains. I can probably convert these to booleans but then converting to int at the end gets complicated.

I think I have a problem. When filtering according to the gamma number, I reach a point where I have 2 records and neither of them match the next digit, so 0. Do I keep both of those and check the next number? Let's see if that works... 

OK so it says the answer is too low, so I'm filtering the actual result I want too early in the process. Need to read through my logic again.

OH I GOT IT! I was looking at the gamma number for the whole set! I'm supposed to get the gamma for the subset! OK, let's put the gamma and epsilon calculations in a function so I can call it all the time.

And there we have it! It took several tries but finally I got it working!

Time: **1 hour 40 minutes** Yea this was a brainy one...

### Upon Review
So the code was taking far longer to run that it was supposed to, like 4.3 seconds, so I looked at it again. TUrns out I was calculating gamma_epsilon in every run of the list comprehension (line 65) when I could do it once per loop. Extracted the function call and boom, back down to the 0.02s we're used to. Now I don't feel bad about them not being one-liners anymore.

## Day 4: Giant Squid
<details>
  <summary>Instructions:</summary>
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

```
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 ```

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

```
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

```
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```

Finally, 24 is drawn:

```
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
 ```

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.
</details>

> To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

We're building a bingo interpreter! What fun!

Let's start by making some data structures. I can probably do this in numpy but I like rolling my own, especially if part 2 is going to make me modify it.

The numbers on the board is a single list of numbers, with a width value so we can slice it into columns and rows. Makes it quick to loop through numbers for marking and scoring.

OK each number needs to remember its own 'marked' state, so dict with int and bool. 

Spent some time compartmentalizing things, both for readible code and because I have a suspicion what part 2 is going to be.

Quick test against the example data comes back correct on the first try, then the real data and we got it.

Time: **1 hour 30 minutes**

### Part 2
<details>
  <summary>Instructions:</summary>
  n the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.
</details>

> Figure out which board will win last. Once it wins, what would its final score be?

Oh this is easy! I just let all the bingos print out and then the the second last output! Just have to make sure once they win that they only call once.

Time: **4 minutes**

## Day 5: Hydrothermal Venture
<details>
  <summary>Instructions:</summary>
  You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

```
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
```

Each line of vents is given as a line segment in the format `x1,y1 -> x2,y2` where `x1,y1` are the coordinates of one end the line segment and `x2,y2` are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like `1,1 -> 1,3` covers points `1,1`, `1,2`, and `1,3`.
An entry like `9,7 -> 7,7` covers points `9,7`, `8,7`, and `7,7`.
For now, only consider horizontal and vertical lines: lines where either `x1 = x2` or `y1 = y2`.

So, the horizontal and vertical lines from the above list would produce the following diagram:

```
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
```

In this diagram, the top left corner is `0,0` and the bottom right corner is `9,9`. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from `2,2 -> 2,1`; the very bottom row is formed by the overlapping lines `0,9 -> 5,9` and `0,9 -> 2,9`.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.
</details>

> Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

This doesn't seem to complicated. We can't generate the entire grid because we don't know how big it is, but we can abstract it. A dict that identifies entries with a tuple (x,y) would do it. If an entry exists we add 1, if it doesn't we make one with value 1. Then we just loop through them all and count the ones with more than 1.

Oh no, forgot that if the second number is smaller, it won't loop correctly. So let's make sure I always pass the smaller number back first.

Why am I getting too many hits? Oh because I have dirty data! I need to actively ignore lines that aren't straight! 

There we go.

Time: **20 minutes**

### Part 2
<details>
  <summary>Instructions:</summary>

Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like `1,1 -> 3,3` covers points `1,1`, `2,2`, and `3,3`.
An entry like `9,7 -> 7,9` covers points `9,7`, `8,8`, and `7,9`.
Considering all lines from the above example would now produce the following diagram:

```
1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
```

You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.
</details>

> Consider all of the lines. At how many points do at least two lines overlap?

OK now we have to code diagonals, which means either x1 and y2 would be the same, or x2 and y1 would be the same? Alternatively x1 and y1 are the same, as well as x2 and y2. 

So diagonal means I have the x and y changing on each iteration of the loop. Time to write a custom enumerator!

That seems to work! With a bit of cleaning up I can make this enumerator handle both situations then the code is cleaner, but this doesn't need to be maintainable... right?

Time: **25 minutes**

## Day 6: Lanternfish
<details>
  <summary>Instructions:</summary>
The sea floor is getting steeper. Maybe the sleigh keys got carried this way?

A massive school of glowing lanternfish swims past. They must spawn quickly to reach such large numbers - maybe exponentially quickly? You should model their growth rate to be sure.

Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, each lanternfish creates a new lanternfish once every 7 days.

However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.

Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.

So, suppose you have a lanternfish with an internal timer value of 3:

* After one day, its internal timer would become 2.
* After another day, its internal timer would become 1.
* After another day, its internal timer would become 0.
* After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
* After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.

A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value). The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.

Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish (your puzzle input). For example, suppose you were given the following list:

```
3,4,3,1,2
```

This list means that the first fish has an internal timer of 3, the second fish has an internal timer of 4, and so on until the fifth fish, which has an internal timer of 2. Simulating these fish over several days would proceed as follows:

```
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
```

Each day, a `0` becomes a `6` and adds a new `8` to the end of the list, while each other number decreases by 1 if it was present at the start of the day.

In this example, after 18 days, there are a total of 26 fish. After 80 days, there would be a total of 5934.
</details>

> Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?

This can get out of hand quickly. If I have to make a list of every single fish with a timer, it would probably explode. But there's only 8 possible numbers, so if I have a list of 8 numbers and the index is what their number is, I can just pop off the beginning and add onto the end... This could work...

OK I've got a function that reads all the inputs and makes a list of how many fish at each number. Now I can write the for loop that "ticks" the timer.

OK the first 18 are working correctly. Now let's simulate the 80 days for the test data... and it works! Now the real test. Cool!

Time: **35 minutes**

### Part 2
<details>
  <summary>Instructions:</summary>
Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!
</details>

> How many lanternfish would there be after 256 days?

Let's just double check the test before running it for real, just in case... Yup it's correct. Here goes.

Did it! All I had to do was change a number and it worked.

Time: **39 seconds**

## Day 7: The Treachery of Whales 
<details>
  <summary>Instructions:</summary>
A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

For example, consider the following horizontal positions:

```
16,1,2,0,4,2,7,1,2,14
```

This means there's a crab with horizontal position `16`, a crab with horizontal position `1`, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position `2`:

* Move from `16` to `2`: 14 fuel
* Move from `1` to `2`: 1 fuel
* Move from `2` to `2`: 0 fuel
* Move from `0` to `2`: 2 fuel
* Move from `4` to `2`: 2 fuel
* Move from `2` to `2`: 0 fuel
* Move from `7` to `2`: 5 fuel
* Move from `1` to `2`: 1 fuel
* Move from `2` to `2`: 0 fuel
* Move from `14` to `2`: 12 fuel

This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).
</details>

> Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

OK this is the first one where I have two possible solutions:
1. We can go the route of the previous challenge and count how many is at which position, then write "ticks" that move them all closer to the largest number so they all converge wherever the largest number happens first
2. We can have the same array as the example, send in a target number and spit out the total fuel spent for each target number in the range until we find the smallest.

I'm not sure which would have less loops, but let's start with idea 1 and see where it goes.

Why am I off by one? I hate being off by one.

Oh because I'm modifying the data as I use it! I need to subtract the number that's moving, not just set it to zero! Otherwise I'm moving the number along from the previous move!

OK it works now, but it gives the wrong answer. I think it's finding a cluster for the highest singular number too soon and then making all the others come towards it, costing extra moves, when the highest cluster could've moved to the middle.

Let's try idea 2.

So the code is actually cleaner this way. It will be running once for every value in the input data, for as many as the highest number in the input data. That's not ideal. It's still very fast though. If optimization is required, I can employ counters again to know how many of which number I have, and then just multiply the fuel usage for each of those. That's cleaner and a 3 line fix.

There we go. That's much cleaner and it seems to output the right total.

And it works! It does take 8.2 seconds to get a result though...

Time: **1 Hour 20 minutes**

### Part 2
<details>
  <summary>Instructions:</summary>
The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes `5`:

```
Move from 16 to 5: 66 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 0 to 5: 15 fuel
Move from 4 to 5: 1 fuel
Move from 2 to 5: 6 fuel
Move from 7 to 5: 3 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 14 to 5: 45 fuel
```

This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.
</details>

> Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?

Oh cumulative cost. So we need to add up all the numbers between 0 and the target? Good thing python has this `range()` function!

Was off by 1 iteration because `range()` doesn't include itself so I had to add 1 to my absolute difference. It works on the test data, let's try the real thing...

After 13.5 seconds of processing time we get the answer! That's OK!

Time: **4 minutes**


## Day 8: Seven Segment Search
<details>
  <summary>Instructions:</summary>
You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named `a` through `g`:

```
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
```

So, to render a `1`, only segments `c` and `f` would be turned on; the rest would be off. To render a `7`, only segments `a`, `c`, and `f` would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires `a` through `g`, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

So, you might know that only signal wires `b` and `g` are turned on, but that doesn't mean segments `b` and `g` are turned on: the only digit that uses two segments is `1`, so it must mean segments `c` and `f` are meant to be on. With just that information, you still can't tell which wire (`b`/`g`) goes to which segment (`c`/`f`). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:
```
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
```

Each entry consists of ten unique signal patterns, a `|` delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because `7` is the only digit that uses three segments, dab in the above example means that to render a `7`, signal lines `d`, `a`, and `b` are on. Because `4` is the only digit that uses four segments, `eafb` means that to render a `4`, signal lines `e`, `a`, `f`, and `b` are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (`cdfeb fcadb cdfeb cdbaf`) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

```
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
```

Because the digits `1`, `4`, `7`, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).
</details>

> In the output values, how many times do digits `1`, `4`, `7`, or `8` appear?

So all we have to check is the length of each output and then count how many of those is in each set. So nested sums. I'd like to spend some time getting the data in a usable structure, because I would be a little disappointed if Part 2 didn't involve solving the wiring puzzle...

So I can't work out how to do nested sums in the same line for for loops inside them. I've never been good at the "pythonic" way of coding. So I'll go with what I know: Nested for loops with a counter.

Time: **10 minutes**

### Part 2
<details>
  <summary>Instructions:</summary>
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

```
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
```

After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

```
 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
```

So, the unique signal patterns would correspond to the following digits:

```
acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
```

Then, the four digits of the output value can be decoded:

```
cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
```
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

```
fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
```

Adding all of the output values in this larger example produces 61229.
</details>

> For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?

Let's get the part done we know. `1`,`4`,`7`,`8`

OK, now using that information we should be able to do a second pass to calculate the rest. All we need is a way of identifying the differences.

Let's start with the set `2`,`3`,`5`. They all have 5 segments. If I put a `1` over a `3`, it covers completely, so that's a `3`. Between the other two, if I put a `4` over it, one of them (`5`) only has 1 difference, the other (`2`) has 2. OK.

For 0,6,9, of I take a `9` and put a `4` over it, only the top and bottom is left. So that's a `9`. Between the remaining two, if it has both pieces on the right (`1`) it's a `0`.

OK the example line works. Now the small set. That also works first try. So here goes the input data... 

And it works! This was the longest I've spent on a puzzle this year, but I think there's probably a more elegant way of doing this...

Time: **2 hours 40 minutes**


## Day 9: Smoke Basin
<details>
  <summary>Instructions:</summary>
  These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

```
2199943210
3987894921
9856789892
8767896789
9899965678
```
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points: two are in the first row (a `1` and a `0`), one is in the third row (a `5`), and one is in the bottom row (also a `5`). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.
</details>

> Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

What's the first thing you think of? Recursion! So here goes.

Pretty straightforward solution. From each point I just find its lowest point in all directions, then send back whatever that coordinate is. Adding them to a set instead of a list means I'll only have one of each coordinate.

Time **20 minutes**

### Part 2
<details>
  <summary>Instructions:</summary>
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins:

* The top-left basin, size 3:
* The top-right basin, size 9:
* The middle basin, size 14:
* The bottom-right basin, size 9:

Find the three largest basins and multiply their sizes together. In the above example, this is `9 * 14 * 9 = 1134`.

</details>

> What do you get if you multiply together the sizes of the three largest basins?

Mm... From each lowest point, I need to run up the ladder until I get no more higher nodes and report them all back. So same idea, except I'm sending a set of coordinates along for the ride.

OK so my code is working but spitting out far too high numbers. Turns out I'm including diagonals! There we go.

I missed a step. I need to only use the largest 3 totals for my result.

Time: Had to stop midway to go do something so didn't time it.

## Day 10: Syntax Scoring
<details>
  <summary>Instructions:</summary>
You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

Syntax error in navigation subsystem on line: all of them
All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).

The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

* If a chunk opens with `(`, it must close with `)`.
* If a chunk opens with `[`, it must close with `]`.
* If a chunk opens with `{`, it must close with `}`.
* If a chunk opens with `<`, it must close with `>`.

So, `()` is a legal chunk that contains no other chunks, as is `[]`. More complex but valid chunks include `([])`, `{()()()}`, `<([{}])>`, `[<>({}){}[([])<>]]`, and even `(((((((((())))))))))`.

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include `(]`, `{()()()>`, `(((()))}`, and `<([]){()}[{}])`. Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

```
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
```

Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

* `{([(<{}[<>[]}>{[]{[(<()>` - Expected `]`, but found `}` instead.
* `[[<[([]))<([[{}[[()]]]` - Expected `]`, but found `)` instead.
* `[{[{({}]{}}([{[{{{}}([] `- Expected `)`, but found `]` instead.
* `[<(<(<(<{}))><([]([]()` - Expected `>`, but found `)` instead.
* `<{([([[(<>()){}]>(<<{{` - Expected `]`, but found `>` instead.

**Stop at the first incorrect closing character on each corrupted line.**

Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

* `)`: 3 points.
* `]`: 57 points.
* `}`: 1197 points.
* `>`: 25137 points.

In the above example, an illegal `)` was found twice (2*3 = 6 points), an illegal `]` was found once (57 points), an illegal `}` was found once (1197 points), and an illegal `>` was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!
</details>

> Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?

I feel I'm supposed to do this with regex, but I'll have an easier time doing it step by step. Oh cool, there's a LifoQueue in the queue class. This thing half writes itself.

Time: **15 minutes**


### Part 2
<details>
  <summary>Instructions:</summary>
Now, discard the corrupted lines. The remaining lines are incomplete.

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

You can only use closing characters (`)`, `]`, `}`, or `>`), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

In the example above, there are five incomplete lines:

* `[({(<(())[]>[[{[]{<()<>>` - Complete by adding `}}]])})]`.
* `[(()[<>])]({[<{<<[]>>(` - Complete by adding `)}>]})`.
* `(((({<>}<{<{<>}{[]{[]{}` - Complete by adding `}}>}>))))`.
* `{<[[]]>}<{[{[{[]{()[[[]` - Complete by adding `]]}}]}]}>`.
* `<{([{{}}[<[[[<>{}]]]>[]]` - Complete by adding `])}>`.

Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. **Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character** in the following table:

* `)`: 1 point.
* `]`: 2 points.
* `}`: 3 points.
* `>`: 4 points.

So, the last completion string above - ])}> - would be scored as follows:

Start with a total score of 0.
Multiply the total score by 5 to get 0, then add the value of `]` (2) to get a new total score of 2.
Multiply the total score by 5 to get 10, then add the value of `)` (1) to get a new total score of 11.
Multiply the total score by 5 to get 55, then add the value of `}` (3) to get a new total score of 58.
Multiply the total score by 5 to get 290, then add the value of `>` (4) to get a new total score of 294.
The five lines' completion strings have total scores as follows:

* `}}]])})]` - 288957 total points.
* `)}>]})` - 5566 total points.
* `}}>}>))))` - 1480781 total points.
* `]]}}]}]}>` - 995444 total points.
* `])}>` - 294 total points.

Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.
</details>

> Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?

Oh, same same, just empty the queue and match what's left. 
Oh no github had a heart attack and committed the wrong files... sigh...

___ 

I'm going to stop copying all the instructions into this file. It's getting a little long in the tooth.

## Day 11: [Dumbo Octopus](https://adventofcode.com/2021/day/11)

> Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are there after 100 steps?

OK I can reuse a lot of code from day 9, but add the queue functionality from day 10. Increase everything by 1, then if it goes over 9 then we add them to a list of blinks.

OK so the queue doesn't work. Maybe we should just iterate over the list.


### Part 2

> If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash?

So when all lines with all values are 0, they all blinked. I guess I can just sum the rows?

## Day 12: [Passage Pathing](https://adventofcode.com/2021/day/12)

> How many paths through this cave system are there that visit small caves at most once?

Oh no node traversal! I'm not good at this stuff...
OK behaviour:
1. Make a set of all nodes and where they go. This can go both ways so we need to store one way and the other way
2. Start with every path that has "start" in the name
3. Make a new entry for every possible way I can go from there, as long as the node we're going to is uppercase or is already in the list, then we add it to the list
4. If the node is the word "end" we add it to the list of completed paths.

### Part 2

> After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. Given these new rules, how many paths through this cave system are there?

So we can't simply check whether the node exists in the string, we need to make sure that adding this node won't make it the second node to repeat. This will need validation.

## [Day 13: Transparent Origami](https://adventofcode.com/2021/day/13)

> How many dots are visible after completing just the first fold instruction on your transparent paper?

So if my calculations are correct, then if I take the fold index and subtract the index, I'll get a negative number and that's the amount that I need to add (subtract) from the fold to get the new position.

It's working and I'm struggling and I can't figure it out until I saw the line at the top says "just the first fold". Idiot!

And now it works.

### Part 2

> Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters. What code do you use to activate the infrared thermal imaging camera system?

Mm... I'm gonna have to write a print grid thing. 
OK that was easy...

## [Day 14:Extended Polymerization] (https://adventofcode.com/2021/day/14)

> Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

So it's a string that we apply templates to over and over, then we put the whole string through a Counter and subtract highest from lowest.


### Part 2

> The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

So just change the sim days... Oh it comes to a standstill at step 25...

Step 27, one of my cores has been running at 100% for an hour and we're at step 27. Can I do what I did last time and just count how many of each I have? REWRITE!

I do need to keep them in their pairs though, so there's going to be some processing at the end...

I don't need to get my final counts from the reactions. They're the workhorse but not the totals. I can keep track of the element count as it runs...

OK for the first time I think I'll have to step away from this one and come back another day.

## [Day 15: Chiton](https://adventofcode.com/2021/day/15)

> What is the lowest total risk of any path from the top left to the bottom right?

Pathfinding. I've never actually implemented A*, let's see if I can work it out.

Let's try [`astar-python`](https://github.com/zephirdeadline/astar_python).

OK so this version doesn't allow for diagonals, but I see someone has made a pull request with diagonals. So now we're using `astar-python` by [Rasengangstarr](https://github.com/Rasengangstarr/astar_python)

OK nevermind, A* doesn't get me the fastest route, it just gives me the first route. Looks like the library doesn't have a way for me to provide my own heuristic function so it always works on manhattan distance + weight of the next node, and that's throwing out the path that will eventually be the correct one. I mean I stepped through their code. It actually finds the correct next node (at least according to the example) but then it backtracks to another node.

Let's try something that's at least past version 0.1.0... [Dijkstar](https://github.com/wylee/Dijkstar).

Hey that worked first try! And this library has the ability to provide a heuristic function if I actually do want to make it A*! This is a much better implementation!


### Part 2

> The entire cave is actually five times larger in both dimensions than you thought; the area you originally scanned is just one tile in a 5x5 tile area that forms the full map. 
Using the full map, what is the lowest total risk of any path from the top left to the bottom right?

So after I made the grid, I need to expand it in both dimensions by 4 more, with increasing values. So that's a 2D loop inside a 2D loop, multiplying each number by the outer loop position. It's ugly but it works. There's probably a simple expression to do this in numpy or something...

## [Day 16 Packet Decoder](https://adventofcode.com/2021/day/16)

> Decode the structure of your hexadecimal-encoded BITS transmission; what do you get if you add up the version numbers in all packets?

OK this is confusing... First things first, lets get this hex information coded to binary.

There we go. That was a one-liner.

OK now we can parse a literal number in a subfunction. Now we need to be able to read numbers inside operators, which means we might need to rethink how we parse type IDs. 

I should probably read to the bottom of this whole thing before I bother writing the entire interpreter. There's probably a clause saying I only have to do the first bit for the answer. But if that's the case, then Part 2 will require the rest of it, so might as well do it now. It's kind of fun.

OK now I have a result class too, called Packet. I considered passing back a tuple with version and value, but then I might need to see the types. Here's to over-engineering simple problems...

One of the hardest things to get right, is having the Bitfeeder give back a "done" status that makes sense. The end of the input is very inconsistent, so I need to check a few things to work out whether it's done.

In my input data is a weird thing where the last string literal doesn't have the correct "end" tag. Should a literal not have either the "keep reading" tag or a predefined length? Otherwise how do we know when it ends? Just run out of bits?

### Part 2

> What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?

OK so theoretically I just need to write the use cases for the other type IDs and we're good.

So all the test cases work, but not my final case. It says the number is too low... I suspect it has to do with how I check whether a bit stream is done. Why would I have 5 zeroes at the end of a packet in the middle of an instruction?

Turns out I can't rely on the "done" value to see whether there's more to read in the bitfeeder. The done property is meant more for the system to know whether there's another typeID coming. Maybe I should add a peak...

## [Day 17: Trick Shot](https://adventofcode.com/2021/day/17)

> Find the initial velocity that causes the probe to reach the highest y position and still eventually be within the target area after any step. What is the highest y position it reaches on this trajectory?

So the easiest would be to seperate the X and Y axis. First calculate what is the most number of steps left to right that I can have to get it there, then work out how high it can do by working towards the middle.

Can't I calculate this backwards? Gravity and air resistance is linear.

OK I've approached it backwards. If I know how high I can launch it and still hit my target accurately, I can afterwards work out how far forward I need to go to make that shot. Will the target always be below me? Doesn't matter, puzzle input is negative so it's fine.

OK I've been able to reproduce the test conditions. Now I need to output the max height.

So my calculations work, but the answer is too low. I feel there might be a higher Y velocity that would still hit the pot shot if I keep running high enough. So let's set an arbitrary maximum and run until we hit that. See what shakes out.

At 10 000 loops I found a target around 85, so maybe I can trim it to 100. But it worked!