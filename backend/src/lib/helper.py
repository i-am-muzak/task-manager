
import unicodedata
import re

def check_email_provider(email: str) -> bool:
    current_provider = email.split("@")

    if len(current_provider) == 1:
        return False

    if current_provider[-1].split(".")[0] in ["gmail", "yahoo", "yandex", "outlook", "hotmail"]:
        return True

    return False


def spacesToChar(text: str, char: str):
    return text.replace(" ", char)

def create_slug(text):
  # Convert the text to lowercase.
  text = text.lower()

  # Replace all non-ASCII characters with their ASCII equivalents.
  text = unicodedata.normalize("NFKD", text)
  text = text.encode("ascii", "ignore").decode()

  # Replace all spaces with hyphens.
  text = text.replace(" ", "-")

  # Remove all characters that are not alphanumeric or hyphens.
  text = re.sub(r"[^\w\-]", "", text)

  # Return the slug.
  return text