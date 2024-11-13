# cspell:words ArcaneSavant chcolor chfont termux

#!/data/data/com.termux/files/usr/bin/bash

########################################################################
# "Termux Appearance" Install Script
# Execute install.sh
#
# Copyright (C) 2024 ArcaneSavant
#
# Authors: ArcaneSavant <https://github.com/ArcaneSavant>
#
# Webpage: https://github.com/ArcaneSavant/termux-appearance
#
# Enjoy "Termux Appearance"!
#
# License: MIT License
########################################################################

# Intro

printf '\n%s\n' "© 2024 ArcaneSavant"
printf '%s\n' "https://github.com/ArcaneSavant/termux-appearance"
printf '%s\n' "Customize Termux With Ease!"

# Storage Permission

printf '\n%s\n' "Grant Storage Permission if Asked"
termux-setup-storage
sleep 5

# Clone Repository

printf '\n%s\n' "→ Cloning Termux Appearance Repo"
git clone https://github.com/ArcaneSavant/termux-appearance.git "${HOME}/archives/termux-appearance"
sleep 1

# Set Up Termux Appearance

printf '\n%s\n' "→ Setting Up Termux Appearance"

if [ -f "${HOME}/.bashrc" ]; then
  printf '%s\n' "Appending Aliases for Termux Appearance Commands to ${HOME}/.bashrc"
  {
    printf '\n%s\n' "# Aliases for Termux Appearance Commands"
    printf '%s\n' "alias chcolor='python3 ${HOME}/archives/termux-appearance/assets/chcolor.py'"
    printf '%s\n' "alias chfont='python3 ${HOME}/archives/termux-appearance/assets/chfont.py'"
  } >>"${HOME}/.bashrc"
else
  printf '%s\n' "bash Configuration File Not Found!"
  printf '%s\n' "Please Add These Aliases to Your Shell Manually:"
  printf '%s\n' "alias chcolor='python3 ${HOME}/archives/termux-appearance/assets/chcolor.py'"
  printf '%s\n' "alias chfont='python3 ${HOME}/archives/termux-appearance/assets/chfont.py'"
fi

# Restart

printf '\n%s\n' "✔ Done."
printf '%s\n' "Please Restart Termux App."
printf '%s\n' "Thank You!"

exit
