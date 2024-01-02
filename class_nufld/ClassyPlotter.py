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

mass = 0.02
Exact = Class()
Exact.set({'omega_b': 0.0223828, 'omega_cdm': 0.1201075,
               'h': 0.67810, 'A_s': 2.100549e-09,
               'n_s': 0.9660499, 'tau_reio': 0.05430842,
               'N_ur': 0.00441, 'N_ncdm': 1,
               'm_ncdm': mass, 'deg_ncdm': 3, 
               'ncdm_fluid_approximation': 3})
Exact.set({'output': 'mTk,vTk', 'lensing': 'no'})
# Exact.set({'z_pk':'10000000'})#, 100000'})
Exact.set({'z_pk':'100, 10000000'})
# print(Exact.get_current_derived_parameters())
Exact.compute()
exact_transf = Exact.get_transfer_and_k_and_z()
print(exact_transf[0].keys())
exact_deltas = exact_transf[0]['d_ncdm[0]']
exact_thetas = exact_transf[0]['t_ncdm[0]']
exact_ks     = exact_transf[1]
exact_zs     = exact_transf[2]

ClFLA = Class()
ClFLA.set({'omega_b': 0.0223828, 'omega_cdm': 0.1201075,
               'h': 0.67810, 'A_s': 2.100549e-09,
               'n_s': 0.9660499, 'tau_reio': 0.05430842,
               'N_ur': 0.00441, 'N_ncdm': 1,
               'm_ncdm': mass, 'deg_ncdm': 3, 
               'ncdm_fluid_approximation': 2,
               'ncdm_fluid_trigger_tau_over_tau_k': 2.0})
ClFLA.set({'output': 'mTk,vTk', 'lensing': 'no'})
# ClFLA.set({'z_pk':'10000000'})#, 100000'})
ClFLA.set({'z_pk':'100, 10000000'})
ClFLA.compute()
clfla_transf = ClFLA.get_transfer_and_k_and_z()
clfla_deltas = clfla_transf[0]['d_ncdm[0]']
clfla_thetas = clfla_transf[0]['t_ncdm[0]']
clfla_ks     = clfla_transf[1]
clfla_zs     = clfla_transf[2]

Caio = Class()
Caio.set({'omega_b': 0.0223828, 'omega_cdm': 0.1201075,
               'h': 0.67810, 'A_s': 2.100549e-09,
               'n_s': 0.9660499, 'tau_reio': 0.05430842,
               'N_ur': 0.00441, 'N_ncdm': 1,
               'm_ncdm': mass, 'deg_ncdm': 3, 
               'ncdm_fluid_approximation': 4, 
               'ncdm_fluid_trigger_tau_over_tau_k': 2.0})
Caio.set({'output': 'mTk,vTk', 'lensing': 'no'})
# Caio.set({'z_pk':'10000000'})#, 100000'})
Caio.set({'z_pk':'100, 10000000'})
Caio.compute()
caio_transf = Caio.get_transfer_and_k_and_z()
caio_deltas = caio_transf[0]['d_ncdm[0]']
caio_thetas = caio_transf[0]['t_ncdm[0]']
caio_ks     = caio_transf[1]
caio_zs     = caio_transf[2]

# print(lcdm_transf.keys())
print(caio_deltas.shape)

fig_delta, ax_delta = plt.subplots(figsize=(6,5))
k_index = 113 #max113
ax_delta.plot(np.log(1/(1+exact_zs)),exact_deltas[k_index]/exact_deltas[k_index,0], lw = 3, color = 'k', label = "Exact")
ax_delta.plot(np.log(1/(1+caio_zs)), caio_deltas[k_index]/caio_deltas[k_index,0], ls = '--', label = "Caio fluid", alpha = 0.6)
ax_delta.plot(np.log(1/(1+clfla_zs)),clfla_deltas[k_index]/clfla_deltas[k_index,0], ls = ':', label = "CLASS approx.")
# ax_delta.set_yscale('log')
# ax_delta.set_xscale('log')
ax_delta.legend()
ax_delta.set_ylabel(r'$\delta/\delta(a_{\mathrm{ini}})$')
ax_delta.set_xlabel(r'$\ln a$')
fig_delta.suptitle(r'$m =\ $'+'{:.2f}'.format(mass)+r'$\mathrm{eV}\, ,\ k =\  $'+'{:.2f}'.format(exact_ks[k_index])+r'$(\mathrm{Mpc})^{-1}$')
fig_delta.tight_layout()
fig_delta.savefig("density_perturbation.png")

fig_delta, ax_delta = plt.subplots(figsize=(6,5))
ax_delta.plot(np.log(1/(1+caio_zs)), (caio_deltas[k_index]-exact_deltas[k_index])/exact_deltas[k_index], label = "Caio fluid")
ax_delta.plot(np.log(1/(1+clfla_zs)),(clfla_deltas[k_index]-exact_deltas[k_index])/exact_deltas[k_index], label = "CLASS approx.")
# ax_delta.set_yscale('log')
# ax_delta.set_xscale('log')
ax_delta.hlines(0,-17,0,'gray','dashed')
ax_delta.legend()
ax_delta.set_ylim([-1,1])
ax_delta.set_ylabel(r'$\delta_\nu/\delta_{\nu,\mathrm{exact}}-1$')
ax_delta.set_xlabel(r'$\ln a$')
fig_delta.suptitle(r'$m =\ $'+'{:.2f}'.format(mass)+r'$\mathrm{eV}\, ,\ k =\  $'+'{:.2f}'.format(exact_ks[k_index])+r'$(\mathrm{Mpc})^{-1}$')
fig_delta.tight_layout()
fig_delta.savefig("density_perturbation_error.png")

fig_theta, ax_theta = plt.subplots(figsize=(6,5))
ax_theta.plot(np.log(1/(1+exact_zs)),exact_thetas[k_index]/exact_thetas[k_index,0], lw = 3, color = 'k', label = "Exact")
ax_theta.plot(np.log(1/(1+clfla_zs)),clfla_thetas[k_index]/clfla_thetas[k_index,0], ls = ':', label = "CLASS approx.")
ax_theta.plot(np.log(1/(1+caio_zs)), caio_thetas[k_index]/caio_thetas[k_index,0], ls = '--', label = "Caio fluid", alpha = 0.6)
# ax_delta.set_yscale('log')
# ax_delta.set_xscale('log')
ax_theta.set_ylabel(r'$\theta/\theta(a_{\mathrm{ini}})$')
ax_theta.set_xlabel(r'$\ln a$')
ax_theta.legend()
fig_theta.suptitle(r'$m =\ $'+'{:.2f}'.format(mass)+r'$\mathrm{eV}\, ,\ k =\  $'+'{:.2f}'.format(exact_ks[k_index])+r'$(\mathrm{Mpc})^{-1}$')
fig_theta.tight_layout()
fig_theta.savefig("velocity_perturbation.png")

# lcdm_cls = LambdaCDM.lensed_cl(2500)
# lcdm_ll = lcdm_cls['ell'][2:]
# lcdm_clTT = lcdm_cls['tt'][2:]