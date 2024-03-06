
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

colors = ["#70CAD1","#7EBC89","#FE5D26","#8338ec"]
colors = ["#0000ff","#cd34b5","#fa8775","#ffd700","black"]

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
                  'rho_ncdm[0]', 'p_ncdm[0]', 'pseudo_p_ncdm[0]', 'rho_lambda', 'rho_ur', 'rho_crit',
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

# planck_data = np.loadtxt("planck_data.dat")
# CMB SUPER PLOT

def prepare_cmb_super_plot(ymin = -1.5e-3, ymax = 4e-3, ylabel = r'$C_\ell/C_\ell^\mathrm{ncdm}-1$'):
    fig = plt.figure(figsize=(9, 7.5), tight_layout=True)
    fig.tight_layout()
    grid = plt.GridSpec(4, 4, hspace=0., wspace=0.)
    grid.tight_layout(fig)

    #bottom right plot
    ax = fig.add_subplot(grid[1:, 1:])
    ax.tick_params(which='both' ,direction='in', width=2)
    ax.tick_params(which='major',direction='in', length=14)
    ax.tick_params(which='minor',direction='in', length=8)
    ax.yaxis.set_tick_params(which='both',left=False,right=True)
    ax.xaxis.set_tick_params(which='both',top=True,bottom=True)
    ax.spines['left'].set_visible(False)
    #ax.set_xlabel(r'$\sin^2(\theta_{12})$')
    xax = np.linspace(1,2500,100)
    ax.plot(xax,np.zeros(len(xax)),color='grey',linewidth=2,zorder=0)
    ax.axvline(30.,-1,1,color='grey',linestyle='--',linewidth=2,zorder=0)
    ax.set_ylim(ymin,ymax)
    ax.set_xlim(30.,2500)
    ax.set_xscale('linear')
    majors = [1, 10, 30, 500, 1000, 1500, 2000, 2500]
    majors_str = ['1', '10', '30', '500', '1000', '1500', '2000', '2500']
    ax.xaxis.set_major_locator(ticker.FixedLocator(majors))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(100))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.02))

    #bottom left plot
    dm_allrange = np.linspace(0.22,0.46,100)
    bl = fig.add_subplot(grid[1:, 0])#, sharey=ax)
    bl.tick_params(which='both' ,direction='in', width=2)
    bl.tick_params(which='major',direction='in', length=14)
    bl.tick_params(which='minor',direction='in', length=8)
    bl.yaxis.set_tick_params(which='both',left=True,right=False)
    bl.xaxis.set_tick_params(which='both',top=True,bottom=True)
    bl.spines['right'].set_visible(False)
    bl.plot(xax,np.zeros(len(xax)),color='grey',linewidth=2,zorder=0)
    bl.axvline(30.,-1,1,color='grey',linestyle='--',linewidth=2,zorder=0)
    bl.set_xscale('log')
    bl.set_xlim(1,30)
    bl.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:g}'.format(int(x))))
    bl.set_ylim(ymin, ymax)
    bl.xaxis.set_major_locator(ticker.FixedLocator(majors))
    bl.yaxis.set_minor_locator(ticker.MultipleLocator(0.02))

    #top right plot
    th_allrange = np.linspace(0.22,0.46,100)
    tr = fig.add_subplot(grid[0, 1:])#, sharex=ax)
    tr.tick_params(which='both' ,direction='in', width=2)
    tr.tick_params(which='major',direction='in', length=14)
    tr.tick_params(which='minor',direction='in', length=8)
    tr.yaxis.set_tick_params(which='both',left=False,right=True)
    tr.xaxis.set_tick_params(which='both',top=True,bottom=True)
    tr.spines['left'].set_visible(False)
    tr.axvline(30.,-1,1,color='grey',linestyle='--',linewidth=2,zorder=0)
    tr.set_xlim(30.,2500)
    tr.set_xscale('linear')
    majors = [1, 10, 30, 500, 1000, 1500, 2000, 2500]
    majors_str = ['1', '10', '30', '500', '1000', '1500', '2000', '2500']
    tr.xaxis.set_major_locator(ticker.FixedLocator(majors))
    tr.xaxis.set_minor_locator(ticker.MultipleLocator(100))
    tr.set_xticklabels([])
    tr.set_yticklabels([])
    tr.set_ylim(0,7500)
    tr.xaxis.set_major_locator(ticker.FixedLocator(majors))
    tr.yaxis.set_minor_locator(ticker.MultipleLocator(1000))
    majorsy = [5000]
    majors_stry = ['5000']
    tr.yaxis.set_major_locator(ticker.FixedLocator(majorsy))

    #top left plot
    tl = fig.add_subplot(grid[0,0])
    tl.tick_params(which='both' ,direction='in', width=2)
    tl.tick_params(which='major',direction='in', length=14)
    tl.tick_params(which='minor',direction='in', length=8)
    tl.yaxis.set_tick_params(which='both',left=True,right=False)
    tl.xaxis.set_tick_params(which='both',top=True,bottom=True)
    tl.spines['right'].set_visible(False)
    tl.axvline(30.,-1,1,color='grey',linestyle='--',linewidth=2,zorder=0)
    tl.set_xscale('log')
    tl.set_xlim(1,30)
    tl.set_xticklabels([])
    tl.set_ylim(0,7500)
    tl.xaxis.set_major_locator(ticker.FixedLocator(majors))
    tl.yaxis.set_minor_locator(ticker.MultipleLocator(1000))
    tl.yaxis.set_major_locator(ticker.FixedLocator(majorsy))

    #remove ticklabels 
    plt.setp(ax.get_yticklabels(), visible=False)
    plt.setp(tr.get_yticklabels(), visible=False)

    #labels
    bl.set_ylabel(ylabel)
    tl.set_ylabel(r'$\frac{\ell(\ell+1)}{2\pi} C_\ell$ [$\mu$K$^2$]')
    ax.xaxis.set_label_coords(0.35, -0.07)
    ax.set_xlabel(r'$\ell$')

    #fill regions of different effects
    tl.axvspan(0.5,31,color='navy',alpha=0.2)
    tr.axvspan(29,400,color='maroon',alpha=0.3)
    tr.axvspan(400,2501,color='tan',alpha=0.6)

    #text
    tl.text(3,6100,r'LISW',color='navy')
    tr.text(60,6100,r'EISW',color='maroon')
    tr.text(1080,6100,r'Silk damping',color='saddlebrown')

    return fig, (ax,bl,tr,tl)

