from utils import load_contributions_sequence_from_excel
from utils import load_contributions_sequence
from collections import defaultdict
import os

load_from_excel: str = os.environ.get('GITCOIN_LOAD_EXCEL')
if load_from_excel == 'yes':
    CONTRIBUTIONS_SEQUENCE = load_contributions_sequence_from_excel('../data/alternate_data.xls')
else:
    timesteps = os.environ.get('GITCOIN_TIMESTEPS')
    if timesteps == 'all':
        CONTRIBUTIONS_SEQUENCE: dict = load_contributions_sequence(None)
    else:
        CONTRIBUTIONS_SEQUENCE: dict = load_contributions_sequence(int(timesteps))
        

sys_params = {
    'contribution_sequence': [CONTRIBUTIONS_SEQUENCE],
    'trust_bonus_per_user': [defaultdict(lambda: 1.0)],
    'v_threshold': [25],
    'simple_threshold': [25],
    'total_pot': [450000]
}