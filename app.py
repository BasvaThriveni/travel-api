from flask import Flask, jsonify, render_template
from urllib.parse import quote

app = Flask(__name__)

def wiki_image(filename, width=800):
    """Build a stable, direct image URL from a Wikimedia Commons filename."""
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{quote(filename)}?width={width}"

# ---- The data: 10 countries I'd love to visit, with a favourite spot in each ----
COUNTRIES = [
    {
        "country": "Japan",
        "spot": "Fushimi Inari Shrine, Kyoto",
        "details": "Famous for its thousands of vermillion torii gates winding up Mount Inari.",
        "lat": 34.9671, "lng": 135.7727,
        "image": wiki_image("FushimiInariTorii.jpg")
    },
    {
        "country": "Italy",
        "spot": "The Colosseum, Rome",
        "details": "The largest ancient amphitheatre ever built, once host to gladiator contests.",
        "lat": 41.8902, "lng": 12.4922,
        "image": wiki_image("Colosseum Rome.jpg")
    },
    {
        "country": "France",
        "spot": "Eiffel Tower, Paris",
        "details": "The iron lattice tower that has become the global symbol of Paris.",
        "lat": 48.8584, "lng": 2.2945,
        "image": wiki_image("Tour Eiffel Wikimedia Commons.jpg")
    },
    {
        "country": "New Zealand",
        "spot": "Milford Sound, Queenstown region",
        "details": "A dramatic fiord with towering cliffs, waterfalls, and rainforest.",
        "lat": -44.6414, "lng": 167.9057,
        "image": wiki_image("MilfordSound.jpg")
    },
    {
        "country": "Iceland",
        "spot": "Jokulsarlon Glacier Lagoon",
        "details": "A glacial lake filled with drifting icebergs calved from a nearby glacier.",
        "lat": 64.0784, "lng": -16.2300,
        "image": wiki_image("Jokulsarlon.JPG")
    },
    {
        "country": "Egypt",
        "spot": "Pyramids of Giza",
        "details": "The last surviving wonder of the ancient world, on the outskirts of Cairo.",
        "lat": 29.9792, "lng": 31.1342,
        "image": wiki_image("Great Pyramid of Giza.jpg")
    },
    {
        "country": "Peru",
        "spot": "Machu Picchu, Cusco region",
        "details": "A 15th-century Inca citadel set high in the Andes Mountains.",
        "lat": -13.1631, "lng": -72.5450,
        "image": wiki_image("Machu Picchu, Peru.jpg")
    },
    {
        "country": "Greece",
        "spot": "Oia, Santorini",
        "details": "A clifftop village famous for whitewashed houses and blue-domed churches.",
        "lat": 36.4620, "lng": 25.3753,
        "image": wiki_image("Church Bells at Oia, Santorini.jpg")
    },
    {
        "country": "Norway",
        "spot": "Lofoten Islands",
        "details": "An archipelago known for dramatic peaks, fishing villages, and the midnight sun.",
        "lat": 68.1489, "lng": 13.6089,
        "image": wiki_image("Lofoten Bunesstranda Norway.jpg")
    },
    {
        "country": "South Africa",
        "spot": "Table Mountain, Cape Town",
        "details": "A flat-topped mountain overlooking Cape Town, reachable by cable car.",
        "lat": -33.9628, "lng": 18.4098,
        "image": wiki_image("Table Mountain panorama.jpg")
    },
]


@app.route("/api/countries")
def api_countries():
    """Pure JSON API endpoint - this is the actual 'API' your mentor asked about."""
    return jsonify(COUNTRIES)


@app.route("/")
def home():
    """
    Serves an empty page shell. The browser's own JavaScript then calls
    /api/countries and builds the page from that response - so the API
    call is now visible in the Network tab, exactly like a real web app.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
