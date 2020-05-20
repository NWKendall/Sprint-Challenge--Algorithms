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

## ITERATIVE
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

## RECURSIVE
`find_floor_that_breaks_eggs(floors, low, high, ):`
- if floors are greater than 1:
    1. find middle floor ( ```mid = (low - high) // 2``` )
    2. execute drop egg function
    3. if `egg_breaks == True`, recursive call with middle floor replacing default high value (step 1)
    4. if `egg_breaks == False`, recursive call with middle floor replacing default low value (step 1)
    5. repeat the above until `mid`, `low` and `high` parameters are the same value (`floor`), and return
- else:
    1. return `"Bungalows have only a ground floor."`

Runtime Explanation:

    A binary search recusrive function is quickest way, with run time complexity of O(logn). Essentially menaing, time goes up linearly while the n goes up exponentially.
    
    It is not however the most egg conservative
