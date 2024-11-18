import re
import string
import pandas

RAW_CREW_PATH = 'data/raw_crew.txt'
PARSED_CREW_PATH = 'data/parsed_crew.csv'

# Load data from skills.txt
with open(RAW_CREW_PATH, 'r') as file:
    data = file.read()

# Remove non-standard characters
printable = set(string.printable)
data = ''.join(filter(lambda x: x in printable, data))

# Split the data into chunks based on double newlines separating records
raw_chunks = re.split(r'\n\n+', data.strip())

# Initialize list to hold properly formatted chunks
formatted_chunks = []

# Combine last two lines of the previous chunk with the current chunk
for i in range(len(raw_chunks)):
    if i > 0:  # For all chunks except the first
        # Get the previous chunk's last two lines
        prev_chunk_lines = raw_chunks[i - 1].splitlines()[-2:]
        current_chunk = raw_chunks[i].splitlines()
        
        # Create combined chunk
        combined_chunk = "\n".join(prev_chunk_lines + current_chunk)
        formatted_chunks.append(combined_chunk)
        
        # Remove the last two lines from the combined chunk
        combined_lines = combined_chunk.splitlines()
        formatted_chunks[-1] = "\n".join(combined_lines[:-2])
    else:  # For the first chunk, add it as is
        formatted_chunks.append(raw_chunks[i])

# Unconditionally remove the first chunk
formatted_chunks.pop(0)

# Remove generic specialist chunks only if "Specialist" is in the first line
formatted_chunks = [chunk for chunk in formatted_chunks if not chunk.splitlines()[0].endswith("Specialist")]
formatted_chunks = [chunk for chunk in formatted_chunks if not chunk.splitlines()[0].endswith("Security Chief")]

# Initialize an empty list to hold the records
records = []

# Iterate through each formatted chunk
for chunk in formatted_chunks:
    # Split the chunk into lines
    lines = chunk.splitlines()
    
    if len(lines) >= 3:
        # Extract name, location, planet, and system from the first two lines
        name = lines[0].strip()
        location_raw = lines[1].strip()
        
        # Extract city, planet and system from the location
        location_full = re.search(r'(.*?)\((.*?)\)', location_raw)
        if location_full:
            city = location_full.group(1).strip()
            planet_system = location_full.group(2).split(', ')
            planet = planet_system[0].strip()
            system = planet_system[1].strip() if len(planet_system) > 1 else ''

        # Extract skills from the remaining lines using regex
        records_table = {}
        for skill_line in lines[2:]:
            # Use regex to match skill name and value
            match = re.match(r'([A-z ]+)(\d)', skill_line)
            if match:
                skill_name = match.group(1).strip()
                skill_value = int(match.group(2).strip())
                records_table[skill_name] = skill_value

        # Create the record
        record = {
            'name': name,
            'location': city,
            'planet': planet,
            'system': system,
            'skills': records_table
        }
        
        # Append the record to the list
        records.append(record)

# Step 1: Collect all unique skills
all_skills = set()
for record in records:
    all_skills.update(record['skills'].keys())

# Step 2: Prepare rows for the DataFrame
data = []
for record in records:
    row = {
        'Name': record['name'],
        'Location': record['location'],
        'System': record['system'],
        'Planet': record['planet']
    }
    # Add skills to the row, defaulting to 0 for skills not in the current record
    for skill in all_skills:
        row[skill] = record['skills'].get(skill, 0)
    data.append(row)

# Step 3: Create the DataFrame
records_table = pandas.DataFrame(data, columns=['Name', 'Location', 'System', 'Planet'] + sorted(all_skills))

# Step 4: Fill NaN values with 0
records_table.fillna(0, inplace=True)

# Export DataFrame to CSV
records_table.to_csv(PARSED_CREW_PATH, index=False)

