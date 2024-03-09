def create_banner_text(text):
    # Define ASCII art characters for each letter
    ascii_art = {
        'a': ["  AA  ", " A  A ", "AAAAA ", "A    A", "A    A"],
        'b': ["BBBB  ", "B   B ", "BBBB  ", "B   B ", "BBBB  "],
        'c': [" CCCC ", "C     ", "C     ", "C     ", " CCCC "],
        'd': ["DDDD  ", "D   D ", "D   D ", "D   D ", "DDDD  "],
        'e': ["EEEEE ", "E     ", "EEEEE ", "E     ", "EEEEE "],
        'f': ["FFFFF ", "F     ", "FFF   ", "F     ", "F     "],
        'g': [" GGGG ", "G     ", "G  GG ", "G   G ", " GGGG "],
        'h': ["H   H ", "H   H ", "HHHHH ", "H   H ", "H   H "],
        'i': [" III  ", "  I   ", "  I   ", "  I   ", " III  "],
        'j': ["   J  ", "   J  ", "   J  ", "J  J  ", " JJ   "],
        'k': ["K   K ", "K  K  ", "KK    ", "K  K  ", "K   K "],
        'l': ["L     ", "L     ", "L     ", "L     ", "LLLLL "],
        'm': ["M   M ", "MM MM ", "M M M ", "M   M ", "M   M "],
        'n': ["N   N ", "NN  N ", "N N N ", "N  NN ", "N   N "],
        'o': [" OOO  ", "O   O ", "O   O ", "O   O ", " OOO  "],
        'p': ["PPPP  ", "P   P ", "PPPP  ", "P     ", "P     "],
        'q': [" QQQQ ", "Q   Q ", "Q Q Q ", "Q  QQ ", " QQQQ "],
        'r': ["RRRR  ", "R   R ", "RRRR  ", "R R   ", "R  RR "],
        's': [" SSSS ", "S     ", " SSS  ", "    S ", "SSSS  "],
        't': ["TTTTT ", "  T   ", "  T   ", "  T   ", "  T   "],
        'u': ["U   U ", "U   U ", "U   U ", "U   U ", " UUU  "],
        'v': ["V   V ", "V   V ", "V   V ", " V V  ", "  V   "],
        'w': ["W   W ", "W W W ", "W W W ", "W W W ", " W W  "],
        'x': ["X   X ", " X X  ", "  X   ", " X X  ", "X   X "],
        'y': ["Y   Y ", " Y Y  ", "  Y   ", "  Y   ", "  Y   "],
        'z': ["ZZZZZ ", "   Z  ", "  Z   ", " Z    ", "ZZZZZ "],
        '0': [" OOO  ", "O   O ", "O O O ", "O   O ", " OOO  "],
        '1': ["  1   ", " 11   ", "  1   ", "  1   ", "11111 "],
        '2': [" 222  ", "2   2 ", "   2  ", "  2   ", "22222 "],
        '3': ["33333 ", "    3 ", " 333  ", "    3 ", "33333 "],
        '4': ["   4  ", "  44  ", " 4 4  ", "44444 ", "   4  "],
        '5': ["55555 ", "5     ", "5555  ", "    5 ", "5555  "],
        '6': [" 666  ", "6     ", "6666  ", "6   6 ", " 666  "],
        '7': ["77777 ", "   7  ", "  7   ", " 7    ", "7     "],
        '8': [" 888  ", "8   8 ", " 888  ", "8   8 ", " 888  "],
        '9': [" 9999 ", "9   9 ", " 9999 ", "    9 ", " 999  "],
        '0': [" OOO  ", "O   O ", "O O O ", "O   O ", " OOO  "],
        ' ': ["      ", "      ", "      ", "      ", "      "],
    }

    # Convert the text to lowercase
    text = text.lower()

    # Initialize the banner lines
    banner_lines = [""] * 5

    # Generate banner text
    for char in text:
        if char in ascii_art:
            letter_ascii = ascii_art[char]
            for i in range(5):
                banner_lines[i] += letter_ascii[i] + " "
        else:
            # If the character is not available in ascii_art, use a space
            for i in range(5):
                banner_lines[i] += "       "

    # Add border and make text italicized
    border = "||"
    for i in range(5):
        banner_lines[i] = f"{border} {banner_lines[i]} {border}"

    # Join banner lines with newline character
    banner_text = "\n".join(banner_lines)
    return banner_text

# Test the function with "sh3n0yh4rry"
banner_text = create_banner_text("sh3n0yh4rry")
print(banner_text)
