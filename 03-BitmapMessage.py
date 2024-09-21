import sys

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
print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print("Enter the message to display using bitmap")
message = input("> ")
if message == "":
    sys.exit()

# Loops over each line in bitmap
for line in bitmap.splitlines():
    # Loops over each character in bitmap
    for bit_index,bit_val in enumerate(line):
        # If space exists print space and connect the below line
        if bit_val == ' ':
            print(" ", end="")
        else:
            # num % num = 0 | num % > lower than num = 0 | num % higher than num = num                
            print(message[bit_index % len(message)], end='')
    print()
