def caesar(text, shift):
    out = []
    for ch in text:
        o = ord(ch)
        if 65 <= o <= 90:
            out.append(chr((o - 65 + shift) % 26 + 65))
        elif 97 <= o <= 122:
            out.append(chr((o - 97 + shift) % 26 + 97))
        else:
            out.append(ch)
    return ''.join(out)

LOCK_ART = r"""
          .--.
         /    \
        |      |
        |      |
      +----------+
      |          |
      |   .--.   |
      |   |  |   |
      |   |__|   |
      |    ||    |
      |    ||    |
      |          |
      +----------+
"""

def main():
    print(LOCK_ART)
    print("="*50)
    print(" Text Encrypt / Decrypt - Caesar Cipher")
    print("="*50)
    print("Note:")
    print(" • Maximum shift value is 25")
    print(" • Intended for messages only, not passwords")
    print(" • Caesar Cipher is not secure")
    print("-"*50)
    
    while True:
        print("\nChoose:")
        print("  [e] Encrypt")
        print("  [d] Decrypt")
        print("  [r] Random shift")
        print("  [q] Quit")
        mode = input("> ").strip().lower()
        
        if mode == 'q':
            print("Bye!")
            break
        
        if mode not in ('e', 'd', 'r'):
            print("Invalid choice")
            continue
        
        text = input("\nEnter your message: ")
        print(f"Characters: {len(text)}")
        
        if mode == 'r':
            import random
            shift = random.randint(1, 25)
            print(f"Random shift chosen: {shift}")
            mode = 'e'
        else:
            try:
                shift_input = input("Shift (1-25) [default 2]: ").strip()
                shift = int(shift_input) if shift_input else 2
                if not 1 <= shift <= 25:
                    raise ValueError
            except ValueError:
                print("Shift must be between 1 and 25. Using 2.")
                shift = 2
        
        if mode == 'd':
            shift = -shift
        
        result = caesar(text, shift)
        
        print("\n" + "-"*50)
        print("Result:")
        print(result)
        print("-"*50)
        
        # try to copy to clipboard if available
        try:
            import pyperclip
            pyperclip.copy(result)
            print("(copied to clipboard)")
        except:
            pass

if __name__ == "__main__":
    main()
