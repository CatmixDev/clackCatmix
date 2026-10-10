import itertools
import os
import sys

# ANSI color codes for styling
RED = "\033[1;31m"          # Red for the logo logo
BRIGHT_RED = "\033[1;91m"   # Bright red for the eyes
WHITE = "\033[1;37m"        # White for main text
CYAN = "\033[1;36m"         # Cyan for parameters
RESET = "\033[0m"           # Reset color

# Dictionary of popular names and their short/diminutive derivatives
NAME_DERIVATIVES = {
    "alexander": ["sasha", "sanya", "sanek", "alex", "aleks", "shurik", "aleksandr", "alexandr"],
    "alexandr": ["sasha", "sanya", "sanek", "alex", "aleks", "shurik", "alexander"],
    "александр": ["sasha", "sanya", "sanek", "alex", "aleks", "shurik", "aleksandr", "alexandr"],
    "alexey": ["lesha", "lyoha", "alex", "aleks", "alexeich"],
    "алексей": ["lesha", "lyoha", "alex", "aleks", "alexeich"],
    "ivan": ["vanya", "vanyek", "vanya777"],
    "иван": ["vanya", "vanyek", "ivan", "vanya777"],
    "dmitry": ["dima", "dimon", "dimas", "mitya"],
    "дмитрий": ["dima", "dimon", "dimas", "mitya"],
    "sergey": ["serega", "serg", "serzh"],
    "сергей": ["serega", "serg", "sergey", "serzh"],
    "vladimir": ["vova", "vovan", "vovchik", "volodya", "vlad"],
    "владимир": ["vova", "vovan", "vovchik", "volodya", "vlad"],
    "andrew": ["andryuha", "andrey", "andy"],
    "андрей": ["andryuha", "andrey", "andy"],
    "artem": ["tema", "temych"],
    "артем": ["tema", "temych", "artem"],
    "nicholas": ["kolya", "kolyan", "nikolas", "nick"],
    "николай": ["kolya", "kolyan", "nikolas", "nick"],
    "michael": ["misha", "mishanya", "miha"],
    "михаил": ["misha", "mishanya", "miha", "michael"],
}

def print_logo():
    """Prints the Arch-Catmix logo and ASCII title."""
    os.system("cls" if os.name == "nt" else "clear")
    logo_lines = [
        (r"    .o+             ", "", ""),
        (r"   ooo/             ", "", ""),
        (r"  +oooo:            ", "", ""),
        (r" +oooooo:           ", "", ""),
        (r"-+oooooo+:          ", "", ""),
        (r"/:-:++oooo+:        ", "", ""),
        (r"/++++/+++++++:      ", "", ""),
        (r"/++++/_", r"/ \ ", r"_+++++: "),
        (r"/+++o/", r"", r"\ooo/     "),
        (r"./oooss|", r"\/", r"|sso+     "),
        (r".oossssso\____/ssss+", "", ""),
        (r"-osssssso.    :ssssssso.", "", ""),
        (r":osssssss/    osssso+++.", "", ""),
        (r"/osssssshu/   +ssssooo/-", "", ""),
        (r"/ossssso+/:-  -:/+osssso+-", "", ""),
        (r"+sso+:-           .-/+oso:", "", ""),
        (r"++:.                -/+/    ", "", ""),
        (r".                      /    ", "", ""),
    ]
    print()
    for left, eyes, right in logo_lines:
        if eyes:
            print(f"{RED}{left}{BRIGHT_RED}{eyes}{RED}{right}{RESET}")
        else:
            print(f"{RED}{left}{RESET}")
            
    # ASCII Art Title
    print(f"\n{WHITE}")
    print(r"  ____   _         _     ____  _  __    ____     _     _____  __  __  ___ __  __ ")
    print(r" / ___| | |       / \   / ___|| |/ /   / ___|   / \   |_   _||  \/  ||_ _|\ \/ / ")
    print(r"| |     | |      / _ \ | |    | ' /   | |      / _ \    | |  | |\/| | | |  \  /  ")
    print(r"| |___  | |___  / ___ \| |___ | . \   | |___  / ___ \   | |  | |  | | | |  /  \  ")
    print(r" \____| |_____|/_/   \_\\____||_|\_\   \____|/_/   \_\  |_|  |_|  |_||___|/_/\_\ ")
    print(f"{RESET}\n")

def transliterate(text):
    """Transliterates Russian Cyrillic characters into Latin equivalents."""
    cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    latin = ["a", "b", "v", "g", "d", "e", "yo", "zh", "z", "i", "y", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh", "shch", "", "y", "", "e", "yu", "ya"]
    tr_dict = dict(zip(cyrillic, latin))
    text = text.lower()
    return "".join(tr_dict.get(char, char) for char in text)

def get_case_mutations(word):
    """Generates all possible case combinations for a word."""
    if not word or word.isdigit():
        return {word}
    return {"".join(x) for x in itertools.product(*((c.lower(), c.upper()) for c in word))}

def get_leet_mutations(word):
    """Replaces characters with leetspeak symbols and numbers."""
    leet_dict = {
        'a': ['4', '@', 'A'],
        'e': ['3', 'E'],
        'i': ['1', '!', 'I'],
        'o': ['0', 'O'],
        's': ['5', '$', 'S'],
        't': ['7', 'T'],
        'b': ['8', 'B'],
        'g': ['9', 'G']
    }
    word = word.lower()
    char_options = []
    for char in word:
        if char in leet_dict:
            char_options.append([char] + leet_dict[char])
        else:
            char_options.append([char])
    return {"".join(x) for x in itertools.product(*char_options)}

def generate_years():
    """Generates a set of modern 4-digit and 2-digit years."""
    years = []
    for y in range(1950, 2027):
        years.append(str(y))
        years.append(str(y)[2:])
    return set(years)

def main():
    print_logo()
    print(f"{WHITE}=== TARGET DATA INPUT FOR DICTIONARY GENERATION ==={RESET}")
    print("Fill in the fields you know (press Enter to skip if unknown):\n")
    
    first_name = input("First Name (e.g., alexander / ivan): ").strip()
    last_name = input("Last Name (e.g., petrov): ").strip()
    nickname = input("Nickname (e.g., vanya777 / sanek): ").strip()
    pet = input("Pet's name: ").strip()
    words_input = input("Other keywords separated by space (city, car model): ").strip().split()
    
    birth_date = input("Birth date (DD.MM.YYYY): ").strip().replace(".", "").replace("/", "")
    
    # Processing raw input and names derivatives
    raw_inputs = [first_name, last_name, nickname, pet] + words_input
    all_raw_words = set()

    for word in raw_inputs:
        if not word:
            continue
        word_lower = word.lower()
        
        # Add basic input and its transliteration
        all_raw_words.add(word_lower)
        all_raw_words.add(transliterate(word_lower))
        
        # Cross-check in the derivatives database
        if word_lower in NAME_DERIVATIVES:
            all_raw_words.update(NAME_DERIVATIVES[word_lower])
            
        for key, derivatives in NAME_DERIVATIVES.items():
            if word_lower in derivatives or word_lower == key:
                all_raw_words.update(derivatives)
                all_raw_words.add(key)

    # Basic data pools
    text_pool = set()
    numbers_pool = set()
    
    print(f"\n{RED}[+]{RESET} Starting word mutation (Cases + Leetspeak)...")
    for word in all_raw_words:
        cases = get_case_mutations(word)
        text_pool.update(cases)
        for c in cases:
            text_pool.update(get_leet_mutations(c))
            
    print(f"{RED}[+]{RESET} Gathering numeric combinations and generating years...")
    text_pool.update(generate_years())
    
    if len(birth_date) == 8 and birth_date.isdigit():
        d, m, y = birth_date[:2], birth_date[2:4], birth_date[4:]
        numbers_pool.update([d, m, y, y[2:], d+m, m+d, d+m+y, d+m+y[2:]])
        
    popular_tails = ["", "1", "12", "123", "1234", "12345", "777", "666", "999", "2024", "2025", "2026"]
    specials = ["", "!", "@", "#", "$", "?", "_", "-", "!!", "!!!"]
    numbers_pool.update(popular_tails)
    
    text_pool = {x for x in text_pool if x}
    numbers_pool = {x for x in numbers_pool if x}
    
    output_file = input(f"\nOutput file name (Enter for {CYAN}mega_dict.txt{RESET}): ").strip()
    if not output_file:
        output_file = "mega_dict.txt"
        
    print(f"\n{RED}[+]{RESET} Deep combinations processing. Please wait...")
    
    try:
        count = 0
        with open(output_file, "w", encoding="utf-8") as f:
            
            for t in text_pool:
                for n in numbers_pool:
                    for s in specials:
                        f.write(f"{t}{n}{s}\n")
                        f.write(f"{t}{s}{n}\n")
                        f.write(f"{s}{t}{n}\n")
                        f.write(f"{n}{t}{s}\n")
                        count += 4
                        
            
            if len(text_pool) > 1:
                for t1, t2 in itertools.permutations(text_pool, 2):
                    if len(t1) + len(t2) > 22:  
                        continue
                    for n in ["", "1", "123", "777"]:
                        for s in ["", "!", "@"]:
                            f.write(f"{t1}{t2}{n}{s}\n")
                            f.write(f"{t1}_{t2}{n}{s}\n")
                            f.write(f"{t1}{s}{t2}{n}\n")
                            count += 3
                            
        print(f"\n{RED}[DONE]{RESET} Generation completed successfully!")
        print(f"Total unique variations recorded: {CYAN}{count:,}{RESET}")
        print(f"Dictionary saved to: {os.path.abspath(output_file)}")
        
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Process interrupted by user.{RESET} Lines written so far: {count:,}")
    except Exception as e:
        print(f"\n{RED}[!] Error writing to file:{RESET} {e}")

if __name__ == "__main__":
    main()
