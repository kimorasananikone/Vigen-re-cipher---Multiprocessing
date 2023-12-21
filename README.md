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



Stage 1.3 – Matrix Processing
Using the matrix you generated in stage 1.2, your solution should then perform the next 100 steps of a
simulation that performs the following during each step:
• For each cell of the matrix, sum up the neighboring cells using the following rules:
o Neighboring cells containing an ‘a’ are equal to 0. ‘a’ = 0
o Neighboring cells containing an ‘b’ are equal to 1. ‘b’ = 1
o Neighboring cells containing an ‘c’ are equal to 2. ‘c’ = 2
• For each cell of the matrix, update the next iteration of the matrix using the following rules:
o If the current cell contains an 'a'
▪ If the sum of the values is a prime number, then the cell remains as an 'a'
▪ If the sum of the values is an even number, then the cell becomes a 'b'.
▪ If the sum of the values is an odd number, then the cell becomes a 'c'.
o If the current cell contains a 'b'
▪ If the sum of the values is a prime number, then the cell remains as a 'b'
▪ If the sum of the values is an even number, then the cell becomes a 'c'.
▪ If the sum of the values is an odd number, then the cell becomes an 'a'.
o If the current cell contains a 'c'
▪ If the sum of the values is a prime number, then the cell remains as a 'c'
▪ If the sum of the values is an even number, then the cell becomes an 'a'.
▪ If the sum of the values is an odd number, then the cell becomes a 'b'.



Stage 1.4 – Decryption
Using the Time Step 100 matrix, your solution will then need to begin the process of decrypting the string using
the data within this final matrix. The decryption process is done using the following steps:
1. Column Summation
a. Starting with the 0th column, sum together all the cells in this column using the following values:
i. Cells containing an ‘a’ add +0.
ii. Cells containing a ‘b’ add +1.
iii. Cells containing a ‘c’ add +2.
2. Decrypt the Letter
a. Using the provided python function “decryptLetter”, pass the 0th character of the encrypted
string and the sum of the 0th column.
b. This function will then rotate the character to its decrypted character and return that character
as a length 1 string.
3. Continue Decryption
a. Once you have decrypted the 0th column, perform the same two steps on all remaining columns.
b. The resulting string created by concatenating all of these decrypted letters together is the
decrypted string.
4. Write to Output File
a. Write the decrypted string to the output file given by the command line argument ‘-o’.



Stage 2.1 – Concurrency Using Multiprocessing
Once Phase 1 has been completed, the next task is to re-write Stage 1.3 (Matrix Processing) to now make use of
currency via the multiprocessing module. As such, your solution is required to effectively utilize the Python
multiprocessing module to enhance its performance. It should be capable of initializing a number of processes
that corresponds to the number specified by the user through the `-p` option. Typically, when not using the
multiprocessing module, your program executes serially—that is, it operates using a single thread or process.
However, for the purpose of this project, you must adapt your program to run in parallel using multiple
processes. To comply with this requirement, ensure that your solution:
• Parses the `-p` option to determine the number of processes the user intends to create.
• Implements the `multiprocessing` module to spawn the exact number of processes requested by the
user.
• Orchestrates these processes to work concurrently on the task at hand, which should demonstrate a
clear understanding and application of parallel processing concepts.
Proper implementation of the multiprocessing module is crucial. If your solution does not conform to these
multiprocessing standards, it will be deemed incorrect. Make sure to test and verify that each process is
performing its intended task and that all processes are running in parallel as expected.
