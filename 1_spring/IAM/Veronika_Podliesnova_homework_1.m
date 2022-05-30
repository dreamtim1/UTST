%Open the input text file
fileID = fopen('dna.txt');

%Read the file, converting into string
input_str = convertCharsToStrings(fscanf(fileID, '%c'));

%Split lines and get an array 
split_str = split(input_str);

%Concatenate these lines into one
dna_data = join(split_str, '');
%Create strings with all plasmid sequences
T7_str = "TAATACGACTCACTATAGG";
SP6_str = "ATTTAGGTGACACTATAG";
T3_str = "ATTAACCCTCACTAAAGGG";
M13F_str = "GTTGTAAAACGACGGCCAGT";
M13R_str = "TCACACAGGAAACAGCTATGA";
AP4_str = "CCCCTGTGAGGAACT";
U19_str = "GTTTTCCCAGTCACGACGT";
BGH_str = "TGTGCCTTCTAGTTGCCAGCCATCTGTTGTTTGCCCCTCCCCCGTGCCTTCCTTGACCCTGGAAGGTGCCACTCCCACTGTCCTTTCCTAATAAAATGAGGAAATTGCATCGCATTGTCTGAGTAGGTGTCATTCTATTCTGGGGGGTGGGGTGGGGCAGGACAGCAAGGGGGAGGATTGGGAAGACAATAGCAGGCATGCTGGGGATGCGGTGGGCTCTATGGC";

%An array of all plasmid sequences
plasmids_arr = [T7, SP6, T3, M13F, M13R, AP4, U19, BGH];

%Empty arrays for counting and saving position
counts = [];
places = [];

%Loop with length equal to number of plasmid sequences)
for n = 1:length(plasmid_seq)

    %Find each of the plasmid sequences, taking into account lower case
    seq_in_data = strfind(dna_data, lower(plasmid_seq(n)));

    %Save the number of times the plasmid sequence was found to the array "counts" 
    counts(end+1) = length(seq_in_data);

    %Save the position(s) to the array "places"
    places = [places seq_in_data];

end

%Print result
disp(counts)
disp(places)