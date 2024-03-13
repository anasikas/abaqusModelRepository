# C:/TEMP/GlobalBuckling/RCM_Default_Parameters_Class.py
"""Class Time with read-write properties."""



# **************************************************************************************
# These pare the initialization parameters for the RCM Analyses - DO NOT CHANGE THEM HERE, but you can 
# always alter their values after calling the initialization procedure in the local namespace in your iterative procedure
# **************************************************************************************
# execfile('C:/TEMP/GlobalBuckling/RCM_Default_Parameters.py', __main__.__dict__)
#---------------------------------------------------------------------------------------
# parameter definitions
#---------------------------------------------------------------------------------------
class mgeom:
    """Class mparam will initialize the parameters/variables used in the model definition in python scripting"""
    
    def __init__(self, 
        diameter  = 324.e-3,
        thickness = 43.93e-3,
        ti        = 45.7e-3,
        m         = 250.7,
        lengthOD  = 3922.,
        R1OD      = 900.,
        ksi1OD    = 235.3,
        w0OD      = 3.5,                            #.38 - 15.1     * diameter   #3.5
        ksi2OD    = 550.,
        groundWidthOD = 70.):
        """Initialize each attribute."""
        
        
        
        
                #    can be changed
        self.diameter  = diameter
        self.thickness = thickness
        self.ti        = ti
        self.m         = m
        self.lengthOD  = lengthOD
        self.R1OD      = R1OD
        self.ksi1OD    = ksi1OD
        self.w0OD      = w0OD                            #.38 - 15.1     * diameter   #3.5
        self.ksi2OD    = ksi2OD
        self.groundWidthOD = groundWidthOD
        # self.r_s = 	8050.
        # self.r_h = 	800.
        # self.r_i = 	833.
        # self.r_w = 	1030.
        
        
        
        
        #    CANNOT be changed individually
        self._Dot =		self.diameter/self.thickness
        self._radius=self.diameter/2.
        self._inner_diameter=self.diameter-2*self.thickness
        self._area = pi/4.*( self.diameter**2 - self._inner_diameter**2)
        self._length = 	self.lengthOD*self.diameter
        self._R1 = 	self.R1OD*self.diameter
        self._ksi1 = 	self.ksi1OD*self.diameter
        self._w0 = 	self.w0OD*self.diameter 
        self._ksi0 = 	2.*self._R1*self._w0/self._ksi1
        self._R2 = 	self._R1*(self._ksi1/self._ksi0-1.)
    
    
    # def __setattr__(self, attribute, value):
        # if not attribute in self.__dict__:
            # print "Cannot set %s" % attribute
        # else:
            # self.__dict__[attribute] = value
    
    
    @property
    def Dot(self):
        return self._Dot
    
    @Dot.setter
    def Dot(self, Dot):
        print self._Dot
        raise ValueError('Dot cannot be set manually, instead appropriately define diameter and thickness')



        
        
class mparam:
    """Class mparam will initialize the parameters/variables used in the model definition in python scripting"""
    
    def __init__(self, 
                modelname='RCM', 
                minute=0, 
                second=0):
        """Initialize each attribute."""
        
        self.modelname = modelname 
        self.geometry = dict()

        T=dict()
        T['geometry']=dict()
        TG=T['geometry']



        #    can be changed
        TG['diameter']  = 324.e-3
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
TM['DT0'] = 16.7
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
# TMS['elemSize']={edge : elemSize for edge,elemSize in zip( edge_name_seq, edge_elem_o_D)}


T['steps']=dict()
TS = T['steps']
TS[0] = {   'timePeriod' : 1e-08,
            'maxNumInc'  : 100,
            'initialInc' : 0.5e-8,
            'minInc'     : 1e-12,
            'maxInc'     : 0.5e-8    }

TS[1] = {   'timePeriod' : 1.,
            'maxNumInc'  : 200,
            'initialInc' : 0.02,
            'minInc'     : 5e-7,
            'maxInc'     : 0.02    }

TS[2] = {   'timePeriod' : .1,
            'maxNumInc'  : 40,
            'initialInc' : 0.01,
            'minInc'     : 5e-7,
            'maxInc'     : 0.01    }

TS[3] = {   'maxLPF' : 1.,
            'maxNumInc'  : 300,
            'initialArcInc' : 0.02,
            'minArcInc'     : 1e-12,
            'maxArcInc'     : 0.05    }