# Non-converging random variables

 In all the exercises we have done thus far we have seen how when we compute sample means by repeatedly sampling a random variable and by using the following formula:
 
 ![](https://render.githubusercontent.com/render/math?math=\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_i)
 
they converge to a particular fixed value.  What we will see in this case is that there are special cases for which this does not happen i.e. the sample mean does not converge to a particular finite value.  The particular special case we are going to look here is a random variable, Y, that is generated as:

![](https://render.githubusercontent.com/render/math?math=Y=2^X)

where X is a geometric random variable with parameter p=0.5.  To complete the code you will need to:

1. Edit the function called `geometric` so that it returns a geometric random variable with parameter 0.5.
2. Set the first element of the array called `indices` equal to 1, the second element of the array called `indices` to 2 and so on.
3. Set the first element of the array called `average` equal to a sample mean calculated by generating 1  random variable Y, the second element of the array `average` equal to a sample mean calculated by generating 2 of these Y random variables, set the third element of the list called `average` equal to a sample mean calculated by generating 3 of these Y random variables and so on until you have computed an average by generating 200 of these random variables.
