# **************************************************************************************
# parametrize pipeline design
# **************************************************************************************
# execfile('C:/TEMP/GlobalBuckling/RCM_riks.py', __main__.__dict__)
#---------------------------------------------------------------------------------------
# parameter definitions
#---------------------------------------------------------------------------------------

manualInitialization=False

if 'initialized' in locals():  # means this script is called as a function from another script
    #exec('??????????????????', __main__.__dict__)
    del initialized
    print 'Called externally by other script'
elif not manualInitialization:
    # manualInitialization==False if want to use the defaults
    execfile('C:/TEMP/GlobalBuckling/RCM_Default_Parameters.py', __main__.__dict__)
else:     # use the parameters from here
    # Manually Initialize defaults # good for debugging and versatility when running a single analysis at a time
    modelname = 'RCM_riks'
    
    
    T=dict()
    T['geometry']=dict()
    TG=T['geometry']
    
    TG['diameter']=324.e-3
    TG['radius']=TG['diameter']/2.
    TG['thickness'] = 43.93e-3
    TG['Dot'] =		7.37
    TG['inner_diameter']=TG['diameter']-2*TG['thickness']
    TG['area'] = pi/4.*( TG['diameter']**2 - TG['inner_diameter']**2)
    TG['ti'] =		45.7e-3
    TG['m'] = 		250.7
    TG['length'] = 	3922*TG['diameter']
    TG['R1'] = 	900*TG['diameter']
    TG['ksi1'] = 	235.3*TG['diameter']
    TG['w0OD'] = 3.5                            #.38 - 15.1     * diameter   #3.5
    TG['w0'] = 	TG['w0OD']*TG['diameter'] 
    
    
    TG['ksi0'] = 	2.*TG['R1']*TG['w0']/TG['ksi1']
    TG['R2'] = 	TG['R1']*(TG['ksi1']/TG['ksi0']-1.)
    
    
    TG['groundWidthOD'] = 70.
    
    
    
    
    TG['r_s'] = 	8050.
    TG['r_h'] = 	800.
    TG['r_i'] = 	833.
    TG['r_w'] = 	1030.
    
    
    T['material'] = dict()
    TM = T['material']
    #   X-65
    TM['E'] = 207E9
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
    TM['DT'] = 167 #
    TM['DT0'] = 16.7
    TM['density'] = 8050
    TM['poisson'] = .3
    TM['plastic']= ((430.4E+06, 0.000E+00) ,
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
    TMS['ksi2']=550*TG['diameter']
    TMS['edgeNameSeq'] = ['ksi0','ksi1','ksi2','Xinf']
    TMS['edgeElemOD']  = [.2, .2, .2, 15.7]
    
    
    
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



# --------------------------------------------------------------------------------------
# Function Definitions
# --------------------------------------------------------------------------------------
def TupleAdd(tuple1,tuple2):
    """ This function adds tuples as if they were vectors"""
    #tuple1=(0,1)
    #tuple2=(1,0)
    #TupleAdd(tuple1,tuple2)
    return tuple([ x+y for x,y in zip(tuple1,tuple2)])

def TupleMid(tuple1,tuple2):
    """ This function find the average of two tuples as if they were vectors"""
    #tuple1=(0,1)
    #tuple2=(1,0)
    #TupleAdd(tuple1,tuple2)
    return tuple([ (x+y)/2. for x,y in zip(tuple1,tuple2)])

def MakeTuple3D(tuple1):
    """ This function adds zeros to a tuple so that it has 3 components"""
    #tuple1=(0,1)
    #tuple2=(1,0)
    #TupleAdd(tuple1,tuple2)
    return tuple1 + tuple([ 0. for i in range(len(tuple1),3)])

def CreateReferencePoints(_Assembly, _point_dictionary):
    """Add Assembly Reference points at every point in _point_dictionary with the provided names
    _point_dictionary = { _point_RP_name : _coords_tuple }"""
    
    for _point_name,_point_coord in _point_dictionary.items():
        _point=MakeTuple3D(_point_coord)
        _Assembly.ReferencePoint( point=  _point)
        _Assembly.features.changeKey(fromName=_Assembly.features.keys()[-1], toName=_point_name)

def ReadSeedDataFromFile(_file_path):
    """ Reads Seed Data line by line from txt file '_file_path' and returns (_dict,_seed_data_headers)
    _dict              ={ edge_name : {_header : values} }
    _seed_data_headers =['_bias' , '_edge_bias' , '_ratio', '_num'] # an ordered list of the _seed_data_headers, necessary if headers names change later, 
                                                                to get items ordered when unpacking (_bias, _bias_edges,_seed_number,_ratio)"""
    
    # # # --------------------------------------
    #  a) read seeding data from file
    # # # --------------------------------------
    with open(_file_path, mode='r') as _myfile:
        _t=_myfile.readline()
        while _t[0]!='_':
            print 'Initial Lines:'+_t
            _t=_myfile.readline()
        
        _seed_data_headers=_t.strip('\n').split("\t")
        _seed_data_headers.pop(0)             # the _seed_data_headers[0] element -'_edge'- is the edge_name, not a _seed_data_header so it is removed
        _t=_myfile.readline()
        _dict={}
        while _t.strip():    # while not emply character
            _t=[int(elem) if elem.isdigit() else elem for elem in _t.strip('\n').split("\t")]
            _dict.update({_t[0] : { key : value for key,value in zip(_seed_data_headers,_t[1:])}})
            _t=_myfile.readline()
    
    return (_dict,_seed_data_headers)



def SeedEdgesAndMesh(_Assembly,_Instance,_EdgeNameDict,_dict,_headers):
    """ Seeds and generates the mesh of an Assembly instance based on the seed data of a dictionary
    _Assembly     = tubeAssembly
    _Instance     = tubeMaleInstance
    _EdgeNameDict = TM['edges']                     # _EdgeNameDict={ abaqus_edge_index : edge_name }  # edge_name based on my convention
    _dict         = _dict                           # _dict        ={ edge_name : {_header : values} }
    _headers      =_headers                         # _headers     =['_bias' , '_edge_bias' , '_ratio', '_num'] # necessary to get items ordered when unpacking (_bias, _bias_edges,_seed_number,_ratio)"""
    
    # ----------------------------
    # assign seeds in each edge
    # ----------------------------
    for i, (edge_id, edge_name) in enumerate(_EdgeNameDict.items()):
        _my_mask=_Instance.edges.findAt( _Instance.edges[edge_id].pointOn )
        _bias        = _dict[edge_name][_headers[0]]        # _bias        ='SINGLE'/'DOUBLE'/'NONE'
        _bias_edges  = _dict[edge_name][_headers[1]]        # _bias_edges  ='end1Edges'/'end2Edges'
        _seed_number = _dict[edge_name][_headers[2]]        # _seed_number = 10
        _ratio       = _dict[edge_name][_headers[3]]        # _ratio       = 5
        
        # seed edge based on own bias options
        if _bias =='SINGLE':
            # the convention is that an edge has the same name as its first vertex, which all have named previously.
            # Hence when bias in the first side of the line (line_name==_bias_edges) in which case _bias_edges is changed to end1Edges - # that happens before this part of the code
            _bias_edges = 'end1Edges' if _bias_edges==edge_name else 'end2Edges'
            if _bias_edges=='end1Edges':
                _Assembly.seedEdgeByBias(biasMethod=SINGLE, end1Edges=_my_mask,
                    ratio=_ratio, number=_seed_number, constraint=FINER)
            elif _bias_edges=='end2Edges':
                _Assembly.seedEdgeByBias(biasMethod=SINGLE, end2Edges=_my_mask,
                    ratio=_ratio, number=_seed_number, constraint=FINER)
            else:
                print 'ERROR: Acceptable {:s} bias values are "end1Edges", "end2Edges"\n The given value is "{:s}"'.format(_bias,_bias_edges)
            
        elif _bias =='DOUBLE':
            if _bias_edges=='endEdges':
                _Assembly.seedEdgeByBias(biasMethod=DOUBLE, endEdges=_my_mask,
                    ratio=_ratio, number=_seed_number, constraint=FINER)
            elif _bias_edges=='centerEdges':
                _Assembly.seedEdgeByBias(biasMethod=DOUBLE, centerEdges=_my_mask,
                    ratio=_ratio, number=_seed_number, constraint=FINER)
            else:
                print 'ERROR: Acceptable {:s} bias values are "end1Edges", "end2Edges"\n The given value is "{:s}"'.format(_bias,_bias_edges)
            
        elif _bias =='NONE' or _bias =='':
            _Assembly.seedEdgeByNumber(edges=_my_mask, number=_seed_number, constraint=FINER)
            
        else:
            print 'ERROR: Acceptable _bias values are SINGLE, DOUBLE, NONE, ""\n' \
                + 'given value is "{:s}"'.format(_bias)
    
    _Assembly.generateMesh(regions=(_Instance,))

# _Assembly.seedEdgeByBias(biasMethod=DOUBLE, endEdges=pickedEndEdges, minSize=0.0038, 
    # maxSize=0.019, constraint=FINER)
# p.seedEdgeByBias(biasMethod=SINGLE, end2Edges=pickedEdges2, minSize=0.00038, 
    # maxSize=0.005, constraint=FINER)
    # p.seedEdgeBySize(edges=pickedEdges, size=0.025, deviationFactor=0.1, 
    # constraint=FINER)

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
    
    # # # Adds _1 etc in the end of the 'name' if it already exists in the 'existing_names' list - this is simpler and more archaic
    # # if name in existing_names:
        # # expand = 0
        # # while True:
            # # expand += 1
            # # new_name = name + '_' + str(expand)
            # # if new_name in existing_names:
                # # continue
            # # else:
                # # name = new_name
                # # print 'Changed name to :'+ name
                # # break
    
    # # return name
    # AutoNumberIfNameExists(modelname,existing_names)




def IdentifyEnd1OfEdge(_Assembly,
                       _Instance,
                       _edge_dict,
                       _vertex_dict):
    """This may be usefull in using bias in lines that are generated my Abaqus and the naming of their sides is not known but it may be obsolete
    it does contain examples of how print might be used"""
    # This little code verifiers that the Bias edge1 of the line segments  is the starting point of the segment as I drew it 
    # e.g. E: O,    V:O,    BIAS:end1Edges
    #      E: O,    V:F0,   BIAS:end2Edges
    _end1IsStartPoint=dict()
    for edge_index,_edge_name in _edge_dict.items():
        _edge   = _Instance.edges[edge_index]
        # bias seed the vertex to find Edge1/Edge2 of each edge and then delete seeds
        _edge_mask=_Instance.edges.findAt( _Instance.edges[edge_index].pointOn )
        _Assembly.seedEdgeByBias(biasMethod=SINGLE, end1Edges=_edge_mask, 
            ratio=5.0, number=5, constraint=FINER)
        _vertex_index = _Assembly.getEdgeSeeds(edge=_edge,attribute=VERTEX_ADJ_TO_SMALLEST_ELEM)
        # alternatively 
        # _vertex_index = _Instance.edges[_edge_index].getVertices()[0]
        _Assembly.deleteSeeds(regions=_edge_mask)
        if _edge_dict[edge_index]==_vertex_dict[_vertex_index]:
            _end1IsStartPoint[_edge_name]=True
        else:
            _end1IsStartPoint[_edge_name]=False
        #
        # print 'E:%4s,    V:%4s,    BIAS:%8s' %(TF['edges'][edge_index], TF['vertices'][_vertex_index],TF['seed_bias'][edge_index])    # https://pyformat.info/
        # print 'E:{:<4s},    V:{:<4s},    BIAS:{:<8s}'.format(TF['edges'][edge_index], TF['vertices'][_vertex_index],TF['seed_bias'][edge_index])
        # print 'E:{edge:<4s},    V:{vertex:<4s},    BIAS:{bias:<8s}'.format(edge=TF['edges'][edge_index], vertex=TF['vertices'][_vertex_index], bias=TF['seed_bias'][edge_index])
        
        # print 'end1Edges: means bias at the "starting" point of the line as I drew it'
        # print 'end2Edges: means bias at the "ending"   point of the line as I drew it'
        # I can see which one is the start by the pointsOn method of the edge which gives a point closer to the begining
    
    
    
    
    return _end1IsStartPoint

# _Assembly    = tubeAssembly
# _Instance    = tubeFemaleInstance
# _edge_dict   = TF['edges']
# _vertex_dict = TF['vertices']
# _end1IsLineStartPoint=IdentifyEnd1OfEdge(_Assembly,
                       # _Instance,
                       # _edge_dict,
                       # _vertex_dict)



# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
from abaqus import *
from abaqusConstants import *
import regionToolset
from textRepr import*

session.viewports['Viewport: 1'].setValues(displayedObject=None)

# -------------------------------------------------------------------------------------
# Create the model
if not ('Model-1' in mdb.models.keys()):
	mdb.Model(name='Model-1', modelType=STANDARD_EXPLICIT)

if modelname in mdb.models.keys():
	del mdb.models[modelname]

mdb.models.changeKey(fromName='Model-1', toName=modelname)
tubeModel=mdb.models[modelname]


# -------------------------------------------------------------------------------------
# Create the part

import sketch
import numpy as np

# *************************************************************************************
# a) Tube
# *************************************************************************************
#
# Define the curve to plot

wo1 = lambda x: TG['w0']*(  1 - x**2/TG['ksi0']/TG['ksi1']  )
wo2 = lambda x: TG['w0']/(  1 - TG['ksi0']/TG['ksi1']  ) *  (  1 - x/TG['ksi1']  )**2
wo3 = lambda x: 0.*x
w   = lambda x: wo1(x) if x<=TG['ksi0'] else wo2(x)


# # # # # # # # # # def w(X):
    # # # # # # # # # # """the curve defined by Zhang_Kyriakides_2021"""
    # # # # # # # # # # # # # # wo1 = lambda x: TG['w0']*(  1 - x**2/TG['ksi0']/TG['ksi1']  )
    # # # # # # # # # # # # # # wo2 = lambda x: TG['w0']/(  1 - TG['ksi0']/TG['ksi1']  ) *  (  1 - x/TG['ksi1']  )**2
    # # # # # # # # # # # # # # wo3 = lambda x: 0.*x
    # # # # # # # # # # # # # # w   = lambda x: wo1(x) if x<=TG['ksi0'] else wo2(x)
    # # # # # # # # # # W=list()
    # # # # # # # # # # for x in t:
        # # # # # # # # # # if x<=TG['ksi0']:
            # # # # # # # # # # W.append(     TG['w0']*(  1 - x**2/TG['ksi0']/TG['ksi1']  )     )
        # # # # # # # # # # elif x<=TG['ksi1']:
            # # # # # # # # # # W.append(     TG['w0']/(  1 - TG['ksi0']/TG['ksi1']  ) *  (  1 - x/TG['ksi1']  )**2     )
        # # # # # # # # # # else:
            # # # # # # # # # # W.append(     0.     )
        
    
    # # # # # # # # # # return W

# define drawing points
n1=int(TG['ksi0']/(.2*TG['diameter']))+1
n1+=  1 - n1 % 2                            # if even, add one to make it odd
n2=int((TG['ksi1']-TG['ksi0'])/(.2*TG['diameter']))+1
n2+=  1 - n1 % 2                            # if even, add one to make it odd

t = np.linspace(0,TG['ksi0'],n1)
tt= np.linspace(TG['ksi0'],TG['ksi1'],n2)
ttt= (TG['ksi1'],TG['length'])

y = map(w,t)
yy = map(w,tt)
yyy = map(wo3,ttt)

ty_data=tuple(zip(t,y)+zip(tt,yy)+zip(ttt,yyy))

# # # # plot curve in viewport
# # # import visualization
# # # import xyPlot
# # # session.viewports['Viewport: 1'].setValues(displayedObject=None)
# # # if 'PipePath' not in session.xyPlots.keys():
    # # # session.XYPlot('PipePath')

# # # xyp = session.xyPlots['PipePath']
# # # chartName = xyp.charts.keys()[0]
# # # chart = xyp.charts[chartName]
# # # xQuantity = visualization.QuantityType(type=NONE)
# # # yQuantity = visualization.QuantityType(type=NONE)
# # # xy1 = xyPlot.XYData(data=ty_data, 
    # # # sourceDescription='Entered from keyboard', axis1QuantityType=xQuantity, 
    # # # axis2QuantityType=yQuantity, )
# # # c1 = session.Curve(xyData=xy1)
# # # chart.setValues(curvesToPlot=(c1, ), )
# # # session.viewports['Viewport: 1'].setValues(displayedObject=xyp)



#) Create the sketch
tubeSketch = tubeModel.ConstrainedSketch(name='tubeSketch', 
    sheetSize=2*TG['length'])                                            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111
# session.viewports['Viewport: 1'].setValues(displayedObject=tubeSketch)
# session.viewports['Viewport: 1'].setValues(displayedObject=None)
# tubeSketch.setPrimaryObject(option=STANDALONE)
TS=dict()
ty_data = tuple( zip(t,y)+ zip(tt,yy) )
ksi0 = tubeSketch.Spline( ty_data )
TS['ksi0']=dict()
TS['ksi0']['id']=ksi0.id
TS['ksi0']['pointOn']=ksi0.pointOn
# ty_data=tuple(zip(tt,yy))
# ksi1 = tubeSketch.Spline( ty_data )
# TS['ksi1']=dict()
# TS['ksi1']['id']=ksi1.id
# TS['ksi1']['pointOn']=ksi1.pointOn
ty_data=tuple(zip(ttt,yyy))
ksi2 = tubeSketch.Line( point1=ty_data[0], point2=ty_data[1] )
TS['ksi2']=dict()
TS['ksi2']['id']=ksi2.id
TS['ksi2']['pointOn']=ksi2.pointOn
# # ksi2 = tubeSketch.Line( point1=(0,0), point2=(TG['length'],0) )
# # TS['ksi2']=dict()
# # TS['ksi2']['id']=ksi2.id
# # TS['ksi2']['pointOn']=ksi2.pointOn
# tubeSketch.unsetPrimaryObject()


# *************************************************************************************
# b) Ground
# *************************************************************************************
#) Create the sketch
groundSketch=tubeModel.ConstrainedSketch(name='groundSketch', 
    sheetSize=2.5*TG['length'])
groundSketch.Line(  point1=(-TG['diameter'], -TG['radius']*0), 
                    point2=(TG['length']+TG['diameter'], -TG['radius']*0))


# *************************************************************************************
# b) Ground Partition
# *************************************************************************************
#) Create the sketch
groundPartitionSketch=tubeModel.ConstrainedSketch(name='groundPartitionSketch', 
    sheetSize=2.5*TG['length'])

my_canvasXZ=[-30, -25, -20, -15, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
for offset in my_canvasXZ:
    groundPartitionSketch.Line(  point1=(-TG['diameter']             , -TG['diameter']*offset), 
                        point2=(TG['length']+TG['diameter'] , -TG['diameter']*offset))

my_canvasYZ=[0, TG['ksi0'], TG['ksi1'], TMS['ksi2'], TG['length']]
for offset in my_canvasYZ:
    groundPartitionSketch.Line(  point1=(offset, -TG['diameter']*TG['groundWidthOD']/2.), 
                        point2=(offset,  TG['diameter']*TG['groundWidthOD']/2))



# ---------------------------------------------------------------------------------------------
# create the Parts
# ---------------------------------------------------------------------------------------------

import part

# *************************************************************************************
# a) Tube
# *************************************************************************************
tubePart=tubeModel.Part(name='tubePart', 
    dimensionality=THREE_D, type=DEFORMABLE_BODY)
tubePart.BaseWire(sketch=tubeSketch)

# Create Reference Point
point=tubePart.vertices.findAt(((0,TG['w0'],0),))[0]
tubePart.ReferencePoint(point=point)

# Create Datums
TMS['datums']=dict()
feature=tubePart.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=0.)
tubePart.features.changeKey(fromName=tubePart.features.keys()[-1] , toName='Datum_X0')
TMS['datums']['X0']=tubePart.datums[feature.id]
feature=tubePart.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=TG['ksi0'])
tubePart.features.changeKey(fromName=tubePart.features.keys()[-1] , toName='Datum_ksi0')
TMS['datums']['ksi0']=tubePart.datums[feature.id]
feature=tubePart.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=TG['ksi1'])
tubePart.features.changeKey(fromName=tubePart.features.keys()[-1] , toName='Datum_ksi1')
TMS['datums']['ksi1']=tubePart.datums[feature.id]
feature=tubePart.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=TMS['ksi2'])
tubePart.features.changeKey(fromName=tubePart.features.keys()[-1] , toName='Datum_ksi2')
TMS['datums']['ksi2']=tubePart.datums[feature.id]
feature=tubePart.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=TG['length'])
tubePart.features.changeKey(fromName=tubePart.features.keys()[-1] , toName='Datum_Xinf')
TMS['datums']['Xinf']=tubePart.datums[feature.id]

# Create Partitions
TMS['partitions']=dict()
pickedEdges = tubePart.edges.findAt(((t[1],y[1],0),))
feature = tubePart.PartitionEdgeByDatumPlane(datumPlane=TMS['datums']['ksi0'], edges=pickedEdges)
tubePart.features.changeKey(fromName=tubePart.features.keys()[-1] , toName='Partition_ksi0')
TMS['partitions']['ksi0']=feature
# pickedEdges = tubePart.edges.findAt(((tt[1],yy[1],0),))
# feature = tubePart.PartitionEdgeByDatumPlane(datumPlane=TMS['datums']['ksi1'], edges=pickedEdges)
# tubePart.features.changeKey(fromName=tubePart.features.keys()[-1] , toName='Partition_ksi1')
# TMS['partitions']['ksi1']=feature
pickedEdges = tubePart.edges.findAt(((TG['length'],0,0),))
feature = tubePart.PartitionEdgeByDatumPlane(datumPlane=TMS['datums']['ksi2'], edges=pickedEdges)
tubePart.features.changeKey(fromName=tubePart.features.keys()[-1] , toName='Partition_ksi2')
TMS['partitions']['ksi2']=feature

# Create Sets
edges=tubePart.edges[0:0]
for coords in tubePart.edges.pointsOn:
    edges+=tubePart.edges.findAt(  coords  )

tubePart.Set(edges=edges, name='tubeLength')

verts = tubePart.vertices.findAt( ( (0., TG['w0'], 0) ,) )
tubePart.Set(vertices=verts, name='X0')
verts = tubePart.vertices.findAt( ((TG['length'],0.,0) ,) )
tubePart.Set(vertices=verts, name='Xinf')

# Create Surfaces
edges=tubePart.edges[0:0]
for coords in tubePart.edges.pointsOn:
    edges+=tubePart.edges.findAt(  coords  )

tubePart.Surface(circumEdges=edges, name='tubeSurf')









# *************************************************************************************
# b) Ground
# *************************************************************************************

groundPart = tubeModel.Part(name='groundPart', dimensionality=THREE_D, 
    type=ANALYTIC_RIGID_SURFACE)
groundPart.AnalyticRigidSurfExtrude(sketch=groundSketch, depth=TG['groundWidthOD']*TG['diameter'])
refPoints = groundPart.ReferencePoint((0,-TG['radius']*0.,0))

# Create Datums
# Create Partitions   this partition creates a grid on ther ground as the sketch indicated but it is not vissible in the output so it is removed here
# # # # # # pickedFaces  = groundPart.faces.findAt( ((0,0,0), ) )
# # # # # # sketchPlane  = pickedFaces[0]
# # # # # # sketchUpEdge = groundPart.edges.findAt( ((TG['length']+TG['diameter'],0,0), ) )[0]
# # # # # # groundPartTransformation = groundPart.MakeSketchTransform(sketchPlane=sketchPlane, sketchUpEdge=sketchUpEdge, 
    # # # # # # sketchPlaneSide=SIDE1, origin=(0, 0.0, 0.0))
# # # # # # s1 = tubeModel.ConstrainedSketch(name='__profile__', 
    # # # # # # sheetSize=2542.88, gridSpacing=63.57, transform=groundPartTransformation)
# # # # # # s1.retrieveSketch( sketch=groundPartitionSketch)
# # # # # # groundPart.PartitionFaceBySketch(sketchUpEdge=sketchUpEdge, faces=pickedFaces, sketch=s1)
# # # # # # del tubeModel.sketches['__profile__']

# Create Sets
refPoints = ( groundPart.referencePoints[refPoints.id] , )
groundPart.Set(referencePoints=refPoints, name='RP')

# Create Surfaces
side1Faces=groundPart.faces[0:0]
for coords in groundPart.faces.pointsOn:
    side1Faces+=groundPart.faces.findAt(  coords  )

groundPart.Surface(side1Faces=side1Faces, name='Ground')


# -------------------------------------------------------------------------------------
# Create material
# -------------------------------------------------------------------------------------

import material

# Create materail

tubeMaterial=tubeModel.Material(name='X65')
tubeMaterial.Density(table=(( TM['density'], ), ))
tubeMaterial.Elastic(table=(( TM['E'], TM['poisson']), ))
tubeMaterial.Plastic(table=TM['plastic'])
tubeMaterial.Expansion(table=(( TM['a'], ), ))

# -------------------------------------------------------------------------------------
# Create solid section and assign parts to it
# -------------------------------------------------------------------------------------

import section

tubeProfile= tubeModel.PipeProfile(name='tubeProfile', r=TG['radius'], t=TG['thickness'], 
    formulation=THICK_WALL)
tubeSection = tubeModel.BeamSection(name='tubeSection', 
    integration=DURING_ANALYSIS, poissonRatio=0.0, profile='tubeProfile', 
    material='X65', temperatureVar=LINEAR, consistentMassMatrix=False)



# Assign this section to the tube and assign section axes

region = tubePart.sets['tubeLength']
tubePart.SectionAssignment(region=region, sectionName='tubeSection', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
tubePart.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
    -1.0))




# -------------------------------------------------------------------------------------
# Create the assembly
# -------------------------------------------------------------------------------------

import assembly

# --------------------------------------
# Create the part Instances
# --------------------------------------
tubeAssembly = tubeModel.rootAssembly
tubeInstance=tubeAssembly.Instance(name='tubeInstance', part=tubePart, dependent=ON)
groundInstance=tubeAssembly.Instance(name='groundInstance', part=groundPart, dependent=ON)

tubeAssembly.rotate(instanceList=('tubeInstance', ), axisPoint=(0.0, 0.0, 0.0), 
    axisDirection=(1.0, 0.0, 0.0), angle=-90.0)
# tubeAssembly.rotate(instanceList=('tubeInstance', ), axisPoint=(0.0, 0.0, 0.0), 
    # axisDirection=(1.0, 0.0, 0.0), angle=-90.0)


# -------------------------------------------------------------------------------------
# Create the step
# -------------------------------------------------------------------------------------

import step

# Create the loading step
tubeModel.StaticStep(name='Weight', 
    previous='Initial', 
    description='Apply Gravity', 
    timePeriod  = T['steps'][0]['timePeriod'],
    maxNumInc   = T['steps'][0]['maxNumInc'], 
    initialInc  = T['steps'][0]['initialInc'], 
    minInc      = T['steps'][0]['minInc'], 
    maxInc      = T['steps'][0]['maxInc'], 
    nlgeom      = ON)

# Create the preloading step
tubeModel.StaticStep(name='Thermal0', 
    previous='Weight', 
    timePeriod  = T['steps'][2]['timePeriod'],
    maxNumInc   = T['steps'][2]['maxNumInc'], 
    initialInc  = T['steps'][2]['initialInc'], 
    minInc      = T['steps'][2]['minInc'], 
    maxInc      = T['steps'][2]['maxInc'], 
    nlgeom      = ON)
region=tubeInstance.sets['X0']
tubeModel.steps['Thermal0'].Monitor(dof=3, node=region, 
    frequency=1)

# Create the riks loading step
region=tubeInstance.sets['X0']
tubeModel.StaticRiksStep(name='ThermalLoad', 
    previous='Thermal0', 
    maxLPF          = T['steps'][3]['maxLPF'], 
    maxNumInc       = T['steps'][3]['maxNumInc'], 
    initialArcInc   = T['steps'][3]['initialArcInc'], 
    minArcInc       = T['steps'][3]['minArcInc'],
    maxArcInc       = T['steps'][3]['maxArcInc'],
    maximumDisplacement=0.001, region=region)
tubeModel.steps['ThermalLoad'].Restart(frequency=50, 
    overlay=OFF)
region=tubeInstance.sets['X0']
tubeModel.steps['ThermalLoad'].Monitor(dof=3, node=region, 
    frequency=1)




# # # # -------------------------------------------------------------------------------------
# # # # Create the field output requests
# # # # Leave the defaults

tubeModel.fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 
    'CDISP', 'NT'))
regionDef=tubeInstance.sets['X0']
tubeModel.HistoryOutputRequest(name='Temperature', 
    createStepName='Thermal0', variables=('NT', 'U3', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
# --------------------------------------
# Create the History Output Requests
# --------------------------------------

# tubeModel.HistoryOutputRequest(name='RPF', 
                                # createStepName='Insertion', 
                                # variables=('U1', 'U2', 'UR1', 'UR2',  
                                    # 'RF1', 'RF2', 'RM1', 'RM2',  
                                    # 'CF1', 'CF2', 'CM1', 'CM2'),
                                # frequency=1,
                                # region=RPF_region, 
                                # sectionPoints=DEFAULT, rebar=EXCLUDE)

# tubeModel.HistoryOutputRequest(name='RPM', 
                                # createStepName='Insertion', 
                                # variables=('U1', 'U2', 'UR1', 'UR2',  
                                    # 'RF1', 'RF2', 'RM1', 'RM2',  
                                    # 'CF1', 'CF2', 'CM1', 'CM2'),
                                # frequency=1,
                                # region=RPM_region, 
                                # sectionPoints=DEFAULT, rebar=EXCLUDE)

# Now delete the original history output request
#del tubeModel.historyOutputRequests['H-Output-1']
# tubeModel.fieldOutputRequests['F-Output-1'].setValues(
    # frequency=10)

# -------------------------------------------------------------------------------------
# Apply boundary conditions & Loads & PredefinedFields

# Step : Initial

region = tubeInstance.sets['X0']
tubeModel.DisplacementBC(name='X0', 
    createStepName='Initial', region=region, u1=SET, u2=UNSET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)

region = tubeInstance.sets['Xinf']
tubeModel.DisplacementBC(name='Xinf', 
    createStepName='Initial', region=region, u1=SET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)

region = groundInstance.sets['RP']
tubeModel.DisplacementBC(name='Ground', 
    createStepName='Initial', region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)

region = tubeInstance.sets['tubeLength']
tubeModel.Temperature(name='T0', createStepName='Initial', 
    region=region, distributionType=UNIFORM, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(0.0, ))




# Step : Weight   #    the cross section is composite , and anosis must be included

region = tubeInstance.sets['tubeLength']
tubeModel.LineLoad(name='Weight', 
    createStepName='Weight', region=region, comp2=-TG['m']*9.81)
# # # tubeModel.Gravity(name='Gravity', createStepName='Weight', 
    # # # comp2=-9.81, distributionType=UNIFORM, field='', region=region)
# # # print 9.81*TG['area']*TM['density']



# Step : Thermal0

# tubeModel.boundaryConditions['Xinf'].setValuesInStep(
    # stepName='ThermalLoad', u1=-1.0)

tubeModel.predefinedFields['T0'].setValuesInStep(
    stepName='Thermal0', magnitudes=(TM['DT0'], ))
# region = tubeInstance.sets['tubeLength']
# tubeModel.Temperature(name='DT', 
    # createStepName='ThermalLoad', region=region, distributionType=UNIFORM, 
    # crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(TM['DT'], ))




# Step : Thermal Load

# tubeModel.boundaryConditions['Xinf'].setValuesInStep(
    # stepName='ThermalLoad', u1=-1.0)

tubeModel.predefinedFields['T0'].setValuesInStep(
    stepName='ThermalLoad', magnitudes=(TM['DT'], ))
# region = tubeInstance.sets['tubeLength']
# tubeModel.Temperature(name='DT', 
    # createStepName='ThermalLoad', region=region, distributionType=UNIFORM, 
    # crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(TM['DT'], ))




# -------------------------------------------------------------------------------------
# Create contact interaction

# Interaction Properties Definition
contactProperty=tubeModel.ContactProperty('contactProperty')
contactProperty.TangentialBehavior(
    formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
    pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((
    TM['m'], ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
    fraction=0.005, elasticSlipStiffness=None)
contactProperty.NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)

# Interaction Definition
contactInteraction = tubeModel.ContactStd(name='contactInteraction', 
    createStepName='Initial')
region1 = groundInstance.surfaces['Ground']
region2 = tubeInstance.surfaces['tubeSurf']
tubeModel.SurfaceToSurfaceContactStd(name='contactInteraction', 
    createStepName='Initial', master=region1, slave=region2, sliding=FINITE, 
    thickness=ON, interactionProperty='contactProperty', adjustMethod=NONE, 
    initialClearance=OMIT, datumAxis=None, clearanceRegion=None)




# -------------------------------------------------------------------------------------
# Create the mesh

import mesh

# Assign Element Type 

elemType1 = mesh.ElemType(elemCode=PIPE32, elemLibrary=STANDARD)                # PIPE32, ELBOW32



# _temp=list(tubePart.edges.pointsOn)
# _temp.sort(reverse=False, key= lambda a: a[0][0])
# print _temp

# edge_names=['ksi0','ksi1','ksi2','Xinf']
# edge_elem_o_D = [.2, .2, .2, 15.7] 
# TMS['edges']=dict()
# for edge_name, point in zip(edge_names,_temp):
    # TMS['edges'][edge_name]=tubePart.edges.findAt( point )[0]


_temp=list(tubePart.edges.pointsOn)
_temp.sort(reverse=False, key= lambda a: a[0][0])



edge_names    = TMS['edgeNameSeq']      # edge_names=['ksi0','ksi1','ksi2','Xinf']
edge_elem_o_D = TMS['edgeElemOD']       # edge_elem_o_D = [.2, .2, .2, 15.7]



for edge_name, point, elem_o_D in zip(edge_names,_temp,edge_elem_o_D):
    pickedEdges=tubePart.edges.findAt( point )
    tubePart.seedEdgeBySize(edges=pickedEdges, size=elem_o_D*TG['diameter'], deviationFactor=0.1, 
        constraint=FINER)
    pickedRegions =regionToolset.Region(edges=pickedEdges)
    tubePart.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))

tubePart.generateMesh()


# -------------------------------------------------------------------------------------
# Define job name
# -------------------------------------------------------------------------------------

job_name=modelname


import os                  # import OS module if needed
# os.chdir(r"C:\TEMP")      # set work directory

path = os.getcwd()                          # get path of scratch directory
dir_files_list=os.listdir(path)             # Get the list of all files and directories

existing_names =[ file.replace('.odb','') for file in dir_files_list \
            if file.startswith(job_name) & file.endswith('.odb') ]          # optionally filter list

job_name = AutoNumberIfNameExists(name=job_name,existing_names=existing_names)



# -------------------------------------------------------------------------------------
# Create and run a job
# -------------------------------------------------------------------------------------

import job

# -------------------
# Create the job
# -------------------

mdb.Job(name= job_name ,model= modelname,type=ANALYSIS,    
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE,
        description='Run the contact simulation',
        parallelizationMethodExplicit=DOMAIN, multiprocessingMode=DEFAULT,
        numDomains=6, userSubroutine='', numCpus=6, memory=90,
        memoryUnits=PERCENTAGE, scratch='',echoPrint=OFF, modelPrint=OFF,
        contactPrint=OFF, historyPrint=OFF)


# -------------------
# Run the job 
# -------------------

mdb.jobs[job_name].submit(consistencyChecking=OFF)

# -------------------
# Do not return control untill the job is finnished running
# -------------------

#mdb.jobs[job_name].waitForCompletion()

# -------------------
# End of run job