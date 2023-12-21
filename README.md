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
