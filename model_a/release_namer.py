import random

from flask import Flask, render_template, redirect

from utils import ClueLogger

app = Flask(__name__)


pokemon_names = ['Bulbasaurdagger', 'Ivysaur', 'Venusaur', 'Charmanderdagger', 'Charmeleon', 'Charizard',
                 'Squirtledagger', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle',
                 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow',
                 'Fearow', 'Ekans', 'Arbok', 'Pikachudagger', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidora',
                 'Nidorina', 'Nidoqueen', 'Nidora', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix',
                 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume',
                 'Paras', 'Parasect', 'Venonat']

adjectives = ['Adamant', 'Adroit', 'Amatory', 'Animistic', 'Antic', 'Arcadian', 'Baleful', 'Bellicose', 'Bilious',
              'Boorish', 'Calamitous', 'Caustic', 'Cerulean', 'Comely', 'Concomitant', 'Contumacious', 'Corpulent',
              'Crapulous', 'Defamatory', 'Didactic', 'Dilatory', 'Dowdy', 'Efficacious', 'Effulgent', 'Egregious',
              'Endemic', 'Equanimous', 'Execrable', 'Fastidious', 'Feckless', 'Fecund', 'Friable', 'Fulsome',
              'Garrulous', 'Guileless', 'Gustatory', 'Heuristic', 'Histrionic', 'Hubristic', 'Incendiary', 'Insidious',
              'Insolent', 'Intransigent', 'Inveterate', 'Invidious', 'Irksome', 'Jejune', 'Jocular', 'Judicious',
              'Lachrymose', 'Limpid', 'Loquacious', 'Luminous', 'Mannered', 'Mendacious', 'Meretricious', 'Minatory',
              'Mordant', 'Munificent', 'Nefarious', 'Noxious', 'Obtuse', 'Parsimonious', 'Pendulous', 'Pernicious',
              'Pervasive', 'Petulant', 'Platitudinous', 'Precipitate', 'Propitious', 'Puckish', 'Querulous',
              'Quiescent', 'Rebarbative', 'Recalcitrant', 'Redolent', 'Rhadamanthine', 'Risible', 'Ruminative',
              'Sagacious', 'Salubrious', 'Sartorial', 'Sclerotic', 'Serpentine', 'Spasmodic', 'Strident', 'Taciturn',
              'Tenacious', 'Tremulous', 'Trenchant', 'Turbulent', 'Turgid', 'Ubiquitous', 'Uxorious', 'Verdant',
              'Voluble', 'Voracious', 'Wheedling', 'Withering']


def generate_name():
    poke = random.choice(pokemon_names)
    adj = random.choice(adjectives)
    return f'{adj}_{poke}'.lower()


@app.route('/')
def index():
    name = generate_name()
    return render_template('index.html', title='Home', name=name)


@app.route('/feedback/<model>/<feedback>/')
def collect_feedback(model, feedback):
    logger.out(model, feedback)
    return redirect("/", code=302)


@app.route('/healthcheck/')
def healthcheck():
    return "I'm okay"


if __name__ == '__main__':
    logger = ClueLogger(block='var_namer', model='model_b')
    app.run(host='0.0.0.0', port=5000)
