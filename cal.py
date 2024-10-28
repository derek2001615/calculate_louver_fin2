class cal:
    def __init__(self, V_c, L_p, viscosity_o, L_alpha, F_p, H, F_d, L_l, T_p, delta_f, Pr_o, A_o, A_c, density_m, Cp_o, T_o2, T_o1):
        self.V_c = V_c
        self.L_p = L_p
        self.viscosity_o = viscosity_o
        self.L_alpha = L_alpha
        self.F_p = F_p
        self.H = H
        self.F_d = F_d
        self.L_l = L_l
        self.T_p = T_p
        self.delta_f = delta_f
        self.Pr_o = Pr_o
        self.A_o = A_o
        self.A_c = A_c
        self.density_m = density_m
        self.Cp_o = Cp_o
        self.T_o2 = T_o2
        self.T_o1 = T_o1

    def cal_Re_Lp(self):
        Re = self.V_c * self.L_p / self.viscosity_o
        return Re

    def cal_colburn_j_factor(self):
        j = self.cal_Re_Lp()**-0.487 * \
        (self.L_alpha / 90)**0.257 * \
        (self.F_p / self.L_p)**-0.13 * \
        (self.H / self.L_p)**-0.29 * \
        (self.F_d / self.L_p)**-0.235 * \
        (self.L_l / self.L_p)**0.68 * \
        (self.T_p / self.L_p)**-0.279 * \
        (self.delta_f / self.L_p)**-0.05
        return j

    def cal_fanning_friction_factor(self):
        f = self.cal_Re_Lp()**-0.781 * \
        (self.L_alpha / 90)**0.444 * \
        (self.F_p / self.L_p)**-1.682 * \
        (self.H / self.L_p)**-1.22 * \
        (self.F_d / self.L_p)**-0.818 * \
        (self.L_l / self.L_p)**1.97
        return f

    def cal_Nusselt_number(self):
        Nu = self.cal_colburn_j_factor() * self.cal_Re_Lp() * self.Pr_o**(1/3)
        return Nu

    def cal_pressure_drop(self):
        delta_P = self.cal_fanning_friction_factor() * self.A_o / self.A_c * self.density_m * self.V_c**2 / 2
        return delta_P

    def cal_h_o(self):
        h_O = self.cal_colburn_j_factor() * self.density_m * self.V_c * self.Cp_o / self.Pr_o**(2/3)
        return h_O

    def cal_heat_transfer(self):
        Q = self.cal_h_o() * self.A_o * (self.T_o2 - self.T_o1)
        return Q

def set_value():
    return (
        3.27,                         # V_c
        0.0017,                       # L_p
        1.85 * 10**-5,                # viscosity_o
        25,                           # L_alpha
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

    print("Re_Lp:", caldata001.cal_Re_Lp())
    print("Colburn j-factor:", caldata001.cal_colburn_j_factor())
    print("Fanning friction factor:", caldata001.cal_fanning_friction_factor())
    print("Nusselt number:", caldata001.cal_Nusselt_number())
    print("Pressure drop:", caldata001.cal_pressure_drop())
    print("Heat transfer coefficient h_o:", caldata001.cal_h_o())
    print("Heat transfer Q:", caldata001.cal_heat_transfer())

if __name__ == '__main__':
    main()
