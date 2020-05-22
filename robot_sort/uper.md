### robot question

Rules
Inside the robot_sort directory you'll find the robot_sort.py file. Open it up and read through each of the robot's abilities. Once you've understood those, start filling out the sort() method following these rules:

- You may NOT modify any pre-defined robot methods.
- You may NOT store any variables. (=)
- You may NOT access any instance variables directly. (self._anything)
- You may NOT use any Python libraries or class methods. (sorted(), etc.)
- You may use any pre-defined robot methods.
- You may use logical operators. (if, and, or, not, etc.)
- You may use comparison operators. (>, >=, <, <=, ==, is, etc.)
- You may use iterators. (while, for, break, continue)
- You may define robot helper methods, as long as they follow all the rules.

Hints
Make sure you understand the problem and all of the rules! A solution that breaks the rules will not receive full credit.

If you're unsure if an operator or method is allowed, ask.

Lay out some numbered cards in a line and try sorting them as if you were the robot.

Come up with a plan and write out your algorithm before coding. If your plan is sound but you don't reach a working implementation in three hours, you may receive partial credit.

There is no efficiency requirement but you may lose points for an unreasonably slow solution. Tests should run in far less than 1 second.

We discussed a sorting method this week that might be useful. Which one?

**The robot has exactly one bit of memory: its light. Why is this important?**

Run python test_robot.py to run the tests for your robot_sort() function to ensure that your implementation is correct.



## UPER
### U
- can move if have values either side
- cannot move if a lowest/highest value
- can compare - only with item immediately in front/behind it
- can swap (tell which one is bigger)
- binary flag for the light on/off

- bubble sort algo
if compare == 1, swap item

drop items to the first None before current location


### P
light is on when list is ordered

if robot holding nothing and can't move right, light off

steps:
    While light is on:

        1. check to move right is true:
            PUT IN FUNC?
            a. move right (1 space)
            b. pick up item (default item == None)
            c. check to move right
            d. move right
            e. compare items
                i. if new item is smaller
                    a. swap item
                    b. check left
                    c. compare item
                    d. swap item
                    e. repeat **1a**
                ii. if new item is bigger
                    a. repeat **1c**
        2. check to move right is false:
            a. check left
            b. compare
                i. **1c**
            
    if light is off:
        1. array is sorted
        
eg. bubblesort: ✅

    def bubble_sort(arr):
        # Your code here
        for i in range (len(arr) -1, 0, -1):
            for j in range (i):
                if arr[j] > arr[j + 1]: # compare items
                    arr[j], arr[j+1] = arr[j+1], arr[j] # swap items
        return arr

### R
- can do one pass from L - R. How to iterate through each instance?
    - function operational while light is on?
    - try
- tried:
    - 