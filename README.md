# Weather Data Application

A personal Python project for exploring weather and climate data. The aim is to build the application from the requirements up, understand how each part works, and practise the full development process: planning, designing, implementing, testing, and documenting a software system.

## Project status

**Design and requirements stage.** The screens below are mock-ups with sample data; the Python application and API integration have not been implemented yet.

## Planned features

- Manage saved locations, including country details, coordinates, search, editing, removal, and favourites.
- Search weather forecasts by location, date range, model, units, and selected hourly or daily variables.
- Search historical weather over a chosen interval using available reanalysis data.
- Search hourly air-quality forecasts, including the European Air Quality Index and a selected domain.
- View results in tables and charts, and export data as CSV, JSON, or XLSX and charts as PNG, JPEG, or PDF.
- Save forecast, historical, and air-quality result sets with descriptions or tags and timestamps; browse saved results and support offline viewing.

The eventual data provider and the exact variables available will be chosen during implementation. Open-Meteo is one possible provider from the original brief.

## Page mock-ups

The latest live-radar designs are below and indexed in [Live Radar Design](docs/design/live-radar/README.md). These are visual mock-ups with sample data. They include the revised panel grouping and alignment, no global top location bar, and a simplified Air Quality Index card.

The [interactive HTML mock-up](docs/design/weather-data-all-pages.html) is an earlier design and has not yet been updated to match these images. Original paper sketches are in [hand-drawn-sketches/](docs/design/hand-drawn-sketches/).

### Home

![Home mock-up](docs/design/live-radar/screenshots/home.jpg)

### Forecast

![Forecast mock-up](docs/design/live-radar/screenshots/forecast-live-radar.jpg)

### Historical weather

![Historical weather mock-up](docs/design/live-radar/screenshots/historical-weather.jpg)

### Air quality

![Air quality mock-up](docs/design/live-radar/screenshots/air-quality.jpg)

### Saved data

![Saved data mock-up](docs/design/live-radar/screenshots/saved-data.jpg)

### Locations

![Locations mock-up](docs/design/live-radar/screenshots/locations.jpg)

### Settings

![Settings mock-up](docs/design/live-radar/screenshots/settings.jpg)

## Planned implementation approach

The Python implementation will be developed in small steps so each feature can be understood and verified before adding the next one. Initial work will establish the project structure and location model, then add forecast requests and result display. Historical data, air quality, exports, and saved/offline data can follow as separate milestones.

## Source requirements

This project follows the supplied Weather Data Application brief and its requirements REQ-1 through REQ-26. Some details in the brief, such as the full list of extra provider variables and the meaning of the air-quality “domain” option, need to be resolved against the chosen API before implementation.
