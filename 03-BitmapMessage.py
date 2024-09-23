import sys



class BitmapMessage:
    def __init__(self):
        self.bitmap = """
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

    def get_input(self):
        return input(">")

    def main(self):
        print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
        print("Enter the message to display using bitmap")  
        message = self.get_input()
        if message == "":
            sys.exit()

        # Loops over each line in bitmap
        for line in self.bitmap.splitlines():
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
    BitmapMessage().main()