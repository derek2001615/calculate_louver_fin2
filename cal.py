class Cal:
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

    def cal_Re_Lp(self, V_c, L_p, viscosity_o):
        Re = V_c * L_p / viscosity_o
        return Re

    def cal_colburn_j_factor(self, L_alpha, F_p, H, F_d, L_l, T_p, delta_f):
        Re = self.cal_Re_Lp(self.V_c, self.L_p, self.viscosity_o)
        j = Re**-0.487 * (L_alpha / 90)**0.257 * (F_p / self.L_p)**-0.13 * \
            (H / self.L_p)**-0.29 * (F_d / self.L_p)**-0.235 * \
            (L_l / self.L_p)**0.68 * (T_p / self.L_p)**-0.279 * \
            (delta_f / self.L_p)**-0.05
        return j

    def cal_fanning_friction_factor(self, L_alpha, F_p, H, F_d, L_l):
        Re = self.cal_Re_Lp(self.V_c, self.L_p, self.viscosity_o)
        f = Re**-0.781 * (L_alpha / 90)**0.444 * (F_p / self.L_p)**-1.682 * \
            (H / self.L_p)**-1.22 * (F_d / self.L_p)**-0.818 * \
            (L_l / self.L_p)**1.97
        return f

    def cal_Nusselt_number(self, Pr_o):
        j_factor = self.cal_colburn_j_factor(self.L_alpha, self.F_p, self.H, self.F_d, self.L_l, self.T_p, self.delta_f)
        return j_factor * self.cal_Re_Lp(self.V_c, self.L_p, self.viscosity_o) * Pr_o**(1/3)

    def cal_pressure_drop(self, A_o, A_c, density_m, V_c):
        f = self.cal_fanning_friction_factor(self.L_alpha, self.F_p, self.H, self.F_d, self.L_l)
        return f * A_o / A_c * density_m * V_c**2 / 2

    def cal_h_o(self, density_m, V_c, Cp_o, Pr_o):
        j_factor = self.cal_colburn_j_factor(self.L_alpha, self.F_p, self.H, self.F_d, self.L_l, self.T_p, self.delta_f)
        return j_factor * density_m * V_c * Cp_o / Pr_o**(2/3)

    def cal_heat_transfer(self, A_o, T_o2, T_o1):
        h_o = self.cal_h_o(self.density_m, self.V_c, self.Cp_o, self.Pr_o)
        return h_o * A_o * (T_o2 - T_o1)

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
    params = set_value()
    calculator = Cal(*params)

    print("Re_Lp:", calculator.cal_Re_Lp(calculator.V_c, calculator.L_p, calculator.viscosity_o))
    print("Colburn j-factor:", calculator.cal_colburn_j_factor(calculator.L_alpha, calculator.F_p, calculator.H, calculator.F_d, calculator.L_l, calculator.T_p, calculator.delta_f))
    print("Fanning friction factor:", calculator.cal_fanning_friction_factor(calculator.L_alpha, calculator.F_p, calculator.H, calculator.F_d, calculator.L_l))
    print("Nusselt number:", calculator.cal_Nusselt_number(calculator.Pr_o))
    print("Pressure drop:", calculator.cal_pressure_drop(calculator.A_o, calculator.A_c, calculator.density_m, calculator.V_c))
    print("Heat transfer coefficient h_o:", calculator.cal_h_o(calculator.density_m, calculator.V_c, calculator.Cp_o, calculator.Pr_o))
    print("Heat transfer Q:", calculator.cal_heat_transfer(calculator.A_o, calculator.T_o2, calculator.T_o1))

if __name__ == '__main__':
    main()
