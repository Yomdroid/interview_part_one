"""You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. 
Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix."""

def word_search(matrix, word):
  text = ""
  for i in range(len(matrix)-1):
    for j in range(len(matrix[i])):
      if word[i] == matrix[i][j]:
        for char in matrix[i][1+i:]:
          text +=char
        print(text)
        if text == word[i:]:
          return True
        else:
          text = ""
          for num,char in enumerate(range(len(word[i:]))):
            text += matrix[num][i]
            print(text) 
          if text == word[i:]:
            return True
          else:
            return False
            


# Fill this in.
matrix = [
['F', 'A', 'C', 'I'],
['O', 'B', 'Q', 'P'],
['A', 'N', 'O', 'B'],
['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))
# True