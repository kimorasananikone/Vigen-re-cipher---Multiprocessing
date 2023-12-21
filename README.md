# Vigenre-cipher---Multiprocessing
Python program capable of deciphering text that has been encrypted using a customized version of a Vigenère cipher to obfuscate the original text.



Stage 1.1 – Data Retrieval
Your solution should begin by parsing and verifying the command line arguments as they are described in the
Command Line Arguments and Examples section on page 5. Once it has verified the command line arguments,
your application should read in the string written into the input file given by the command line argument ‘-i’.
This file will follow the specification as described in the Input File Specification section on page 6.



Stage 1.2 – Matrix Generation
Your solution should first generate a matrix with dimensions L x L, where L corresponds to the length of the
string obtained from the input file in Stage 1.1. Next, using the seed string supplied via the '-s' command-line
argument, populate the matrix according to the following rules:



1. Initialize Your Matrix
a. Start by creating an empty matrix with L rows and L columns, where L is the length of the string
located in the input file retrieved in Stage 1.
b. Once generated, your matrix will have a total of 𝐿2 cells to fill.
2. Fill the Matrix
a. Begin at the top-left cell of your matrix and proceed to fill the matrix with the characters from
the seed string provided to your application by the ‘-s’ command line argument.
b. Place each character in the cells moving from left to right across the top row.
3. Continue Filling Rows
a. Once you reach the end of the first row, move down to the first cell of the next row and
continue filling in the same left-to-right pattern.
4. Repeat the String
a. If you reach the end of seed string before filling all the cells, start again with the first character
of seed string.
b. Continue this process until every cell in the matrix is filled.
5. Consider the Whole Matrix
a. Make sure you view the matrix as a continuous loop for the string, wrapping around when the
end of the string is reached and resuming from its start.
