#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime: O(n)
The code will run once no matter what the size of n is and will only repeat once the while loop starts.
This results a linear complexity.

b) Runtime: O(n log n)
The outer loop runs n times. The inner loop starts at 1 and then doubles until it's greater than n.
Doubling every time means that the loop will complete in O(log 2 n). Since they are nested loops,
the time complexity is multiplied, thus becoming O(n log n) 

c) Runtime: O(n)
The code is a recursion call and the algorithm will always execute bunnies n times.

## Exercise II
For this example, I would use a binary search where I start in the middle floor and drop an egg.
If it breaks, I proceed to the next floor downwards and repeat.
If it didn't break, I will proceed to the next floor upwards and repeat.
I do this until I have it break on one floor, and stay intact on the one below it.
This results in the runtime complexity of O(log n).