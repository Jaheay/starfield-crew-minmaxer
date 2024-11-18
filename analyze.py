import pandas
pandas.options.mode.chained_assignment = None
# Step 1: Load the skills CSV into a DataFrame
crew = pandas.read_csv('crew.csv')

# Define killed or banned characters
#dead_characters = ['Sarah Morgan']
#dead_characters = ["Mathis Castillo", "Jessamine Griffin", "Sarah Morgan"]
dead_characters = ["Barrett", "Sam Coe", "Sarah Morgan", "VASCO", "Rafael Aguerro"]
# Step 2: Define skill categories
ship_skills = [
    'Astrodynamics', 
    'Leadership', 
    'Aneutronic Fusion', 
    'Piloting', 
    'Payloads', 
    'Shield Systems', 
    'Starship Engineering',
]

weapon_skills = [
#    'Ballistic Weapon Systems',    
#    'Missile Weapon Systems', 
    'Particle Beam Weapon Systems', 
#    'Energy Weapon Systems', 
#    'EM Weapon Systems',
]

# Combine the skill categories for filtering
all_meaningful_skills = ship_skills + weapon_skills
all_skills = crew.columns.difference(['Name', 'Location', 'System', 'Planet'])

# Filter crew members without any required skills
filtered_overridden_crew = crew[crew[all_meaningful_skills].gt(0).any(axis=1)]

# Remove dead characters from filtered crew
filtered_overridden_crew = filtered_overridden_crew[~filtered_overridden_crew['Name'].isin(dead_characters)]

# Calculate the total skill values for tie-breaking
crew_skill_values = crew[all_skills].gt(0).sum(axis=1).add(crew[all_meaningful_skills].gt(0).sum(axis=1), fill_value=0)
filtered_skill_values = filtered_overridden_crew[all_skills].gt(0).sum(axis=1).add(filtered_overridden_crew[all_meaningful_skills].gt(0).sum(axis=1), fill_value=0)

# Assign total skill values back to crew and filtered crew
crew['Crew Value'] = crew_skill_values
filtered_overridden_crew['Crew Value'] = filtered_skill_values 

# Override skills based on the highest value
for skill in all_meaningful_skills:
    max_skill_value = filtered_overridden_crew[skill].max()
    if max_skill_value > 0:
        # Set all other values for this skill to 0 except the max one using .loc
        filtered_overridden_crew.loc[:, skill] = filtered_overridden_crew[skill].where(filtered_overridden_crew[skill] != max_skill_value, max_skill_value)

# Tie-breaker logic for selecting the best skill holders
reasons = []
for name in dead_characters:
    reasons.append((name, "Dead"))
                   
for skill in all_meaningful_skills:
    max_value = filtered_overridden_crew[skill].max()
    if max_value > 0:
        # Find the crew members with the maximum value for this skill
        finalists = filtered_overridden_crew[filtered_overridden_crew[skill] == max_value]

        for index, row in finalists.iterrows():
            reasons.append((row['Name'], skill))
        
        # If there are multiple winners, choose the one with the highest total skill value
        if len(finalists) > 1:
            # Find the maximum crew value among the finalists
            max_crew_value = finalists['Crew Value'].max()
            # Get all members with the maximum crew value (VASCO vs Kelper)
            best_members = finalists[finalists['Crew Value'] == max_crew_value]

            # Set the skill value for all best members
            filtered_overridden_crew[skill] = 0  # Set others to 0
            filtered_overridden_crew.loc[filtered_overridden_crew['Name'].isin(best_members['Name']), skill] = max_value
        else:
            # If only one member has the max value, keep it
            filtered_overridden_crew[skill] = 0
            filtered_overridden_crew.loc[filtered_overridden_crew['Name'] == finalists['Name'].values[0], skill] = max_value

# Filter crew members with remaining non-zero skills
final_crew = filtered_overridden_crew[(filtered_overridden_crew[all_meaningful_skills] > 0).any(axis=1)]

# Initialize the 'Reason' column for final_crew_df
final_crew.loc[:, 'Reason'] = ''
crew.loc[:, 'Reason'] = ''

# Set reasons based on the collected reasons list
for name, skill in reasons:
    final_crew.loc[final_crew['Name'] == name, 'Reason'] += f"{skill}, "
    crew.loc[crew['Name'] == name, 'Reason'] += f"{skill}, "

# Strip trailing commas from the 'Reason' column
final_crew['Reason'] = final_crew['Reason'].str.rstrip(', ')
crew['Reason'] = crew['Reason'].str.rstrip(', ')

# Print the resulting DataFrames
desired_order = ['Name', 'Location', 'System', 'Planet', 'Reason', 'Crew Value'] + sorted(all_skills.tolist())
crew = crew[desired_order]
final_crew = final_crew[desired_order]

crew.to_csv('all_crew.csv', index=False)
final_crew.to_csv('fin_crew.csv', index=False)
print(final_crew[['Name', 'Reason', 'System', 'Planet']].to_string(index=False))
