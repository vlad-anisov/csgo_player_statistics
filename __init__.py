from . import models
from odoo.api import Environment, SUPERUSER_ID
from .hltv_api.main import get_top_players

def load_players(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    env['csgo_player_statistics.player'].create(get_top_players())