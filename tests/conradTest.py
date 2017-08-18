from jpype import *
from pyconrad import pyCONRAD

# def test_conrad():
conrad = pyCONRAD.getInstance()
#conrad.setup('8G', '1G',devdir=["C:\\Reconstruction\\CONRAD","C:\\Reconstruction\\CONRADRSL"])
conrad.setup('8G', '1G',dev_dirs=["C:\\Reconstruction\\CONRADRSL"])
#conrad.setup('8G', '1G')
#conrad.setup('8G', '1G')
conrad.start_reconstruction_filter_pipeline()
#conrad.startConrad()


imagePath = 'D:\\Data\\mrt_raw\\0016.tif'
#
# print('Load Image')
#
test = conrad.ij.ImagePlus(JString(imagePath))
test.show()

#Test for Singleton
conradSecondInstance = pyCONRAD.getInstance()
conradThirdInstance = pyCONRAD.PyConrad()

if conrad is conradSecondInstance is conradThirdInstance:
    print('Singleton test: passed')
else:
    print('Singleton test: failed')


#Forward and Backprojection Test
try:
    #Phantom parameter
    height_phantom = 512
    width_phantom = 512
    spacing_phantom = 0.5

    #Projection parameters
    detectorSpacing = 1.0
    detectorRows = 512

    # ...for parallel Beam
    projections_p = 250
    scanRange_p = 180

    # ...for fan beam
    projections_f = 250
    scanRange_f = 200
    angularIncrement_f = scanRange_f / projections_f

    # Reconstruction parameter
    recoX = 512
    recoY = 512
    recoSpacing = 0.5

    # Additional Parameter for Fan Beam Geometry
    d_si = 700
    d_sd = 1200

    # Using Fan Beam Geometry ?
    fanBeamGeometry = False

    #// // // // // // //
    #// Pipeline //
    #// // // // // // //


    phantom = conrad.classes.stanford.rsl.science.bier.flatPanel.myPhantom(height_phantom, width_phantom, spacing_phantom)
    phantom.show("Phantom")

    sinogram = conrad.classes.stanford.rsl.conrad.data.numeric.Grid2D
    if fanBeamGeometry is False:
        radon = conrad.classes.stanford.rsl.science.bier.flatPanel.Radon()
        sinogram = radon.calculateSinogram(phantom, JInt(projections_p), JDouble(detectorSpacing), JInt(detectorRows), JDouble(scanRange_p))
    else:
        fbp = conrad.classes.stanford.rsl.science.bier.flatPanel.FanBeamProjector(detectorSpacing, 512, angularIncrement_f, projections_f, d_si, d_sd)
        sinogram = fbp.calculateFanOgram(phantom)
        sinogram.show("Sinogram")
        sinogram = fbp.rebinSinogram(sinogram)
        sinogram.show("Sinogram rebinned")

    sinogram.show("Sinogram")

    # Ramp Filtering
    filter = conrad.classes.stanford.rsl.science.bier.flatPanel.RampFilter()


    sinogramFrequency = conrad.classes.stanford.rsl.conrad.data.numeric.Grid2D(filter.applyRampFilter(sinogram, detectorSpacing))

    sinogramSpatial = conrad.classes.stanford.rsl.conrad.data.numeric.Grid2D(filter.applyRamLakFilter(sinogram, detectorSpacing))

    # Backprojection

    back = conrad.classes.stanford.rsl.science.bier.flatPanel.Backprojector()
    #time1 = System.currentTimeMillis() TODO:Currently no access to java namespace except with import jpype -> make java namespace available over pyrad so noone needs to use jpype?
    reco2 = back.backproject(sinogramSpatial, recoX, recoY, recoSpacing);
    #time2 = System.currentTimeMillis();
    reco3 = back.backprojectOpenCL(sinogramSpatial, recoX, recoY, recoSpacing, 32);
    #time3 = System.currentTimeMillis();

    reco2.show("CPU");
    reco3.show("GPU");
    print('Flatpanel test passed')
except Exception as ex:
    print('Flatpanel test failed with Exception:',ex)
