% Given an array of integers, return indices of the two numbers such that they
% add up to a specific target.

ex1Array = [15, 11, 2, 7];
ex1Target =  9;

function [i,j] = twosum(a,t)
  for i = 1:(length(a)-1)
    for j = i+1:length(a)
      if (a(i) + a(j)) == t
        return;
      end
    end
  end
end

[i,j] = twosum(ex1Array, ex1Target);
fprintf("The first number in the two sums is: %d\n", ex1Array(i));
fprintf("The second number in the two sums is: %d\n", ex1Array(j));