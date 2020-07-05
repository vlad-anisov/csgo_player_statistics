from odoo import models, fields
from ..hltv_api.main import get_top_players

class Player(models.Model):
    _name = 'csgo_player_statistics.player'
    _description = 'Player'

    country = fields.Char(String='Country', required=True)
    name = fields.Char(string="Name", required=True)
    nickname = fields.Char(string="Nickname", required=True)
    rating = fields.Float(string="Rating", required=True)
    maps_played = fields.Integer(string="Maps played", required=True)

    def update_players(self):
        players = self.env['csgo_player_statistics.player']
        players.search([]).unlink()
        players.create(get_top_players())
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }
