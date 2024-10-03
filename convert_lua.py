def convert_ox_to_qbcore(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    converted_lines = []

    for line in lines:
        line = line.strip()
        
        if line.startswith("['"):  # Checks for item entry
            item_name = line.split('=')[0].strip().strip(" ,")
            item_data = line.split('=')[1].strip().rstrip(',')

            # Extracting properties
            properties = {}
            for prop in item_data.split(','):
                key_value = prop.split('=')
                if len(key_value) == 2:
                    key = key_value[0].strip().strip("' ")
                    value = key_value[1].strip()
                    properties[key] = value

            # Constructing the new QBCore format
            new_format = (
                f"{item_name} = {{\n"
                f"    ['name'] = '{item_name.strip('[]')}',\n"
                f"    ['label'] = '{properties.get('label', 'Unknown')}',\n"
                f"    ['weight'] = {properties.get('weight', 1)},\n"
                f"    ['type'] = 'item',\n"
                f"    ['image'] = '{item_name.strip('[]')}.png',\n"
                f"    ['unique'] = false,\n"
                f"    ['useable'] = true,\n"
                f"    ['shouldClose'] = true,\n"
                f"    ['description'] = nil\n"
                f"}}"
            )
            converted_lines.append(new_format + ",\n")

    with open(output_file, 'w') as outfile:
        outfile.writelines(converted_lines)

if __name__ == "__main__":
    input_filename = 'input.lua'  # Name of the input Lua file
    output_filename = 'output.lua'  # Name of the output Lua file

    convert_ox_to_qbcore(input_filename, output_filename)

    print(f"Conversion completed. Output written to {output_filename}.")
