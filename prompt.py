"""
we are given a name of an exoplanet and i want you to return a json file like this 
{
    "constellations": [
      {
        "name": "Ursa Major",
        "stars": [
          {"name": "Dubhe", "x": 320, "y": 150, "mag": 1.79},
          {"name": "Merak", "x": 280, "y": 180, "mag": 2.37},
          {"name": "Phecda", "x": 350, "y": 220, "mag": 2.44},
          {"name": "Megrez", "x": 390, "y": 190, "mag": 3.31},
          {"name": "Alioth", "x": 450, "y": 170, "mag": 1.77},
          {"name": "Mizar", "x": 510, "y": 140, "mag": 2.23},
          {"name": "Alkaid", "x": 570, "y": 120, "mag": 1.85}
        ]
      },
      {
        "name": "Orion",
        "stars": [
          {"name": "Betelgeuse", "x": 600, "y": 450, "mag": 0.42},
          {"name": "Rigel", "x": 500, "y": 650, "mag": 0.13},
          {"name": "Bellatrix", "x": 450, "y": 400, "mag": 1.64},
          {"name": "Mintaka", "x": 480, "y": 550, "mag": 2.25},
          {"name": "Alnilam", "x": 520, "y": 570, "mag": 1.69},
          {"name": "Alnitak", "x": 560, "y": 590, "mag": 1.88},
          {"name": "Saiph", "x": 620, "y": 680, "mag": 2.06}
        ]
      }
    ]
  }

where you need to use knowledge from NASA Exoplanet Archive and Gaia DR3 to get all stars for a given exoplanet in the radius of 10 parsecs and then use the data from the exoplanet to generate the json file.
return only json code.
exoplanet name: Kepler-452b
"""