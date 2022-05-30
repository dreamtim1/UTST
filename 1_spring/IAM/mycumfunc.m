function output = mycumulativesumfunc(vector)
    res = vector(1); %Creating a variable
    for i = 1:size(vector, 2)-1 %Creating a loop to modify the input vector
        next = res(i) + vector(i+1);
        res = [res, next];
    end
    output = res; %Displaying the output
end
