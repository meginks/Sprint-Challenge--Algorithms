#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) running time = O(n) 
This one is linear because it's one calculation performed for one iteration of a sequence. 


b) running time = O(n^2) 
B is quadratic runtime because it's a nested iterative loop. Essentially for every i in the first loop on line 17, it runs the entire loop that starts on line 19. This makes the amount of steps required to complete the function the size of the n multiplied by itself in the worst case! That's not a good runtime. Nested loops are not fast.


c) running time = O(n log n) 
I learned about a thing called the "Master Theorem for Divide and Conquer Recurrences" (https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) when I was reading about big O so I am going to attempt to apply it to this problem because I believe it qualifies for the criteria required to use this theorem and I don't know what else to do.
T(n) = aT(n/b) + f(n) --- This is the base theorem 
n = the size of the input problem 
a = number of sub-problems in the recursion 
b = the factor by which the sub-problem goes down each time the recursive call is made 
(there are also certain assumptions made about negative inputs that are not relevant for this problem because you can't have negative bunnies. Even dead ones are there.) 

T(big O of bunnyEars) = number of times bunnyEars is called * T(big O of bunnyEars / how much smaller the big O of bunnyEars gets every time bunnyEars is run) + one run time of bunnyEars (i.e., n) 
In other words:
Big O of bunnyEars problem is the number of steps we must walk through in bunny ears multiplied by [the number of steps we must walk through to get bunny ears divided by the factor that the number of steps we must walk through to get bunny ears is reduced every time the call is made until we get to the base case] + one run through of bunny ears because every function that actually has an operation or calculation has to have a Big O of more than O(1) and a call using recursion necessarily does. 
So what do we know about bunnyEars?
if we don't have a bunny, there are no bunny ears.
If we have a bunny, it has 2 ears. 
In this function:
bunnies is the input, so that's the number of steps at base if we're looping through them. 
However, we're *not* using iteration to solve this problem, we're using *recursion*. 
The number of our *total big o time* actually is reduced when each recursive call of bunnyEars is made. How? LOGARITHMS. That little aT(n/b) part of the theorem. Honestly my mind is kind of blown right now because I just now feel like I understood this so I hope I'm right. 
The size of this problem is either O(log n) or O(n log n). I'm still shaky on the difference between those two but I don't want to waste my whole 3 hours on this. I'm already at an hour and 8 minutes on this section.                       



## Exercise II

tl;dr O(1)

We know we have the following: 
1. a building with n stories 
2. eggs 

What we need to find out:
1. the floor number that an egg will necessarily be broken. 

What it would be nice to know / Assumptions I made: 
1. Do we start at the ground floor and then have 1 and above like the UK or do we start at 1 and then go up like in the US? For the purposes of this problem I will assume that we are in the US. 
2. Do we have infinitely many eggs or do we have a finite number? Pat says to assume infinitely many, so that's what I am going to do.

PseudoPython: 
    ``` 
    def broken_eggs(num_of_floors):
        dead_zone = floor that eggs start breaking 
        number_of_eggs_broken = 0 
        for current_floor in num_of_floors: 
            if egg breaks: 
                dead_zone = current_floor 
                break out of function and return current_floor 
        return dead_zone
    ``` 
    Above is O(n) because you have to run through the number of floors.          
               
    
optimized solution: 
    def height_at_which_egg_breaks(circumstances required to determine egg breakage): 
            some formula for determining when an egg breaks -- some kind of gravity times mass divided by whatever thing 
            floor = this is actually a standard in building code, so find out what that is.
           height an average egg breaks which was determined by formula for egg breakage on line 64 / standard floor height = number of floors at which an egg breaks. 
           return number of floors at which an egg breaks. 
    
This is optimized because you don't have to go through all the floors to find out if an egg breaks. You can use your physics friends and building codes to get a real math formula and solve it. 
It could potentially be O(1) because it wouldn't matter how many floors your specific building had. 
    Physics is cool. 