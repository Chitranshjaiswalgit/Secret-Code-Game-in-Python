# Secret-Code-Game-in-Python

This Pytom script’s Secret Code Game is amongst a few that enables users to either encode or decode a message. When the program is started, a welcome message is given, and then the user is requested to enter ‘1’ if he or she would like to code the English characters or ‘0’ if he or she would like to decode the Morse code. Later, the user inputs the message which needs to be processed.

During the coding stage, each word of the message undergoes transformation based upon a specific pattern utilized by the script. For longer characters with three or more, it rearranges the words by placing the first and last character characters at alternating positions parts to form an encrypted version. If the letter is less than three characters, it then needs to the simple reversal. This is further translated to a corresponding encoded message which is later printed.

To decode, the script tries to process what is written backwards, so to speak. When the length of a word is three or more; it changes the position of some of the characters to introduce in the original message. If a mistake occurs, for instance, an IndexError, the script sends a warning message to the user saying to input the valid decoded message and by this, finishes the work. If the decoding procedure is completed correctly, a printed version of the decoded message is provided.

At the end, the script thanks the user for indulging him or her in the Secret Code Game. Generally speaking, this program is one with which a user can interact because users decrypt, or encrypt texts in accordance with a defined pattern.
