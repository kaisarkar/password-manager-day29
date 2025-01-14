import secrets
import string

class PasswordGenerator:
  def __init__(self):
    self.password = ""
    self.generated_passwords = set()

  def generate_random_password(self, length=12):
    """Generates a random password with the specified length using cryptographically secure randomness.

    Args:
      length: The desired length of the password (default: 12).

    Returns:
      A string containing a randomly generated password.
    """

    # Character sets for password generation
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine character sets for diversity
    all_chars = lower + upper + digits + punctuation

    # Create an empty set to store generated passwords

    while True:
      # Generate a random password using secrets.token_urlsafe()
      self.password = ''.join(secrets.choice(all_chars) for _ in range(length))

      # Check if the password is already generated
      if self.password not in self.generated_passwords:
        self.generated_passwords.add(self.password)  # Add to the set to prevent repetition
        return self.password
