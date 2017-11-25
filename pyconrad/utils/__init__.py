import pyconrad

_ = pyconrad.ClassGetter(
    'edu.stanford.rsl.conrad.utils',
    'java.beans',
    'java.io',
    'edu.stanford.rsl.conrad.geometry.trajectories'
)


def get_conf() -> pyconrad.AutoCompleteConrad.edu.stanford.rsl.conrad.utils.Configuration:
    conf = _.Configuration.getGlobalConfiguration()

    return conf


def get_geometry() -> pyconrad.AutoCompleteConrad.edu.stanford.rsl.conrad.geometry.trajectories.Trajectory:
    #  #TODO load config on pyconrad startup
    geo = _.Configuration.getGlobalConfiguration().getGeometry()
    return geo
