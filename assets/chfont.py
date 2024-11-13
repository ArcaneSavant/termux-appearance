# cspell:words ArcaneSavant termux

# Import Necessary Modules
import os
import shutil
import subprocess


# Define Fonts Directory
fonts_dir = os.path.expanduser("~/archives/termux-appearance/assets/fonts")


def find_fonts(directory):
    fonts = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".ttf"):
                fonts.append(os.path.join(root, filename))
    return fonts


# List Fonts & Get User Input
def choose_font():
    fonts = find_fonts(fonts_dir)
    if not fonts:
        print(
            "Looks like there are no font files in",
            fonts_dir,
            "or its subdirectories.",
        )
        return None

    i = 1
    for font in fonts:
        print(f"{i}. {os.path.basename(font)}")
        i += 1

    while True:
        try:
            choice = input("Enter the number of the font to copy (or 'q' to quit): ")
            if choice.lower() == "q":
                print("Exiting...")
                return None
            choice = int(choice)
            if 0 < choice <= len(fonts):
                return fonts[choice - 1]
            else:
                print(
                    f"Hmm, that number seems a bit off. Try entering a number (integer) between 1 and {len(fonts)}."
                )
        except ValueError:
            print("It looks like you didn't enter a number or 'q'. Please try again.")


# Main Program
font_to_copy = choose_font()

# Exit if User Quits
if not font_to_copy:
    exit()

# Set Destination Path
destination = os.path.expanduser("~/.termux/font.ttf")

# Copy the Font File
try:
    shutil.copy(font_to_copy, destination)
    print(
        f"Font '{os.path.basename(font_to_copy)}' has been successfully copied to {destination}."
    )

    # Reload Termux Settings to Apply the New Font
    bash_cmd = "termux-reload-settings"
    subprocess.run(bash_cmd, shell=True, check=True)

except (FileNotFoundError, PermissionError) as e:
    print(f"There was a problem copying the font: {e}.")
