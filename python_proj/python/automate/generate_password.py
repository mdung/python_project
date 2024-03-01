import secrets
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = string.ascii_lowercase

    if include_uppercase:
        characters += string.ascii_uppercase

    if include_digits:
        characters += string.digits

    if include_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        print("Error: No character set selected. Please include at least one character set.")
        return None

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Customize the criteria as needed
    password_length = 16
    include_uppercase = True
    include_digits = True
    include_special_chars = True

    generated_password = generate_password(
        length=password_length,
        include_uppercase=include_uppercase,
        include_digits=include_digits,
        include_special_chars=include_special_chars
    )

    if generated_password:
        print("Generated Password:", generated_password)
