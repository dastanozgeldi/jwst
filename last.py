import json
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.style.use('dark_background')

# Load the constellation data
with open('constellations.json', 'r') as f:
    data = json.load(f)

def generate_star_field(width, height):
    fig, ax = plt.subplots(figsize=(width/100, height/100), dpi=100)
    ax.set_facecolor('black')
    
    # Set the plot limits to match our image size
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    
    # Plot stars
    for constellation in data['constellations']:
        x_coords = []
        y_coords = []
        for star in constellation['stars']:
            x_coords.append(star['x'])
            y_coords.append(star['y'])
            
            # Calculate star size based on magnitude (smaller magnitude = larger star)
            size = max(20 * (5 - star['mag']) / 3, 5)
            
            # Plot the star
            circle = Circle((star['x'], star['y']), size/2, edgecolor='none', facecolor="white", alpha=0.8)
            ax.add_patch(circle)
        
        # Plot constellation lines
        ax.plot(x_coords, y_coords, color='white', alpha=0.3, linewidth=1.5)
    
    # Remove axes
    ax.set_axis_off()
    
    # Invert y-axis to match image coordinates (0,0 at top-left)
    ax.invert_yaxis()
    
    return fig

# Generate star field
width, height = 700, 700  # Image size in pixels

fig = generate_star_field(width, height)

# Save the image
fig.savefig('results/kepler_452b_night_sky.png', bbox_inches='tight', pad_inches=0)
plt.close(fig)

print("Night sky image for Kepler-452b generated as 'kepler_452b_night_sky.png'")