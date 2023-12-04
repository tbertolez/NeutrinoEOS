# this code cannot be run directly
# do 'source /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/bin/clik_profile.sh' from your sh shell or put it in your profile

function addvar () {
local tmp="${!1}" ;
tmp="${tmp//:${2}:/:}" ; tmp="${tmp/#${2}:/}" ; tmp="${tmp/%:${2}/}" ;
export $1="${2}:${tmp}" ;
} 

if [ -z "${PATH}" ]; then 
PATH=/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/bin
export PATH
else
addvar PATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/bin
fi
if [ -z "${PYTHONPATH}" ]; then 
PYTHONPATH=/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib/python/site-packages
export PYTHONPATH
else
addvar PYTHONPATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib/python/site-packages
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib
export LD_LIBRARY_PATH
else
addvar LD_LIBRARY_PATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01
export LD_LIBRARY_PATH
else
addvar LD_LIBRARY_PATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01
fi
CLIK_PATH=/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01
export CLIK_PATH

CLIK_DATA=/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/share/clik
export CLIK_DATA

CLIK_PLUGIN=rel2015
export CLIK_PLUGIN

