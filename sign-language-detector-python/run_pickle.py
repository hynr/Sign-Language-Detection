import pickle

# Load the data from the .pickle file
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)

# Access the loaded data and labels
loaded_data, loaded_labels = loaded_data['data'], loaded_data['labels']

# Print the loaded data and labels
print("Loaded Data:")
print(loaded_data)
print("\nLoaded Labels:")
print(loaded_labels)
