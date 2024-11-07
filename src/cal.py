class MultiLouvered:
    def __init__(self, **kwargs):
        self.V_c = kwargs['V_c']
        self.L_p = kwargs['L_p']
        self.viscosity_o = kwargs['viscosity_o']
        self.L_alpha = kwargs['L_alpha']
        self.F_p = kwargs['F_p']
        self.H = kwargs['H']
        self.F_d = kwargs['F_d']
        self.L_l = kwargs['L_l']
        self.T_p = kwargs['T_p']
        self.delta_f = kwargs['delta_f']
        self.Pr_o = kwargs['Pr_o']
        self.A_o = kwargs['A_o']
        self.A_c = kwargs['A_c']
        self.density_m = kwargs['density_m']
        self.Cp_o = kwargs['Cp_o']
        self.T_o2 = kwargs['T_o2']
        self.T_o1 = kwargs['T_o1']

        self._calc_Re_Lp()
        self._calc_colburn_j_factor()
        self._calc_fanning_friction_factor()
        self._calc_h_o()
 
    def _calc_Re_Lp(self):
        self.Re_Lp = self.V_c * self.L_p / self.viscosity_o
        
    def _calc_colburn_j_factor(self):
        self.j = self.Re_Lp**-0.487 * \
        (self.L_alpha / 90)**0.257 * \
        (self.F_p / self.L_p)**-0.13 * \
        (self.H / self.L_p)**-0.29 * \
        (self.F_d / self.L_p)**-0.235 * \
        (self.L_l / self.L_p)**0.68 * \
        (self.T_p / self.L_p)**-0.279 * \
        (self.delta_f / self.L_p)**-0.05
        
    def _calc_fanning_friction_factor(self):
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

    def _calc_h_o(self):
        self.h_o = self.j * self.density_m * self.V_c * self.Cp_o / self.Pr_o**(2/3)
        
    def cal_heat_transfer(self):
        Q = self.h_o * self.A_o * (self.T_o2 - self.T_o1)
        return Q
    