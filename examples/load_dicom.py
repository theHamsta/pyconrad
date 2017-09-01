# install: pip install pydicom
# tutorial: http://pydicom.readthedocs.io/en/stable/pydicom_user_guide.html
import dicom
from pyconrad import PyConrad


jvm = PyConrad()
jvm.setup()

jvm.add_import('edu.stanford.rsl.conrad.data.numeric')

dicom_path = '/dos/d/endres_2017-08-04/NS_Fistel/rohdata1.IMA'
ds = dicom.read_file(dicom_path)

print("Patient age: %s" % ds.PatientsAge)
# get numpy array
pixel_array = ds.pixel_array
# get conrad grid
grid3d = jvm['Grid3D'].from_numpy(pixel_array)

grid3d.show()
