from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')

# E-commerce UI के लिए सैंपल डेटा
cats = [
    {'id': 1, 'name': 'Flowers'},
    {'id': 2, 'name': 'Gifts & Cakes'},
    {'id': 3, 'name': 'Personalized Offers'}
]

pro = [
    {'id': 1, 'name': 'Red Rose Bouquet', 'desc': 'Fresh premium red roses bouquet for all occasions.', 'price': '499'},
    {'id': 2, 'name': 'Orchid Arrangement', 'desc': 'Exotic purple orchids in a stylish glass vase.', 'price': '899'},
    {'id': 3, 'name': 'Chocolate & Flower Combo', 'desc': 'Assorted chocolates with fresh pink carnations.', 'price': '1299'}
]

@app.route('/')
def index():
    return render_template('index.html', cats=cats, pro=pro)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
