from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *


@app.route('/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    player_1 = Player("Alex1", player_1_choice)
    player_2 = Player("Alex2", player_2_choice)    
    game = Game()
    winner = game.play(player_1, player_2)
    if winner:
        return render_template('index.html', title='Game Results', result=f"The winner is {winner.name} with {winner.choice}!")
    
    else: return render_template('index.html', title='Game Results', result="DRAW!")


@app.route('/play')
def index():
    return render_template('index.html', title='Game Play')


@app.route('/play', methods=['POST'])
def results():
    player_1 = Player((request.form["player-1-name"]), (request.form["player-1-choice"]))
    player_2 = Player((request.form["player-2-name"]), (request.form["player-2-choice"])) 
    game = Game()
    winner = game.play(player_1, player_2)
    if winner:
        return render_template('index.html', title='Game Results', result=f"The winner is {winner.name} with {winner.choice}!")
    
    else: return render_template('index.html', title='Game Results', result="DRAW!")
