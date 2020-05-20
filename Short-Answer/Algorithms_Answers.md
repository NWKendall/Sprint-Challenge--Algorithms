#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - A linear, iterative function. Duration of function is contingent of value of n.


b) O(nlogn) - Superlinear iterative algorithm with run time growing proportionally to lenth of n.


c) O(c) - Recursive function. Each operation requires same amount of time to execute.

## Exercise II


building levels = n
eggs
egg break on f-floor or higher
eggs survive < f-floor

Q. Can dropped eggs be returned to the pile?

1. ensure receive eggs
2. levels of building passed into function is len(f)
3. take an egg and set to current_egg
4. drop current_egg fromm ground floor (f[0])
    - if current_egg survives f+=1
    - re-use current_egg for next floor (minimise multi drops)*
    - repeat step 2 on next floor until egg breaks (`while egg_break = False`)
5. return f[n]

Runtime Explanation:

Option A:
    Assuming the floor level that breaks the egg is a constant across buildings, it could have an O(c) runtime. Checking to see if that floor exists for each building, the egg could be dropped on the floor beneath it. One operation per buiding, no eggs lost.

option B:
    If it varies across building floor levels, this algorthm would have a linear RT complexity - O(n). Starting from the bottom, until egg-break floor is reached per building. Only one egg lost per building.


