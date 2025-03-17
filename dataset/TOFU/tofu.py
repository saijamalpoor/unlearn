from datasets import load_dataset
import json

# Load the TOFU dataset
dataset = load_dataset("locuslab/TOFU", "retain99")

# Print the dataset to see its structure
print(dataset)

# Convert the dataset to a list of dictionaries (e.g., from the 'train' split)
train_data = dataset['train'].to_dict()

# Save the dataset as a JSON file
with open('retain99.json', 'w') as json_file:
    json.dump(train_data, json_file, indent=4)
