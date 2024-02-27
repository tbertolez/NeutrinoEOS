import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# THIS PLOTS OUTPUT_BACKGROUND FILES FROM CLASS, E.G. PRESSURE/DENSITY, EQUATION OF STATE

plt.style.use('paper.mplstyle')
matplotlib.rcParams.update({'text.usetex': True})
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
matplotlib.rcParams['figure.facecolor'] = 'white'

cols_nufld = ['z','t','tau','H','x','Dang','Dlum','rs','rho_g', 'rho_b','rho_cdm', 'rho_nufld[0]', 'p_nufld[0]', 'w_nufld[0]', 'w_prime_nufld[0]', 'w_mass_nufld[0]', 'w_prime_mass_nufld[0]',
              'rho_lambda', 'rho_ur', 'rho_crit',
              'rho_tot', 'p_tot', 'p_tot_prime', 'gr.fac.D', 'gr.fac.f']
cols_ncdm = ['z','t','tau','H','x','Dang','Dlum','rs','rho_g', 'rho_b','rho_cdm', 'rho_ncdm[0]', 'p_ncdm[0]', 'rho_lambda', 'rho_ur', 'rho_crit',
        'rho_tot', 'p_tot', 'p_tot_prime', 'gr.fac.D', 'gr.fac.f']

def class_bkgout_to_df(file, cols = cols_nufld):
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

# 1eV

# bkg_lcdm  = class_bkgout_to_df('output/lcdm_background.dat')
nufld = class_bkgout_to_df('class_nufld/output/default_nufld_background.dat')
ncdm  = class_bkgout_to_df('class_nufld/output/default_ncdm_background.dat', cols=cols_ncdm)

# bkg_class = class_bkgout_to_df('output/class_fla_background.dat')
# bkg_caio  = class_bkgout_to_df('output/caio_fla_background.dat')

fig_rho, ax_rho = plt.subplots(figsize=(6,5))
ax_rho.plot(1/(nufld['z']+1), nufld['rho_nufld[0]']/(nufld['z']+1)**3, color = 'k', lw = 3, label = r'$\rho,\, m = 0.01\, \mathrm{eV}$')
ax_rho.plot(1/(nufld['z']+1), nufld['p_nufld[0]']/(nufld['z']+1)**3, color = 'k', lw = 3, ls = '--', label = r'$p,\, m= 0.01\, \mathrm{eV}$')
ax_rho.plot(1/(ncdm['z']+1), ncdm['rho_ncdm[0]']/(ncdm['z']+1)**3, color = 'b', lw = 2, label = r'$\rho,\, \mathrm{Caio}$')
ax_rho.plot(1/(ncdm['z']+1), ncdm['p_ncdm[0]']/(ncdm['z']+1)**3, color = 'b', lw = 2, ls = '--', label = r'$p,\,\mathrm{Caio}$')
# ax_rho.plot(1/(bkg_class['z']+1), bkg_class['rho_ncdm[0]']/(bkg_class['z']+1)**3, color = 'g', lw = 1, label = r'$\rho,\, \mathrm{CLASS}$')
# ax_rho.plot(1/(bkg_class['z']+1), bkg_class['p_ncdm[0]']/(bkg_class['z']+1)**3, color = 'g', lw = 1, ls = '--', label = r'$p,\, \mathrm{CLASS}$')
# ax_rho.plot(1/(data_tanh_fl['z']+1), data_tanh_fl['rho_ncdm[0]']/(data_tanh_fl['z']+1)**3, color = 'r', lw = 2, label = r'$\rho,\, \mathrm{fluid, tanh}$')
# ax_rho.plot(1/(data_tanh_fl['z']+1), data_tanh_fl['p_ncdm[0]']/(data_tanh_fl['z']+1)**3, color = 'r', lw = 2, ls = '--', label = r'$p,\, \mathrm{fluid, tanh}$')


ax_rho.set_xscale('log')
ax_rho.set_yscale('log')
ax_rho.set_ylabel(r'$\rho\, a^3\ (\mathrm{ua})$')
ax_rho.set_xlabel(r'$a$')
ax_rho.set_xlim(1e-5,1)
ax_rho.set_ylim(1e-15,1e-6)
ax_rho.legend(fontsize = 12)
fig_rho.tight_layout()
fig_rho.savefig("1.00eV_evolution.png")

fig_eos, ax_eos = plt.subplots(figsize=(6,5))
ax_eos.plot(1/(nufld['z']+1),nufld['p_nufld[0]']/nufld['rho_nufld[0]'], color = 'k', lw = 3, label = r'$p/\rho$')
# ax_eos.plot(1/(ncdm['z']+1), ncdm['p_ncdm[0]']/ncdm['rho_ncdm[0]'], label = r'fluid, tanh')
ax_eos.plot(1/(nufld['z']+1),nufld['w_nufld[0]'], color = 'r', lw = 2, label = r'$w_{\mathrm{tanh}}$')
ax_eos.plot(1/(nufld['z']+1),nufld['w_mass_nufld[0]'], color = 'c', lw = 2, label = r'$w_{\mathrm{mass}}$')
ax_eos.set_xscale('log')
ax_eos.set_xlim(1e-5,1)
ax_eos.set_ylabel(r'$p/\rho$')
ax_eos.set_xlabel(r'$a$')
ax_eos.legend(fontsize = 16)
fig_eos.tight_layout()
fig_eos.savefig("eos.png")

fig_eosp, ax_eosp = plt.subplots(figsize=(6,5))
w_prime_nufld = np.gradient(nufld['w_nufld[0]'],nufld['tau'])
w_prime_mass_nufld = np.gradient(nufld['w_mass_nufld[0]'],nufld['tau'])
ax_eosp.plot(1/(nufld['z']+1),w_prime_nufld, color = 'r', lw = 2, ls = '--', label = r'${\mathrm{tanh, numpy}}$')
# ax_eosp.plot(1/(nufld['z']+1),nufld['w_prime_nufld[0]'], color = 'orange', lw = 3, label = r'${\mathrm{tanh}}$')
# ax_eosp.plot(1/(nufld['z']+1),nufld['w_prime_mass_nufld[0]'], color = 'c', lw = 3, label = r'${\mathrm{mass}}$')
ax_eosp.plot(1/(nufld['z']+1),w_prime_mass_nufld, color = 'b', lw = 2, ls = '--', label = r'${\mathrm{mass, numpy}}$')
ax_eosp.set_xscale('log')
# ax_eosp.set_yscale('log')
ax_eosp.set_xlim(1e-5,1)
# ax_eosp.set_ylim(0,2.5e-4)
ax_eosp.set_ylabel(r'$dw/d\tau$')
ax_eosp.set_xlabel(r'$a$')
ax_eosp.legend(fontsize = 16)
fig_eosp.tight_layout()
fig_eosp.savefig("eosp.png")