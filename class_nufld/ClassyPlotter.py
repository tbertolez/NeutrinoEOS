from classy import Class
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# THIS RUNS CLASS AND COMPUTES TRANSFER FUNCTIONS
# (BUT WE CAN ASK IT TO COMPUTE OTHER THINGS!)

plt.style.use('paper.mplstyle')
matplotlib.rcParams.update({'text.usetex': True})
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
matplotlib.rcParams['figure.facecolor'] = 'white'

# This is for massless neutrinos, always ultrarelativistic (LambdaCDM). Must be run after the rest!
# LambdaCDM = Class()
# LambdaCDM.set({'omega_b': 0.0223828, 'omega_cdm': 0.1201075,
#                'h': 0.67810, 'A_s': 2.100549e-09,
#                'n_s': 0.9660499, 'tau_reio': 0.05430842,
#                'N_ur': 3.044, 'N_ncdm': 0})
# LambdaCDM.set({'output': 'mTk,vTk', 'lensing': 'no'})
# LambdaCDM.set({'z_pk':'10000000'})#, 100000'})
# LambdaCDM.compute()
# lcdm_transf = LambdaCDM.get_transfer_and_k_and_z()
# lcdm_deltas = lcdm_transf[0]['d_tot']
# lcdm_ks     = lcdm_transf[1]
# lcdm_zs     = lcdm_transf[2]

mass = 0.05
ncdm = Class()
ncdm.set({'omega_b': 0.0223828, 'omega_cdm': 0.1201075,
               'h': 0.67810, 'A_s': 2.100549e-09,
               'n_s': 0.9660499, 'tau_reio': 0.05430842,
               'N_ur': 0.00441, 'N_ncdm': 1, 'N_nufld': 0,
               'm_ncdm': mass, 'deg_ncdm': 3, 
               'ncdm_fluid_approximation': 3})
ncdm.set({'output': 'mTk,vTk', 'lensing': 'no'})
# ncdm.set({'z_pk':'10000000'})#, 100000'})
ncdm.set({'z_pk':'100, 10000000'})
# print(ncdm.get_current_derived_parameters())
ncdm.compute()
ncdm_transf = ncdm.get_transfer_and_k_and_z()
print(ncdm_transf[0].keys())
ncdm_deltas = ncdm_transf[0]['d_ncdm[0]']
ncdm_thetas = ncdm_transf[0]['t_ncdm[0]']
ncdm_ks     = ncdm_transf[1]
ncdm_zs     = ncdm_transf[2]

nufld = Class()
nufld.set({'omega_b': 0.0223828, 'omega_cdm': 0.1201075,
               'h': 0.67810, 'A_s': 2.100549e-09,
               'n_s': 0.9660499, 'tau_reio': 0.05430842,
               'N_ur': 0.00441, 'N_nufld': 1,
               'm_nufld': mass, 'deg_nufld': 3,
               'nufld_fluid_approximation': 3,
               'nufld_parametrisation': 'tanh',
               'nufld_pars': '0.90885, 0.01047120'})
nufld.set({'output': 'mTk,vTk', 'lensing': 'no'})
# nufld.set({'z_pk':'10000000'})#, 100000'})
nufld.set({'z_pk':'100, 10000000'})
nufld.compute()
nufld_transf = nufld.get_transfer_and_k_and_z()
nufld_deltas = nufld_transf[0]['d_nufld[0]']
nufld_thetas = nufld_transf[0]['t_nufld[0]']
nufld_ks     = nufld_transf[1]
nufld_zs     = nufld_transf[2]

# Caio = Class()
# Caio.set({'omega_b': 0.0223828, 'omega_cdm': 0.1201075,
#                'h': 0.67810, 'A_s': 2.100549e-09,
#                'n_s': 0.9660499, 'tau_reio': 0.05430842,
#                'N_ur': 0.00441, 'N_ncdm': 1,
#                'm_ncdm': mass, 'deg_ncdm': 3, 
#                'ncdm_fluid_approximation': 4, 
#                'ncdm_fluid_trigger_tau_over_tau_k': 2.0})
# Caio.set({'output': 'mTk,vTk', 'lensing': 'no'})
# # Caio.set({'z_pk':'10000000'})#, 100000'})
# Caio.set({'z_pk':'100, 10000000'})
# Caio.compute()
# caio_transf = Caio.get_transfer_and_k_and_z()
# caio_deltas = caio_transf[0]['d_ncdm[0]']
# caio_thetas = caio_transf[0]['t_ncdm[0]']
# caio_ks     = caio_transf[1]
# caio_zs     = caio_transf[2]

# # print(lcdm_transf.keys())
# print(caio_deltas.shape)

fig_delta, ax_delta = plt.subplots(figsize=(6,5))
k_index = 113 #max113
ax_delta.plot(np.log(1/(1+ncdm_zs)),ncdm_deltas[k_index]/ncdm_deltas[k_index,0], lw = 3, color = 'k', label = "ncdm")
# ax_delta.plot(np.log(1/(1+caio_zs)), caio_deltas[k_index]/caio_deltas[k_index,0], ls = '--', label = "Caio fluid", alpha = 0.6)
ax_delta.plot(np.log(1/(1+nufld_zs)),nufld_deltas[k_index]/nufld_deltas[k_index,0], ls = ':', label = "nufld")
# ax_delta.set_yscale('log')
# ax_delta.set_xscale('log')
ax_delta.legend()
ax_delta.set_xlim([-2,-0.3])
ax_delta.set_ylim([-1e41,1e41])
ax_delta.set_ylabel(r'$\delta/\delta(a_{\mathrm{ini}})$')
ax_delta.set_xlabel(r'$\ln a$')
fig_delta.suptitle(r'$m =\ $'+'{:.2f}'.format(mass)+r'$\mathrm{eV}\, ,\ k =\  $'+'{:.4f}'.format(ncdm_ks[k_index])+r'$(\mathrm{Mpc})^{-1}$')
fig_delta.tight_layout()
fig_delta.savefig("density_perturbation.png")

fig_delta, ax_delta = plt.subplots(figsize=(6,5))
# ax_delta.plot(np.log(1/(1+caio_zs)), (caio_deltas[k_index]-ncdm_deltas[k_index])/ncdm_deltas[k_index], label = "Caio fluid")
ax_delta.plot(np.log(1/(1+nufld_zs)),(nufld_deltas[k_index]-ncdm_deltas[k_index])/ncdm_deltas[k_index], label = "nufld")
# ax_delta.set_yscale('log')
# ax_delta.set_xscale('log')
ax_delta.hlines(0,-17,0,'gray','dashed')
ax_delta.legend()
ax_delta.set_ylim([-1,1])
ax_delta.set_ylabel(r'$\delta_\nu/\delta_{\nu,\mathrm{ncdm}}-1$')
ax_delta.set_xlabel(r'$\ln a$')
fig_delta.suptitle(r'$m =\ $'+'{:.2f}'.format(mass)+r'$\mathrm{eV}\, ,\ k =\  $'+'{:.2f}'.format(ncdm_ks[k_index])+r'$(\mathrm{Mpc})^{-1}$')
fig_delta.tight_layout()
fig_delta.savefig("density_perturbation_error.png")

fig_theta, ax_theta = plt.subplots(figsize=(6,5))
ax_theta.plot(np.log(1/(1+ncdm_zs)),ncdm_thetas[k_index]/ncdm_thetas[k_index,0], lw = 3, color = 'k', label = "ncdm")
ax_theta.plot(np.log(1/(1+nufld_zs)),nufld_thetas[k_index]/nufld_thetas[k_index,0], ls = ':', label = "nufld")
# ax_theta.plot(np.log(1/(1+caio_zs)), caio_thetas[k_index]/caio_thetas[k_index,0], ls = '--', label = "Caio fluid", alpha = 0.6)
# ax_delta.set_yscale('log')
# ax_delta.set_xscale('log')
ax_theta.set_ylabel(r'$\theta/\theta(a_{\mathrm{ini}})$')
ax_theta.set_xlabel(r'$\ln a$')
ax_theta.legend()
fig_theta.suptitle(r'$m =\ $'+'{:.2f}'.format(mass)+r'$\mathrm{eV}\, ,\ k =\  $'+'{:.2f}'.format(ncdm_ks[k_index])+r'$(\mathrm{Mpc})^{-1}$')
fig_theta.tight_layout()
fig_theta.savefig("velocity_perturbation.png")

# lcdm_cls = LambdaCDM.lensed_cl(2500)
# lcdm_ll = lcdm_cls['ell'][2:]
# lcdm_clTT = lcdm_cls['tt'][2:]