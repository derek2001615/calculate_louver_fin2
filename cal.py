class MultiLouvered:
    def __init__(self, **kwargs):
        self.V_c = kwargs.get('V_c', 3.27)
        self.L_p = kwargs.get('L_p', 0.0017)
        self.viscosity_o = kwargs.get('viscosity_o', 1.85 * 10**-5)
        self.L_alpha = kwargs.get('L_alpha', 23)
        self.F_p = kwargs.get('F_p', 0.0014)
        self.H = kwargs.get('H', 0.00815)
        self.F_d = kwargs.get('F_d', 0.02)
        self.L_l = kwargs.get('L_l', 0.0064)
        self.T_p = kwargs.get('T_p', 0.01015)
        self.delta_f = kwargs.get('delta_f', 0.0001)
        self.Pr_o = kwargs.get('Pr_o', 0.71)
        self.A_o = kwargs.get('A_o', 0.1785)
        self.A_c = kwargs.get('A_c', 0.0084)
        self.density_m = kwargs.get('density_m', 1.225)
        self.Cp_o = kwargs.get('Cp_o', 1007)
        self.T_o2 = kwargs.get('T_o2', 30)
        self.T_o1 = kwargs.get('T_o1', 21)

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
    