class MultiLouvered:
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
        self.cal_Re_Lp()
        self.cal_colburn_j_factor()
        self.cal_fanning_friction_factor()
        self.cal_h_o()

    def cal_Re_Lp(self):
        self.Re_Lp = self.V_c * self.L_p / self.viscosity_o
        
    def cal_colburn_j_factor(self):
        Re_Lp = self.Re_Lp
        self.j = Re_Lp**-0.487 * \
        (self.L_alpha / 90)**0.257 * \
        (self.F_p / self.L_p)**-0.13 * \
        (self.H / self.L_p)**-0.29 * \
        (self.F_d / self.L_p)**-0.235 * \
        (self.L_l / self.L_p)**0.68 * \
        (self.T_p / self.L_p)**-0.279 * \
        (self.delta_f / self.L_p)**-0.05
        
    def cal_fanning_friction_factor(self):
        self.f = self.Re_Lp**-0.781 * \
        (self.L_alpha / 90)**0.444 * \
        (self.F_p / self.L_p)**-1.682 * \
        (self.H / self.L_p)**-1.22 * \
        (self.F_d / self.L_p)**0.818 * \
        (self.L_l / self.L_p)**1.97

    def cal_Nusselt_number(self):
        Nu = self.j * self.Re_Lp * self.Pr_o**(1/3)
        return Nu

    def cal_pressure_drop(self):
        delta_P = self.f * self.A_o / self.A_c * self.density_m * self.V_c**2 / 2
        return delta_P

    def cal_h_o(self):
        self.h_o = self.j * self.density_m * self.V_c * self.Cp_o / self.Pr_o**(2/3)
        
    def cal_heat_transfer(self):
        Q = self.h_o * self.A_o * (self.T_o2 - self.T_o1)
        return Q
    