import random
import sys

LETTER_SWITCH_LEN = 2
APOSTROPHE = True
VOWEL_INSERTION = True
WORD_CUT_ON = True
WORD_CUT_LENGTH = 1
WORD_SWITCH_SPLIT = False
WORD_SWITCH_LEN_L = 1
WORD_SWITCH_LEN_R = 1
REMOVE_SUFFIX_ON = True
VISION = False
GENERATE_PORTRAIT = True

intro_shown = False

suffixes = ['able', 'acy', 'ae', 'al',  'ance', 'ate',  'dom', 'en', 'ence', 'er',
            'esque', 'ful', 'fy', 'ible', 'ic', 'ical', 'ify', 'ing', 'ious', 'ise', 'ish',
            'ism', 'ist', 'ity', 'ive', 'ize', 'less', 'ly', 'ment', 'ness', 'or',
            'ous', 'ship', 'sion', 'ato', 'tion'
            ]
favorites = []
runtime_list = []
last_gen = ""

def word_splitter(user_input):
    """ Take in 1 string separated by a space, split a word into 2 parts, return 2 words as a tuple"""
    while True:
        word_list = user_input.split(" ")
        if len(word_list[0]) <= 2:
            word1 = "---Add more letters to first word---"
            word2 = "   "
            return word1.upper(), word2.upper()
        elif len(word_list[1]) <= 2:
            word1 = "   "
            word2 = "---Add more letters to second word---"
            return word1.upper(), word2.upper()
        elif len(word_list) == 2:
            word1 = word_list[0]
            word2 = word_list[1]
            return word1.strip().upper(), word2.strip().upper()
        elif len(word_list) != 2:
            word1 = "Indd"
            word2 = "Baputt"
            return word1.upper(), word2.upper()
        else:
            print("Try again, use 2 words only separated by a space")
            break


def switch_letters(word1st, word2nd):
    """ Switch letters, analyze output, add vowels, apostrophes, remove letters as per set options """

    first_part, second_part = switch_based_on_length(word1st, word2nd)

    if VOWEL_INSERTION:
        first_part, second_part = handle_vowel_insertion(first_part, second_part)

    if APOSTROPHE:
        first_part, second_part = handle_apostrophe_insertion(first_part, second_part)

    if REMOVE_SUFFIX_ON:
        first_part, second_part = remove_suffixes(first_part, second_part)

    if WORD_CUT_ON:
        first_part = cut_off_right_end(first_part, WORD_CUT_LENGTH)
        second_part = cut_off_right_end(second_part, WORD_CUT_LENGTH)
        if VISION:
            print("Right End Both Words Cut!")

    switched_phrase = first_part + " " + second_part
    runtime_list.append(f"{switched_phrase.lower().title()}")
    global last_gen
    last_gen = switched_phrase

    return switched_phrase.lower().title()

def switch_based_on_length(word1st, word2nd):
    if not WORD_SWITCH_SPLIT:
        first_part = word2nd[:LETTER_SWITCH_LEN] + word1st[LETTER_SWITCH_LEN:]
        second_part = word1st[:LETTER_SWITCH_LEN] + word2nd[LETTER_SWITCH_LEN:]
    else:
        first_part = word2nd[:WORD_SWITCH_LEN_L] + word1st[WORD_SWITCH_LEN_L:]
        second_part = word1st[:WORD_SWITCH_LEN_R] + word2nd[WORD_SWITCH_LEN_R]
    return first_part, second_part

def handle_vowel_insertion(first_part, second_part):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    if all(char in consonants for char in first_part[:3]):
        first_part = insert_char(first_part, random.choice(vowels), LETTER_SWITCH_LEN if not WORD_SWITCH_SPLIT else WORD_SWITCH_LEN_L)
        if VISION:
            print("Vowel!")
    if all(char in consonants for char in second_part[:3]):
        second_part = insert_char(second_part, random.choice(vowels), LETTER_SWITCH_LEN if not WORD_SWITCH_SPLIT else WORD_SWITCH_LEN_R)
        if VISION:
            print("Vowel!")

    return first_part, second_part

def handle_apostrophe_insertion(first_part, second_part):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    if all(char in consonants for char in first_part[:3]):
        first_part = insert_char(first_part, '\'', LETTER_SWITCH_LEN if not WORD_SWITCH_SPLIT else WORD_SWITCH_LEN_L)
        if VISION:
            print("Apostrophe!")
    if all(char in consonants for char in second_part[:3]):
        second_part = insert_char(second_part, '\'', LETTER_SWITCH_LEN if not WORD_SWITCH_SPLIT else WORD_SWITCH_LEN_R)
        if VISION:
            print("Apostrophe!")

    if all(char in vowels for char in first_part[1:3]):
        if random.randint(1, 2) == 1:
            first_part = insert_char(first_part, '\'', LETTER_SWITCH_LEN if not WORD_SWITCH_SPLIT else WORD_SWITCH_LEN_L)
        if VISION:
            print("Apostrophe!")
    if all(char in vowels for char in second_part[1:3]):
        if random.randint(1, 2) == 1:
            second_part = insert_char(second_part, '\'', LETTER_SWITCH_LEN if not WORD_SWITCH_SPLIT else WORD_SWITCH_LEN_R)
        if VISION:
            print("Apostrophe!")

    return first_part, second_part

def insert_char(original_string, char_to_insert, position):
    """ Insert desired character into any string """
    return original_string[:position] + char_to_insert + original_string[position:]

def remove_suffixes(p1, p2):
    for suffix in suffixes:
        if p1.lower().endswith(suffix):
            p1 = p1[:-len(suffix)]
            if VISION:
                print("Suffix!")
            break
    for suffix in suffixes:
        if p2.lower().endswith(suffix):
            p2 = p2[:-len(suffix)]
            if VISION:
                print("Suffix!")
            break
    return p1, p2

def cut_off_right_end(word, cut_length):
    if len(word) <= cut_length:
        return word
    return word[:-cut_length]

def generate_mode():
    print(R"""

   _____________   ____________  ___  __________  ____       __  _______  ____  ______
  / ____/ ____/ | / / ____/ __ \/   |/_  __/ __ \/ __ \     /  |/  / __ \/ __ \/ ____/
 / / __/ __/ /  |/ / __/ / /_/ / /| | / / / / / / /_/ /    / /|_/ / / / / / / / __/
/ /_/ / /___/ /|  / /___/ _, _/ ___ |/ / / /_/ / _, _/    / /  / / /_/ / /_/ / /___
\____/_____/_/ |_/_____/_/ |_/_/  |_/_/  \____/_/ |_|    /_/  /_/\____/_____/_____/


    Press enter to generate a new name from a vast library of 2 word phrases.
    You will see the original phrase followed by the generated phrase.

    Available Commands:
    Type "help", "h", for more instructions.
    Type "exit", "e", to leave this mode.
    Type "fav", "f", to see your current favorites list
    Type "o" to jump straight to options from this mode at any time
          """)

    while True:
        user_input = input("\nPress Enter for a new generation: ")
        if user_input == "*":
            favorites.append(switched_output)
            print("Saved Successfuly! See Export Mode or type 'fav' to see current list.")
            continue
        elif user_input in ("fav", "favorite", "favorites", "f"):
            # print(f"\nYour Current Favorites:\n{favorites}\n")
            print ('\n'.join(favorites),'\n')
            continue
        if user_input == "":
            generate = random.choice(genlist)
            generate_giant = giant_list()
        elif user_input in ("exit", "e"):
            main()
        elif user_input in ("options", "o"):
            options_menu()
        elif user_input in ("help", "h"):
            print("""
    Kick back and relax! This mode will make a new name every time
    you press enter. All generations will be stored in the generate list.

    Depending on other settings, it will add vowels and apostrophes
    to the newly generated word (on by default, changeable in settings).

    If you like a generation, type "*" and it will add it to your favorites list!

    To see your favorites, type "f" or "fav" to print it out in the terminal.
    Just remember if you use Ctrl-C in the terminal it can crash the program! Try using Ctrl-Shift-C first.

    If you'd like to export favorites or all generations as a txt file, go to the Export mode in the main menu.

    Remember to experiment with different settings in the options mode!
    Options mode is accessible directly from here by typing "o" and pressing enter.
    From there you can change which manipulations are turned on and off.

    By default, ends of words are cut off by 1, common suffixes are removed,
    vowels are inserted if only consonants are present at the beginning of words,
    and apostraphes are also added to long strings of either consonants or vowels.
                """)
            continue
        else:
            continue

        one_or_two = random.randint(1, 2)
        if one_or_two == 1:
            print(f"\nOriginal:{generate}")
            input1, input2 = word_splitter(generate)
        else:
            print(f"\nOriginal:{generate_giant}")
            input1, input2 = word_splitter(generate_giant)
            # print("from giantlist")

        switched_output = switch_letters(input1, input2)
        print(switched_output)


def input_mode():
    print(R"""
    ____                  __     __  ___          __
   /  _/___  ____  __  __/ /_   /  |/  /___  ____/ /__
   / // __ \/ __ \/ / / / __/  / /|_/ / __ \/ __  / _ \
 _/ // / / / /_/ / /_/ / /_   / /  / / /_/ / /_/ /  __/
/___/_/ /_/ .___/\__,_/\__/  /_/  /_/\____/\__,_/\___/
         /_/

    Welcome to Input Mode! Input your own 2-word phrase.
    Commands available:

    Input 2 words: Get a switched-up version of your words
    Type "help" for more instructions
    Type "exit" to leave this mode
    Type "inspo" to enter the Inspiration Mode
    Type "fav" to see your current favorites list
    Type "o" or "options" to switch to Options Mode

          """)

    while True:
        user_input = input("Enter a two word phrase: ")
        if user_input == "*":
            favorites.append(switched_output)
            print("Saved Successfuly! See Export Mode or type 'fav' to see current list.\n")
            continue
        elif user_input in ("fav", "favorite", "favorites", "f"):
            # print(f"\nYour Current Favorites:\n{favorites}\n")
            if len(favorites) >= 1:
                print ('\n'.join(favorites),'\n')
                continue
            else:
                print("No favorites saved yet, use * to save a favorite after you make a generation!\n")
        elif user_input in ("exit", "e"):
            main()
        elif user_input in ("i", "inspo"):
            inspiration_guide()
        elif user_input in ("options", "o"):
            options_menu()
        elif user_input in ("help", "h"):
            print("""
    This mode asks you for an input and returns the first two letters of each word
    switched around, (plus other stuff which you can see with VISION activated).

    If you use 1-2 letters in a word don't expect much; it'll just add a vowel or return a Bad Input error.
    If you need some ideas for 2 word phrases, try inspiration mode! Available through just entering
    "i" in this mode, or get to it through the main menu accessible by "e" or "exit".

    Make sure theres a space between the two words!
    "Hello There" is acceptable; "Hello-There", "Hello", "Wow Such Hello" "Hello_There" won't work.

    Depending on other settings, it will add vowels and apostrophes
    to the newly generated word (on by default, changeable in settings).

    If you like a generation, type "*" and it will add it to your favorites list!

    To see your favorites, type "f" or "fav" to print it out in the terminal.
    Just remember if you use Ctrl-C in the terminal it can crash the program! Try using Ctrl-Shift-C first.

    If you'd like to export favorites or all generations as a txt file, go to the Export mode in the main menu.

    Remember to experiment with different settings in the options mode!
    Options mode is accessible directly from here by typing "o" and pressing enter.
    From there you can change which manipulations are turned on and off.

    By default, ends of words are cut off by 1, common suffixes are removed,
    vowels are inserted if only consonants are present at the beginning of words,
    and apostraphes are also added to long strings of either consonants or vowels.
                """)
            continue
        # elif len(word_splitter(user_input)) == 2:

        elif len(user_input.strip().split(" ")) < 2:
            print("Woops, try at least 2 words\n")
            continue
        elif len(user_input.strip().split(" ")) > 2:
            print("Woops, too many words, type exactly 2\n")
            continue
        elif len(word_splitter(user_input)) == 2:
            input1, input2 = word_splitter(user_input)
            switched_output = switch_letters(input1, input2)
            print(f"{switched_output}\n")


def inspiration_guide():
    print(R"""
    ____                 _            __  _                __  ___          __
   /  _/___  _________  (_)________ _/ /_(_)___  ____     /  |/  /___  ____/ /__
   / // __ \/ ___/ __ \/ / ___/ __ `/ __/ / __ \/ __ \   / /|_/ / __ \/ __  / _ \
 _/ // / / (__  ) /_/ / / /  / /_/ / /_/ / /_/ / / / /  / /  / / /_/ / /_/ /  __/
/___/_/ /_/____/ .___/_/_/   \__,_/\__/_/\____/_/ /_/  /_/  /_/\____/\__,_/\___/
              /_/
             /_/

    Welcome to the Inspiration guide!
    Heres the commands available in this mode:

    Press Enter: Get a category to get inspired by!
    Type "input": Switch to Input mode directly from this mode
    Type "e" or "exit": Go back to main menu

          """)
    while True:
        user_input = (input("Choose your option: "))
        if user_input == "":
            print(random.sample(inspirations, 1))
            print("Press Enter to see another category\n")
        elif user_input in ("i", "input"):
            input_mode()
        elif user_input in ("exit", "e"):
            main()
        else:
            print("Press enter or type 'exit' or 'e' to leave mode.")


def export_mode():
    import os
    import datetime

    print(R"""
    ______                      __     __  ___          __
   / ____/  ______  ____  _____/ /_   /  |/  /___  ____/ /__
  / __/ | |/_/ __ \/ __ \/ ___/ __/  / /|_/ / __ \/ __  / _ \
 / /____>  </ /_/ / /_/ / /  / /_   / /  / / /_/ / /_/ /  __/
/_____/_/|_/ .___/\____/_/   \__/  /_/  /_/\____/\__,_/\___/
          /_/

    Welcome to export mode! Currently you can only export as a list in terminal.
    Use the following commands to export accordingly:

    Press Enter: Print out all of your saved favorites into the terminal
    Type "favtxt": Export favorites into a .txt file in local directory
    Type "txt": Export all generations from this session in local directory
    Type "pdf": Export favorites into a .pdf file in local directory (Not implemented yet)
    Type "exit" or "e": to go back to main menu
          """)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base_path = os.path.dirname(__file__)
    fav_output_file = os.path.join(base_path, f'fav_output_{timestamp}.txt')
    session_output_file = os.path.join(base_path, f'session_output_{timestamp}.txt')
    
    while True:
        user_input = (input("Choose your option: "))
        if user_input == "":
            print('\n'.join(favorites))
            print("Happy with the export? Use 'exit' or 'e' to go back to the main menu.")
        elif user_input == "favtxt":
            with open(fav_output_file, 'w') as file:
                file.write('\n'.join(favorites))
                print(f"Success! Your favorites were saved to {fav_output_file}\n")
                continue
        elif user_input == "txt":
            with open(session_output_file, 'w') as file:
                file.write('\n'.join(runtime_list))
                print(f"Success! All generations from this session have been saved to {session_output_file}.\n")
                continue
        elif user_input in ("exit", "e"):
            main()
        else:
            print("Press enter or type 'exit' or 'e' to leave mode.")


def import_mode():
    print(R"""
    ____                           __     __    _      __     __  ___          __
   /  _/___ ___  ____  ____  _____/ /_   / /   (_)____/ /_   /  |/  /___  ____/ /__
   / // __ `__ \/ __ \/ __ \/ ___/ __/  / /   / / ___/ __/  / /|_/ / __ \/ __  / _ \
 _/ // / / / / / /_/ / /_/ / /  / /_   / /___/ (__  ) /_   / /  / / /_/ / /_/ /  __/
/___/_/ /_/ /_/ .___/\____/_/   \__/  /_____/_/____/\__/  /_/  /_/\____/\__,_/\___/
             /_/

    Welcome to Import List Mode!
    Please see the help command in this mode to see how to make your list compatible with this mode.

    Heres the available commands:
        Type "import" or "i": Follow the prompts to import, process, and output your list as a file
        Type "print": Type your list directly into terminal, print out your altered file directly into the terminal
        Type "help" or "h":  Shows how to use this mode, prepare your file for use.
        Type "exit" or "e":  Go to back to main menu

          """)
    while True:
        try:
            user_input = input("Input a command: ")
        except KeyboardInterrupt:
            "Invalid input, please input a command"
            continue
        except UnboundLocalError:
            "Watch those ctrl-whatevers, input a command: "
            continue
        if user_input in ("help", "h"):
            print("""
    Use the 'import' mode to import your own .txt file into the program and output a new file.
    Make sure the .txt file is in the same directory as this program. The output file will also appear there.

    Use the 'print' mode to paste a python list directly into the terminal. It'll output directly into the terminal
    as well. Careful when trying to copy/paste it as you may send a command into the terminal to cancel the program.
    Try Ctrl-Shift-C first before trying just Ctrl-C.
                  """)
            pass
        if user_input in ("exit", "e"):
            main()
        if user_input in ("print", "p"):
            print_in_terminal()
        if user_input in ("import", "i"):
            print(R"""
        Have your .txt file ready with a comma separated python-friendly list inside
        with all your two-word phrases ready. The list should not be named.

        Type "example" for an example of a correct list format.
        Once file is input, it will be processed and output as:
            "output_(current_time)"
        Type "e" or "exit" to leave without doing anything.
                """)
            process_text(get_input())


def get_input():
    import re
    """Get input for file imports"""
    pattern = r'.+\.txt$'
    while True:
        input_file = input(("Enter the filename of your list(ex. mylist.txt): "))
        match = re.match(pattern, input_file)
        if input_file == "example":
            print("""
Heres an example of an acceptable list:
["Take Five", "elephant tusk", "mass layoffs", "latestage capitalism"...]
ALL IN ONE LINE, if list is in separate lines, it will stop at the first break.
        """)
            continue
        elif input_file in ("exit", "e"):
            import_mode()
        elif match:
            process_text(input_file)
            break
        else:
            print("Improper input, must be a filename folowed by '.txt'; example 'yourfile.txt'.")


def print_in_terminal():
    print("""
    Prepare your list by copying it in its entirety without any breaklines.
    It must have brackets at the either end. ex: ["Buddy Holly", "Mike Jones", "Bill Murray"]
    Type "e" to go back to Import Mode Menu.
          """)
    terminal_list = input("Input/Paste the list: ")
    if terminal_list in ("exit", "e"):
        import_mode()
    else:
        processed_phrases = print_in_terminal_process(terminal_list)
        if processed_phrases:
            for phrase in processed_phrases:
                print(phrase)

    more_lists = input("Would you like to process more lists? (Y/N) ")

    if more_lists in ("Yes", "y", "yes", "Y"):
        print_in_terminal()
    else:
        import_mode()


def print_in_terminal_process(tlist):
    try:
        phrases = eval(tlist)
    except:
        print("Invalid input format. Please input a python-compatible list of 2 word phrases.")
        print_in_terminal()

    if not isinstance(phrases, list):
        print("Invalid input format. Please input a python-compatible list of 2 word phrases.")
        print_in_terminal()

    processed_phrases = []

    try:
        for phrase in phrases:
            word1, word2 = word_splitter(phrase)
            new_phrase = switch_letters(word1, word2)
            processed_phrases.append(f"{new_phrase}")
    except:
        print("Something wasn't right about your list. Are you sure every list item had 2 words separated by a space?\n")
        print_in_terminal()

    return processed_phrases

def process_text(input_file):
    """Imports, processes, then exports line-separated list"""
    import datetime
    with open(input_file, 'r') as file:
        phrases = eval(file.read())

    processed_phrases = []

    for phrase in phrases:
        word1, word2 = word_splitter(phrase)
        new_phrase = switch_letters(word1, word2)
        processed_phrases.append(f"{new_phrase}")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f'output_{timestamp}.txt'

    with open(output_file, 'w') as file:
        file.write(str(processed_phrases))
        print(f"Processed phrases saved to {output_file}\n")
        more_lists = input("Would you like to process more lists? (Y/N) ")
        if more_lists in ("Yes", "y", "yes"):
            process_text(get_input())
        else:
            import_mode()


def options_menu():
    print(R"""
   ____        __  _
  / __ \____  / /_(_)___  ____  _____
 / / / / __ \/ __/ / __ \/ __ \/ ___/
/ /_/ / /_/ / /_/ / /_/ / / / (__  )
\____/ .___/\__/_/\____/_/ /_/____/
    /_/


    Each option below will elaborate a little upon selection. For more in-depth info for all options, type "h" or "help".
    If you don't want to change the value, type in the default value given.
    If you're here from another mode:
    Type "g" or "generate" to go back to Generate Mode
    Type "i" or "input" to go back to Input Mode
          """)

    while True:
        print_options()
        try:
            user_input = input("Pick an option to change: (ex 8) ").strip().lower()
            if user_input in ('e', 'exit'):
                break
            elif user_input in ('generate', 'g'):
                generate_mode()
            elif user_input in ('h', 'help'):
                optionshelp()
            elif user_input in ('i', 'input'):
                input_mode()
            user_input = int(user_input)
        except ValueError:
            print("Please enter a valid option number.")
            continue

        if user_input == 1:
            try:
                global LETTER_SWITCH_LEN
                LETTER_SWITCH_LEN = int(input("Default value = 2. \nLetter switch length. \nSwitch to? "))
            except ValueError:
                print("Type a single integer, no spaces. Numbers > 4 will start to get wonky with Generate mode.")
        elif user_input == 2:
            try:
                global APOSTROPHE
                print(f"Current Value: {APOSTROPHE}")
                APOSTROPHE = input("Default value = True. \nApostrophe injection. \nSwitch to (True/False)? ").strip().lower() == 'true'
            except ValueError:
                print("Type only True or False.")
        elif user_input == 3:
            try:
                global VOWEL_INSERTION
                print(f"Current Value: {VOWEL_INSERTION}")
                VOWEL_INSERTION = input("Default value = True. \nVowel insertion. \nSwitch to (True/False)? ").strip().lower() == 'true'
            except ValueError:
                print("Type only True or False.")
        elif user_input == 4:
            try:
                global WORD_CUT_ON
                print(f"Current Value: {WORD_CUT_ON}")
                WORD_CUT_ON = input("Default value = False. \nCut off ends of words. \nSwitch to (True/False)? ").strip().lower() == 'true'
            except ValueError:
                print("Type only True or False.")
        elif user_input == 5:
            try:
                global WORD_SWITCH_SPLIT
                print(f"Current Value: {WORD_SWITCH_SPLIT}")
                WORD_SWITCH_SPLIT = input("Default value = False. \nChange WORD_SWITCH_L/R if you change this. \nSwitch to (True/False)? ").strip().lower() == 'true'
            except ValueError:
                print("Type only True or False.")
        elif user_input == 6:
            try:
                global WORD_SWITCH_LEN_L
                WORD_SWITCH_LEN_L = int(input("Default value = 1. \nWord switch length left word. \nSwitch to? "))
            except ValueError:
                print("Type a single integer, no spaces.")
        elif user_input == 7:
            try:
                global WORD_SWITCH_LEN_R
                WORD_SWITCH_LEN_R = int(input("Default value = 1. \nWord switch length right word. \nSwitch to? "))
            except ValueError:
                print("Type a single integer, no spaces.")
        elif user_input == 8:
            try:
                global REMOVE_SUFFIX_ON
                print(f"Current Value: {REMOVE_SUFFIX_ON}")
                REMOVE_SUFFIX_ON = input("Default value = True. \nRemove common suffixes. \nSwitch to (True/False)? ").strip().lower() == 'true'
            except ValueError:
                print("Type only True or False.")
        elif user_input == 9:
            try:
                global GENERATE_PORTRAIT
                print(f"Current Value: {GENERATE_PORTRAIT}")
                GENERATE_PORTRAIT = input("Default value = True. \nGenerate portrait with AI. Currently not working. \nSwitch to (True/False)? ").strip().lower() == 'true'
            except ValueError:
                print("Type only True or False.")
        elif user_input == 10:
            try:
                global VISION
                print(f"Current Value: {VISION}")
                VISION = input("Default value = False. \nSee which adjustments made during generation. \nSwitch to (True/False)? ").strip().lower() == 'true'
            except ValueError:
                print("Type only True or False.")
        else:
            print("Invalid option, pick 1-10 or type 'e'/'exit'.")


def print_options():
    print("\n")
    print(f"1. LETTER_SWITCH_LEN = {LETTER_SWITCH_LEN}")
    print(f"2. APOSTROPHE = {APOSTROPHE}")
    print(f"3. VOWEL_INSERTION = {VOWEL_INSERTION}")
    print(f"4. WORD_CUT_ON = {WORD_CUT_ON}")
    print(f"5. WORD_SWITCH_SPLIT = {WORD_SWITCH_SPLIT}")
    print(f"6. WORD_SWITCH_LEN_L = {WORD_SWITCH_LEN_L}")
    print(f"7. WORD_SWITCH_LEN_R = {WORD_SWITCH_LEN_R}")
    print(f"8. REMOVE_SUFFIX_ON) = {REMOVE_SUFFIX_ON}")
    print(f"9. GENERATE_PORTRAIT = {GENERATE_PORTRAIT}")
    print(f"10. VISION = {VISION}")
    print("\n")


def optionshelp():
    print("""
    Below is each setting explained, along with some basic examples of what changing them does.
    As a recommendation, try turning on WORD_CUT_ON for at least 1 letter
    LETTER_SWITCH_LEN:
          Define the length from each word to be switched.
          Ex with 2:
                Truly Ridiculous --> Riuly Trdiculous
          Ex with 3:
                Truly Ridiculous --> Ridly Truiculous
          Recommendations: A letter switch length of 2 or 3 is optimal, but more than that
                you may start to just be switching entire words' positions.

    APOSTROPHE:
          Decide whether you want apostraphes in your generations.
          Apostraphes will be inserted if there are too many consecutive vowel or consonants.
          The length of them is defined by the logic as being 3 or more.
          Ex True:
                Petrified Wood --> Wotrified Pe'od
          Ex False:
                Petrified Wood --> Wotrified Peod

    VOWEL_INSERTION:
          Decide whether you want added vowels in your generations.
          Vowels will be inserted if there are too many consecutive consonants.
          The length of consecutive consonants is determined in the logic as being 3 or more
          at the beginning of the newly generated phrase. The vowel gets inserted after the first letter.
          The vowel is chosen randomly from all possible vowels (aeiouy).
          Ex True:
                Pterydactyl Psyonics --> Poserydactyl Putyonics
          Ex False:
                Pterydactyl Psyonics --> Pserydactyl Ptyonics

    WORD_CUT_ON:
          Decide whether you'd like to cut off the ends of words from your generations.
          This will completely cut off letters from the end of generations by the number
          specified by WORD_CUT_LENGTH (WCL). Helpful if you want to remove familiarity with
          certain endings of common words like -ato in potato or tomato, or common suffixes like
          "-aly" or "-tial" or "-ing".
          Ex True, WCL of 2:
                Potato Lettuce --> Leta Pottu
          Ex False:
                Potato Lettuce --> Letato Pottuce

    WORD_CUT_LENGTH:
          Determines the length of letters to be cut off the end of a word. See WORD_CUT_ON for more details.

    WORD_SWITCH_SPLIT:
          Determines if you'd like to turn on having each word have a different amount of letters taken
          from the other. So the left word could have 1 letter taken from it and placed on the right,
          while the right word can have 3 letters taken from it and put on the left. Letters cut from
          left and right are defined by WORD_SWITCH_LEN_L (WSLL) and WORD_SWITCH_LEN_R (WSLR) respectively.

          Ex True, WSSL of 1, WSSR of 3:
                Something Wrong --> Wroomething Srong
          Ex False, defaults to LETTER_SWITCH_LEN of 2:
                Something Wrong --> Wrmething Soong

    WORD_SWITCH_LEN_L:
          Changes the length taken from the left word to be given to the right word.
          See WORD_SWITCH_SPLIT for more details.

    WORD_SWITCH_LEN_R:
          Changes the length taken from the right word to be given to the left word.
          See WORD_SWITCH_SPLIT for more details.

    REMOVE_SUFFIX_ON:
          Removes common suffixes from the end of words in order to make them sound more like a name.
          Most names dont end in '-aly' or '-tion', or '-ing', so removing them gives more validity to
          the generated name. The full list of suffixes that get removed will be listed below.
          Ex: True
                Floating Totally --> To'oat Flatal
          Ex: False
                Floating Totally --> To'oating Flatally

    VISION:
          If on, shows which logic was used in the generation of the last phrase.
          Ex: True
                Original:decide slowness
                Vowel!
                Suffix!
                Slocid Deo
          Ex: False
                Original:decide slowness
                Slocid Deo

    The default values of all the above settings approximate what the original post logic was like;
    switch 2 letters of the beginning of 2 words. Vowel insertion, 1 cut length, and apostraphes were added to smooth
    out the unpronouncable generations, but by making use of these options, it helps even further remove one from
    the possible remnants of the original words and provide a new "feeling" to the output generation that
    doesn't at all feel familiar. Maybe, perhaps, making the name feel like it came from far, far away...


        """)

def about_mode():
    print(R"""
     ___    __                __
   /   |  / /_  ____  __  __/ /_
  / /| | / __ \/ __ \/ / / / __/
 / ___ |/ /_/ / /_/ / /_/ / /_
/_/  |_/_.___/\____/\__,_/\__/

    This program was inspired by a reddit post I saw here:
    https://www.reddit.com/r/OTMemes/comments/196ghjm/wuffalo_bings/
    Original BlueSky post here:
    https://bsky.app/profile/ogfattcatt.bsky.social/post/3kiwfjsxzkk25

    Hence, the name of this program; Weef Bellington.
    This is basically just a fancy name generator that requires an input.

    At its inception, the program just followed the post 'rules' and took any input of two words and switched
    the first two letters of each word, generating a "Star Wars" name.
    In terms of a Python program that could accomplish this, it felt too simple for a final CS50P project.
    I started thinking up how to add complexity, so I added more and more features which can be used during runtime.
    This resulted in the introduction of a lot of different modes and options for word manipulation.
    This struck a good balance of of disovering new letter combinations with familiar letter-pairings
    to form new names while not being phonetically unreadable. I found it fascinating to discover new combinations
    using Generate mode that felt like a little window into the unknown. This especially came out more with
    the introduction of using 2-3 rules simultaneously at low intensity. It's like an emergent property of a
    lot of small adjustments to words create new ones.

    Is it overall pretty silly? Yes, it is. However this program still feels like it was worth making.
    Doing the letter switching by hand is easy to do one or two times, but becomes quite mentally taxing to do a lot.
    Add cutting off the last letter or adding vowels or apostraphes, it becomes a lot of work to go through a long list!


    *** Tips and Tricks: ***
        - Use '*' during Generation or Input mode to save the last generation to favorites, then print them out in Export Mode
        - Use 'e' during any time to go back to the main menu
        - Try changing the LETTER_SWITCH_LEN to 3!
        - Generate a portrait image your last generation with an Open AI API key! Type 9 at the main menu to get started.


    Overview of Modes:

    - Generate Mode pulls from a huge library of common words and phrases.

    - Input Mode asks the user to input their own 2 word phrase; this lets you try out your own combinations.

    - Inspiration Guide can be directly accessed from Input Mode and from the main menu. It just
      gives some categories to the user to get inspired to use in Input Mode.

    - Export Mode allows users to export their favorite generations, which can be tagged
      right after a generation during Generate or Input mode by using "*".
      In other words, if the user never uses the "*" command, favorites will be empty.
      However all generations for each session are saved during each runtime and can also be exported.

    - Import Mode allows someone to import a python structured list into the program either through the
      terminal or a txt file, processing them all in one batch.

    - Options allows the user to change the core elements of the letter switch logic, such as
      the length that gets swapped, even down to each word (word 1 gets 2 letters taken out, but word 2 gets 3 etc.)
      Other options include whether apostraphes or vowels should be injected in words combinations that generate
      multiple consonants or vowels in a row. Vision lets you see which manipulations were performed if they triggered.


    Have fun! If you somehow end up using this program to generate some names for your star wars or general naming needs,
    feel free to give a shout out to Kirill Volguin or @kvolguin on instagram or just the name!

    Kirill Volguin is the author of this program. Copyright 2024.


    If somehow this program impressed you so much you feel like you need to hire me,
    send a message over to kvolguin@gmail.com!
          """)
    print(input("Scroll up to see all of the About text!\nPress enter again to go back to the main menu :)"))

def first_time_mode():
    print("\nWIP\n")
def portrait_generation_mode():
    print("""
Hey there. I couldn't get this to work, my bad. I'll learn one day and maybe update it...
I decided to abandon calling the OpenAI API from within this program.
Instead, just paste the below text into any image generator:

'
generate an portrait image of a (choose one
[person, Hutt, Wookie, Geonosian, Kaminoan, Zabrak, Gungan, Bith, Nautolan, Bothan, Trandoshan, Rodian, Mon Calamari, Toydarian, Kel Dors, Zabrak, Twi-lek, Togruta, robot,])
in a sci-fi universe identically resembling the most famous sci-fi trilogy.
Draw it in the style of a concept drawing whose main character trait is (choose one at random:
[anti-hero, amusing, aggressive, robotic, assertive, brave, benevolent, careful, mysterious, clumsy,
condescending, content, dark, daring, devious, devout, religious, disgruntled, distant, dim, dreamy, energetic, ethical,
transactional, excitable, extroverted, introverted, honorable, fair-minded, feisty, rebellious, flawed, forgiving,
generous, gentle, giant, tiny, grumpy, hardworking, impulsive, intellectual, irritating, jealous,
laid-back, larger-than-life, likeable, loveable, manipulative, modest, naive, motivated, neurotic, noble,
philosophical, placid, polite, powerful, practical, protagonist, quick-witted, prudent, reverent,
reliable, sassy, rude, selfish, realistic, simple-minded, sincere, snivelling, soft, athletic, studious,
temperamental, territorial, thick-skinned, tidy, timid, frugal, ugly, trustworthy, unlucky, unselfish,
upbeat, vain, versatile, virtuous, wild, wise, witless, witty, youthful, zealous])
The name of the character is ____ _____.
'
I had good luck as of 7/11/2024 with DALL-E 3 since it sometimes includes the name of the character as well.
    """)

    """
    import openai
    from PIL import Image, ImageDraw, ImageFont
    import requests
    from io import BytesIO

    # Step 1: Install the necessary libraries

    print("You need to install the openai and pillow packages. Run the following command if you haven't already:")
    print("pip install openai pillow requests")
    print("Then you need to download the following font file and install it on your device:")
    print("https://www.fontsquirrel.com/fonts/distant-galaxy")

    api_key = input("Please enter your OpenAI API key: ")

    openai.api_key = api_key

    prompt = look_above

    response = openai.Image.create_edit(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    global last_gen

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("Distant Galaxy.ttf", 50)

    width, height = image.size

    text_width, text_height = draw.textsize(last_gen, font=font)

    x = (width - text_width) / 2
    y = height - text_height - 20

    draw.text((x, y), last_gen, font=font, fill="white")

    # Show the image
    image.show()

    # Save the image
    image.save(f"{last_gen}.png")

    print(f"Image generated and saved as '{last_gen}.png'")
    """


def menu():
    print("Please select from the following: ")
    print(R"""
    __  ___      _          __  ___
   /  |/  /___ _(_)___     /  |/  /__  ____  __  __
  / /|_/ / __ `/ / __ \   / /|_/ / _ \/ __ \/ / / /
 / /  / / /_/ / / / / /  / /  / /  __/ / / / /_/ /
/_/  /_/\__,_/_/_/ /_/  /_/  /_/\___/_/ /_/\__,_/

    1. Generate Mode
    2. Input Mode
    3. Inspiration Guide
    4. Export Mode
    5. Import List
    6. Options
    7. About, Help
    8. Exit (WILL ERASE PROGRESS IF NO EXPORT MADE)
    """)


def show_intro_message():
    print("Welcome to Weef Bellington, where your Star Wars name generation dreams come true!")
    print("Would you like to get a rundown of how this works? (Type yes or no; Y/N; y/n)")
    first_time = input("(Y/N)")
    if first_time == "Y" or "y" or "Yes" or "yes" or "yeah" or "yep" or "yuh" or "ok" or "OK":
        first_time_mode()


def main():
    print(R"""

******************************************************************************************
*   *                             *                            *                    *    *
*                  *                               *                      *              *
*         *              _    _                          ____                            *
*  *                    F L  J J     ____      ____     / ___J                   *       *
*                      | | .. | |   F __ J    F __ J   | |_                              *
*                      | |/  \| |  | _____|  | _____|  |  _|             *               *
*      *       *       F   /\   J  F L___--. F L___--. F |                               *
*                     J___//\\___LJ\______/FJ\______/FJ__F                               *
*    *                |___/  \___| J______F  J______F |__|       *                *      *
*         ___             __  __  __                       _                             *
*        F _ ",   ____    LJ  LJ  LJ   _ ___      ___ _   FJ_      ____     _ ___        *
*       J `-' |  F __ J   FJ  FJ      J '__ J    F __` L J  _|    F __ J   J '__ J       *
*       | ,--.\ | _____J J  LJ  L FJ  | |__| |  | |--| | | |-'   | |--| |  | |__| |      *
*       F L__J \F L___--.J  LJ  LJ  L F L  J J  F L__J J F |__-. F L__J J  F L  J J      *
*      J_______J\______/FJ__LJ__LJ__LJ__L  J__L )-____  L\_____/J\______/FJ__L  J__L     *
*      |_______FJ______F |__||__||__||__L  J__|J\______/FJ_____F J______F |__L  J__|     *
*                                               J______F                                 *
*                             *                                        *                 *
*        *                                          *                                    *
******************************************************************************************
          """)
    global intro_shown
    intro_shown = True

    if not intro_shown:
        show_intro_message()
        intro_shown = True

    while True:
        menu()
        menu_select = input("\nChoose a menu item above (ex: 1): ")
        if menu_select in ("1", "1."):
            generate_mode()
        elif menu_select in ("2", "2."):
            input_mode()
        elif menu_select in ("3", "3."):
            inspiration_guide()
        elif menu_select in ("4", "4."):
            export_mode()
        elif menu_select in ("5", "5."):
            import_mode()
        elif menu_select in ("6", "6."):
            options_menu()
        elif menu_select in ("7", "7."):
            about_mode()
        elif menu_select in ("8", "8.", "exit", "e"):
            sys.exit("A good day to you and I hope you have enjoyed your Weef Bellington.\n" )
        elif menu_select in ("9", "9."):
            portrait_generation_mode()
        else:
            print("\nOi, select something from 1-8 eh?\n")










































"""
Attributions
ASCII Art: https://www.asciiart.eu/text-to-ascii-art#google_vignette

"""

def giant_list():
    import os
    import random
    import ast

    base_path = os.path.dirname(__file__) # where .py lives
    file_path = os.path.join(base_path, 'longestlist2.txt')
    with open (file_path, 'r') as file:
            content = file.read()

    words = ast.literal_eval(content)
    random_words = random.sample(words, 2)
    combined_string = ' '.join(random_words)
    return combined_string

def random_words():
    """ Source from MIT: https://www.mit.edu/~ecprice/wordlist.10000 and https://websites.umich.edu/~jlawler/wordlist
        Cleaned with this: https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/blob/master/en
        There still may be some "naughty" words in this list, discretion is advised.
    """
    import os
    import random
    import ast

    base_path = os.path.dirname(__file__) # where .py lives
    file_path = os.path.join(base_path, 'filtered_ultralist.txt')
    with open (file_path, 'r') as file:
        content = file.read()

    words = ast.literal_eval(content)
    random_words = random.sample(words, 2)
    combined_string = ' '.join(random_words)
    return combined_string

inspirations = ["Try a food: Ex: Beef Wellington, Chicken Kebab,  Swedish Meatball",
                "Try a Species name: Ex: Redfooted Warbler, Green Thrush, Dromia personata",
                "Try a Landmark: Ex: Golden Gate, Great Wall, Uluru Rock",
                "Try any old phrase: Ex: 'Hello World', 'Significant Other', 'Great Minds'",
                "Try locations: Ex: 'Los Angeles California', 'Sicily Italy', 'Houston Texas'",
                "Try books, movies, or Games. Ex: 'Metal Gear', 'Bagend Shire', 'Independence Day'",
                "Try common Names: 'John Cena', 'Mike Wazowski', 'Terry Pratchet'",
                "Try random words: 'barely sentient', 'feeling bananas', 'squiggly flies'",
                "Try two random objects around you: 'lamp desk', 'bottle glass', 'controller speaker'",
                "Try two animals: 'lion parrot', 'giraffe elephant', 'marmoset binturong'",
                "Try two science concepts: 'hadron collider', 'sulfur carbon', 'centripetal inertia'",
                "Try actors names!: 'Bill Murray', 'Tom Hanks', 'Jessica Alba'",
                "Try character names: 'Harry Potter', 'Frodo Baggins', 'Banjo Kazooie'",
                "Try nonsense: 'jeryl fangus', 'troddy bleue', 'felky sinkins'"
                ]

genlist = [
    #Random phrases that just came to my head
#    phrases == list(set(["Howdy There", "Skibidi Toilet", "Nobody Knows", "Elaborate Ruse", "Contain Multitudes", "You Died",
    "Backup Terry", "New World", "Take Five", "Whos There", "Anyone Home", "Every Time", "Skipping School"
    "Delicate Flower", "Terrible Consequence", "Miracle Baby", "Feeling Lucky", "Getting Schooled",
    "Astral Vibes", "Smelly Feet", "Beautiful World", "Hello World", "Obscure Mechanics", "Thousand Year",
    "Worst Matchup", "Auto Farm", "Animal Crossing", "Very Complicated", "Great Minds",
    "Significant Other", "Sicko Mode", "Hello There", "Your Father", "Itsa Trap", "New Hope",
    "Lackof Faith", "Arent Droids", "Youre Lookingfor", "Obi Wan", "High Ground", "Han Shot", "Stuck Up",
    "Half Witted", "Scruffy Looking", "Nerf Herder", "Hate Sand", "Course'n Rough", "Gets Everywhere",
    "Liberty Dies", "Thunderous Applause", "Thatsno Moon", "Sacred Texts", "Boring Conversation", "Clone Wars",
    "Darth Vader", "Luke Skywalker", "Dark Side", "Light Side", "Sobeit Jedi", "Adventure Excitement",

    #Phrases from https://parade.com/living/two-word-phrases
    "Good News", "Accept Yourself", "Be Honest", "Chill Out", "Dont Panic",
    "Enjoy Life", "Forever Free", "Baby Steps", "Miss You", "Good Job",
    "Be Spontaneous", "Have Faith", "Explore Magic", "Hold On", "Imperfectly Perfect",
    "Invite Tranquility", "Just Imagine", "Laugh Today", "Be Kind", "Notice Things",
    "Shift Happens", "Have Patience", "Let Go", "Stay Strong", "Slow Down",
    "Be Still", "Start Living", "Keep Calm", "Thank You", "Think Differently",
    "Start Somewhere", "Be Optimistic", "Dream Big", "Aim High", "Be Yourself",
    "Dance Today", "Dont Stop", "Breathe Deeply", "Enjoy Today", "Fear Not",
    "Cherish Today", "Getting There", "Well Done", "I Can", "Find Balance",
    "Be Fearless", "I Will", "Infinite Possibilities", "Look Within", "Stay Focused",
    "Just Believe", "Give Thanks", "Follow Through", "Inhale Exhale", "Everything Counts",
    "Everyones Special", "Call Me", "Come Back", "Hello Gorgeous", "Just Because",
    "Love Endures", "Love You", "Miracles Happen", "Perfectly Content", "Friends Forever",
    "Be Safe", "Stay Beautiful", "True Love", "Hello Beautiful", "You Matter",
    "Trust Me", "Love Fearlessly", "You Sparkle", "Much Love", "Love Struck",
    "Unconditional Love", "Love Fiercely", "Adore You", "Butterflies Still", "Feeling Groovy",
    "For Real", "Game On", "Forget This", "Keep Calm", "Oh really",
    "No Boundaries", "Shine On", "Have Fun", "Stay True", "Take Chances",
    "Pretty Awesome", "Keep Smiling", "Oh Snap", "Think Twice", "Loosen Up",
    "Treasure Today", "Not Yet", "Try Again", "What If", "Tickled Pink",
    "You Can", "Wanna Play", "Rise Above", "Why Not",
    #]))

    # Giant list of words

    # Foods
#    foods == list(set(["Rooibos Tea", "Pizza Napoletana", "Fried Chicken", "Beef Wellington", "Kolache Donuts", "Phanaeng Curry",
    "Chicken Curry", "Roti Canai", "Garlic Naan", "Chuck Roast", "Beef Mushroom", "Macaroni Cheese", "Chicken Potpie",
    "Broccoli Casserole", "Celery Soup", "Chicken Paprikash", "Shrimp Quesadilla",
    "Chicken Gravy", "Salmon Chowder", "Broccoli Chicken", "Shepherd’s Pie",
    "Turkey Soup", "Steak Kabob", "Shrimp Kabob", "Pork Loin", "Swedish Meatball",
    "Sparerib", "Chicken Spaghetti", "Turkey Chili", "Whole Chicken",
    "Hamburger Stroganoff", "Zucchini Boat", "Tuna Casserole", "Pork Skillet",
    "Pot Roast", "Salisbury Steak", "Cube Steak", "Salsa Beef", "Chicken Bake",
    "Roast Chicken", "Rice Soup", "Rigatoni Sausage", "Ham Chowder",
    "Roast Beef", "Fried Chicken", "Firecracker Shrimp", "Pizza Dish",
    "Vegetable Roast", "Meatball Stroganoff", "Chili Casserole", "Spaghetti Meatball",
    "Crab Cake", "Potato Soup", "Pork Chop", "Creole Jambalaya", "Swiss Chicken",
    "Sirloin Steak", "Roasted Chicken", "French Cassoulet", "Hungarian Beef",
    "Skillet Chicken", "Stuffed Chop", "Dumpling Chicken", "Chili Beef",
    "Valencian Paella", "Butter Chicken", "Pizza Margherita", "Yangzhou Rice",
    "Mixed Bibimbap", "Grilled Asado", "Lamb Plov", "Seafood Sushi", "Meat Tacos",
    "Pork Feijoada", "Vegetable Ratatouille", "Eggplant Moussaka", "Meat Goulash",
    "Beet Borscht", "Cheese Pierogi", "Fried Currywurst", "Chickpea Falafel",
    "Thai Noodles", "Jollof Rice", "Uzbek Plov", "Natto Beans", "Black Beans", "Tiramisu Cake", "French Fries",
    "Chicken Nuggets", "Bison Burger", "Jambalaya Rice", "Houston Roll", "Banh Mi", "Veggie Gyoza", "Beef Pho",
    "Chicken Pho", "Vindaloo Chicken", "Borscht Soup", "Truffle Pasta", "Kale Salad", "Quinoa Salad", "Chicken Parmesan",
    "Belgian Waffles", "Buttered Popcorn", "Masala Dosa", "Potato Chips", "Seafood paella", "Som Tam", "Birria Tacos"
    "Crunchy Taco", "Soft Taco", "Carnitas Tacos", "Pollo Asado", "Al Pastor", "Cochinita Pibil", "Buttered Toast",
    "Stinky Tofu", "French Toast", "Chili Crab", "Maple Syrup", "Parma Ham", "Goi cuon", "Ohmi Gyu", "Bunny Chow",
    "Shish kebab", "Custard Tart", "Fruit Tart", "Cob Corn", "Cobb Salad", "Caesar Salad", "Rendang Beef", "Chicken muamba",
    "Ice Cream", "Massaman curry",
    #]))
    # Species Names list(set([]))
#    species == list(set(["Black buck", "Antelope cervicapra", "Gazella bennettii", "Boselaphus tragocamelus",
    "Canis lupus", "Panthera leo", "Elephas maximus", "Equus africanus asinus",
    "Panthera pardus", "Cervus canadensis", "Pavo cristatus", "Grus leucogeranus",
    "Vulpes vulpes", "Rhinoceros unicornis", "Panthera Tigris", "Crocodylus palustris",
    "Gavialis gangeticus", "Equus caballus", "Equus quagga", "Babalus bubalis",
    "Sus scrofa", "Camelus dromedaries", "Giraffa camelopardalis", "Hemidactylus flaviviridis",
    "Hippopotamus amphibius", "Macaca mulatta", "Canis lupus", "Felis domesticus",
    "Acinonyx jubatus", "Rattus rattus", "Mus musculus", "Oryctolagus cuniculus",
    "Bubo virginianus", "Passer domesticus", "Corvus splendens", "Acridotheres tristis",
    "Psittacula eupatria", "Molpastes cafer", "Eudynamis scolopaccus", "Columba livia",
    "Ophiophagus hannah", "Hydrophiinae", "Python molurus", "Ptyas mucosa"
    "Black buck", "Wild Donkey", "House Lizard", "Rhesus monkey", "Horned owl",
    "House sparrow", "House crow", "Common myna", "Indian parrot", "King Cobra",
    "King cobra", "Sea snake", "Indian Python", "Sea Snake", "Rat Snake", "Arabian Camel",
    # following from this URL: https://www.fs.usda.gov/Internet/FSE_DOCUMENTS/stelprdb5166443.pdf
    "Adder's tongue", "Ophioglossum vulgatum",
    "Buck bean", "Menyanthes trifoliata", "Medicago sativa", "Buffalo berry", "Alkali cordgrass", "Spartina gracilis",
    "Buffalo grass", "Buchloe dactyloides", "Alkali grass", "Puccinellia nuttaliana", "Alkali sacton", "Sporobolus airoides",
    "Bur oak", "Quercus macrocarpa", "Alyssum phlox", "Phlox alyssifolia", "Canada anemone", "Anemone candensis",
    "American elm", "Ulmus americana", "Canada goldenrod", "Solidago canadensis", "American plum", "Prunus americana",
    "Canada thistle", "Cirsium canadensis", "American sea", "Suaeda caleoliformis", "Canada rye", "Elymus canadensis",
    "Annual ragweed", "Ambrosia artemisiifolia", "Cat tail", "Arrow head", "Cheat grass", "Aspen tree", "Choke cherry", "Prunus virginiana",
    "Austrian pine", "Pinus balfouriana", "Club moss", "Baltic rush", "Juncus balticus", "Common rabbitbrush", "Chrysothamnus nauseosus",
    "Barrs milkvetch", "Astragalus barii", "Common Rush", " Equisetum hyemale", "Basin rye", "Leymus cinerus", "Common spikesedge",
    "Bass wood", "Tilia americana", "Cone flower", "Beach heather", "Hudsonia tomentosa",
    "Zea mays", "Beaked willow", "Salix bebbiana", "Cotton wood", "Populus deltoides", "Bearded wheatgrass", "Agropyron subsecundum",
    "Creeping cedar", "Juniperus horizontalis", "Bee balm", "Crested fern", "Dryopteris cristata", "Big bluestem", "Andropogon gerardii",
    "Crested wheatgrass", "Agropyron cristatum", "Birdfoot sagebrush", "Artemisia pedatifida", "Crested woodfern", "Dryopteris cristata",
    "Black greasewood", "Sarcobatus vermiculatus", "Dakota buckwheat", "Eriogonum visheri", "Black-eyed Susan", "Rudbeckia hirta",
    "Delicate sedge", "Carex leptalea", "Blanket flower", "Dog berry", "Ribes cynosbati", "Blowout grass", "Redfieldia flexuosa",
    "Dotted gayfeather", "Liatris punctata", "Blowout penstemon", "Penstemon haydenii", "Douglas knotweed", "Polygonum douglasii",
    "Blue grama", "Bouteloua gracilis", "Downy brome", "Bromus tectorum", "Blue lips", "Collinsia parviflora",
    "Dwarf juniper", "Juniperus communis", "Bluebunch wheatgrass", "Agropyron spicatum", "Eastern cedar", " Juniperus virginiana",
    "Blue joint", "Calamagrostis canadensis", "Fescue sedge", "Carex alopecoidea", "Bog willow", "Salix pedicellaris",
    "Flea bane", "Boston ivy", "Parthenocissus tricuspidata", "Four-wing saltbush", "Atriplex canescens",
    "Box elder", "Acer negundo", "Fowl bluegrass", "Poa palustris", "golden rod", "Solidago flexcaulis",
    "Foxtail barley", "Hordeum jubatum", "Broom snakeweed", "Gutierrezia dracunculoides", "Foxtail sedge", "Carex alopecoidea",
    "Fringed sage", "Artemisia frigida", "Littleseed ricegrass", "Oryzopsis micrantha", "Frost weed", "Helianthemum bicknelli",
    "Robina pseudo-acacia", "Gardners saltbush", "Atriplex gardneri", "Loesels twayblade", "Liparis loeselii",
    "Gay feather", "cone flower", "Golden stickleaf", "Mentzelia pumila", "Marsh bellflower", "Campanula aparinoides",
    "Grass-leaved goldenrod", "Euthamia graminifolia", "Marsh fern", "Thelypteris palustris", "Gray sagewort", "Artemisia ludoviciana",
    "Marsh horsetail", "Equisetum palustre", "Grease wood", "Sarcobatus vermiculatus", "Mat muhly", "Muhlenbergia richardsonis",
    "Green ash", "Fraxinus pennsylvanica", "Meadow brome", "Bromus erectus", "Green needlegrass", "Stipa viridula",
    "Meadow horsetail", "Equisetum pratense", "Green sagewort", "Artemisia dracunculus", "Meadow Willow", "Salix petiolaris",
    "Gumbo lily", "Oenothera caespitosa", "Milk weed", "Hack berry", "Celtis occidentalis",
    "Mountain brome", "Bromus marginatus", "Hairy grama", "Bouteloua hirsuta", "Mountain mahogany", "Cercocarpus montanus",
    "Handsome sedge", "Carex formosa", "Musk thistle", "Carduus nutans", "Hardstem bulrush", "Scripus acutus",
    "purple coneflower", "Echinacea angustifolia", "Hare bell", "Campanula rotundifolia",
    "Needle thread", "Stipa comata", "Haw thorn", "Needleleaf sedge", "Carex duriuscula",
    "Hedge-nettle", "Stachys palustris", "Nodding buckwheat", "Eriogonum cernuum", "Hoary cress", "Cardaria draba",
    "Northern green", "orchid Platanthera hyperborea", "Hoary vervain", "Verbena stricta",
    "Northern pin", "oak Quercus ellipsoidalis", "Hooker's townsendia", "Townsendia hookeri",
    "Northern reedgrass", "Calamagrostis stricta", "sumac Rhus trilobata", "Nuttall grass", " Puccinellia nuttaliana",
    "Indian grass", "Sorghastrum nutans", "Oakfern", "Gymnocarpium dryopteris",
    "Inland saltgrass", "Distichlis spicata", "Oregon grape", "Berberis repens", "Iron wood", "Ostrya virginiana",
    "Pale echinacea", "Echinacea pallida", "Jack pine", "Pinus bansian", "Panicled aster", "Aster simplex",
    "Japanese brome", "Bromus japonicus", "Paper birch", "Betula papyrifera", "Joe Pye", "weed Eupatorium macutatum bruneri",
    "Peachleaf willow", "Salix amygdaloides", "Junegrass", "Koeleria pyramidata", "Pen stemon",
    "Kochia scoparia", "Labrador bedstraw", "Galium labradoricum", "Lady fern", "Athyrium filix-femina",
    "Lancefeaf cottonwood", "Populus x acuminata", "Lead plant", "Amorpha canescens",
    "Leafy bulrush", "Scirpus polyphyllus", "Leafy spruge", "Euphorbia esula", "Leathery grapefern", "Botrychium multifidum",
    "Limber pine", "Pinus flexilis", "Little bluestem", "Andropogon scoparius", "Little grapefern", "Botrychium simplex",
    "Red clover", "Trifolium pratense", "Iron wood", "Ostrya virginiana", "Jack pine", "Pinus bansian", "Japanese brome", "Bromus japonicus",
    "Eupatorium macutatum", "June grass", "Koeleria pyramidata", "Kentucky bluegrass", "Poa pratensis",
    "Red osier dogwood", "Red threeawn", "Redtop", "Ricegrass", "Rubber rabbitbrush",
    "Russian knapweed", "Rydberg's sunflower", "Sand bluestem", "Sand dropseed",
    "Sand lily", "Sand lovegrass", "Sand muhly", "Sand sagebrush", "Sandbar willow",
    "Sandberg bluegrass", "Sandgrass", "Scotch pine", "Sensitive fern",
    "Service berry", "Shad scale", "Shining flatsedge", "Lady's slipper",
    "Shrubby cinquefoil", "Sideoats grama", "Silky prairie clover", "Silver buffaloberry",
    "Silver sage", "Silver sagebrush", "Silver berry", "Silverweed cinquefoil",
    "Skunk brush", "Skunkbrush sumac", "Slendar cottongrass", "Slendar wheatgrass",
    "Smart weed", "Smooth brome", "Smooth goosefoot", "Smooth rush",
    "Smooth sumac", "Smoothbark cottonwood",
     "Cornus sericea", "Aristida robusta", "Agrostis stolonifera",
    "Juniperus scopulorum", "Chrysothamnus nauseosus", "Centaurea repens",
    "Andropogon hallii", "Sporobolus cryptandrius", "Leucocrinum montanum",
    "Eragrostis trichodes", "Muhlenbergia arenicola", "Artemisia filifolia",
    "Salix exigua", "Poa sandbergii", "Triplasis purpurea", "Pinus sylvestris",
    "Onoclea sensibilis", "Atriplex confertifolia", "Cyperus bipartitus",
    "Cypridpedium reginae", "Pentaphylloides floribunda", "Bouteloua curtipendula",
    "Dalea villosa", "Shepherdia argentea", "Artemisia cana", "Elaegnus commutata",
    "Potenilla argentea", "Rhus aromatica", "Eriphorum gracile",
    "Agropyron trachycaulum", "Cypripedium candidum", "Bromus inermis",
    "Chenopodium subglabrum", "Equisetum laevigatum", "Rhus glabra",
    "Populus acuminata",
    "fairy shrimp", "American bittern", "burying beetle", "American crow",
    "American goldfinch", "peregrine falcon", "American wigeon", "Argos skipper",
    "Common Badger", "Baird's sparrow", "Bald eagle", "Brown Beaver",
    "Belfragiis bug", "Bells vireo", "Belted kingfisher", "American Bison",
    "Black bullhead", "Black tern", "Black woodpecker", "Black cuckoo",
    "Black magpie", "Black chickadee", "Black ferret", "prairie dog",
    "Blandings turtle", "Blue grosbeak", "Blue jay", "Bluegill",
    "Blue-winged teal", "Bobcat", "Bobolink", "Box turtle",
    "Brewer's sparrow", "Brook trout", "Brown trout",
    "Botaurus lentiginousus", "Nicrophorus americanus", "Corvus brachyrhynchos",
    "Carduelis tristis", "Falco peregrinus", "Anas americana", "Atrytone arogos",
    "Taxidea taxus", "Ammodramus bairdii", "Haliaeetus leucocephalus",
    "Castor canadensis", "Chlorochroa belfragii", "Vireo bellii", "Ceryle alcyon",
    "Bison bison", "Ameiurus melas", "Chlidonias niger", "Picoides arcticus",
    "Cuccyzus erythropthalmus", "Pica hudsonia", "Poecile atricapilla",
    "Mustela nigripes", "Cynomys ludovicianus", "Emydoidea blandingii",
    "Guiraca caerulea", "Cyanocitta cristata", "Lepomis macrochirus",
    "Anas discors", "Felis rufus", "Dolichonys oryzivorus", "Terrapene ornata",
    "Spizella brewi", "Salvelinus fontinalis", "Salmo trutta"
    "Bull snake", "Bullfrog", "Bullock's oriole", "Bumble bees", "Burrowing owl",
    "Bighorn sheep", "Canada goose", "Red Cardinal", "Channel catfish",
    "Chestnut longspur", "Chorus frog", "Clarks nutcracker", "Clay-colored sparrow",
    "Common loon", "Cooper's hawk", "Common Cottontail", "Gray Coyote",
    "Dakota skipper", "Dickcissel", "Downy woodpecker", "Dwarf shrew",
    "Eastern bluebird", "Eastern screechowl", "Eastern pewee",
    "Fathead minnow", "Ferruginous hawk", "field sparrow", "Finscale dace",
    "Flathead chub", "Fox sparrow", "Fox squirrel", "ground squirrel",
    "Fringed myotis",
    "Pituophis sayi", "Rana catesbeiana", "Icterus bullocki", "Speotyto cunicularia",
    "Ovis canadensis californiana", "Branta canadensis", "Cardinalis cardinalis",
    "Ictalurus punctatus", "Calcrius ornatus", "Nucifraga columbiana",
    "Spizella pallida", "Gavia immer", "Accipiter cooperi", "Canis latrans",
    "Hesperia dacotae", "Spiza americana", "Picoides pubescens", "Sorex nanus",
    "Sialia sialis", "Otus asio", "Contopus virens", "Cervus elaphus",
    "Pimephales promelas", "Buteo regalis", "Spizella pusilla", "Phoxinus neogaeus",
    "Platygobio gracilis", "Passerella iliaca", "Sciurus niger", "Spermophilus franklinii",
    "Myotis thysanodes",
    "Garter snake", "Golden eagle", "Goshawk", "Grasshopper sparrow",
    "Gray catbird", "Gray fox", "Gray partridge", "Gray squirrel",
    "Great heron", "Crested flycatcher", "Prairie chicken", "Green teal",
    "Ground squirrel", "Hairy woodpecker", "Hispid mouse", "Hognose snake",
    "Horned lark", "House wren", "Iowa darter", "Jack rabbit",
    "Large-mouthed bass", "Lark bunting", "Lark sparrow", "Lazuli bunting",
    "Least flycatcher", "Least weasel", "LeConte's sparrow", "Lewis woodpecker",
    "Loggerhead shrike", "Long-billed curlew", "Long-eared owl", "Longnose dace",
    "Longnose sucker", "Long-tailed weasel", "Marbled godwit", "Marsh wren",
    "McCown's longspur", "Meadow lark", "Milk snake",
    "Anas strepera", "Thamnophis radix", "Aquila chrysaetos", "Accipiter gentilis",
    "Ammodramus savannarum", "Dumetella carolinensis", "Urocyon cinereoargenteus",
    "Perdix perdix", "Sciurus carolinensis", "Ardea herodias", "Bubo virginianus",
    "Myiarchus crinitus", "Tympanuchus cupido pinnatus", "Anas crecca",
    "Picoides villosus", "Chaetodipus hispidus", "Heterodon nasicus",
    "Eremophila alpestris", "Equus caballus", "Troglodytes aedon", "Etheostama exile",
    "Lepus townsendii", "Micropterus salmoides", "Calamospiza melanocorys",
    "Chondestes grammacus", "Passerina amoena", "Empidonax minimus",
    "Mustela nivalis", "Ammodramus belconteii", "Melanerpes lewis", "Lanius ludovicianus",
    "Numenius americanus", "Asio otus", "Rhinichthys cataractae",
    "Catostomus catostomus", "Mustela frenata", "Anas platyrhyncos", "Limosa fedoa",
    "Cistothorus palustris", "Calcarius mccownii", "Falco columbarius",
    "Lampropeltis triangulum", "Mustela vison",
    "Buteo jamaiicensis", "Spyeria idalia", "Spermophilus richardsonii", "Phasianus colchicus",
    "Lantra canadensis", "Ovis canadensis canadensis", "Archilochus colubris",
    "Pipilo erythrophthalmus", "Centrocerus urophasianus", "Amphispiza belli",
    "Oreoscoptes montanus", "Lagurus curtatus", "Notropis stramineus",
    "Passerculus sandwichensis", "Piranga ludoviciana", "Cistothorus platensis",
    "Accipiter striatus", "Tympanuchus phasianellus jamesi", "Ammodramus nelsoni",
    "Asio flammeus", "Maxostoma macrolepidotum", "Anas clypeata", "Trionyx spinifer",
    "Euderma maculatum", "Anthus spragueii", "Noturus flavus", "Mephitus mephitus",
    "Macrohybopsis gelida", "Piranga rubra", "Buteo swainsoni", "Vulpes velox",
    "Spermophilus tridecemlineatus", "Ambrystoma tigrinum", "Notropis topeka",
    "Corynorhinus townsendii", "Cygnus buccinator", "Cathartes aura",
    "Bartramia longicauda", "Pooecetes gramineus", "Vireo gilous",
    "Plecotus townsendii", "Speotyto cunicularia", "Otus kennicottii",
    "Liochlorophis vernalis", "Piranga ludoviciana",
    "Catostomus commersoni", "Sitta carolinensis", "Plegadis chihi",
    "Arborimus albipes", "Odocoileus virginianus", "Lepus townsendii",
    "Grus americana", "Meleagris gallopavo", "Empidonax trailii",
    "Aix sponsa", "Bufo woodhousii", "Perca flavescens",
    "Dendroica petechia", "Coccyzus americanus", "Icteria virens",
    "Xanthocephalus xanthocephalus", "Vireo flavifrons",
    "Alces alces", "Sialia cursucoides", "Puma concolor", "Charadrius montanus",
    "Zenaida macroura", "Odocoileus hemionus", "Ondatra zibethicus",
    "Haliaeetus leucephalus alascanus", "Colaptes auratus", "Accipiter gentilius",
    "Onychomys leucogaster", "Circus cyaneus", "Rana pipiens", "Icterus bullocki",
    "Esox lucius", "Thomomys talpoides", "Phrynosoma douglasii douglasii",
    "Perognathus fasciatus", "Icterus spurius", "Pandion haliaetus", "Hesperia ottoe",
    "Sciurus aurocapiilus", "Lampropeltis triangulum", "Scaphirhynchus albus",
    "Semotilus margarita", "Falco peregrinus", "Anas acuta", "Reithrodeontomys montanus",
    "Perognathus flavescens", "Spea bombifrons", "Spilogale putorius interrupta",
    "Fundulus sciadicus", "Erithizon dorsalis", "Oarisma powesheik", "Falco mexicanus",
    "Crotalus viridis viridis", "Eumeces septentrionalis", "Microtus ochrogaster",
    "Antilocapra americana", "Sitta pygmaea", "Procyon lotor", "Loxia curvirostra",
    "Vulpes vulpes", "Notropis lutrensis", "Sitta canadensis", "Melanerpes erythrocephalus"
    "Mountain Bluebird", "Mountain Lion", "Mountain Plover", "Mourning Dove",
    "Mule Deer", "Musk rat", "Northern Eagle", "Northern Flicker", "Northern Goshawk",
    "Northern Mouse", "Northern Harrier", "Northern Frog", "Northern Oriole", "Northern Pike",
    "Northern Gopher", "Pocket Mouse", "Orchard Oriole", "Olive Osprey",
    "Milk Snake", "Pallid Sturgeon", "Pearl Dace", "Peregrine Falcon",
    "Harvest Mouse", "Pocket Mouse", "Plains Spadefoot", "Spotted Skunk",
    "Plains Topminnow", "Prairie Falcon", "Prairie Rattlesnake", "Prairie Skink",
    "Prairie Vole", "Pygmy Nuthatch", "Raccoon Raccoon", "Red Crossbill", "Red Fox",
    "Red Shiner", "Red Nuthatch", "Red Woodpecker",
    "Garter Snake", "Golden Eagle", "Grasshopper Sparrow", "Gray Catbird", "Gray Fox",
    "Gray Partridge", "Gray Squirrel", "Great Heron", "Great Owl", "Prairie Chicken",
    "Green Teal", "Ground Squirrel", "Hairy Woodpecker", "Hispid Mouse", "Hognose Snake",
    "Horned Lark", "House Wren", "Iowa Darter", "Jack Rabbit", "Mouthed Bass",
    "Lark Bunting", "Lark Sparrow", "Lazuli Bunting", "Least Flycatcher", "Least Weasel",
    "LeConte Sparrow", "Lewis Woodpecker", "Loggerhead Shrike", "Long Curlew", "Long Owl",
    "Longnose Dace", "Longnose Sucker", "Long Weasel", "Marbled Godwit", "Marsh Wren",
    "McCown Longspur", "Milk Snake",
#]))


    # Landmarks
#landmarks == list(set([
    "Arlington Cemetery", "Blue Mosque", "Bondi Beach", "Brandenburg Gate", "Carcassonne City",
    "Christ Redeemer", "Diamond Head", "Eiffel Tower", "Golden Gate", "Grand Bazaar", "Grand Canyon",
    "Great Barrier", "Harbour Bridge", "Metropolitan Museum", "Michael's Mount", "Mount Kilimanjaro",
    "Mount Rushmore", "Opera House", "Petra Jordan", "Sacred Heart", "Sigiriya Rock", "Sistine Chapel",
    "Space Needle", "Stonehenge Monument", "Terracotta Army", "Trevi Fountain", "Twelve Apostles",
    "World Trade", "Potala Palace", "Alcatraz Island", "Angkor Wat", "Arc Triomphe", "Banff National",
    "Barrier Reef", "Buckingham Palace", "Central Park", "Chrysler Building", "Cloud Gate",
    "Delicate Arch", "Easter Island", "Eden Project", "Ellis Island", "Empire State", "Everglades Park",
    "Forbidden City", "Great Wall", "Hollywood Sign", "Hoover Dam", "Las Vegas", "Machu Picchu",
    "Louvre Museum", "Mount Everest", "Mount Rainier", "Neuschwanstein Castle", "Pearl Harbor",
    "Pisa Tower", "Red Square", "Saint Michel", "Statue Liberty", "Table Mountain", "Taj Mahal",
    "Times Square", "Uluru Rock", "Versailles Palace", "Victoria Falls", "Volcanoes Park",
    "Washington Monument", "White House", "Yellowstone Park", "Yosemite Park",
#]))

#locations = list(set([
    "New York", "Los Angeles", "Chicago Illinois", "Houston Texas", "Phoenix Arizona",
    "Philadelphia Pennsylvania", "San Antonio", "San Diego", "Dallas Texas", "San Jose",
    "Austin Texas", "Jacksonville Florida", "Fort Worth", "Columbus Ohio", "Indianapolis Indiana",
    "Charlotte North Carolina", "San Francisco", "Seattle Washington", "Denver Colorado", "Washington DC",
    "Boston Massachusetts", "El Paso", "Detroit Michigan", "Nashville Tennessee", "Memphis Tennessee",
    "Portland Oregon", "Oklahoma City", "Las Vegas", "Louisville Kentucky", "Baltimore Maryland",
    "Milwaukee Wisconsin", "Albuquerque New Mexico", "Tucson Arizona", "Fresno California", "Sacramento California",
    "Kansas City", "Mesa Arizona", "Atlanta Georgia", "Omaha Nebraska", "Miami Florida",
    "Paris France", "London England", "Berlin Brandenburg", "Madrid Spain", "Rome Lazio",
    "Tokyo Japan", "Beijing China", "Moscow Russia", "South Wales", "Rio Brazil", "Sydney Australia",
    "Cape Town", "Mexico City", "Buenos Aires", "Sao Paulo", "Cairo Egypt",
    "Istanbul Turkey", "Bangkok Thailand", "Seoul Korea",
    "Toronto Canada", "Vancouver Canada", "Mumbai India", "Delhi India", "Hong Kong",
    "Jakarta Indonesia", "Lagos Nigeria", "Karachi Pakistan", "Lima Peru",
    "Bogota Colombia", "Dhaka Bangladesh", "Manila Philippines", "Kuala Lumpur",
    "Tehran Iran", "Warsaw Masovia", "Budapest Hungary", "Prague Bohemia",
    "Vienna Austria", "Zurich Switzerland", "Brussels Belgium", "Lisbon Portugal",
    "Athens Attica", "Oslo Norway", "Stockholm Stockholm", "Copenhagen Zealand",
    "Helsinki Uusimaa", "Dublin Ireland", "Edinburgh Scotland", "Glasgow Scotland", "Manchester England",
    "Birmingham England", "Munich Bavaria", "Amsterdam North Holland", "Barcelona Catalonia",
    "Milan Lombardy", "Venice Italy",
#]))

    # Movie/Game/Book titles

#    movies = list(set([
    "Inception Dream", "Titanic Voyage", "Gladiator Arena", "Avatar World", "Frozen Heart",
    "Jaws Shark", "Rocky Balboa", "Gravity Force", "Skyfall Mission", "Interstellar Journey",
    "Incredible Heroes", "Up Adventure", "Coco Spirit", "Moana Ocean", "Shrek Ogre",
    "Memento Memory", "Casino Royale", "Speed Racer", "Twilight Saga", "Batman Begins",
    "Tangled Rapunzel", "Braveheart Warrior", "Alien Covenant", "Predator Hunt", "Zootopia City",
    "Psycho Thriller", "Shining Horror", "Drive Fast", "Kick Ass", "Whiplash Beat",
    "Rush Race", "Heat Intense", "Hancock Superhero", "Pulp Fiction", "Clueless Teen",
    "Ghostbusters Team", "Aladdin Genie", "Brave Adventure", "Cars Speed", "Jumanji Game",
    "Se7en Sins", "Spectre Bond", "Superman Returns", "Thor Ragnarok", "Ironman Hero",
    "Gremlin Chaos", "Vertigo Twist", "Terminator Future", "Godfather Legacy", "Divergent Path",
    "Minion Madness", "Notting Hill", "Road House", "Hercules Strength", "Aqua Man",
    "Dracula Blood", "Chinatown Mystery", "Goodfellas Mafia", "Bride War", "Mulan Warrior",
    "Madagascar Escape", "Hulk Smash", "Cinderella Story", "Deadpool Mercenary", "Robocop Future",
    "Watchmen Vigilante", "Zombie Land", "Side Ways", "Manhattan Tale", "Carrie Horror",
    "Blade Runner", "Chocolat Romance", "Elysium Future", "Warcraft Battle", "Birdman Fly",
    "Mega Mind", "Godzilla Attack", "Finding Nemo", "Coraline Adventure", "Lego Movie",
    "Pacific Rim", "Beetle Juice", "Django Unchained", "Avatar Return", "Speed Demon",
    "War Craft", "Interstellar Voyage", "Thor God", "Matrix Reloaded", "Moon Light",
    "Black Panther", "Great Escape", "True Grit", "Blade Runner", "Little Women",
    "Jungle Book", "Blue Lagoon", "Wild West", "Silent Hill", "White House", "Independence Day",
#    ]))

#    games = list(set([
    "Super Mario", "Legend Zelda", "Final Fantasy", "Metal Gear", "Minecraft Dungeons",
    "Halo Infinite", "Call Duty", "Red Dead", "Grand Theft", "Assassin Creed",
    "Fortnite Battle", "Over watch", "Dark Souls", "Skyrim Elder", "Splinter Cell",
    "Half Life", "Portal Portal", "Street Fighter", "Mortal Kombat", "Resident Evil",
    "Doom Eternal", "Star craft", "Sonic Hedgehog", "Gears War", "Battle field",
    "Border lands", "Kingdom Hearts", "Fallout New", "Tomb Raider", "Destiny Forever",
    "Mass Effect", "Pac Man", "Civilization Infinite", "Geralt Rivia", "Butcher Blaviken",
    "Dead Space", "Fire Emblem", "Diablo Again", "Bayo netta", "Spla toon",
    "Mario Kart", "FIFA Soccer", "Rocket League", "Monster Hunter", "Far Cry",
    "Watch Dogs", "Star Wars", "Team Fortress", "Golden Eye", "Pikmin Bloom",
    "Banjo Kazooie", "Kirby Star", "War craft", "Animal Crossing", "League Legends",
    "Donkey Kong", "Command Conquer", "Zelda Breath", "Super Smash", "Ninja Gaiden",
    "Little Big", "Beyond Good", "Soul Calibur", "Stardew Valley", "Blood borne",
    "Persona Five", "Fort nite", "League Legends", "Counter Strike",
    "Metroid Prime", "Star Wars", "Mass Effect", "Splinter Cell", "Ratchet Clank",
    "Tony Hawk", "World Warcraft", "Final Fantasy", "Battle toads", "BioShock Infinite",
    "Street Fighter", "Guitar Hero", "Dance Revolution", "Hearth stone", "Mega Man",
#   ]))


# books = list(set([
    "Harry Potter", "Lord Rings", "Game Thrones", "Great Gatsby", "Catch Mockingbird",
    "1984 Orwell", "To Kill", "Pride Prejudice", "Hobbit Adventure", "Da Vinci",
    "Moby Dick", "Jane Eyre", "Frankenstein Shelley", "Alice Wonderland", "Dracula Vampire",
    "Fahrenheit 451", "Brave New", "Grapes Wrath", "Sherlock Holmes", "War Peace",
    "Catch-22 Heller", "Little Women", "Call Wild", "Chronicles Narnia", "Wuthering Heights",
    "Count Monte", "Slaughterhouse-Five", "Dune Arakis", "Portrait Artist", "Sense Sensibility",
    "Color Purple", "Animal Farm", "Chronicle Death", "Siddhartha Hermann",
    "Great Expectations", "Handmaid Tale", "One Flew", "Outsider King", "Gone Wind",
    "Catcher Rye", "Mists Avalon",
    "Ready Player", "Giver Giver", "Bridges Madison", "Silent Patient", "Alchemist Scientist",
    "Princess Bride", "Watership Down", "Silence Lambs", "Atlas Shrugged", "Gunslinger Dark",
    "Shining Axeman", "Civil War", "Invisible Man", "Educated Memoir", "Lovely Bones",
    "Good Earth", "Handmaid Tale", "Death Salesman", "Olive Kitteridge", "Ender Game",
    "Wrinkle Time", "Tale Two", "Goldfinch Tartt", "Unbearable Lightness", "Atlas Shrugged",
    "Grapes Wrath", "Pillars Earth", "Secret History", "Glass Castle", "Divine Comedy",
    "Cloud Atlas", "Three Musketeers", "Heart Darkness", "Wind Willows", "Counte Cristo",
    "Anna Karenina", "Moon Palace", "Pride Prejudice", "Wheel Time", "Sense Sensibility",
    "Portrait Lady", "Tale Cities", "Water Elephants", "Life Pi", "Night Circus"
#   ]))
]

if __name__ == "__main__":
    main()
