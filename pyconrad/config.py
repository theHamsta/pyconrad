from pyconrad import ClassGetter, AutoCompleteConrad
import os

_ = ClassGetter(
    'edu.stanford.rsl.conrad.utils',
    'java.beans',
    'java.io',
    'edu.stanford.rsl.conrad.geometry.trajectories'
)

# def initconfig( projtable_file):
#     conf = _.Configuration()
#     traj = _.ConfigFileBasedTrajectory.openAsGeometrySource(projtable_file, conf.getGeometry())
#     conf.setGeometry(traj)
#
#     print( "Source-Detector distance %f" % traj.getSourceToDetectorDistance())
#     print( "Pixel dimensions %fx%f" % (traj.getPixelDimensionX(), traj.getPixelDimensionY()))
#
#     return conf
def initconfig_fromxml(xmlfile):
    conf = _.Configuration.loadConfiguration(xmlfile)
    _.Configuration.setGlobalConfiguration(conf)

    geo = conf.getGeometry()
    # print( "Configuration loaded" )
    return conf

def initconfig_fromtrajxml(xmlfile):
    _.Configuration.loadConfiguration()
    conf = _.Configuration.getGlobalConfiguration()
    traj = _.Trajectory(deserialize_java_object(xmlfile))
    conf.setGeometry(traj)
    _.Configuration.setGlobalConfiguration(conf)

    # print( "Configuration loaded" )
    return conf
def initconfig_fromglobal():
    _.Configuration.loadConfiguration()
    conf = _.Configuration.getGlobalConfiguration()
    return conf

def change_detector_size( new_size ):
    geo = _.Configuration.getGlobalConfiguration().getGeometry()
    if new_size == [geo.getDetectorWidth(), geo.getDetectorHeight()]:
        return geo

    scaling = [ new_size[0] / geo.getDetectorWidth() ,
                new_size[1] / geo.getDetectorHeight() ]

    geo.setDetectorWidth(int(new_size[0]))
    geo.setDetectorHeight(int(new_size[1]))

    for i in range(geo.getProjectionStackSize()):
        p = geo.getProjectionMatrix(i)
        p.setKFromDistancesSpacingsSizeOffset(
            geo.getSourceToDetectorDistance(),
            _.SimpleVector.from_list([geo.getPixelDimensionX() / scaling[0], geo.getPixelDimensionY() / scaling[1] ]),
            _.SimpleVector.from_list(new_size),
            _.SimpleVector.from_list([0.,0.]),
            -1.,
            0.
        )
        geo.setProjectionMatrix(i,p)
    _.Configuration.getGlobalConfiguration().setGeometry(geo)
    return geo

def loadprojtable(projtable_file):
    if not os.path.isfile(projtable_file):
        raise ValueError('File does not exist')
    conf = _.Configuration.getGlobalConfiguration()
    traj = _.ConfigFileBasedTrajectory.openAsGeometrySource(projtable_file, conf.getGeometry())
    conf.setGeometry(traj)
    return conf

def serialize_java_object(xmlfile):
    ois = _.XMLDecoder(_.FileInputStream(xmlfile))
    obj = ois.readObject()
    ois.close()
    return obj

def deserialize_java_object(obj, xmlfile):
    ois = _.XMLEncoder(_.FileOutputStream(xmlfile))
    obj.prepareForSerialization()
    ois.writeObject(obj)
    ois.close()

def printconfig_info():
    conf = _.Configuration.getGlobalConfiguration()
    geo = conf.getGeometry()

    print( "Num projection matrices:  %i" % geo.getProjectionStackSize())
    print( "Source-Detector distance: %f" % geo.getSourceToDetectorDistance())
    print( "Pixel dimensions: %fx%f" % (geo.getPixelDimensionX(), geo.getPixelDimensionY()))

def get_conf() -> AutoCompleteConrad.edu.stanford.rsl.conrad.utils.Configuration:
    conf = _.Configuration.getGlobalConfiguration()
    return conf

def get_geometry() -> AutoCompleteConrad.edu.stanford.rsl.conrad.geometry.trajectories.Trajectory:
    conf = _.Configuration.getGlobalConfiguration()
    geo = conf.getGeometry()
    return geo
