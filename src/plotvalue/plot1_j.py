import sys
import os
sys.path.append(r"C:\Users\derek\Desktop\pythoncode\calculate_louver_fin2\src\calvalue")

from val1 import calculate_colburn_j_factor_values001 as j1
from val1 import calculate_colburn_j_factor_values002 as j2
from val1 import calculate_colburn_j_factor_values003 as j3
from val1 import calculate_colburn_j_factor_values004 as j4
from val1 import calculate_Re_Lp_values as Re_Lp

import plotly.graph_objects as go

Re_Lp_values = Re_Lp()
j1_values = j1()
j2_values = j2()
j3_values = j3()
j4_values = j4()

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=Re_Lp_values, y=j1_values, mode='lines+markers', name='23 degree', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=j2_values, mode='lines+markers', name='25 degree', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=j3_values, mode='lines+markers', name='27 degree', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_Lp_values, y=j4_values, mode='lines+markers', name='29 degree', line=dict(shape='spline')))

fig1.update_layout(title="Fd=16mm", xaxis_title="Re_Lp", yaxis_title="colburn_j_factor", template="plotly_dark")

fig1.show()
fig1.write_html("F_d16_j.html")

