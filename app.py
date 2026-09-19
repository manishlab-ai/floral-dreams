
from flask import Flask, render_template, session
import os

app = Flask(__name__, template_folder='templates')
app.secret_key = 'super-secret-key-for-floral-dreams'

# E-commerce UI के लिए सैंपल डेटा
cats = [
    {'id': 1, 'name': 'Flowers'},
    {'id': 2, 'name': 'Gifts & Cakes'}
]

pro = [
    {'id': 1, 'name': 'Red Rose Bouquet', 'desc': 'Fresh premium red roses bouquet for all occasions.', 'price': '499'},
    {'id': 2, 'name': 'Orchid Arrangement', 'desc': 'Exotic purple orchids in a stylish glass vase.', 'price': '899'}
]

class DummySession(dict):
    def __getattr__(self, item):
        return self.get(item, None)

@app.before_request
def make_session_compat():
    from flask import request
    dummy = DummySession({'email': None, 'user': None})
    object.__setattr__(request, 'session', dummy)

@app.route('/')
def index():
    return render_template('index.html', cats=cats, pro=pro)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
