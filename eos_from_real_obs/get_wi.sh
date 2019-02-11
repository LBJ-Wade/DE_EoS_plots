#!/bin/bash

# awk 'NR==9, NR==28' '../DDE_wmap9/dist/snls3_bao_hz_h0_a_2.0_sm_0.04.margestats' | \
# awk '{print $2,$3}' > 'wmap9_snls3_bao_hz_h0_a_2.0_sm_0.04.txt'
#
# awk 'NR==9, NR==28' '../DDE_check/dist/snls3_bao_hz_h0_a_2.0_sm_0.02.margestats' | \
# awk '{print $2,$3}' > 'wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.02.txt'
#
# awk 'NR==9, NR==28' '../DDE_check/dist/snls3_bao_hz_h0_a_2.0_sm_0.04.margestats' | \
# awk '{print $2,$3}' > 'wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.04.txt'
#
# awk 'NR==9, NR==28' '../DDE_check/dist/snls3_bao_hz_h0_a_2.0_sm_0.08.margestats' | \
# awk '{print $2,$3}' > 'wmap9dp_snls3_bao_hz_h0_a_2.0_sm_0.08.txt'
#
# awk 'NR==10, NR==29' '../DDE_plk2015/dist/snls3_bao_hz_h0_a_2.0_sm_0.04.margestats' | \
# awk '{print $2,$3}' > 'plk2015_snls3_bao_hz_h0_a_2.0_sm_0.04.txt'

awk 'NR==7, NR==26' '../DDE_wmap9/dist/union_bao_hz_h0_a_2.0_sm_0.02.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'wmap9dp_union_bao_hz_h0_a_2.0_sm_0.02.txt'

awk 'NR==7, NR==26' '../DDE_wmap9/dist/union_bao_hz_h0_a_2.0_sm_0.04.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'wmap9dp_union_bao_hz_h0_a_2.0_sm_0.04.txt'


awk 'NR==11, NR==30' '../DDE_wmap9/dist/jla_bao_hz_h0_a_2.0_sm_0.02.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'wmap9dp_jla_bao_hz_h0_a_2.0_sm_0.02.txt'

awk 'NR==11, NR==30' '../DDE_wmap9/dist/jla_bao_hz_h0_a_2.0_sm_0.04.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'wmap9dp_jla_bao_hz_h0_a_2.0_sm_0.04.txt'

awk 'NR==11, NR==30' '../DDE_wmap9/dist/jla_bao_hz_a_2.0_sm_0.02_0.04.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'wmap9dp_jla_bao_hz_a_2.0_sm_0.02_0.04.txt'

awk 'NR==9, NR==28' '../DDE_wmap9/dist/snls3_bao_hz_h0_a_2.0_sm_0.04.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'wmap9_snls3_bao_hz_h0_a_2.0_sm_0.04.txt'

awk 'NR==9, NR==28' '../DDE_wmap9/dist/snls3_bao_hz_h0_a_2.0_sm_0.04_wider_w_range.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'wmap9_snls3_bao_hz_h0_a_2.0_sm_0.04.txt_0'

awk 'NR==9, NR==28' '../DDE_check/dist/snls3_bao_hz_h0_a_2.0_sm_0.02.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.02.txt'

awk 'NR==9, NR==28' '../DDE_check/dist/snls3_bao_hz_h0_a_2.0_sm_0.04.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.04.txt'

awk 'NR==9, NR==28' '../DDE_check/dist/snls3_bao_hz_h0_a_2.0_sm_0.08.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'wmap9dp_snls3_bao_hz_h0_a_2.0_sm_0.08.txt'

awk 'NR==10, NR==29' '../DDE_plk2015/dist/snls3_bao_hz_h0_a_2.0_sm_0.04.margestats' | \
awk '{print $2,$3,$4,$5,$7,$8}' > 'plk2015_snls3_bao_hz_h0_a_2.0_sm_0.04.txt'
