#Plot a line with dataframe
#Dataframe -> 2 dimenstional tabular data
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Cricket_Bat": ["SG", "BDM", "SS", "GM", "KUKABURRA", "SPARTAN"],
    "MRP": [2000,2200,2400,2500,2600,3000],
    "Weight_grams": [1100,1200,1250,1330,1480,1600]
}

# Dataframe
dataFrame = pd.DataFrame(data)

# Plot a line using the pyplot
# The x and y coordinates are the columns of the dataframe

plt.plot(dataFrame["MRP"], dataFrame["Weight_grams"])

# Add grid lines
plt.grid()
# Plot labels
plt.xlabel("Bat price(USD)")
plt.ylabel("Bat Weight(Grams)")

# Plot title
plt.title("Bat Price VS Weight", loc='left')  # by default center

# Display the figure
plt.show()