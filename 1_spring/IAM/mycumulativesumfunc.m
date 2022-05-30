function output = mycumulativesumfunc(vector)
    s = vector(1); %A variable to store the sum
    for i = 1:size(vector, 2)-1 %Accumulate in loop
        next = s(i) + vector(i+1); %The next value
        s = [s, next]; %Change the sum
    end
    output = s;
end
