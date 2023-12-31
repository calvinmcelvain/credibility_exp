from otree.api import *


doc = """
Stage 2 Decision 1 Instructions
"""


class C(BaseConstants):
    NAME_IN_URL = 'STG2_D1_BGN'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Timeout seconds
    instructions_time = None
    standby_time = None

    # Decision Payoff dictionaries
    pb_payoff = {
        1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
        3: {1: 300, 2: 300, 3: 300, 4: 300, 5: 300},
    }
    pa_payoff = {
        1: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300},
        3: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300}
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Page continue validation field
    all_players_ready = models.IntegerField(initial=0)


class Player(BasePlayer):
    pass


# PAGES
class P1(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P2(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P3(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P4_standby(Page):
    timeout_seconds = C.standby_time

    @staticmethod
    def vars_for_template(player: Player):
        if player.participant.vars['role'] == 'Advisor':
            return {'role': 'Advisor'}
        else:
            return {'role': 'Investor'}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


page_sequence = [P1, P2, P3, P4_standby]
