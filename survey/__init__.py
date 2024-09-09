from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = ('survey'
                   )
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number = models.IntegerField(label='Participant Number?', min=1, max=50)

    accident = models.IntegerField(
        label="1) Accidents are a serious health problem in any organization?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    accident_avoid = models.IntegerField(
        label="2) Based on your personal opinion, can accidents be avoided?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    safety_level = models.IntegerField(
        label="3) Please identify based on your personal opinion the level of safety in the company.",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    uderst_hazard = models.IntegerField(
        label="4) What do you think - how important is it for employees at all levels "
              "of the organization to be made aware of and able to understand hazards in the workplace?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    tools = models.IntegerField(
        label="5) Do you think that you have all the necessary tools which you need to perform work safely?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    wp_safety = models.IntegerField(
        label="6) Do you think that all devices used at the workplace are safe enough?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    nec_ks = models.IntegerField(
        label="7) Based on your personal opinion, do you have, the necessary knowledge and skills to perform your job?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    ppe = models.IntegerField(
        label="8) Based on your personal opinion, do you have available all the PPEs that you need to perform work safely?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    acc = models.IntegerField(
        label="9) Do you think that Accidents in your company are caused by factors that are out of Employee control?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    wri = models.IntegerField(
        label="10) Based on your personal opinion, are your work-related instructions easily understandable "
              "and are you aware of and do you understand the purpose of work-related instruction?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    inc_safety = models.IntegerField(
        label="11) Do you think that you are somehow personally able to increase of being safe at your workplace/ work?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    dir_lead = models.IntegerField(
        label="12) Do you think that your direct Leader is personally able to influence necessary changes "
              "at the workplace and increase of being safe at your workplace/ work?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    inc_wp_safety = models.IntegerField(
        label="13) Do you think, (if you have an idea) that you can change/ improve your workplace safety "
              "through existing company tools/ procedures?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    atten = models.IntegerField(
        label="14) Do you think that there is enough attention/ appreciation taken to your proposal/ offers "
              "for workplace safety improvements?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )
    listen = models.IntegerField(
        label="15) Do you think that Safety people listen to workers’ ideas and care enough about improving safety?",
        choices=[[i, str(i)] for i in range(1, 6)],
        widget=widgets.RadioSelectHorizontal,
    )

# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['number', 'accident', 'accident_avoid', 'safety_level', 'uderst_hazard', 'tools', 'wp_safety',
                   'nec_ks', 'ppe', 'acc', 'wri', 'inc_safety', 'inc_wp_safety', 'atten', 'listen']

page_sequence = [Demographics]
