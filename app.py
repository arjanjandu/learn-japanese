from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import random
import time
import os

app = Flask(__name__)
CORS(app)

hiragana = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n'
}

katakana = {
    'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
    'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
    'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
    'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to',
    'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
    'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho',
    'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
    'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo',
    'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',
    'ワ': 'wa', 'ヲ': 'wo', 'ン': 'n'
}

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/get_kana', methods=['GET'])
def get_kana():
    return jsonify({
        'hiragana': list(hiragana.items()),
        'katakana': list(katakana.items())
    })

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data['answer']
    kana_char = data['kana']
    kana_type = data['type']
    
    correct_answer = hiragana[kana_char] if kana_type == 'hiragana' else katakana[kana_char]
    is_correct = user_answer.lower() == correct_answer.lower()
    return jsonify({'correct': is_correct, 'correct_answer': correct_answer})

@app.route('/start_timer', methods=['GET'])
def start_timer():
    return jsonify({'start_time': time.time()})

@app.route('/end_timer', methods=['POST'])
def end_timer():
    data = request.json
    start_time = data['start_time']
    end_time = time.time()
    duration = end_time - start_time
    return jsonify({'duration': duration})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)