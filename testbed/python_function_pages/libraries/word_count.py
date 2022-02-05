def wc(text):
    lines = text.splitlines()
        
    lines_count = 0
    words_count = 0
    characters_count = 0
    
    for line_character in lines:
        words = line_character.split()
        
        lines_count += 1
        words_count += len(words)
        characters_count += len(line_character)
        
    return f"{lines_count}, {words_count}, {characters_count}"