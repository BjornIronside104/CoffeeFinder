def get_shops():
    return [
        {
            "id": 1,
            "name": "The Green House",
            "address": "Oudezijds Voorburgwal 191",
            "vibe": ["chill", "artsy", "eco", "plant-daddy",],
            "music": ["lo-fi beats", "nature sounds", "ambient"],
            "strains": ["Amnesia Haze", "Super Lemon Haze", "White Widow"],
            "rating": 4.7,
            "hours": "8:00-01:00",
            "description": "Eco-conscious spot with living walls and premium organic strains"
        },
        {
            "id": 2,
            "name": "Boerejongens Lounge",
            "address": "Baarsjesweg 239",
            "vibe": ["classy", "luxe", "bougie", "insta-worthy"],
            "music": ["jazz", "lounge", "smooth"],
            "strains": ["Silver Haze", "OG Kush", "Blue Cheese"],
            "rating": 4.9,
            "hours": "9:00-00:00",
            "description": "Upscale dispensary with pharmaceutical-grade cannabis"
        },
        {
            "id": 3,
            "name": "Dampkring",
            "address": "Handboogstraat 29",
            "vibe": ["trippy", "artsy", "colorful", "good-vibes"],
            "music": ["psytrance", "classic rock", "80s synth"],
            "strains": ["Jack Herer", "Super Polm", "Nepalese"],
            "rating": 4.6,
            "hours": "10:00-23:00",
            "description": "Iconic spot featured in Oceans 12 with psychedelic decor"
        },
        {
            "id": 4,
            "name": "Paradox",
            "address": "Kerkstraat 113",
            "vibe": ["cozy", "chill", "hidden", "book-nook"],
            "music": ["acoustic", "folk", "soft reggae"],
            "strains": ["Northern Lights", "Hindu Kush", "AK-47"],
            "rating": 4.8,
            "hours": "11:00-22:00",
            "description": "Tiny hidden gem known for strong edibles and comfy couches"
        },
        {
            "id": 5,
            "name": "Green Place",
            "address": "Nieuwmarkt 17",
            "vibe": ["artsy", "social", "creative", "vibes"],
            "music": ["indie", "experimental", "alt"],
            "strains": ["Sour Diesel", "G13 Haze", "Cheese"],
            "rating": 4.5,
            "hours": "10:00-01:00",
            "description": "Modern spot with rotating art exhibits and premium extracts"
        },
        {
            "id": 6,
            "name": "Katsu Coffeeshop",
            "address": "Warmoesstraat 35",
            "vibe": ["lit", "party", "dance", "turn-up"],
            "music": ["drum & bass", "EDM", "techno"],
            "strains": ["Blueberry", "Bubble Gum", "Amnesia Core Cut"],
            "rating": 4.4,
            "hours": "9:00-01:00",
            "description": "Energetic De Pijp staple with Moroccan hash specialists"
        },
        {
            "id": 7,
            "name": "Grey Area",
            "address": "Oude Leliestraat 2",
            "vibe": ["hidden", "artsy", "grunge", "edgy"],
            "music": ["underground hip-hop", "trap", "punk"],
            "strains": ["Grey Haze", "Sol Sweet", "Kosher Kush"],
            "rating": 4.9,
            "hours": "12:00-23:00",
            "description": "Tiny legendary spot favored by Snoop Dogg with California imports"
        },
        {
            "id": 8,
            "name": "Barney's Coffeeshop",
            "address": "Haarlemmerstraat 102",
            "vibe": ["luxe", "classy", "bougie", "high-roller"],
            "music": ["jazz fusion", "bossa nova", "lounge"],
            "strains": ["Tangerine Dream", "Cookies Kush", "Morning Glory"],
            "rating": 4.7,
            "hours": "7:00-01:00",
            "description": "Award-winning upscale experience with coffee bar and vaporizers"
        },
        {
            "id": 9,
            "name": "Amnesia",
            "address": "Haarlemmerdijk 33",
            "vibe": ["chill", "cozy", "comfy", "nap-zone"],
            "music": ["downtempo", "chillhop", "ambient"],
            "strains": ["Amnesia Haze", "Crystal Clear", "Lavender"],
            "rating": 4.3,
            "hours": "10:00-22:00",
            "description": "Chill canalside spot famous for its namesake strain"
        },
        {
            "id": 10,
            "name": "Coffeeshop Amsterdam",
            "address": "Rembrandtplein 17",
            "vibe": ["social", "tourist", "scenic", "gram-spot"],
            "music": ["dutch pop", "top 40", "eurodance"],
            "strains": ["Hawaiian Snow", "Mango Haze", "Power Plant"],
            "rating": 4.2,
            "hours": "8:00-23:00",
            "description": "Multi-level hotspot with Rembrandtplein views and extensive menu"
        },
        {
            "id": 11,
            "name": "Boerejongens Center",
            "address": "Utrechtsestraat 21",
            "vibe": ["classy", "techy", "modern", "slick"],
            "music": ["synthwave", "minimal", "electronic"],
            "strains": ["White Choco", "Ice-o-Lator", "Ghost OG"],
            "rating": 4.8,
            "hours": "9:00-00:00",
            "description": "Sleek modern dispensary with pharmacist-style service"
        },
        {
            "id": 12,
            "name": "Coffeeshop Rusland",
            "address": "Marnixstraat 260",
            "vibe": ["rustic", "cozy", "old-school", "retro"],
            "music": ["classical", "folk", "baroque"],
            "strains": ["Super Silver Haze", "Early Girl", "Afghaan"],
            "rating": 4.5,
            "hours": "11:00-21:00",
            "description": "Oldest coffeeshop in Amsterdam with vintage charm"
        },
        {
            "id": 13,
            "name": "The Bulldog",
            "address": "Oudezijds Voorburgwal 90",
            "vibe": ["lit", "party", "iconic", "tourist"],
            "music": ["dance hits", "remixes", "party"],
            "strains": ["White Widow", "Jack Herer", "Sensi Star"],
            "rating": 4.3,
            "hours": "9:00-02:00",
            "description": "World-famous chain with lively atmosphere and branded merchandise"
        },
        {
            "id": 14,
            "name": "1e Hulp",
            "address": "Spuistraat 112",
            "vibe": ["cozy", "homey", "comfy", "blanket-fort"],
            "music": ["soft jazz", "vintage soul", "lofi"],
            "strains": ["Laughing Buddha", "Black Widow", "Shiva"],
            "rating": 4.7,
            "hours": "12:00-22:00",
            "description": "Homey spot with friendly budtenders and strong hashes"
        },
        {
            "id": 15,
            "name": "Siberië",
            "address": "Brouwersgracht 11",
            "vibe": ["chill", "quiet", "study", "focus"],
            "music": ["acoustic", "folk", "soft rock"],
            "strains": ["Siberian Haze", "Orange Bud", "White Russian"],
            "rating": 4.6,
            "hours": "10:00-22:00",
            "description": "Sustainable coffeeshop with organic options and work-friendly space"
        }
    ]

