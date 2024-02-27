
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

colors = ["#70CAD1","#7EBC89","#FE5D26","#8338ec"]
colors = ["#0000ff","#cd34b5","#fa8775","#ffd700"]

def load_style():
    plt.style.use('paper.mplstyle')
    matplotlib.rcParams.update({'text.usetex': True})
    matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
    matplotlib.rcParams['figure.facecolor'] = 'white' 

# READING THE BACKGROUND

cols_bkg_nufld = ['z','t','tau','H','x','Dang','Dlum','rs','rho_g', 'rho_b','rho_cdm', 
                  'rho_nufld[0]', 'p_nufld[0]', 'w_nufld[0]', 
                  'w_prime_nufld[0]', 'w_mass_nufld[0]', 'w_prime_mass_nufld[0]',
                  'rho_lambda', 'rho_ur', 'rho_crit',
                  'rho_tot', 'p_tot', 'p_tot_prime', 'gr.fac.D', 'gr.fac.f']

cols_bkg_ncdm =  ['z','t','tau','H','x','Dang','Dlum','rs','rho_g', 'rho_b','rho_cdm', 
                  'rho_ncdm[0]', 'p_ncdm[0]', 'rho_lambda', 'rho_ur', 'rho_crit',
                  'rho_tot', 'p_tot', 'p_tot_prime', 'gr.fac.D', 'gr.fac.f']

def class_bkgout_to_df(file, cols = cols_bkg_nufld):
    with open(file, 'r+') as myfile:
        lines = []
        i = 0
        for line in myfile.readlines():
            if i < 4:
                i += 1
                continue
            # print(line.strip().split("\t"))
            lines.append(line.strip().split("      "))

    npbkgdata = np.array(lines, dtype=np.float64)
    bkgdata = pd.DataFrame(npbkgdata,columns=cols)
    return bkgdata

# READING FUNCTIONS(k) OF PERTURBATIONS

cols_vars_ncdm = ['tau', 'a', 'delta_g', 'theta_g', 'shear_g', 'pol0_g', 'pol1_g', 'pol2_g',
                  'delta_b', 'theta_b', 'psi', 'phi',
                  'delta_ur', 'theta_ur', 'shear_ur', 
                  'delta_cdm', 'theta_cdm',
                  'delta_ncdm[0]', 'theta_ncdm[0]', 'shear_ncdm[0]', 'cs2_ncdm[0]']

cols_vars_nufld = ['tau', 'a', 'delta_g', 'theta_g', 'shear_g', 'pol0_g', 'pol1_g', 'pol2_g',
                   'delta_b', 'theta_b', 'psi', 'phi',
                   'delta_ur', 'theta_ur', 'shear_ur', 
                   'delta_cdm', 'theta_cdm',
                   'delta_nufld[0]', 'theta_nufld[0]', 'shear_nufld[0]', 'cs2_gauge[0]', 'cs2_fluid[0]']

def class_pertvars_to_df(file, cols = cols_vars_nufld):
    with open(file, 'r+') as myfile:
        lines = []
        i = 0
        for line in myfile.readlines():
            if i < 2:
                i += 1
                continue
            # print(line.strip().split("\t"))
            lines.append(line.strip().split("      "))

    npbkgdata = np.array(lines, dtype=np.float64)
    bkgdata = pd.DataFrame(npbkgdata,columns=cols)
    return bkgdata


# READ CMB

cols_cls = ['l', 'TT', 'EE', 'TE', 'BB', 'phiphi', 'TPhi', 'Ephi']

def class_clout_to_df(file):
    with open(file, 'r+') as myfile:
        lines = []
        i = 0
        for line in myfile.readlines():
            if i < 11:
                i += 1
                continue
            # print(line.strip().split("\t"))
            lines.append(line.strip().split("      "))

    npbkgdata = np.array(lines, dtype=np.float64)
    bkgdata = pd.DataFrame(npbkgdata,columns=cols_cls)
    return bkgdata

# READ POWER SPECTRUM

cols_pk = ['k', 'P']
def class_pkout_to_df(file):
    with open(file, 'r+') as myfile:
        lines = []
        i = 0
        for line in myfile.readlines():
            if i < 4:
                i += 1
                continue
            # print(line.strip().split("\t"))
            lines.append(line.strip().split("      "))

    npbkgdata = np.array(lines, dtype=np.float64)
    bkgdata = pd.DataFrame(npbkgdata,columns=cols_pk)
    return bkgdata


# READ TRANSFER FUNCTIONS TODAY

cols_tk = ['k', 'd_g', 'd_b', 'd_cdm', 'd_ur', 'd_ncdm','d_m','d_tot','phi','psi','t_g','t_b', 't_ur', 't_ncdm', 't_tot']
def class_tkout_to_df(file):
    with open(file, 'r+') as myfile:
        lines = []
        i = 0
        for line in myfile.readlines():
            if i < 11:
                i += 1
                continue
            # print(line.strip().split("\t"))
            lines.append(line.strip().split("      "))

    nptkdata = np.array(lines, dtype=np.float64)
    tkdata = pd.DataFrame(nptkdata,columns=cols_tk)
    return tkdata