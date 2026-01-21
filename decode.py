def morse_solver():

    morse_map = {
        "._": "A", "_...": "B", "_._.": "C", "_..": "D", ".": "E", ".._.": "F",
        "__.": "G", "....": "H", "..": "I", ".___": "J", "_._": "K", "._..": "L",
        "__": "M", "_.": "N", "___": "O", ".__.": "P", "__._": "Q", "._.": "R",
        "...": "S", "_": "T", ".._": "U", "..._": "V", ".__": "W", "_.._": "X",
        "_.__": "Y", "__..": "Z"
    }

    
    encoded_message = input().strip()
    
    
    all_decodings = []

    
    def decode(remaining_str, current_word):
        
        if len(remaining_str) == 0:
            all_decodings.append(current_word)
            return

        for i in range(1, 5):
            
            if i <= len(remaining_str):
                part = remaining_str[:i]  
                
                if part in morse_map:
                    
                    letter = morse_map[part]
                    decode(remaining_str[i:], current_word + letter)

    decode(encoded_message, "")

    all_decodings.sort()
    
    for word in all_decodings:
        print(word)

if __name__ == "__main__":
    morse_solver()
