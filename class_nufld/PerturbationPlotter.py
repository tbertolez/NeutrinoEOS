import numpy as np
import matplotlib.pyplot as plt
import MyFunctions as funs

# THIS PLOTS OUTPUT_PERTURBATIONS FROM CLASS, E.G. CMB AND POWER SPECTRUM

funs.load_style()

####################################################
# COSMIC MICROWAVE BACKGROUND PLOTS
####################################################

pert_lcdm  = funs.class_clout_to_df('class_nufld/output/explanatory00_cl_lensed.dat')
pert_nufld1 = funs.class_clout_to_df('class_nufld/output/default_nufld_1eV_1e-1_cl_lensed.dat')
pert_nufld2 = funs.class_clout_to_df('class_nufld/output/default_nufld_1eV_1e-4_cl_lensed.dat')
pert_ncdm  = funs.class_clout_to_df('class_nufld/output/default_ncdm_cl_lensed.dat')

# # DIFFERENCE TO LAMBDA-CDM PLOTS
# # --------------------------------------------------

fig_cl, axs_cl = plt.subplots(ncols = 1, nrows = 2, figsize = (6,9))

what_to_plot = 'diff-ncdm'

for ax_cl in axs_cl:
    ax_cl.hlines(0.0,2,2500, ls = '--', lw = 1, color = 'gray')
    if what_to_plot == 'abs':
        ax_cl.plot(pert_nufld1['l'], pert_nufld1['l']*(pert_nufld1['l']+1)/(2*np.pi)*pert_nufld1['TT'], color = 'c', ls = '--', lw = 2, label = r'Continuity equation')
        ax_cl.plot(pert_ncdm['l'], pert_ncdm['l']*(pert_ncdm['l']+1)/(2*np.pi)*pert_ncdm['TT'], color = 'r', ls = '--', lw = 2, label = r'Full Boltzmann tower')
        ax_cl.plot(pert_lcdm['l'], pert_lcdm['l']*(pert_lcdm['l']+1)/(2*np.pi)*pert_lcdm['TT'], color = 'k', ls = '--', lw = 1, label = r'LCDM')
    elif what_to_plot == 'diff-lcdm':
        ax_cl.plot(pert_nufld1['l'], (pert_nufld1['TT']-pert_lcdm['TT'])/pert_lcdm['TT'], color = 'k', lw = 3, label = r'nufld')
        ax_cl.plot(pert_ncdm['l'], (pert_ncdm['TT']-pert_lcdm['TT'])/pert_lcdm['TT'], color = 'r', ls = '--', lw = 2, label = r'ncdm')
    elif what_to_plot == 'diff-ncdm':
        ax_cl.plot(pert_ncdm['l'], (pert_nufld1['TT']-pert_ncdm['TT'])/pert_ncdm['TT'], color = 'r', ls = '--', lw = 2, label = r'1e-1')
        ax_cl.plot(pert_ncdm['l'], (pert_nufld2['TT']-pert_ncdm['TT'])/pert_ncdm['TT'], color = 'r', ls = '--', lw = 2, label = r'1e-4')
    
    if what_to_plot == 'abs':
        ax_cl.set_ylabel(r'$\frac{l(l+1)}{2\pi}C_\ell^\mathrm{TT}$')
    else:        
        # ax_cl.set_ylabel(r'$(C_\ell^\mathrm{TT}-C_{\ell,\mathrm{exact}}^\mathrm{TT})/C_{\ell,\mathrm{exact}}^\mathrm{TT}$')
        ax_cl.set_ylabel("Relative difference")

    ax_cl.set_xlabel(r'$\ell$')
    ax_cl.set_xlim(2,2500)
    ax_cl.legend(fontsize = 12)

axs_cl[0].set_xscale('log')
axs_cl[1].set_xscale('linear')
# ax_cl.set_xscale('log')

# axs_cl[0].set_ylim(-1e-7,1e-7)
# axs_cl[1].set_ylim(-0.2,0.2) # 1 eV
# axs_cl[0].set_ylim(-0.05,0.05) # 0.1 eV
# axs_cl[1].set_ylim(-0.05,0.05) # 0.1 eV
# axs_cl[1].set_ylim(-0.002,0.002) # 0.01 eV

fig_cl.tight_layout()
fig_cl.savefig("comparison_cl_lensed_TT.png")


# # K_CUT COMPARISON
fig_cl, axs_cl = plt.subplots(ncols = 1, nrows = 2, figsize = (6,9))




#######################################################
#               POWER SPECTRUM PLOTS                  #
#######################################################

lcdm_pk  = funs.class_pkout_to_df('class_nufld/output/explanatory00_pk.dat')
nufld_pk = funs.class_pkout_to_df('class_nufld/output/default_nufld_pk.dat')
ncdm_pk  = funs.class_pkout_to_df('class_nufld/output/default_ncdm_pk.dat')

# PLOTTING THE POWER SPECTRUM AND THE DIFFERENCE TO THE EXACT COMPUTATION
# -----------------------------------------------------------------------

fig_pk, axs_pk = plt.subplots(ncols = 1, nrows = 2, figsize = (6,9))
# print(caio_pk['k'], caio_pk['P'])
axs_pk[0].set_xscale('log')
axs_pk[0].set_yscale('log')
axs_pk[0].set_xlim((1e-3,0.8))
# axs_pk[0].set_ylim((3e2,3.5e4))
axs_pk[0].plot(nufld_pk['k'], nufld_pk['P'], label = "nufld")
axs_pk[0].plot( ncdm_pk['k'],  ncdm_pk['P'], label = "ncdm")
axs_pk[0].plot( lcdm_pk['k'],  lcdm_pk['P'], label = "lcdm")
axs_pk[1].plot(nufld_pk['k'], nufld_pk['P']/lcdm_pk['P']-1, lw = 3, label = "Full Boltzmann tower")
axs_pk[1].plot(ncdm_pk['k'], ncdm_pk['P']/lcdm_pk['P']-1, lw = 3, label = "Continuity equation")
axs_pk[0].set_ylabel(r'$P(k)$')
axs_pk[1].set_ylabel(r'$P(k)/P_{\Lambda\mathrm{CDM}}(k)-1$')
axs_pk[0].set_xlabel(r'$k\ (h/\mathrm{Mpc})$')
axs_pk[1].set_xlabel(r'$k\ (h/\mathrm{Mpc})$')
axs_pk[1].set_xlim((1e-3,0.7))
# axs_pk[1].set_ylim((-0.1,0.0))
axs_pk[1].set_xscale('log')
axs_pk[0].legend()
axs_pk[1].legend(fontsize = 16)
fig_pk.tight_layout()
fig_pk.savefig('power_spectrum.png')

exit()