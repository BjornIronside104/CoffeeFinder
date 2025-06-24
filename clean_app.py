from flask import Flask, render_template, request
from create_coffee_data import get_shops

app = Flask(__name__)
shops = get_shops()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    vibe_input = request.values.get('vibe', '').strip().lower()
    music_input = request.values.get('music', '').strip().lower()
    strain_input = request.values.get('strain', '').strip().lower()

    strains = [s.strip() for s in strain_input.split(',')] if strain_input else []

    filtered = []
    for shop in shops:
        shop_vibes = [v.lower() for v in shop.get('vibe', [])]
        shop_music = [m.lower() for m in shop.get('music', [])]
        shop_strains = [s.lower() for s in shop.get('strains', [])]

        if vibe_input and not any(vibe_input in v for v in shop_vibes):
            continue
        if music_input and not any(music_input in m for m in shop_music):
            continue
        if strains and not any(s in shop_strains for s in strains):
            continue

        filtered.append(shop)

    return render_template('results.html', shops=filtered)

if __name__ == '__main__':
    app.run(debug=True)
