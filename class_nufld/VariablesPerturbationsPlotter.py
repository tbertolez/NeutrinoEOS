import numpy as np
import MyFunctions as funs
import matplotlib.pyplot as plt
# import matplotlib

funs.load_style()
# THIS PLOTS _perturbations_kX_s FROM CLASS, E.G. variables as a function of a, tau

# Load background
bkg_nufld = funs.class_bkgout_to_df('class_nufld/output/default_nufld_background.dat')
bkg_ncdm  = funs.class_bkgout_to_df('class_nufld/output/default_ncdm_background.dat', cols=funs.cols_bkg_ncdm)

# Load variables
output_k = [1e-4,1e-3,1e-2,1e-1]
# output_k = [1e-4,1e-3]
# output_k = [5.58480e-01, 6.27416e-01, 7.37130e-01]

pert_nufld = {}
pert_ncdm  = {}
for i in range(len(output_k)):
    pert_nufld.update({output_k[i]: funs.class_pertvars_to_df('class_nufld/output/default_nufld_perturbations_k'+str(i)+'_s.dat')})
    pert_ncdm.update({output_k[i]: funs.class_pertvars_to_df('class_nufld/output/default_ncdm_perturbations_k'+str(i)+'_s.dat', cols = funs.cols_vars_ncdm)})

###########################################
#           TRANSFER FUNCTIONS            #
###########################################

# # DENSITY TRANSFER FUNCTION
# ------------------------------------------

fig_dtk, axs_dtk = plt.subplots(ncols=1, nrows=1, figsize = (7,5))

what_to_plot = 'diff'
# what_to_plot = 'abs'

def plot_delta(axs_dtk,pert_nufld,pert_ncdm,what_to_plot='abs'):
    axs_dtk.hlines(0,1e-7,1,ls = '--', colors = 'gray')
    for i in range(len(output_k)):
        k = output_k[i]

        if what_to_plot == 'abs':
            axs_dtk.plot(pert_nufld[k]['a'],  pert_nufld[k]['delta_nufld[0]'], 
                            color = funs.colors[i], ls = '-',  lw = 2,  label = r"$\mathrm{Continuity}$"+r"$\, k = $ {}".format(k))
            axs_dtk.plot(pert_ncdm[k]['a'],   pert_ncdm[k]['delta_ncdm[0]'], 
                            color = funs.colors[i],        ls = '--', lw = 2,  label = r"$\mathrm{Original}$"+r"$\, k = $ {}".format(k))

        if what_to_plot == 'diff':
            # Arrays have different sizes, interpolate one of them :(
            delta_nufld = np.interp(pert_ncdm[k]['a'],pert_nufld[k]['a'],pert_nufld[k]['delta_nufld[0]'])
            axs_dtk.plot(pert_ncdm[k]['a'],  (pert_ncdm[k]['delta_ncdm[0]']-delta_nufld)/pert_ncdm[k]['delta_ncdm[0]'], 
                    color = funs.colors[i],  ls = '-', lw = 2,  label = r"$k = $ {}".format(k))

    axs_dtk.set_xscale('log')
    axs_dtk.set_xlim([1e-7,1])
    axs_dtk.set_xlim([0.5e-4,1])
    axs_dtk.set_xlabel(r'$\tau$')
    if what_to_plot == 'abs':
        axs_dtk.set_ylabel(r'$\delta(k)$')
    elif what_to_plot == 'diff':
        # axs_dtk.set_ylim([-0.5,0.1])
        axs_dtk.set_ylabel(r'$(\delta_{\mathrm{nufld}}-\delta_{\mathrm{ncdm}})/\delta_{\mathrm{ncdm}}$')

    axs_dtk.legend()
    return

plot_delta(axs_dtk,pert_nufld,pert_ncdm,'diff')
fig_dtk.tight_layout()
fig_dtk.savefig('delta_transfer.png')


# # VELOCITY TRANSFER FUNCTION
# ------------------------------------------

fig_ttk, axs_ttk = plt.subplots(ncols=1, nrows=1, figsize = (7,5))

what_to_plot = 'diff'
# what_to_plot = 'abs'

def plot_theta(axs_ttk,pert_nufld,pert_ncdm,what_to_plot = 'abs'):
    axs_ttk.hlines(0,1e-7,1,ls = '--', colors = 'gray')
    for i in range(len(output_k)):
        k = output_k[i]
    
        if what_to_plot == 'abs':
            axs_ttk.plot(pert_nufld[k]['a'],  pert_nufld[k]['theta_nufld[0]'], 
                            color = funs.colors[i], ls = '-',  lw = 2,  label = r"$\mathrm{Continuity}$"+r"$\, k = $ {}".format(k))
            axs_ttk.plot(pert_ncdm[k]['a'],   pert_ncdm[k]['theta_ncdm[0]'], 
                            color = funs.colors[i],        ls = '--', lw = 2,  label = r"$\mathrm{Original}$"+r"$\, k = $ {}".format(k))

        if what_to_plot == 'diff':
            # Arrays have different sizes, interpolate one of them :(
            theta_nufld = np.interp(pert_ncdm[k]['a'],pert_nufld[k]['a'],pert_nufld[k]['theta_nufld[0]'])
            axs_ttk.plot(pert_ncdm[k]['a'],  (pert_ncdm[k]['theta_ncdm[0]']-theta_nufld)/pert_ncdm[k]['theta_ncdm[0]'], 
                    color = funs.colors[i],  ls = '-', lw = 2,  label = r"$k = $ {}".format(k))

    axs_ttk.set_xscale('log')
    # axs_ttk.set_ylim([-0.005,0.01])
    # axs_ttk.set_xlim([1e-0,1e3])
    axs_ttk.set_xlim([0.5e-4,1])

    # axs_ttk.set_xlim([1e3,2e4])
    axs_ttk.set_xlabel(r'$a$')
    if what_to_plot == 'abs':
        axs_ttk.set_ylabel(r'$\theta(k)$')
    elif what_to_plot == 'diff':
        axs_ttk.set_ylabel(r'$(\theta_{\mathrm{nufld}}-\theta_{\mathrm{ncdm}})/\theta_{\mathrm{ncdm}}$')
    axs_ttk.legend(loc = 'lower left')
    return

plot_theta(axs_ttk,pert_nufld,pert_ncdm,'diff')
fig_ttk.tight_layout()
fig_ttk.savefig('theta_transfer.png')


###########################################
#               SOUND SPEED               #
###########################################

# Plotting just one sound speed
fig_cs2, axs_cs2 = plt.subplots(ncols=1, nrows=1, figsize = (7,5))

def plot_cs2(axs_cs2,pert_nufld,pert_ncdm,what_to_plot='abs'):
    for i in range(len(output_k)):
        k = output_k[i]
        axs_cs2.hlines(0,1e-7,1,ls = '--', colors = 'gray')
        if what_to_plot == 'abs':
            axs_cs2.fill_between([0.5e-3,2.5e-2],-0.05,0.5,alpha = 0.05, color = "gray", edgecolor = None)
            axs_cs2.plot(pert_nufld[k]['a'], pert_nufld[k]['cs2_gauge[0]'], lw = 2,  ls = '-', color = funs.colors[i], label = r"Modified, $k = $ "+str(k))
            axs_cs2.plot(pert_ncdm[k]['a'],  pert_ncdm[k]['cs2_ncdm[0]'], lw = 1.5, ls = '--', color = funs.colors[i], label = r"Original, $k = $ "+str(k))
        if what_to_plot == 'diff':
            cs2_nufld = np.interp(pert_ncdm[k]['a'],pert_nufld[k]['a'],pert_nufld[k]['cs2_gauge[0]'])
            axs_cs2.plot(pert_ncdm[k]['a'],  (pert_ncdm[k]['cs2_ncdm[0]']-cs2_nufld)/pert_ncdm[k]['cs2_ncdm[0]'], lw =2, ls = '-', color = funs.colors[i], label = r"$k = $ {}".format(str(k)))

        axs_cs2.set_xscale('log')
    axs_cs2.set_xlim([1e-7,1])
    axs_cs2.set_xlim([0.5e-4,1])
    axs_cs2.legend()
    axs_cs2.set_xlabel(r'$a$')
    if what_to_plot == 'abs':
        axs_cs2.set_ylim([0,0.5])
        axs_cs2.set_ylabel(r'$c_s^{\, 2}$')
    elif what_to_plot == 'diff':
        # axs_cs2.set_ylim([-0.05,0.05])
        axs_cs2.set_ylabel(r'$(c_{s,\mathrm{nufld}}^{\, 2}-c_{s,\mathrm{ncdm}}^{\, 2})/c_{s,\mathrm{ncdm}}^{\, 2}$')
    return

plot_cs2(axs_cs2,pert_nufld,pert_ncdm,'diff')
fig_cs2.tight_layout()
fig_cs2.savefig('sound_speed.png')


# Sound speed comparison

# fig_cs2, axs_cs2 = plt.subplots(ncols=3, nrows=3, figsize = (15,15))
# for i in range(len(output_k)):
#     k = output_k[i]
#     col = i%3
#     row = int(i/3)
#     # axs_cs2[row,col].fill_between([0.5e-3,2.5e-2],-0.05,0.5,alpha = 0.05, color = "gray", edgecolor = None)
#     axs_cs2[row,col].hlines(0,1e-7,1,ls = '--', colors = 'gray')
#     # axs_cs2.plot(pert_nufld[k]['a'], pert_nufld[k]['cs2_nufld[0]'], lw = 2,  ls = '-', color = colors[i], label = r"Modified, $k = $ "+str(k))
#     axs_cs2[row,col].plot(pert_ncdm[k]['a'],  pert_ncdm[k]['cs2_fluid[0]'], lw = 3, ls = '-', color ='#3a5a40', label = r"$k = $ "+str(k), zorder = 10)
#     axs_cs2[row,col].plot(pert_ncdm[k]['a'],  pert_ncdm[k]['cs2_gauge[0]'], lw = 1.5, ls = '--', color = '#a3b18a')
#     axs_cs2[row,col].set_xscale('log')
#     axs_cs2[row,col].set_ylim([-0.05,0.4])
#     axs_cs2[row,col].set_xlim([1e-6,1])
#     axs_cs2[row,col].legend(loc = "upper right", fontsize = 20)
#     axs_cs2[row,col].set_xlabel(r'$a$')
#     axs_cs2[row,col].set_ylabel(r'$c_s^{\, 2}$')
# fig_cs2.suptitle(r'$\sum m_\nu =\ $'+mass+', l_max_ncdm = '+lmax)
# fig_cs2.tight_layout()
# fig_cs2.savefig('sound_speed_3x3_'+mass+'_'+lmax+'.png')


###########################################
#               SHEAR                     #
###########################################

fig_sig, axs_sig = plt.subplots(ncols=1, nrows=1, figsize = (7,5))

what_to_plot = 'diff'
# what_to_plot = 'abs'

def plot_shear(axs_sig,pert_nufld,pert_ncdm,what_to_plot='abs'):
    axs_sig.hlines(0,1e-7,1,ls = '--', colors = 'gray')

    for i in range(len(output_k)):
        k = output_k[i]
        if what_to_plot == 'abs':
            axs_sig.plot(pert_nufld[k]['a'], pert_nufld[k]['shear_nufld[0]'], 
                        lw = 3, color = funs.colors[i],label = "Our k = "+str(k))
            axs_sig.plot(pert_ncdm[k]['a'], pert_ncdm[k]['shear_ncdm[0]'], 
                        lw = 2, color = funs.colors[i], ls = '--', label = "CLASS k = "+str(k))
        
        if what_to_plot == 'diff':
            shear_nufld = np.interp(pert_ncdm[k]['a'],pert_nufld[k]['a'],pert_nufld[k]['shear_nufld[0]'])
            axs_sig.plot(pert_ncdm[k]['a'],  (pert_ncdm[k]['shear_ncdm[0]']-shear_nufld)/pert_ncdm[k]['shear_ncdm[0]'], 
                    color = funs.colors[i],  ls = '-', lw = 2,  label = r"$k = $ {}".format(k))

    axs_sig.set_xscale('log')
    axs_sig.set_xlabel(r'$a$')
    if what_to_plot == 'abs':
        axs_sig.set_ylabel(r'$\sigma(k)$')
    elif what_to_plot == 'diff':
        # axs_sig.set_ylim(-0.2,0.2)
        axs_sig.set_ylabel(r'$(\sigma_{\mathrm{nufld}}-\sigma_{\mathrm{ncdm}})/\sigma_{\mathrm{ncdm}}$')
    axs_sig.set_xlim([1e-7,1])
    axs_sig.set_xlim([0.5e-4,1])
    axs_sig.legend()
    return

plot_shear(axs_sig,pert_nufld,pert_ncdm,'diff')
fig_sig.tight_layout()
fig_sig.savefig('shear.png')


# exit()

# ALL 4 VARIABLES IN ONE PLOT
fig_all, axs_all = plt.subplots(ncols=2, nrows=2, figsize = (9,9))
plot_delta(axs_all[0,0],pert_nufld,pert_ncdm,'abs')
plot_theta(axs_all[0,1],pert_nufld,pert_ncdm,'abs')
plot_shear(axs_all[1,0],pert_nufld,pert_ncdm,'abs')
plot_cs2(axs_all[1,1],pert_nufld,pert_ncdm,'abs')
fig_all.tight_layout()
fig_all.savefig('4variables.pdf')


# CONTINUITY EQUATIONS
# ----------------------------------------------------

fig_cont, axs_cont = plt.subplots(ncols=2, nrows = 1, figsize = (12,5))
ax_delta = axs_cont[0]
ax_theta = axs_cont[1]

def compute_delta(k,bkg_array, pert_array, species):
    w_bkg = bkg_array['p_'+species+'[0]']/bkg_array['rho_'+species+'[0]'] # This has a different shape :(
    w = np.interp(pert_array['a'],1/(1+bkg_array['z']),w_bkg) # This has been checked to work right!
    wprime = np.gradient(w,pert_array['tau'])

    a_prime_over_a = np.gradient(pert_array['a'],pert_array['tau'])/pert_array['a']

    delta = pert_array['delta_'+species+'[0]']
    theta = pert_array['theta_'+species+'[0]']
    shear = pert_array['shear_'+species+'[0]']

    phip = np.gradient(pert_array['phi'],pert_array['tau'])
    if species == 'ncdm':
        cs2 = pert_array['cs2_'+species+'[0]']
    elif species == 'nufld':
        cs2 = pert_array['cs2_gauge[0]']

    deltarhs  = -(1+w)*(theta-3*phip) 
    deltarhs += -3*a_prime_over_a*(cs2-w)*delta
    deltalhs = np.gradient(pert_array['delta_'+species+'[0]'],pert_array['tau'])

    thetarhs = 0
    thetarhs += -a_prime_over_a*(1-3*w)*theta 
    thetarhs += -wprime/(1+w)*theta 
    thetarhs += +cs2/(1+w)*k**2*delta 
    thetarhs += -k**2*shear 
    thetarhs += +k**2*pert_array['psi']
    thetalhs = np.gradient(pert_array['theta_'+species+'[0]'],pert_array['tau'])

    return deltalhs, deltarhs, thetalhs, thetarhs


# deltalhs_ncdm  = np.gradient(pert_ncdm[k]['delta_ncdm[0]'],pert_ncdm[k]['tau'])

# what_to_plot = 'diff'
what_to_plot = 'diff'

# Absolute values 
for i in range(len(output_k)):
    k = output_k[i]
    deltalhs_nufld, deltarhs_nufld, thetalhs_nufld, thetarhs_nufld = compute_delta(k, bkg_nufld,pert_nufld[k],'nufld')
    deltalhs_ncdm,  deltarhs_ncdm,  thetalhs_ncdm,  thetarhs_ncdm  = compute_delta(k, bkg_ncdm,pert_ncdm[k],'ncdm')

    if what_to_plot == 'abs':
        ax_delta.plot(pert_nufld[k]['a'],deltarhs_nufld, lw = 3, color = funs.colors[i], label = 'nufld RHS')
        # ax_delta.plot(pert_nufld[k]['a'],deltalhs_nufld, lw = 3, label = 'nufld LHS')
        ax_delta.plot(pert_ncdm[k]['a'], deltarhs_ncdm, lw = 3, ls = '--',  color = funs.colors[i], label = 'ncdm RHS')
        # ax_delta.plot(pert_ncdm[k]['a'], deltalhs_ncdm, lw = 3, ls = '--', label = 'ncdm LHS')
        ax_theta.plot(pert_nufld[k]['a'],thetarhs_nufld, lw = 3, color = funs.colors[i], label = 'nufld RHS')
        # ax_theta.plot(pert_nufld[k]['a'],thetalhs_nufld, lw = 3, label = 'nufld LHS')
        ax_theta.plot(pert_ncdm[k]['a'], thetarhs_ncdm, lw = 3, ls = '--', color = funs.colors[i], label = 'ncdm RHS')
        # ax_theta.plot(pert_ncdm[k]['a'], thetalhs_ncdm, lw = 3, ls = '--', label = 'ncdm LHS')

    if what_to_plot == 'diff':
        delta_nufld = np.interp(pert_ncdm[k]['a'],pert_nufld[k]['a'],deltarhs_nufld)
        theta_nufld = np.interp(pert_ncdm[k]['a'],pert_nufld[k]['a'],thetarhs_nufld)
        ax_delta.plot(pert_ncdm[k]['a'],(deltarhs_ncdm-delta_nufld)/deltarhs_ncdm, lw = 3, color = funs.colors[i], label = r"$k = $ {}".format(k))
        ax_theta.plot(pert_ncdm[k]['a'],(thetarhs_ncdm-theta_nufld)/thetarhs_ncdm, lw = 3, color = funs.colors[i], label = r"$k = $ {}".format(k))

        ax_delta.set_ylim(-0.2,0.2)
        ax_theta.set_ylim(-0.2,0.2)

ax_delta.set_xlim(1e-7,1)
ax_theta.set_xlim(1e-7,1)

ax_delta.set_ylabel(r'$\dot\delta$')
ax_theta.set_ylabel(r'$\dot\theta$')
for ax in axs_cont:
    ax.set_xscale('log')
    ax.legend()
    ax.set_xlabel(r'$a$')
# ax_delta.set_ylim([-10,10])
# ax_theta.set_ylim([-10,10])
fig_cont.tight_layout()
fig_cont.savefig('continuity.png')

