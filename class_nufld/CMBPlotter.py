import MyFunctions as funs
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

funs.load_style()

fig, (ax, bl, tr, tl) = funs.prepare_cmb_super_plot(-0.1,0.1)#(-1.5e-3,0.5e-2)

# plot data
k_cuts = ['1e-2','3e-2','1e-1','3e-1','1e0']
mass = '3eV'

pert_nufld = {}
for i in range(len(k_cuts)):
    pert_nufld.update({k_cuts[i]: funs.class_clout_to_df('class_nufld/output/default_nufld_'+mass+'_'+k_cuts[i]+'_cl_lensed.dat')})
pert_lcdm  = funs.class_clout_to_df('class_nufld/output/explanatory00_cl_lensed.dat')
pert_ncdm  = funs.class_clout_to_df('class_nufld/output/default_ncdm_'+mass+'_cl_lensed.dat')

for axs in ax, bl:
    for i in range(len(k_cuts)):
        axs.plot(pert_ncdm['l'], (pert_nufld[k_cuts[i]]['TT']-pert_ncdm['TT'])/pert_ncdm['TT'], color = funs.colors[i], ls = ':', lw = 3, label = r'$k_{\mathrm{cut}} = \ $'+k_cuts[i], zorder = 5)
for axs in tr,tl:
    axs.plot(pert_ncdm['l'], 1e12*(2.7255)**2*pert_lcdm['TT'], color = 'g', ls = '--', lw = 1, label = r'LCDM')
    axs.plot(pert_lcdm['l'], 1e12*(2.7255)**2*pert_lcdm['TT'], color = 'k', ls = '--', lw = 1, label = r'LCDM')
    axs.plot(pert_nufld['1e-2']['l'], 1e12*(2.7255)**2*pert_nufld['1e-2']['TT'], color = funs.colors[0], ls = '-', lw = 2, label = r'LCDM')

# plot planck error
pred = np.interp(funs.planck_data[:,0],pert_ncdm['l'],1e12*(2.7255)**2*pert_ncdm['TT'])
ax.errorbar(funs.planck_data[:,0],funs.planck_data[:,0]*0.,#funs.planck_data[:,1]/pred-1,
            yerr = funs.planck_data[:,2]/pred,#lolims=funs.planck_data[:,2]/pred,uplims=funs.planck_data[:,3]/pred,#funs.planck_data[:,1]/pred-1,
            marker='o', markersize=2,linestyle='none', color = 'gray', zorder = 4)#lolims=funs.planck_data[:,2],uplims=funs.planck_data[:,3],marker='o', markersize=2,linestyle='none', color = 'gray')
tr.errorbar(funs.planck_data[:,0],funs.planck_data[:,1],lolims=funs.planck_data[:,2],uplims=funs.planck_data[:,3],marker='o', markersize=2,linestyle='none', color = 'gray')

#legends
ax.legend(fontsize=18,loc='lower right',frameon=False,ncol = 2)
# tr.legend(fontsize=24,loc='center right',frameon=False)

fig.suptitle(r'$\sum m_\nu = \ $'+mass)
fig.tight_layout()
fig.savefig('cmb_'+mass+'.png')