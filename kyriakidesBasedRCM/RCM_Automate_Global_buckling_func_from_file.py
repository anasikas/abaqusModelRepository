# **************************************************************************************
# Automate global buckling analysis until success
# **************************************************************************************
# execfile('C:/TEMP/GlobalBuckling/RCM_Automate_Global_Buckling.py', __main__.__dict__)
#---------------------------------------------------------------------------------------
# parameter definitions
#---------------------------------------------------------------------------------------


def AutoNumberIfNameExists(name,existing_names):
    """Search in existing_names for elements with the pattern     name+'_'+{number*}+'{alpha*} 
    and rename to name+='_'+max{number*}+1"""
    
    if name in existing_names:
        min_id=1
        for ex_name in [x for x in existing_names if x!=name]:
            str_id=ex_name.replace(name,'').split('_')[1]
            if str_id[0].isdigit():
                num_id=str_id[0]
                for c in str_id[1:]:
                    if not c.isdigit():
                        break
                    num_id+= c
                min_id= max(int(num_id)+1,min_id)
        
        name=name+'_'+str(min_id)
        print "NewName:  "+name
        
    return name


def extractU3NT11CurveFromOdb(job_name):
    # session.currentViewportName
    # odb_name=session.viewports[session.currentViewportName].displayedObject.name
    # odb = session.odbs[odb_name]
    #print session.viewports[session.currentViewportName].odbDisplay.historyVariables.keys()
    
    
    import os
    path = os.getcwd()
    #job_name = 'riks5_5'
    odbName  = job_name
    odbPath  = path+'\\'+odbName+'.odb'
    odb      = session.openOdb(name=odbPath)
    
    
    import xyPlot
    myxy=xyPlot.XYData(name='_temp', data=((0, 0), ))
    for step in odb.steps.keys()[1:]:
        xy0 = xyPlot.XYDataFromHistory(odb=odb, 
            outputVariableName='Spatial displacement: U3 PI: TUBEINSTANCE Node 1 in NSET X0', 
            steps=(step, ))
        xy1 = xyPlot.XYDataFromHistory(odb=odb, 
            outputVariableName='Nodal temperature: NT11 PI: TUBEINSTANCE Node 1 in NSET X0', 
            steps=(step, ))
        xy2 = combine(xy0, xy1, )
        myxy = append((myxy, xy2))
        del session.xyDataObjects[xy0.name]
        del session.xyDataObjects[xy1.name]
        del session.xyDataObjects[xy2.name]
    
    name = 'U3_NT11_' + odbName.replace('.odb','').rpartition('/')[-1]
    xy_result = session.XYData(name=name, objectToCopy=myxy)
    
    fileName = xy_result.name+'.txt'
    xyData   = xy_result
    session.writeXYReport(fileName = fileName,xyData=xyData, appendMode=OFF)
    #odb.close()
    maxReachedTemperature=xyData.data[-1][-1]
    return maxReachedTemperature




# First check that the mdb is named and the intended work directory is used

import os                  # import OS module if needed
# os.chdir(r"C:\TEMP")      # set work directory
path = os.getcwd()                          # get path of scratch directory

if mdb.pathName=='<unnamed>':
    mdbNameSuggestion = 'RCM'
    dir_files_list=os.listdir(path)             # Get the list of all files and directories
    existing_names =[ file.replace('.cae','') for file in dir_files_list \
            if file.startswith(mdbNameSuggestion) & file.endswith('.cae') ]          # optionally filter list
    mdbNameSuggestion = AutoNumberIfNameExists(mdbNameSuggestion,existing_names)
    warningText = \
"""To run this analysis first you need to save the *.cae model in the desired path.
The current work directory is   {one}
How do you wanna name the model in the current work directory?
The results will be saved in    {one}\\results 
Press "NO" to abort the analysis and change the work directory""".format(one = path)
    userResponse = getInput(warningText,mdbNameSuggestion)
    if userResponse is None:
        ABORT_UNNAMED_MDB
    
    mdb.saveAs(pathName=path+'\\'+userResponse+'.cae')

new_dir="{}\\results".format(path)
if not os.path.isdir(new_dir):
    os.mkdir(new_dir)

os.chdir(new_dir)


# Initialize model geometry / loading parameters
manualInitialization=False
if not manualInitialization:
    # Import defaults
    execfile('C:/TEMP/GlobalBuckling/RCM_Default_Parameters.py', __main__.__dict__)
else:     # use the parameters from here
    # Manually Initialize defaults # good for debugging and versatility when running a single analysis at a time
    modelname = 'RCM_w0_3_5'
    
    
    T=dict()
    T['geometry']=dict()
    TG=T['geometry']
    
    
    
    #    can be changed
    TG['diameter']=324.e-3
    TG['thickness'] = 43.93e-3
    TG['ti'] =		45.7e-3
    TG['m'] = 		250.7
    TG['lengthOD'] = 3922.
    TG['R1OD']     = 900.
    TG['ksi1OD']   = 235.3
    TG['w0OD']     =3.5                            #.38 - 15.1     * diameter   #3.5
    TG['ksi2OD']   = 550.
    TG['groundWidthOD'] = 70.
    
    
    
    
    
    
    
    #    CANNOT be changed individually
    TG['Dot'] =		TG['diameter']/TG['thickness']
    TG['radius']=TG['diameter']/2.
    TG['inner_diameter']=TG['diameter']-2*TG['thickness']
    TG['area'] = pi/4.*( TG['diameter']**2 - TG['inner_diameter']**2)
    TG['length'] = 	TG['lengthOD']*TG['diameter']
    TG['R1'] = 	TG['R1OD']*TG['diameter']
    TG['ksi1'] = 	TG['ksi1OD']*TG['diameter']
    TG['w0'] = 	TG['w0OD']*TG['diameter'] 
    TG['ksi0'] = 	2.*TG['R1']*TG['w0']/TG['ksi1']
    TG['R2'] = 	TG['R1']*(TG['ksi1']/TG['ksi0']-1.)
    # TG['r_s'] = 	8050.
    # TG['r_h'] = 	800.
    # TG['r_i'] = 	833.
    # TG['r_w'] = 	1030.
    
    
    
    T['material'] = dict()
    TM = T['material']
    #   X-65
    TM['E']  = 207E9
    TM['s_y'] = 408.e6
    TM['s_0'] = 437.e6
    TM['e_0'] = .5/100.
    TM['n_exp'] = 13
    TM['n'] = .3
    TM['a'] = 10.8E-6
    # friction
    TM['m'] = 1.0
    TM['m_A'] = TM['m']
    TM['m_L'] = TM['m']
    TM['DT']  = 167 #
    TM['DT0'] = 0
    TM['density'] = 8050
    TM['poisson'] = .3
    TM['plastic'] =((430.4E+06, 0.000E+00) ,
                    (448.6E+06, 1.028E-03) ,
                    (458.5E+06, 1.842E-03) ,
                    (468.5E+06, 2.880E-03) ,
                    (478.5E+06, 4.186E-03) ,
                    (488.4E+06, 5.807E-03) ,
                    (498.4E+06, 7.788E-03) ,
                    (508.4E+06, 1.017E-02) ,
                    (518.4E+06, 1.300E-02) ,
                    (528.3E+06, 1.631E-02) ,
                    (538.3E+06, 2.011E-02) ,
                    (548.3E+06, 2.441E-02) ,
                    (558.2E+06, 2.922E-02) ,
                    (568.2E+06, 3.451E-02) ,
                    (578.2E+06, 4.028E-02) ,
                    (588.1E+06, 4.648E-02) ,
                    (598.1E+06, 5.310E-02) ,
                    (608.1E+06, 6.008E-02) ,
                    (618.0E+06, 6.739E-02) ,
                    (628.0E+06, 7.499E-02) ,
                    (638.0E+06, 8.286E-02) ,
                    (647.9E+06, 9.095E-02) ,
                    (657.9E+06, 9.924E-02) ,
                    (667.9E+06, 1.077E-01) ,
                    (677.8E+06, 1.163E-01) ,
                    (687.8E+06, 1.250E-01) ,
                    (697.8E+06, 1.338E-01) ,
                    (707.7E+06, 1.427E-01) ,
                    (717.7E+06, 1.516E-01) ,
                    (727.7E+06, 1.606E-01) ,
                    (737.7E+06, 1.696E-01) ,
                    (747.6E+06, 1.786E-01) ,
                    (757.6E+06, 1.876E-01) ,
                    (767.6E+06, 1.967E-01) ,
                    (777.5E+06, 2.057E-01) ,
                    (787.5E+06, 2.147E-01) ,
                    (797.5E+06, 2.237E-01) ,
                    (807.4E+06, 2.327E-01) ,
                    (817.4E+06, 2.417E-01) ,
                    (827.4E+06, 2.506E-01) ,
                    (837.3E+06, 2.594E-01) ,
                    (847.3E+06, 2.683E-01) ,
                    (857.3E+06, 2.771E-01) ,
                    (867.2E+06, 2.858E-01) ,
                    (877.2E+06, 2.945E-01) ,
                    (887.2E+06, 3.032E-01) ,
                    (897.1E+06, 3.117E-01) ,
                    (907.1E+06, 3.203E-01) ,
                    (917.1E+06, 3.288E-01) ,
                    (927.0E+06, 3.372E-01) ,
                    (937.0E+06, 3.456E-01) ,
                    (947.0E+06, 3.539E-01) ,
                    (957.0E+06, 3.622E-01) ,
                    (966.9E+06, 3.704E-01) ,
                    (976.9E+06, 3.786E-01) ,
                    (986.9E+06, 3.867E-01) ,
                    (996.8E+06, 3.948E-01) , )
    
    
    
    
    
    
    T['mesh']=dict()
    TMS=T['mesh']
    TMS['ksi2']=TG['ksi2OD']*TG['diameter']
    TMS['edgeNameSeq'] = ['ksi0','ksi1','ksi2','Xinf']
    TMS['edgeElemOD']  = [.2, .2, .2, 15.7]




modelname0=modelname
# Here make changes to the default parameters and the modelname
# Here update all dependent values : not done automatically
# Carefull if changing something that is not in TG !!!!!!! the following doe not work 

#                               TUPDATE={   key   :  ( value , format_in_modelname )    }
TUPDATE={           \
    'w0OD' : (.47, '_w0_{:5.2f}')        ,\
    }
    # 'lengthOD' :        ,\
    # 'ksi1OD' :          ,\
    # 'R1OD' :            ,\
modelname=modelname0
for key,value in TUPDATE.items():
    TG[key]=value[0]
    modelname+=value[1].format(value[0]).replace('.','_').replace(' ','_')




#    CANNOT be changed individually           SOS   but these should be updated after changes in geometry, hence they are here
TG['Dot'] =		TG['diameter']/TG['thickness']
TG['radius']=TG['diameter']/2.
TG['inner_diameter']=TG['diameter']-2*TG['thickness']
TG['area'] = pi/4.*( TG['diameter']**2 - TG['inner_diameter']**2)
TG['length'] = 	TG['lengthOD']*TG['diameter']
TG['R1'] = 	TG['R1OD']*TG['diameter']
TG['ksi1'] = 	TG['ksi1OD']*TG['diameter']
TG['w0'] = 	TG['w0OD']*TG['diameter'] 
TG['ksi0'] = 	2.*TG['R1']*TG['w0']/TG['ksi1']
TG['R2'] = 	TG['R1']*(TG['ksi1']/TG['ksi0']-1.)



# run the static
initialized = True
execfile('C:/TEMP/GlobalBuckling/RCM_static.py', __main__.__dict__)
mdb.jobs[job_name].waitForCompletion()
maxReachedTemperature = extractU3NT11CurveFromOdb(job_name)
completeJob = maxReachedTemperature >= TM['DT']


if not completeJob:
    # initialize necessery things
    print job_name+' - Needs further simulation with Riks algorithm'
    for k in range(3):
        TM['DT0']   = maxReachedTemperature * .8
        initialized = True
        execfile('C:/TEMP/GlobalBuckling/RCM_riks.py', __main__.__dict__)
        mdb.jobs[job_name].waitForCompletion()
        maxReachedTemperature = extractU3NT11CurveFromOdb(job_name)
        completeJob = maxReachedTemperature >= TM['DT']
        if completeJob:
            break
        
    

if not completeJob:
    print job_name+' - Failed to get to the necessary temperature with 3 Riks attempts'
# do any further post processing of all previous models

mdb.save()










# # # # These lines are a draftr for a code reading line by line a file of Initialization, and updating parameters that have not been updated already.
# It does not work currently
# # # line0="modelname = 'RCM_w0_3_5'"

# # # command="""modelname = 'RCM_w0_3_5'
    
    
    # # # """
# # # line="T=dict()"
# # # if line.contains('='):
    # # # lineInf=line
# # # else:
    # # # command+=line

# # # line0.replace(' ','').replace('\t','').split('=')[0]


# # # readline
# # # read until '=' is ecountered

# # # command = ????

# # # command[0].strip().split('=')
# # # check if this is any of the changed parameter
# # # if not, exec(command up to here)

# # # got to next
