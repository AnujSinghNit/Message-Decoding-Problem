# Message Decoding Problem
# Project Description
This project is used to decode an encrypted message.
The message is written using dots (.) and underscores (_),
similar to Morse code.

Each pattern of dots and underscores represents one English letter.
The Python program reads the encoded message and converts it
into normal readable words.



# Technology Used
 1.Python 3
 2.Dictionary
 3.Recursion
 4.String handling



# Project Structure
Message-Decoding-Problem
 ├── decode.py
 ├── README.md
 └── output
     └── output.pdf

# How the Code Works

# Step 1: Mapping
The program first creates a dictionary.
This dictionary connects dot and underscore patterns
to English letters from A to Z.

# Step 2: Input
The user gives an encoded message as input.
The input contains only dots and underscores.

# Step 3: Decoding Logic
The program uses a recursive function to decode the message.
It checks the input string from left to right.
It tries small parts of the string (up to 4 characters).
If a part matches a valid pattern, it converts it into a letter.

This process continues until the full message is decoded.
All possible valid words are stored.

# Step 4: Output
All decoded words are sorted in alphabetical order.
The final results are printed and saved.


# How to Run the Program
1. Install Python on your system.
2. Open the terminal in the project folder.
3. Run the command:
   bash
   python decode.py
