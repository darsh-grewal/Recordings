import physiolabxr as xr
from physiolabxr.utils.RNStream import RNStream


stream = RNStream('10_02_2025_12_15_58-Exp_W1-Sbj_darsh-Ssn_0.dats')
print(len(stream.stream_in(jitter_removal=False)['Explore_8443_ExG'][0]))
