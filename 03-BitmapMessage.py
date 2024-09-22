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
def main():
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
                # Modulo Logic     
                print(message[bit_index % len(message)], end='')
        print()

if __name__ == '__main__':
    main()