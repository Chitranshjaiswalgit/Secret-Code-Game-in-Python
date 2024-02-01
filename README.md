# Secret-Code-Game-in-Python

This Python script implements a basic Secret Code Game, offering users the choice to either encode or decode a message. Upon initiating the program, a welcome message is displayed, and users are prompted to enter '1' for coding or '0' for decoding. Subsequently, the user inputs the message they want to process.

In the coding phase, the script applies a specific pattern to each word in the message. For words with a length of three or more characters, it rearranges the letters by placing the first and last characters at specific positions, forming a coded version. If a word has less than three characters, it is simply reversed. The resulting coded message is then printed.

For decoding, the script attempts to reverse the coding pattern. If a word has a length of three or more characters, it adjusts the positions of specific characters to reconstruct the original word. In case of an error, such as an IndexError, the script informs the user to enter a valid decoded message and exits the program. The decoded message is printed if successful.

The script concludes by expressing gratitude to the user for playing the Secret Code Game. Overall, this program provides an interactive and engaging experience by allowing users to encode or decode messages using a predefined pattern.
