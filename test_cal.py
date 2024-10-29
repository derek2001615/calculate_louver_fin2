from cal import MultiLouvered as cal

def set_value():
    return (
        3.27,                         # V_c
        0.0017,                       # L_p
        1.85 * 10**-5,                # viscosity_o
        23,                           # L_alpha
        0.0014,                       # F_p
        0.00815,                      # H
        0.02,                         # F_d
        0.0064,                       # L_l
        0.01015,                      # T_p
        0.0001,                       # delta_f
        0.71,                         # Pr_o
        0.1785,                       # A_o
        0.0084,                       # A_c
        1.225,                        # density_m
        1007,                         # Cp_o
        30,                           # T_o2
        21                            # T_o1
    )

def main():
    data001 = set_value()
    caldata001 = cal(*data001)

    print("Re_Lp:", caldata001.Re_Lp)
    print("Colburn j-factor:", caldata001.j)
    print("Fanning friction factor:", caldata001.f)
    print("Nusselt number:", caldata001.cal_Nusselt_number())
    print("Pressure drop:", caldata001.cal_pressure_drop())
    print("Heat transfer coefficient h_o:", caldata001.h_o)
    print("Heat transfer Q:", caldata001.cal_heat_transfer())

if __name__ == '__main__':
    main()
    