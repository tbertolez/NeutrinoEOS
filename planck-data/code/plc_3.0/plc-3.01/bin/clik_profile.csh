# this code cannot be run directly
# do 'source /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/bin/clik_profile.csh' from your csh shell or put it in your profile

 

if !($?PATH) then
setenv PATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/bin
else
set newvar=$PATH
set newvar=`echo ${newvar} | sed s@:/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/bin:@:@g`
set newvar=`echo ${newvar} | sed s@:/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/bin\$@@` 
set newvar=`echo ${newvar} | sed s@^/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/bin:@@`  
set newvar=/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/bin:${newvar}                     
setenv PATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/bin:${newvar} 
endif
if !($?PYTHONPATH) then
setenv PYTHONPATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib/python/site-packages
else
set newvar=$PYTHONPATH
set newvar=`echo ${newvar} | sed s@:/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib/python/site-packages:@:@g`
set newvar=`echo ${newvar} | sed s@:/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib/python/site-packages\$@@` 
set newvar=`echo ${newvar} | sed s@^/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib/python/site-packages:@@`  
set newvar=/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib/python/site-packages:${newvar}                     
setenv PYTHONPATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib/python/site-packages:${newvar} 
endif
if !($?LD_LIBRARY_PATH) then
setenv LD_LIBRARY_PATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib
else
set newvar=$LD_LIBRARY_PATH
set newvar=`echo ${newvar} | sed s@:/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib:@:@g`
set newvar=`echo ${newvar} | sed s@:/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib\$@@` 
set newvar=`echo ${newvar} | sed s@^/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib:@@`  
set newvar=/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib:${newvar}                     
setenv LD_LIBRARY_PATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/lib:${newvar} 
endif
if !($?LD_LIBRARY_PATH) then
setenv LD_LIBRARY_PATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01
else
set newvar=$LD_LIBRARY_PATH
set newvar=`echo ${newvar} | sed s@:/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01:@:@g`
set newvar=`echo ${newvar} | sed s@:/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01\$@@` 
set newvar=`echo ${newvar} | sed s@^/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01:@@`  
set newvar=/home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01:${newvar}                     
setenv LD_LIBRARY_PATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01:${newvar} 
endif
setenv CLIK_PATH /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01

setenv CLIK_DATA /home/tbertolez/Dropbox/Doctorat/Neutrinos/NeutrinoEOS/planck-data/code/plc_3.0/plc-3.01/share/clik

setenv CLIK_PLUGIN rel2015

