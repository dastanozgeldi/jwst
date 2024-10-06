import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
from astropy import units as u
from astroquery.vizier import Vizier

def simulate_night_sky(exoplanet_name='Earth'):
    # Step 1: Get the exoplanet's position
    if exoplanet_name == 'Earth':
        # Earth's position is at the origin
        exoplanet = SkyCoord(x=0*u.pc, y=0*u.pc, z=0*u.pc, representation_type='cartesian', frame='icrs')
    elif exoplanet_name == 'Proxima Centauri b':
        # Proxima Centauri's coordinates
        exoplanet = SkyCoord('14h 29m 42.9487s', '-62d 40m 46.141s', distance=1.295*u.pc, frame='icrs')
    else:
        # For other exoplanets, you'd fetch the position from an API or database
        print(f"Exoplanet '{exoplanet_name}' not recognized. Defaulting to Earth.")
        exoplanet = SkyCoord(x=0*u.pc, y=0*u.pc, z=0*u.pc, representation_type='cartesian', frame='icrs')
    
    exo_cartesian = exoplanet.cartesian

    # Step 2: Load the Hipparcos catalog
    Vizier.ROW_LIMIT = -1  # Remove row limit
    hipparcos_catalog = Vizier.get_catalogs('I/239/hip_main')[0]
    hip = hipparcos_catalog[hipparcos_catalog['Plx'] > 0]  # Filter out stars with non-positive parallax

    # Step 3: Extract necessary data
    parallax_mas = hip['Plx'].quantity  # Parallax in milliarcseconds, as Quantity
    distance_pc = (1000 * u.mas) / parallax_mas  # Convert parallax to distance
    distance_pc = distance_pc.to(u.pc)  # Ensure distance is in parsecs

    ra = hip['_RA.icrs'].quantity  # RA with units already attached
    dec = hip['_DE.icrs'].quantity  # Dec with units already attached
    vmag = hip['Vmag']

    # Step 4: Create SkyCoord objects for the stars
    stars = SkyCoord(ra=ra, dec=dec, distance=distance_pc, frame='icrs')
    stars_cartesian = stars.cartesian

    # Step 5: Compute relative positions
    relative_positions = stars_cartesian - exo_cartesian
    new_coords = SkyCoord(x=relative_positions.x, y=relative_positions.y, z=relative_positions.z,
                          representation_type='cartesian', frame='icrs')

    # Step 6: Compute new distances and adjust magnitudes
    new_distances = relative_positions.norm()
    orig_distances = stars.distance
    delta_m = 5 * np.log10(new_distances / orig_distances)
    new_vmag = vmag + delta_m

    # Step 7: Filter visible stars based on magnitude limit
    mag_limit = 8  # You can adjust this value
    visible = new_vmag <= mag_limit
    plot_ra = new_coords.ra[visible]
    plot_dec = new_coords.dec[visible]
    plot_vmag = new_vmag[visible]
    sizes = (mag_limit - plot_vmag + 0.5) ** 1.5  # Adjust marker sizes for visibility

    # Step 8: Plot the night sky
    plt.figure(figsize=(12, 6))
    plt.style.use('dark_background')
    plt.scatter(plot_ra.wrap_at(180*u.deg).deg, plot_dec.deg, s=sizes, color='white', alpha=0.8)
    plt.gca().invert_xaxis()
    plt.xlabel('Right Ascension [deg]')
    plt.ylabel('Declination [deg]')
    plt.title(f'Night Sky as Seen from {exoplanet_name}')
    plt.show()

# Example usage:
simulate_night_sky('Earth')  # Simulate night sky from Earth
simulate_night_sky('Proxima Centauri b')  # Simulate night sky from Proxima Centauri b
