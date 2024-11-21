import sys
import os
sys.path.append(r"C:\Users\derek\Desktop\pythoncode\calculate_louver_fin2\src")

import numpy as np
from cal import MultiLouvered as cal

def get_data001():
    return {
        'V_c': None,
        'L_p': 0.0017,
        'viscosity_o': 1.85 * 10**-5,
        'L_alpha': 23,
        'F_p': 0.0014,
        'H': 0.00815,
        'F_d': 0.024,
        'L_l': 0.0064,
        'T_p': 0.01015,
        'delta_f': 0.0001,
        'Pr_o': 0.71,
        'A_o': 0.1785,
        'A_c': 0.0084,
        'density_m': 1.225,
        'Cp_o': 1007,
        'T_o2': 30,
        'T_o1': 21
    }

def calculate_colburn_j_factor_values001():
    data = get_data001()
    V_c_values = [1.09, 2.18, 3.27, 4.36, 5.45]
    j_values = []

    for V_c in V_c_values:
        data['V_c'] = V_c  
        multi_louvered = cal(**data)  
        j_values.append(multi_louvered.j)  

    return np.array(j_values)

def calculate_fanning_friction_factor_values001():
    data = get_data001()
    V_c_values = [1.09, 2.18, 3.27, 4.36, 5.45]
    f_values = []

    for V_c in V_c_values:
        data['V_c'] = V_c  
        multi_louvered = cal(**data)  
        f_values.append(multi_louvered.f)  

    return np.array(f_values)

def calculate_Re_Lp_values():
    data = get_data001()
    V_c_values = [1.09, 2.18, 3.27, 4.36, 5.45]
    Re_Lp_values = []

    for V_c in V_c_values:
        data['V_c'] = V_c  
        multi_louvered = cal(**data)  
        Re_Lp_values.append(multi_louvered.Re_Lp)  

    return np.array(Re_Lp_values)

def get_data002():
    return {
        'V_c': None,
        'L_p': 0.0017,
        'viscosity_o': 1.85 * 10**-5,
        'L_alpha': 25,
        'F_p': 0.0014,
        'H': 0.00815,
        'F_d': 0.024,
        'L_l': 0.0064,
        'T_p': 0.01015,
        'delta_f': 0.0001,
        'Pr_o': 0.71,
        'A_o': 0.1785,
        'A_c': 0.0084,
        'density_m': 1.225,
        'Cp_o': 1007,
        'T_o2': 30,
        'T_o1': 21
    }

def calculate_colburn_j_factor_values002():
    data = get_data002()
    V_c_values = [1.09, 2.18, 3.27, 4.36, 5.45]
    j_values = []

    for V_c in V_c_values:
        data['V_c'] = V_c  
        multi_louvered = cal(**data)  
        j_values.append(multi_louvered.j)  

    return np.array(j_values)

def calculate_fanning_friction_factor_values002():
    data = get_data002()
    V_c_values = [1.09, 2.18, 3.27, 4.36, 5.45]
    f_values = []

    for V_c in V_c_values:
        data['V_c'] = V_c  
        multi_louvered = cal(**data)  
        f_values.append(multi_louvered.f)  

    return np.array(f_values)

def get_data003():
    return {
        'V_c': None,
        'L_p': 0.0017,
        'viscosity_o': 1.85 * 10**-5,
        'L_alpha': 27,
        'F_p': 0.0014,
        'H': 0.00815,
        'F_d': 0.024,
        'L_l': 0.0064,
        'T_p': 0.01015,
        'delta_f': 0.0001,
        'Pr_o': 0.71,
        'A_o': 0.1785,
        'A_c': 0.0084,
        'density_m': 1.225,
        'Cp_o': 1007,
        'T_o2': 30,
        'T_o1': 21
    }

def calculate_colburn_j_factor_values003():
    data = get_data003()
    V_c_values = [1.09, 2.18, 3.27, 4.36, 5.45]
    j_values = []

    for V_c in V_c_values:
        data['V_c'] = V_c  
        multi_louvered = cal(**data)  
        j_values.append(multi_louvered.j)  

    return np.array(j_values)

def calculate_fanning_friction_factor_values003():
    data = get_data003()
    V_c_values = [1.09, 2.18, 3.27, 4.36, 5.45]
    f_values = []

    for V_c in V_c_values:
        data['V_c'] = V_c  
        multi_louvered = cal(**data)  
        f_values.append(multi_louvered.f)  

    return np.array(f_values)

def get_data004():
    return {
        'V_c': None,
        'L_p': 0.0017,
        'viscosity_o': 1.85 * 10**-5,
        'L_alpha': 29,
        'F_p': 0.0014,
        'H': 0.00815,
        'F_d': 0.024,
        'L_l': 0.0064,
        'T_p': 0.01015,
        'delta_f': 0.0001,
        'Pr_o': 0.71,
        'A_o': 0.1785,
        'A_c': 0.0084,
        'density_m': 1.225,
        'Cp_o': 1007,
        'T_o2': 30,
        'T_o1': 21
    }

def calculate_colburn_j_factor_values004():
    data = get_data004()
    V_c_values = [1.09, 2.18, 3.27, 4.36, 5.45]
    j_values = []

    for V_c in V_c_values:
        data['V_c'] = V_c  
        multi_louvered = cal(**data)  
        j_values.append(multi_louvered.j)  

    return np.array(j_values)

def calculate_fanning_friction_factor_values004():
    data = get_data004()
    V_c_values = [1.09, 2.18, 3.27, 4.36, 5.45]
    f_values = []

    for V_c in V_c_values:
        data['V_c'] = V_c  
        multi_louvered = cal(**data)  
        f_values.append(multi_louvered.f)  

    return np.array(f_values)

