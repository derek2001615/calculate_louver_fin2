import sys
import os
sys.path.append(r"C:\Users\derek\Desktop\pythoncode\calculate_louver_fin2\src\calvalue")

from val1 import calculate_fanning_friction_factor_values001 as f1
from val1 import calculate_fanning_friction_factor_values002 as f2
from val1 import calculate_fanning_friction_factor_values003 as f3
from val1 import calculate_fanning_friction_factor_values004 as f4
from val1 import calculate_Re_Lp_values as Re_Lp

import plotly.graph_objects as go

Re_Lp_values = Re_Lp()
f1_values = f1()
f2_values = f2()
f3_values = f3()
f4_values = f4()

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=Re_Lp_values, y=f1_values, mode='lines+markers', name='23 degree', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=f2_values, mode='lines+markers', name='25 degree', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=f3_values, mode='lines+markers', name='27 degree', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=f4_values, mode='lines+markers', name='29 degree', line=dict(shape='spline')))

fig1.update_layout(title="Fd=20mm", xaxis_title="Re_Lp", yaxis_title="fanning_friction_factor", template="plotly_dark")

fig1.show()
fig1.write_html("F_d20_f.html")

