import random
import string

# 📝 Plan of Action:
# 1️⃣ Collect user preferences:
#      - password length
#      - include uppercase letters
#      - include special characters
#      - include digits
# 2️⃣ Build the pool of available characters
# 3️⃣ Ensure at least one of each selected character type
# 4️⃣ Fill remaining characters randomly
# 5️⃣ Shuffle and combine into final password
# 6️⃣ Display the generated password

# 🔑 Generate a random password based on user prefs
def generate_password():
    """Generate a random password based on user preferences."""

    while True:
        # 🎯 Get password length
        try:
            length = int(input('Enter desired password length (minimum 4): ').strip())
            if length < 4:
                print('❌ Password must be at least 4 characters long.\n')
                continue
        except ValueError:
            print('❌ Please enter a valid number.\n')
            continue

        # ✅ Helper for yes/no questions
        def ask_yes_no(prompt):
            while True:
                answer = input(prompt).strip().lower()
                if answer in ('yes', 'no') or answer in ('y', 'n'):
                    return answer
                print('Please enter "yes" or "no".')

        # 📋 Collect user preferences
        include_uppercase = ask_yes_no('Include uppercase letters (yes/no)? ')
        include_special = ask_yes_no('Include special characters (yes/no)? ')
        include_digits = ask_yes_no('Include digits (yes/no)? ')

        # 🅰️ Build character pool
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase if include_uppercase == 'yes' else ''
        special = string.punctuation if include_special == 'yes' else ''
        digits = string.digits if include_digits == 'yes' else ''
        all_characters = lowercase + uppercase + special + digits

        # ⚡ Ensure at least one of each selected type
        required_chars = []
        if include_uppercase == 'yes':
            required_chars.append(random.choice(uppercase))
        if include_special == 'yes':
            required_chars.append(random.choice(special))
        if include_digits == 'yes':
            required_chars.append(random.choice(digits))

        # 🔄 Fill remaining characters
        remaining_length = length - len(required_chars)
        password_chars = required_chars + [random.choice(all_characters) for _ in range(remaining_length)]

        # 🔀 Shuffle to randomize
        random.shuffle(password_chars)
        password = ''.join(password_chars)

        # 🏁 Show generated password
        print(f'\n✅ Generated Password: {password}\n')
        break

# ▶️ Run generator
if __name__ == "__main__":
    generate_password()
