import sys
import os
sys.path.append(r"C:\Users\derek\Desktop\pythoncode\calculate_louver_fin2\src\calvalue")

from val1 import calculate_fanning_friction_factor_values001 as f1
from val1 import calculate_fanning_friction_factor_values002 as f2
from val1 import calculate_fanning_friction_factor_values003 as f3
from val1 import calculate_fanning_friction_factor_values004 as f4

from val1 import calculate_colburn_j_factor_values001 as j1
from val1 import calculate_colburn_j_factor_values002 as j2
from val1 import calculate_colburn_j_factor_values003 as j3
from val1 import calculate_colburn_j_factor_values004 as j4

from val1 import calculate_Re_Lp_values as Re_Lp

import plotly.graph_objects as go

Re_Lp_values = Re_Lp()
f1_values = f1()
f2_values = f2()
f3_values = f3()
f4_values = f4()

Re_Lp_values = Re_Lp()
j1_values = j1()
j2_values = j2()
j3_values = j3()
j4_values = j4()

f_min = min(min(f1_values), min(f2_values), min(f3_values), min(f4_values))
f_max = max(max(f1_values), max(f2_values), max(f3_values), max(f4_values))
j_min = min(min(j1_values), min(j2_values), min(j3_values), min(j4_values))
j_max = max(max(j1_values), max(j2_values), max(j3_values), max(j4_values))

min_y = min(f_min, j_min)
max_y = max(f_max, j_max)

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=Re_Lp_values, y=f1_values, mode='lines+markers', name='23 degree', yaxis='y1', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=f2_values, mode='lines+markers', name='25 degree', yaxis='y1', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=f3_values, mode='lines+markers', name='27 degree', yaxis='y1', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=f4_values, mode='lines+markers', name='29 degree', yaxis='y1', line=dict(shape='spline')))

fig1.add_trace(go.Scatter(x=Re_Lp_values, y=j1_values, mode='lines+markers', name='23 degree', yaxis='y2', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=j2_values, mode='lines+markers', name='25 degree', yaxis='y2', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=j3_values, mode='lines+markers', name='27 degree', yaxis='y2', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=j4_values, mode='lines+markers', name='29 degree', yaxis='y2', line=dict(shape='spline')))



fig1.update_layout(
    title="Fd=16mm",
    xaxis=dict(title='Re_Lp'), 
    yaxis=dict(
        title='fanning_friction_factor',
        range=[min_y, max_y]
    ),
    yaxis2=dict(
        title='colburn_j_factor',
        overlaying='y',
        side='right',
        range=[min_y, max_y]
    ), 
    template="plotly_dark"
    )

fig1.show()
fig1.write_html("F_d16.html")

