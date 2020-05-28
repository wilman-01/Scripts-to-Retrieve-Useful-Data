#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
foward02132014i0_1vtk = LegacyVTKReader(FileNames=['C:\\Users\\wilma\\Desktop\\Compare_vtk_files\\Foward-02-13-2014i0_1.vtk'])

# create a new 'Legacy VTK Reader'
foward02132014i0_2vtk = LegacyVTKReader(FileNames=['C:\\Users\\wilma\\Desktop\\Compare_vtk_files\\Foward-02-13-2014i0_2.vtk'])

# create a new 'Legacy VTK Reader'
foward02132014i0_3vtk = LegacyVTKReader(FileNames=['C:\\Users\\wilma\\Desktop\\Compare_vtk_files\\Foward-02-13-2014i0_3.vtk'])

# create a new 'Legacy VTK Reader'
foward02132014i0_4vtk = LegacyVTKReader(FileNames=['C:\\Users\\wilma\\Desktop\\Compare_vtk_files\\Foward-02-13-2014i0_4.vtk'])

# create a new 'Legacy VTK Reader'
foward02132014i0_5vtk = LegacyVTKReader(FileNames=['C:\\Users\\wilma\\Desktop\\Compare_vtk_files\\Foward-02-13-2014i0_5.vtk'])

# create a new 'Legacy VTK Reader'
foward02132014i0_6vtk = LegacyVTKReader(FileNames=['C:\\Users\\wilma\\Desktop\\Compare_vtk_files\\Foward-02-13-2014i0_6.vtk'])

# create a new 'Legacy VTK Reader'
foward02132014i0_7vtk = LegacyVTKReader(FileNames=['C:\\Users\\wilma\\Desktop\\Compare_vtk_files\\Foward-02-13-2014i0_7.vtk'])

######################################Create gradients ################################################

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1495, 720]

# show data in view
foward02132014i0_1vtkDisplay = Show(foward02132014i0_1vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(Input=foward02132014i0_1vtk)
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'predictedDisp11']
# Hide data in view
Hide(foward02132014i0_1vtk, renderView1)
# create a new 'Calculator'
calculator1 = Calculator(Input=gradientOfUnstructuredDataSet1)
calculator1.ResultArrayName = 'Result1'
calculator1.Function = 'Gradients_Y'
# show data in view
foward02132014i0_1vtkDisplay = Show(calculator1, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet2 = GradientOfUnstructuredDataSet(Input=calculator1)
gradientOfUnstructuredDataSet2.ScalarArray = ['POINTS', 'predictedDisp12']
# Hide data in view
Hide(calculator1, renderView1)
# create a new 'Calculator'
calculator2 = Calculator(Input=gradientOfUnstructuredDataSet2)
calculator2.ResultArrayName = 'Result2'
calculator2.Function = 'Gradients_X'


# show data in view
foward02132014i0_2vtkDisplay = Show(foward02132014i0_2vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet3 = GradientOfUnstructuredDataSet(Input=foward02132014i0_2vtk)
gradientOfUnstructuredDataSet3.ScalarArray = ['POINTS', 'predictedDisp11']
# Hide data in view
Hide(foward02132014i0_2vtk, renderView1)
# create a new 'Calculator'
calculator3 = Calculator(Input=gradientOfUnstructuredDataSet3)
calculator3.ResultArrayName = 'Result3'
calculator3.Function = 'Gradients_Y'
# show data in view
foward02132014i0_1vtkDisplay = Show(calculator3, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet4 = GradientOfUnstructuredDataSet(Input=calculator3)
gradientOfUnstructuredDataSet4.ScalarArray = ['POINTS', 'predictedDisp12']
# Hide data in view
Hide(calculator3, renderView1)
# create a new 'Calculator'
calculator4 = Calculator(Input=gradientOfUnstructuredDataSet4)
calculator4.ResultArrayName = 'Result4'
calculator4.Function = 'Gradients_X'

# show data in view
foward02132014i0_3vtkDisplay = Show(foward02132014i0_3vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet5 = GradientOfUnstructuredDataSet(Input=foward02132014i0_3vtk)
gradientOfUnstructuredDataSet5.ScalarArray = ['POINTS', 'predictedDisp11']
# Hide data in view
Hide(foward02132014i0_3vtk, renderView1)
# create a new 'Calculator'
calculator5 = Calculator(Input=gradientOfUnstructuredDataSet5)
calculator5.ResultArrayName = 'Result5'
calculator5.Function = 'Gradients_Y'
# show data in view
foward02132014i0_1vtkDisplay = Show(calculator5, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet6 = GradientOfUnstructuredDataSet(Input=calculator5)
gradientOfUnstructuredDataSet6.ScalarArray = ['POINTS', 'predictedDisp12']
# Hide data in view
Hide(calculator5, renderView1)
# create a new 'Calculator'
calculator6 = Calculator(Input=gradientOfUnstructuredDataSet6)
calculator6.ResultArrayName = 'Result6'
calculator6.Function = 'Gradients_X'

# show data in view
foward02132014i0_4vtkDisplay = Show(foward02132014i0_4vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet7 = GradientOfUnstructuredDataSet(Input=foward02132014i0_4vtk)
gradientOfUnstructuredDataSet7.ScalarArray = ['POINTS', 'predictedDisp11']
# Hide data in view
Hide(foward02132014i0_4vtk, renderView1)
# create a new 'Calculator'
calculator7 = Calculator(Input=gradientOfUnstructuredDataSet7)
calculator7.ResultArrayName = 'Result7'
calculator7.Function = 'Gradients_Y'
# show data in view
foward02132014i0_1vtkDisplay = Show(calculator7, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet8 = GradientOfUnstructuredDataSet(Input=calculator7)
gradientOfUnstructuredDataSet8.ScalarArray = ['POINTS', 'predictedDisp12']
# Hide data in view
Hide(calculator7, renderView1)
# create a new 'Calculator'
calculator8 = Calculator(Input=gradientOfUnstructuredDataSet8)
calculator8.ResultArrayName = 'Result8'
calculator8.Function = 'Gradients_X'

# show data in view
foward02132014i0_5vtkDisplay = Show(foward02132014i0_5vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet9 = GradientOfUnstructuredDataSet(Input=foward02132014i0_5vtk)
gradientOfUnstructuredDataSet9.ScalarArray = ['POINTS', 'predictedDisp11']
# Hide data in view
Hide(foward02132014i0_5vtk, renderView1)
# create a new 'Calculator'
calculator9 = Calculator(Input=gradientOfUnstructuredDataSet9)
calculator9.ResultArrayName = 'Result9'
calculator9.Function = 'Gradients_Y'
# show data in view
foward02132014i0_1vtkDisplay = Show(calculator9, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet10 = GradientOfUnstructuredDataSet(Input=calculator9)
gradientOfUnstructuredDataSet10.ScalarArray = ['POINTS', 'predictedDisp12']
# Hide data in view
Hide(calculator9, renderView1)
# create a new 'Calculator'
calculator10 = Calculator(Input=gradientOfUnstructuredDataSet10)
calculator10.ResultArrayName = 'Result10'
calculator10.Function = 'Gradients_X'

# show data in view
foward02132014i0_6vtkDisplay = Show(foward02132014i0_6vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet11 = GradientOfUnstructuredDataSet(Input=foward02132014i0_6vtk)
gradientOfUnstructuredDataSet11.ScalarArray = ['POINTS', 'predictedDisp11']
# Hide data in view
Hide(foward02132014i0_6vtk, renderView1)
# create a new 'Calculator'
calculator11 = Calculator(Input=gradientOfUnstructuredDataSet11)
calculator11.ResultArrayName = 'Result11'
calculator11.Function = 'Gradients_Y'
# show data in view
foward02132014i0_1vtkDisplay = Show(calculator11, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet12 = GradientOfUnstructuredDataSet(Input=calculator11)
gradientOfUnstructuredDataSet12.ScalarArray = ['POINTS', 'predictedDisp12']
# Hide data in view
Hide(calculator11, renderView1)
# create a new 'Calculator'
calculator12 = Calculator(Input=gradientOfUnstructuredDataSet12)
calculator12.ResultArrayName = 'Result12'
calculator12.Function = 'Gradients_X'

# show data in view
foward02132014i0_7vtkDisplay = Show(foward02132014i0_7vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet13 = GradientOfUnstructuredDataSet(Input=foward02132014i0_7vtk)
gradientOfUnstructuredDataSet13.ScalarArray = ['POINTS', 'predictedDisp11']
# Hide data in view
Hide(foward02132014i0_7vtk, renderView1)
# create a new 'Calculator'
calculator13 = Calculator(Input=gradientOfUnstructuredDataSet13)
calculator13.ResultArrayName = 'Result13'
calculator13.Function = 'Gradients_Y'
# show data in view
foward02132014i0_1vtkDisplay = Show(calculator13, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet14 = GradientOfUnstructuredDataSet(Input=calculator13)
gradientOfUnstructuredDataSet14.ScalarArray = ['POINTS', 'predictedDisp12']
# Hide data in view
Hide(calculator13, renderView1)
# create a new 'Calculator'
calculator14 = Calculator(Input=gradientOfUnstructuredDataSet14)
calculator14.ResultArrayName = 'Result14'
calculator14.Function = 'Gradients_X'

####################### Shear Strain #######################################
# create a new 'Calculator'
calculator15 = Calculator(Input=calculator2)
calculator15.ResultArrayName = 'Shear Strain BC1'
calculator15.Function = '1/2*(Result1+Result2)'
# create a new 'Calculator'
calculator16 = Calculator(Input=calculator4)
calculator16.ResultArrayName = 'Shear Strain BC2'
calculator16.Function = '1/2*(Result3+Result4)'
# create a new 'Calculator'
calculator17 = Calculator(Input=calculator6)
calculator17.ResultArrayName = 'Shear Strain BC3'
calculator17.Function = '1/2*(Result5+Result6)'
# create a new 'Calculator'
calculator18 = Calculator(Input=calculator8)
calculator18.ResultArrayName = 'Shear Strain BC4'
calculator18.Function = '1/2*(Result7+Result8)'
# create a new 'Calculator'
calculator19 = Calculator(Input=calculator10)
calculator19.ResultArrayName = 'Shear Strain BC5'
calculator19.Function = '1/2*(Result9+Result10)'
# create a new 'Calculator'
calculator20 = Calculator(Input=calculator12)
calculator20.ResultArrayName = 'Shear Strain BC6'
calculator20.Function = '1/2*(Result11+Result12)'
# create a new 'Calculator'
calculator21 = Calculator(Input=calculator14)
calculator21.ResultArrayName = 'Shear Strain BC7'
calculator21.Function = '1/2*(Result13+Result14)'




