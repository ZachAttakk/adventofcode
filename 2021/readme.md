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