# cspell:words ArcaneSavant termux

# Import Necessary Modules
import os
import shutil
import subprocess


# Define Color Schemes Directory
colors_dir = os.path.expanduser("~/archives/termux-appearance/assets/colors")


def find_colors(directory):
    colors = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".properties"):
                colors.append(os.path.join(root, filename))
    return colors


# List Color Schemes & Get User Input
def choose_color():
    colors = find_colors(colors_dir)
    if not colors:
        print(
            "Looks like there are no color scheme files in",
            colors_dir,
            "or its subdirectories.",
        )
        return None

    i = 1
    for color in colors:
        print(f"{i}. {os.path.basename(color)}")
        i += 1

    while True:
        try:
            choice = input(
                "Enter the number of the color scheme to copy (or 'q' to quit): "
            )
            if choice.lower() == "q":
                print("Exiting...")
                return None
            choice = int(choice)
            if 0 < choice <= len(colors):
                return colors[choice - 1]
            else:
                print(
                    f"Hmm, that number seems a bit off. Try entering a number (integer) between 1 and {len(colors)}."
                )
        except ValueError:
            print("It looks like you didn't enter a number or 'q'. Please try again.")


# Main Program
color_to_copy = choose_color()

# Exit if User Quits
if not color_to_copy:
    exit()

# Set Destination Path
destination = os.path.expanduser("~/.termux/colors.properties")

# Copy the Color Scheme File
try:
    shutil.copy(color_to_copy, destination)
    print(
        f"Color Scheme '{os.path.basename(color_to_copy)}' has been successfully copied to {destination}."
    )

    # Reload Termux Settings to Apply the New Color Scheme
    bash_cmd = "termux-reload-settings"
    subprocess.run(bash_cmd, shell=True, check=True)

except (FileNotFoundError, PermissionError) as e:
    print(f"There was a problem copying the color scheme: {e}.")
