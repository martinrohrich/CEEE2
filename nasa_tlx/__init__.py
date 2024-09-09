from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'nasa_tlx'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    part_number = models.IntegerField(label='Participant Number?', min=1, max=50)
    mental_demand = models.IntegerField(
        label="Mental Demand - How mentally demanding was the task?",
        choices=[[i, str(i)] for i in range(1, 21)],
        widget=widgets.RadioSelectHorizontal,
    )
    physical_demand = models.IntegerField(
        label="Physical Demand - How physically demanding was the task?",
        choices=[[i, str(i)] for i in range(1, 21)],
        widget=widgets.RadioSelectHorizontal,
    )
    temporal_demand = models.IntegerField(
        label="Temporal Demand - How hurried or rushed was the pace of the task?",
        choices=[[i, str(i)] for i in range(1, 21)],
        widget=widgets.RadioSelectHorizontal,
    )
    performance = models.IntegerField(
        label="Own Performance - How successful were you in accomplishing what you were asked to do?",
        choices=[[i, str(i)] for i in range(1, 21)],
        widget=widgets.RadioSelectHorizontal,
    )
    effort = models.IntegerField(
        label="Effort - How hard did you have to work to accomplish your level of performance?",
        choices=[[i, str(i)] for i in range(1, 21)],
        widget=widgets.RadioSelectHorizontal,
    )
    frustration = models.IntegerField(
        label="Frustration Level - How insecure, discouraged, irritated, stressed, and annoyed were you?",
        choices=[[i, str(i)] for i in range(1, 21)],
        widget=widgets.RadioSelectHorizontal,
    )

class NASA_TLX(Page):
    form_model = 'player'
    form_fields = ['part_number',
        'mental_demand', 'physical_demand', 'temporal_demand',
        'performance', 'effort', 'frustration'
    ]

page_sequence = [NASA_TLX]
