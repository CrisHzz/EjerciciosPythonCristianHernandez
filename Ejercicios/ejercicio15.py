if __name__ == "__main__":
   word=input("Please enter a word: ")

   is_palindrome = True #bandera en true
   long = len(word) #longitud de la palabra

   for i in range(long // 2): #recorremos la palabra hasta la mitad
       if word[i] != word[long - i - 1]: #si la primera letra es diferente a la ultima automaticamente es falsa
           is_palindrome = False
           break #si es falsa salimos del bucle

   if is_palindrome:
       print("the word is palindrome.")
   else:
       print("the word is not palindrome.")
