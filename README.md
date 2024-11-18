# Starfield Crew Minmaxer

Unlock the full potential of your Starfield crew! This tool helps you optimize your crew selection based on your specific needs and preferences, ensuring you always have the best team by your side in the vastness of space.

## Overview

Starfield Crew Minmaxer is a Python script designed to help players select the optimal crew members for their spaceship in the game **Starfield**. By considering your preferred ship weapons and excluding any characters you don't want (or who are no longer available), the script generates a customized list of the best crew members to enhance your gameplay experience.

## Features

- **Customized Crew Selection**: Choose your preferred ship weapons and exclude unwanted characters to get a tailored list of crew members.
- **Optimized Recommendations**: The script calculates the best crew members based on their skills and your preferences.
- **Easy to Use**: Simple editing of a Python script and straightforward execution.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/Starfield-Crew-Minmaxer.git
   ```

2. **Navigate to the Directory**:

   ```bash
   cd Starfield-Crew-Minmaxer
   ```

3. **Install Dependencies**:

   Ensure you have Python installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Edit `minmax_crew.py`**:

   - Open the script in your favorite text editor.
   - **Specify Dead or Unwanted Characters**:

     Locate the `dead_characters` list and add any characters you want to exclude:

     ```python
     dead_characters = ["Character Name 1", "Character Name 2"]
     ```

   - **Select Your Ship Weapons**:

     Uncomment the weapons you use on your ship in the `weapon_skills` list:

     ```python
     weapon_skills = [
         'Ballistic Weapon Systems',
         'Missile Weapon Systems',
         # 'Particle Beam Weapon Systems',
         # 'Energy Weapon Systems',
         # 'EM Weapon Systems',
     ]
     ```

2. **Run the Script**:

   Execute the script to get your optimized crew recommendations:

   ```bash
   python minmax_crew.py
   ```

3. **View the Output**:

   The script will display a list of the best crew members based on your preferences. For example:

   **All Weapons - No Constellation Members**:

| Name              | Reason                                        | System          | Planet  |
|-------------------|-----------------------------------------------|-----------------|---------|
| Barrett           | Starship Engineering, Particle Beam Weapon Systems | Alpha Centauri | Jemison |
| Sam Coe           | Piloting, Payloads                            | Alpha Centauri  | Jemison |
| Sarah Morgan      | Astrodynamics, Leadership                     | Alpha Centauri  | Jemison |
| VASCO             | Aneutronic Fusion                             | Alpha Centauri  | Jemison |
| Andromeda Kepler  | Aneutronic Fusion                             | Sol             | Mars    |
| Omari Hassan      | Shield Systems                                | Cheyenne        | Akila   |


Note that VASCO and Andromeda are tied for usefulness in this example, so both are listed. 

## How It Works

The script processes crew data sourced from [INARA](https://inara.cz/starfield/companions/) to determine the best crew members based on:

- **Skills**: Matches crew skills with your selected ship and weapon skills.
- **Preferences**: Excludes any characters you've listed as dead or unwanted.
- **Optimization**: Selects the best crew member for the relevant skills. Sometimes there is a tie, in which case both are listed. 

## Examples

### Particle Beams Only - Nobody Missing

| Name              | Reason                                        | System          | Planet  |
|-------------------|-----------------------------------------------|-----------------|---------|
| Barrett           | Starship Engineering, Particle Beam Weapon Systems | Alpha Centauri | Jemison |
| Sam Coe           | Piloting, Payloads                            | Alpha Centauri  | Jemison |
| Sarah Morgan      | Astrodynamics, Leadership                     | Alpha Centauri  | Jemison |
| VASCO             | Aneutronic Fusion                             | Alpha Centauri  | Jemison |
| Andromeda Kepler  | Aneutronic Fusion                             | Sol             | Mars    |
| Omari Hassan      | Shield Systems                                | Cheyenne        | Akila   |


### All Weapons - No Constellation

| Name              | Reason                                        | System          | Planet        |
|-------------------|-----------------------------------------------|-----------------|---------------|
| Amelia Earhart    | Piloting                                      | Charybdis       | Charybdis III |
| Andromeda Kepler  | Aneutronic Fusion                             | Sol             | Mars          |
| Dani Garcia       | Energy Weapon Systems                         | Volii           | Volii Alpha   |
| Erick Von Price   | Astrodynamics, Payloads                       | Sol             | Mars          |
| Gideon Aker       | Ballistic Weapon Systems, Missile Weapon Systems | Alpha Centauri | Jemison       |
| Marika Boros      | Particle Beam Weapon Systems                  | Alpha Centauri  | Jemison       |
| Omari Hassan      | Shield Systems, Starship Engineering          | Cheyenne        | Akila         |
| Sahima Ka'dic     | Aneutronic Fusion, EM Weapon Systems          | Kavnyk          | Va'ruun'kai   |
| Tane Salavea      | Payloads                                      | Kavnyk          | Va'ruun'kai   |


### All Weapons - Nobody Missing

| Name              | Reason                                        | System          | Planet        |
|-------------------|-----------------------------------------------|-----------------|---------------|
| Andreja           | Energy Weapon Systems                         | Alpha Centauri  | Jemison       |
| Barrett           | Starship Engineering, Particle Beam Weapon Systems | Alpha Centauri | Jemison       |
| Sam Coe           | Piloting, Payloads                            | Alpha Centauri  | Jemison       |
| Sarah Morgan      | Astrodynamics, Leadership                     | Alpha Centauri  | Jemison       |
| VASCO             | Aneutronic Fusion                             | Alpha Centauri  | Jemison       |
| Gideon Aker       | Ballistic Weapon Systems, Missile Weapon Systems | Alpha Centauri | Jemison       |
| Jessamine Griffin | Ballistic Weapon Systems                      | Kryx            | Suvorov       |
| Omari Hassan      | Shield Systems                                | Cheyenne        | Akila         |
| Sahima Ka'dic     | Aneutronic Fusion, EM Weapon Systems          | Kavnyk          | Va'ruun'kai   |


## Credits

- **Data Source**: Crew data was sourced from [INARA](https://inara.cz/starfield/companions/).

## License

This project is open-source and available under the [MIT License](LICENSE.txt).

**Disclaimer**: 
Starfield is a product of ZeniMax Media Inc. All game data, assets, and intellectual property are the property of ZeniMax Media Inc.
The crew data used in this project was sourced from [INARA](https://inara.cz/). All INARA data is the property of its respective owners.
This project is not affiliated with or endorsed by ZeniMax Media Inc. or INARA.
