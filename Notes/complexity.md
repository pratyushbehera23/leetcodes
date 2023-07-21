# Complexity

Complexity of an algorithm is a measure of the amount of computing resources (time and space) that a particular algorithm consumes when it runs.

Measuring: bigO, theta, omega

BigO: worst-case(upper-bond)
theta: avg complexity
Omega lowest bond

Big-O-notation [ O() ]:
3rules while computing BigO:

- TC worst case scenario
- avoid constants
- avoid lower values

## Time complexity

Time complexity is the rate at which the time increases wrt input size.
Note: TC != time taken

## Space complexity

memory space ; auxiliary space (space taken to solve the problem) + input space (space taken to store the input)
eg. c = a+b
auxiliary space -> c  ;  input space -> a,b

// extra point:
never manipulate/change the input(data) itself thinking of saving space,
like: b = a + b
