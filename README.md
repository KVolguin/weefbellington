# Weef Bellington
#### Video Demo: (https://youtu.be/ZIjyKQLSU98)

## Description:

### Abstract
    This project generates plausible Star Wars names by taking the first two letters of any two-word phrases
    and switching them with each other. For example taking the phrase "Cloud Storage" would turn into "Stoud Clorage".

    This program was inspired by a reddit post I saw here:
    https://www.reddit.com/r/OTMemes/comments/196ghjm/wuffalo_bings/
    Original BlueSky post here:
    https://bsky.app/profile/ogfattcatt.bsky.social/post/3kiwfjsxzkk25


### Runtime Behavior
    At its simplest, the program will always ask the user for the next step; navigate through menus based on inputs.
    Core modes take any input and switch the first two letters of each word, generating the "Star Wars" name.
    However, I've implemented more modes and features, which can be turned on or changed during runtime.
    The list of features I'd like to include are included in the Wishlist below.
    Typical usage would be that once the program is started, you're met with the main menu and continue on from there. The menu and elaborations are described below.
    I've found myself gravitating towards Generate Mode the most, saving favorites, then exporting them in Export mode;
    I also like changing options and playing with Input mode.


### Menu (DONE)
    At run time, the user would be met with a menu to chose which "mode" they'd like to use. The options so far would include:
    1. Generate Mode
    2. Input Mode
    3. Inspiration Guide
    4. Export Mode
    5. Import List
    6. Options
    7. About, Help
    8. Exit (WILL ERASE PROGRESS IF NO EXPORT MADE)

### Generate Mode (DONE)
    It picks from a vast swath of 2-word phrases compiled by yours truly and randomly selects one. "Seed" names could include food items, common phrases, quotes, and existing names.
    Upon selecting this mode, it would continue asking the user whether to generate another name until the user exits the mode with a command like "EXIT".
    You can also

### Input Mode (DONE)
    Ask the user for 2 words to switch around instead of generating from a list.

### Inspiration Mode (DONE)
    Provide a category with examples to inspire the user to find 2 word phrases from. Categories are provided 1 at a time so user has to actually consider each suggestion for a moment.
    Will probably include: Inspirational Quotes, Movie Names, Landmarks, Real Names, Food Dishes, Book Titles, Species names, etc.

### Export (DONE)
    When the user hits export, it will immediately provide a small section of text detailing the current output settings. Settings can be changed by going back to the main menu and changing options for export.

### Options(DONE)
    Various options for generation, export settings, and anything else that can be changed will be available here. The Wishlist below expands on the options in further detail.

### About/Help(DONE)
    Prints out the help guide options in a sub-menu. Choosing a sub-menu item prints out the directions for use of that module along with any further detail of usage.

### Exit(DONE)
    Exits the program, but before doing so, asks the user whether they wish to export their work before closing, as all generated names will be deleted.

## Wishlist of Features (Can turn on/off in Options)

#### Apostrophe in Names (On by default) (DONE)
    Outputs can also be changed based on the presence of vowels at the beginning of switched phrases. For example, the phrase "Never Stop" would get turned into "Stver Neop" at first.
    The vowel detection would automatically change it to "St'ver Neop" to provide the needed "invisible vowel". It should also be applied to any names that end up with 2+ vowels in a row.
    For example, "Hunting Boaring" would turn into "Bonting Huaring", which would then become "Bonting Hu'aring". Can turn on and off during Generate or Input mode by typing single character "'"

#### Letter ending cutoff (1 by default) (DONE)
    Allow a predetermined amount of letter cutoff at the end of a word to make it less obvious where the original word came from.
    Helps remove familiar endings of words if not included in the suffix list, and in general dissociates from the original language.
    This also helps modify the ending of the word, as the beginning is changed by the letter switch.

#### Suffix removal(DONE)
    Phrases like "Potato Chip" sound obvious when you transform them into "Ch'tato Piop". Or words like "flying"; ing will be left in the left over of one word.
    This feature removes common suffixes from a list and makes the resulting names more dissociated from the original language.

#### Letter Switch length (2 by default) (DONE)
    Decide how many letters get switched from the beginning of each word. Default is 2. Any number is possible, but not recommendable beyond 3 or maybe 4.

#### Letter Switch L/R Split (DONE)
    Make it so that user can change the switch length for each word individually.
    Ex: first word = 1 switched letter, second word 2 switched letters

#### Vowel Insertion (On by default) (DONE)
    In the case that absolutely no vowels are available once a switch is complete, an extra vowel will be added. For instance "Store List" turns into "Liore Stst";
    by adding a vowel to "Stst" you can get various names like "Stost, Stist, Styst, Stest, Stast" instead.

#### Import a list (DONE)
    Allow the user to import their own list and turn all items on the list into Star Wars names based on the given settings.

#### Export settings (DONE)
    Allow currently compiled list be exported into terminal, as a CSV file, .txt file, as a list, or PDF.

#### Generate Portrait (Not Implemented)
    Connect to LLM API that generates a portrait with a file name and metadata that matches the output from the program

#### Generated List (DONE)
    Allow users to output all names generated in current runtime session in preferred output.

#### Favorites (DONE)
    Allow users to "star" their favorite outputs, which can be output as a seperate list from the regular "Store List" output. If a subsequent input is just a single "*" character, it will attempt to append the last output in the "favorites" list.
