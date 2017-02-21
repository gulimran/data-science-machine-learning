# Dictionaries are like a map or hash table in other languages

# Declaration
captains = {}

# Assign values for keys
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print captains

# Get a value for a given key, throws error on non-existing key
print captains["Voyager"]

# To avoid error for non-existing key, use 'get'
print captains.get("Enterprise")
print captains.get("NX-01")

# Iterate over key set of the dictionary
for ship in captains:
    print ship + ": " + captains[ship]