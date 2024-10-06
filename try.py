import requests
import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive
from astroquery.gaia import Gaia

def fetch_exoplanet_data(planet_name='Earth'):
    if planet_name.lower() == 'earth':
        return {'ra': 0, 'dec': 0, 'distance': 0}
    
    url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps+where+pl_name+=+'{planet_name}'&format=json"
    response = requests.get(url)
    data = response.json()
    
    if not data:
        raise ValueError(f"No data found for planet: {planet_name}")
    
    planet_data = data[0]
    return {
        'ra': float(planet_data['ra']),
        'dec': float(planet_data['dec']),
        'distance': float(planet_data['sy_dist'])
    }

def fetch_nearby_stars(ra, dec, radius=10, limit=1000):
    coord = SkyCoord(ra=ra, dec=dec, unit='deg')
    j = Gaia.cone_search_async(coord, radius=(radius,radius))
    r = j.get_results()
    return r[:limit]

def generate_night_sky(planet_name='Earth'):
    # Fetch exoplanet data
    planet_data = fetch_exoplanet_data(planet_name)
    
    # Fetch nearby stars
    stars = fetch_nearby_stars(planet_data['ra'], planet_data['dec'])
    
    # Create a plot
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
    ax.set_facecolor('black')
    
    # Plot stars
    magnitudes = stars['phot_g_mean_mag']
    sizes = 1000 / (magnitudes + 5)**2  # Adjust size based on magnitude
    ax.scatter(stars['ra'], stars['dec'], s=sizes, color='white', alpha=0.8)
    
    # Set labels and title
    ax.set_xlabel('Right Ascension')
    ax.set_ylabel('Declination')
    ax.set_title(f"Simulated Night Sky from {planet_name}")
    
    # Invert x-axis to match celestial sphere convention
    ax.invert_xaxis()
    
    # Remove axes for a cleaner look
    ax.axis('off')
    
    # Save the plot
    plt.savefig(f"{planet_name.lower()}_night_sky.png", dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Night sky image for {planet_name} has been generated and saved as '{planet_name.lower()}_night_sky.png'")

# Example usage
generate_night_sky()  # Generates Earth's night sky by default
# generate_night_sky("Kepler-16b")  # Uncomment to generate night sky for a specific exoplanet