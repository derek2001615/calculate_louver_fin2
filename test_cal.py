from cal import MultiLouvered as cal

def get_data001():
    return {
        'V_c': 3.27,
        'L_p': 0.0017,
        'viscosity_o': 1.85 * 10**-5,
        'L_alpha': 23,
        'F_p': 0.0014,
        'H': 0.00815,
        'F_d': 0.02,
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

def get_data002():
    return {}

def main():
    data001 = get_data001()
    caldata001 = cal(**data001)

    print("Re_Lp:", caldata001.Re_Lp)
    print("Colburn j-factor:", caldata001.j)
    print("Fanning friction factor:", caldata001.f)
    print("Nusselt number:", caldata001.cal_Nusselt_number())
    print("Pressure drop:", caldata001.cal_pressure_drop())
    print("Heat transfer coefficient h_o:", caldata001.h_o)
    print("Heat transfer Q:", caldata001.cal_heat_transfer())


    data002 = get_data002()
    caldata002 = cal(**data002)

    print("Re_Lp:", caldata002.Re_Lp)
    print("Colburn j-factor:", caldata002.j)
    print("Fanning friction factor:", caldata002.f)
    print("Nusselt number:", caldata002.cal_Nusselt_number())
    print("Pressure drop:", caldata002.cal_pressure_drop())
    print("Heat transfer coefficient h_o:", caldata002.h_o)
    print("Heat transfer Q:", caldata002.cal_heat_transfer())


if __name__ == '__main__':
    main()
    