import random
import string
import pyinputplus as pyip

# 📝 Plan of Action:
# 1️⃣ Get user preferences:
#      - password length
#      - include uppercase
#      - include special chars
#      - include digits
# 2️⃣ Build character sets
# 3️⃣ Ensure at least one of each selected type
# 4️⃣ Fill remaining characters randomly
# 5️⃣ Shuffle and create password
# 6️⃣ Display the password

def generate_password():
    print("\n🔐 Password Generator 🔐")

    # 🎯 Get valid password length (≥4)
    length = pyip.inputInt(
        prompt='Enter the desired password length (min 4): ',
        min=4
    )

    # ✅ Ask yes/no for character types
    include_uppercase = pyip.inputYesNo('Include uppercase letters? (yes/no): ')
    include_special = pyip.inputYesNo('Include special characters? (yes/no): ')
    include_digits = pyip.inputYesNo('Include digits? (yes/no): ')

    # 🅰️ Build character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == 'yes' else ''
    special = string.punctuation if include_special == 'yes' else ''
    digits = string.digits if include_digits == 'yes' else ''
    all_characters = lowercase + uppercase + special + digits

    # ⚡ Ensure at least one of each selected type
    required_characters = []
    if include_uppercase == 'yes':
        required_characters.append(random.choice(uppercase))
    if include_special == 'yes':
        required_characters.append(random.choice(special))
    if include_digits == 'yes':
        required_characters.append(random.choice(digits))

    # 🔄 Fill remaining characters
    remaining_length = length - len(required_characters)
    password_chars = required_characters + [random.choice(all_characters) for _ in range(remaining_length)]

    # 🔀 Shuffle for randomness
    random.shuffle(password_chars)

    # 🏁 Create final password
    password = ''.join(password_chars)
    print(f"\n✅ Generated Password: {password}\n")

# ▶️ Run the generator
if __name__ == "__main__":
    generate_password()
