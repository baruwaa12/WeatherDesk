import json
from pathlib import Path

# Location.py
# Two classes:
#   Location        = one saved place (name, country, map coordinates)
#   LocationManager = a list of those places you can add, find, edit, delete


class Location:
    """One place on the map, e.g. London or Paris."""

    def __init__(self, ID, name, CName, CCode, lat, long):
        # Runs once when you create a Location(...)
        self.ID = ID
        self.favourite = False  # not starred unless the user marks it later
        # Reuse the edit method so create and edit use the same checks
        self.modifyLocationData(name, CName, CCode, lat, long)

    def modifyLocationData(self, new_name, new_cname,
                           new_ccode, new_lat, new_long):
        """Check the details, then save them. Used for both create and edit."""

        # Convert text like "51.52" into real numbers
        latitude = float(new_lat)
        longitude = float(new_long)

        # .strip() removes extra spaces. Empty name or country is not allowed.
        if not new_name.strip() or not new_cname.strip():
            raise ValueError("Location name and country cannot be empty.")

        # Latitude: north/south. Only valid between the South Pole and North Pole.
        if not -90 <= latitude <= 90:
            raise ValueError("Latitude must be between -90 and 90.")

        # Longitude: east/west. Only valid all the way around the Earth.
        if not -180 <= longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180.")

        # Checks passed — store the cleaned values
        self.name = new_name.strip()
        self.CName = new_cname.strip()
        self.CCode = new_ccode.strip().upper()  # e.g. "gbr" becomes "GBR"
        self.lat = latitude
        self.long = longitude

    def __str__(self):
        # Controls what print(location) shows.
        # Add a star only if this place is a favourite.
        star = " ★" if self.favourite else ""
        return (
            f"{self.ID}: {self.name}, {self.CName} "
            f"({self.lat}, {self.long}){star}"
        )


class LocationManager:

    """Holds all saved locations and lets you add / search / edit / remove them."""

    def __init__(self):
        self.locations = []  # starts empty; add() fills this list
        self.file = Path("locations.json")


    def save_locations(self):

        # Convert each Location object into a dictionary for JSON storage.
        data = [vars(location) for location in self.locations]

        # Replace the file contents with the current collection.
        with self.file.open("w") as saved_file
        json.dump(data, saved_file, indent=4)

    
    def load_locations(self):
          """Restore saved locations from the JSON file."""
        
        # On the first run, there may be no saved file.
        if not self.file.exists():
            return

        with self.file.open("r") as saved_file:
            data = json.load(saved_file)
        
        loaded_locations = []

        # Rebuild Location objects from the saved dictionaries. 
        for record in data:
            location = Location(
                record["ID"],
                record["name"],
                record["CName"],
                record["CCode"],
                record["lat"],
                record["long"]
            )
            location.favourite = record.get("favourite", False)
            loaded_locations.append(location)

        # Update the manager once all records have been loaded.
        self.locations = loaded_locations


    def add(self, location):
        # any(...) is True if even one existing item already uses this ID
        if any(item.ID == location.ID for item in self.locations):
            raise ValueError("A location with that ID already exists.")

        self.locations.append(location)

    def get(self, location_id):
        """Find one location by its ID. Other methods reuse this."""
        for location in self.locations:
            if location.ID == location_id:
                return location

        raise ValueError("Location not found.")

    def modify(self, location_id, name, country, code, lat, long):
        # Look it up, then run the same validation used when creating one
        location = self.get(location_id)
        location.modifyLocationData(name, country, code, lat, long)

    def search(self, query):
        """Return every location that matches (partial match on name/country)."""
        # casefold() = lowercase, so "paris" matches "Paris"
        query = str(query).strip().casefold()

        # List comprehension: keep a location if the query matches ID,
        # or appears *inside* the name, country name, or country code.
        # "Par" would match Paris. Returns a new list; original list is unchanged.
        return [
            location
            for location in self.locations
            if query == str(location.ID).casefold()
            or query in location.name.casefold()
            or query in location.CName.casefold()
            or query in location.CCode.casefold()
        ]

    def remove(self, name_or_id):
        """Delete one location. Needs an exact ID or exact name (safer than search)."""
        query = str(name_or_id).strip().casefold()

        # Exact match only: "Par" will NOT delete Paris
        matches = [
            location
            for location in self.locations
            if query == str(location.ID).casefold()
            or query == location.name.casefold()
        ]

        if not matches:
            raise ValueError("Location not found.")

        # Two cities with the same name: don't guess — ask for the ID
        if len(matches) > 1:
            raise ValueError("Multiple locations match. Use the ID.")

        self.locations.remove(matches[0])

    def set_favourite(self, location_id, favourite=True):
        # Default is True (star it). Pass False to un-star.
        self.get(location_id).favourite = favourite

    def list_locations(self):
        # .copy() so the caller can look at the list without changing ours
        return self.locations.copy()


# This block only runs if you start THIS file (python Location.py).
# If another file does "import Location", the demo below is skipped.
if __name__ == "__main__":
    manager = LocationManager()

    manager.add(Location(1, "London", "UK", "GBR", 51.52, -0.127))
    manager.add(Location(2, "Paris", "France", "FRA", 48.85, 2.35))

    manager.set_favourite(1)  # star London

    print("All locations:")
    for location in manager.list_locations():
        print(location)

    print("\nSearch results:")
    for location in manager.search("Paris"):
        print(location)

    manager.modify(2, "Lyon", "France", "FRA", 45.76, 4.84)
    print("\nAfter modifying location 2:")
    print(manager.get(2))

    manager.remove(2)

    print("\nAfter removing location 2:")
    for location in manager.list_locations():
        print(location)


