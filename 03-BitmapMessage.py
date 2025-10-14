bitmap = """
....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
....................................................................

"""

## Gets User Input
def get_input(): 
  print("Enter the message to display with the bitmap")
  message = input("> ")
  if message == "":
      exit()
  return message
 
def main():
  text = get_input()
  for lines in bitmap.splitlines(): ## Separtes each Lines
    for index, bit in enumerate(lines):
      if bit == "*" or bit == ".":
        print(text[index % len(text)], end="") # because 
        # 0 % 5 = 0 | 1 % 5 = 1 | 2 % 5 = 2 | 3 % 5 = 3 | 4 % 5 = 4 | 5 % 5 = 0 | 6 % 5 = 1
      else:
          print(" ",end='')
    print() # need space between each printed line
    
    #  print(message[index % len(message)])

main()

# Learn OOP
# Learn Nested For Loops
# Learn Print Parameter Values