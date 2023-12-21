import argparse
from multiprocessing import Pool


''' Command Line Arguments : -i inputFile.txt -s abc -o decrypted.txt -p 36
- i : path to input file 
- s : seed string 
- o : path to output file 
- p : number of processes '''
def args():
  parser = argparse.ArgumentParser(description='Description of your program')
  parser.add_argument('-i', '--input', type=str, help='Path to input file')
  parser.add_argument('-s', '--seed', type=str, help='Seed string')
  parser.add_argument('-o', '--output', type=str, help='Path to output file')
  parser.add_argument('-p',  '--process', type=int, default=1,  help='Number of process')
  return parser.parse_args()

''' The purpose of this function is to decrypt a single character by apply the rotation cipher. It'll rotate a given character by the specified value in the predefined character set'''

def decryptLetter(letter, rotationValue):
  rotationString = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ "
  currentPosition = rotationString.find(letter)
  return rotationString[(currentPosition + rotationValue) % 95]


'''Stage 1.2 - Matrix Generation 
- It creates a square matrix that is LxL and calculates the Length of the input string and fills the matrix with the characters from the seed string and cycles through it. '''


def create_matrix(input_string, seed_string):
  L = len(input_string)
  matrix = [['' for _ in range(L)] for _ in range(L)]
  seed_index = 0
  for i in range(L):
    for j in range(L):
      matrix[i][j] = seed_string[seed_index % len(seed_string)]
      seed_index = seed_index + 1
  return matrix


''' This function takes the matrix and returns a list of the neighboring elements that are surrounding that specific value but doesn't include the value itself.  '''

def neighbor(matrix, rowNumber, colNumber):
  result = []
  for rowAdd in range(-1, 2):
   newRow = rowNumber + rowAdd
   if newRow >= 0 and newRow < len(matrix):
     for colAdd in range(-1, 2):
        newCol = colNumber + colAdd
        if newCol >= 0 and newCol < len(matrix[0]):
          if newCol == colNumber and newRow == rowNumber:
            continue
          result.append(matrix[newRow][newCol])
  return result

def prime(n):
  if n <= 1:
    return False
  for i in range (2,int(n**0.5)+1):
    if n % i == 0:
      return False
  return True



'''Stage 1.3: Follows the rules of: 
- If a is prime then the cell remains 'a', but if it's even the cell becomes 'b' and if it's odd the cell becomes 'c' 
 - If b is prime then the cell remains 'b', but if it's even the cell becomes 'a' and if it's odd the cell becomes 'c
 - If c is prime then the cell remains 'c', but if it's even the cell becomes 'a' and if it's odd the cell becomes 'b' '''

def numVal(cell,val):
  if cell == 'a':
      return 'a' if prime(val) else 'b' if val % 2 == 0 else 'c'
  elif cell == 'b':
      return 'b' if prime(val) else 'c' if val % 2 == 0 else 'a'
  elif cell == 'c':
      return 'c' if prime(val) else 'a' if val % 2 == 0 else 'b'
  else:
    return cell 



''' Stage 1.3: Summing up the neighbor cells. 
- The neighboring cell that contain 'a' = 0 
- The neighboring cell that contains 'b' = 1
- The neighboring cell that contains 'c' = 2'''

def sum_neighbors(neighbor):
  if neighbor == 'a':
      return 0
  elif neighbor == 'b':
      return 1
  elif neighbor == 'c':
      return 2
  else:
      return 0


'''Stage 1.4.1: Decryption - Column Summation 
- This takes the 0th column and sums up the neighboring values, once the sum of the neighboring values is calculated it then gets stored into the updatedMtx. '''

def col_sum(args):
  mtx, length, rowStart, rowEnd, splice = args
  updatedMtx = []
  for i in range(rowStart, rowEnd):
      row = []
      for j in range(length):
        neighbors = neighbor(mtx, i, j)
        sum_val = sum(map(sum_neighbors, neighbors))
        row.append(numVal(mtx[i][j], sum_val))  

      updatedMtx.append(row)

  return updatedMtx


'''Stage 2.1 - Concurrency Using Multiprocessing 
In this function multiprocessing is used to parallelize the processing of the matrix by dividing it into segments and applys the col_sum concurrently. It will then combine the results from each of the process and put into the original matrix. Once the parallel processing is complete it then returns the modified matrix 
'''
def process(matrix, num_processes):
  chunk_size = len(matrix) // num_processes
  processData = Pool(processes=num_processes)
  poolData = []

  for i in range(num_processes):
      start_row = i * chunk_size
      end_row = (i + 1) * chunk_size if i < num_processes - 1 else len(matrix)
      mtxData = [matrix, len(matrix), start_row, end_row, i]
      poolData.append(mtxData)

  final_data = processData.map(col_sum, poolData)
  processData.close()
  processData.join()

  for i in range(num_processes):
      start_row = i * chunk_size
      end_row = (i + 1) * chunk_size if i < num_processes - 1 else len(matrix)
      matrix[start_row:end_row] = final_data[i]

  return matrix

''' This function decrypts a string by processing it in the columns. For each of the columns it gets the sum of the neighbors of each element inside that column and uses the result to decrypt the characters from the input. It gets stored inside the decrypted_string.'''

def decrypt(matrix, length, string):
  decrypted_string = ""
  cols = []

  for index in range(length):
    cols.append(0)
    for j in range(len(matrix)):
      cols[index] += sum_neighbors(matrix[j][index])
    decrypted_string += decryptLetter(string[index], cols[index])
  return decrypted_string

''' The purpose of def main(): 
- Opens the file when the command arguments are called and then reads the input file into the input_string 
- It then creates a matrix based on what the input string and the seed string is 
- It will the loop a 100 times and gets the number of processes 
- It then opens the output file and writes the decrypted string into the output file '''

def main():
  print("Project :: R11726246")
  arg = args()
  with open(arg.input) as input_file:
      input_string =  input_file.read()
  matrix = create_matrix(input_string, arg.seed)
  for i in range(100):
      matrix = process(matrix, int(arg.process))
  decrypt_string = decrypt(matrix,len(matrix),input_string)
  with open(arg.output,'w') as output_file:
      output_file.write(decrypt_string)

if __name__ == '__main__':
   main()



