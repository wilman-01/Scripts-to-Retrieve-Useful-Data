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

# create a new 'Legacy VTK Reader'
sMm1InvNoise3Alfa1e1203132014i12000vtk = LegacyVTKReader(FileNames=['C:\\Users\\wilma\\Desktop\\Compare_vtk_files\\SM-m1InvNoise3Alfa1e12-03-13-2014i12000.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1495, 720]

# get color transfer function/color map for 'predictedDisp11'
predictedDisp11LUT = GetColorTransferFunction('predictedDisp11')

# show data in view
foward02132014i0_1vtkDisplay = Show(foward02132014i0_1vtk, renderView1)
# trace defaults for the display properties.
foward02132014i0_1vtkDisplay.Representation = 'Surface'
foward02132014i0_1vtkDisplay.ColorArrayName = ['POINTS', 'predictedDisp11']
foward02132014i0_1vtkDisplay.LookupTable = predictedDisp11LUT
foward02132014i0_1vtkDisplay.OSPRayScaleArray = 'predictedDisp11'
foward02132014i0_1vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
foward02132014i0_1vtkDisplay.SelectOrientationVectors = 'NLP'
foward02132014i0_1vtkDisplay.ScaleFactor = 14.0
foward02132014i0_1vtkDisplay.SelectScaleArray = 'predictedDisp11'
foward02132014i0_1vtkDisplay.GlyphType = 'Arrow'
foward02132014i0_1vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
foward02132014i0_1vtkDisplay.ScalarOpacityUnitDistance = 12.347338516726966
foward02132014i0_1vtkDisplay.GaussianRadius = 7.0
foward02132014i0_1vtkDisplay.SetScaleArray = ['POINTS', 'predictedDisp11']
foward02132014i0_1vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
foward02132014i0_1vtkDisplay.OpacityArray = ['POINTS', 'predictedDisp11']
foward02132014i0_1vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [44.0, 70.0, 10000.0]
renderView1.CameraFocalPoint = [44.0, 70.0, 0.0]

# show color bar/color legend
foward02132014i0_1vtkDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
foward02132014i0_2vtkDisplay = Show(foward02132014i0_2vtk, renderView1)
# trace defaults for the display properties.
foward02132014i0_2vtkDisplay.Representation = 'Surface'
foward02132014i0_2vtkDisplay.ColorArrayName = ['POINTS', 'predictedDisp11']
foward02132014i0_2vtkDisplay.LookupTable = predictedDisp11LUT
foward02132014i0_2vtkDisplay.OSPRayScaleArray = 'predictedDisp11'
foward02132014i0_2vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
foward02132014i0_2vtkDisplay.SelectOrientationVectors = 'NLP'
foward02132014i0_2vtkDisplay.ScaleFactor = 14.0
foward02132014i0_2vtkDisplay.SelectScaleArray = 'predictedDisp11'
foward02132014i0_2vtkDisplay.GlyphType = 'Arrow'
foward02132014i0_2vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
foward02132014i0_2vtkDisplay.ScalarOpacityUnitDistance = 12.347338516726966
foward02132014i0_2vtkDisplay.GaussianRadius = 7.0
foward02132014i0_2vtkDisplay.SetScaleArray = ['POINTS', 'predictedDisp11']
foward02132014i0_2vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
foward02132014i0_2vtkDisplay.OpacityArray = ['POINTS', 'predictedDisp11']
foward02132014i0_2vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
foward02132014i0_2vtkDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
foward02132014i0_3vtkDisplay = Show(foward02132014i0_3vtk, renderView1)
# trace defaults for the display properties.
foward02132014i0_3vtkDisplay.Representation = 'Surface'
foward02132014i0_3vtkDisplay.ColorArrayName = ['POINTS', 'predictedDisp11']
foward02132014i0_3vtkDisplay.LookupTable = predictedDisp11LUT
foward02132014i0_3vtkDisplay.OSPRayScaleArray = 'predictedDisp11'
foward02132014i0_3vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
foward02132014i0_3vtkDisplay.SelectOrientationVectors = 'NLP'
foward02132014i0_3vtkDisplay.ScaleFactor = 14.0
foward02132014i0_3vtkDisplay.SelectScaleArray = 'predictedDisp11'
foward02132014i0_3vtkDisplay.GlyphType = 'Arrow'
foward02132014i0_3vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
foward02132014i0_3vtkDisplay.ScalarOpacityUnitDistance = 12.347338516726966
foward02132014i0_3vtkDisplay.GaussianRadius = 7.0
foward02132014i0_3vtkDisplay.SetScaleArray = ['POINTS', 'predictedDisp11']
foward02132014i0_3vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
foward02132014i0_3vtkDisplay.OpacityArray = ['POINTS', 'predictedDisp11']
foward02132014i0_3vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
foward02132014i0_3vtkDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
foward02132014i0_4vtkDisplay = Show(foward02132014i0_4vtk, renderView1)
# trace defaults for the display properties.
foward02132014i0_4vtkDisplay.Representation = 'Surface'
foward02132014i0_4vtkDisplay.ColorArrayName = ['POINTS', 'predictedDisp11']
foward02132014i0_4vtkDisplay.LookupTable = predictedDisp11LUT
foward02132014i0_4vtkDisplay.OSPRayScaleArray = 'predictedDisp11'
foward02132014i0_4vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
foward02132014i0_4vtkDisplay.SelectOrientationVectors = 'NLP'
foward02132014i0_4vtkDisplay.ScaleFactor = 14.0
foward02132014i0_4vtkDisplay.SelectScaleArray = 'predictedDisp11'
foward02132014i0_4vtkDisplay.GlyphType = 'Arrow'
foward02132014i0_4vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
foward02132014i0_4vtkDisplay.ScalarOpacityUnitDistance = 12.347338516726966
foward02132014i0_4vtkDisplay.GaussianRadius = 7.0
foward02132014i0_4vtkDisplay.SetScaleArray = ['POINTS', 'predictedDisp11']
foward02132014i0_4vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
foward02132014i0_4vtkDisplay.OpacityArray = ['POINTS', 'predictedDisp11']
foward02132014i0_4vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
foward02132014i0_4vtkDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
foward02132014i0_5vtkDisplay = Show(foward02132014i0_5vtk, renderView1)
# trace defaults for the display properties.
foward02132014i0_5vtkDisplay.Representation = 'Surface'
foward02132014i0_5vtkDisplay.ColorArrayName = ['POINTS', 'predictedDisp11']
foward02132014i0_5vtkDisplay.LookupTable = predictedDisp11LUT
foward02132014i0_5vtkDisplay.OSPRayScaleArray = 'predictedDisp11'
foward02132014i0_5vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
foward02132014i0_5vtkDisplay.SelectOrientationVectors = 'NLP'
foward02132014i0_5vtkDisplay.ScaleFactor = 14.0
foward02132014i0_5vtkDisplay.SelectScaleArray = 'predictedDisp11'
foward02132014i0_5vtkDisplay.GlyphType = 'Arrow'
foward02132014i0_5vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
foward02132014i0_5vtkDisplay.ScalarOpacityUnitDistance = 12.347338516726966
foward02132014i0_5vtkDisplay.GaussianRadius = 7.0
foward02132014i0_5vtkDisplay.SetScaleArray = ['POINTS', 'predictedDisp11']
foward02132014i0_5vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
foward02132014i0_5vtkDisplay.OpacityArray = ['POINTS', 'predictedDisp11']
foward02132014i0_5vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
foward02132014i0_5vtkDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
foward02132014i0_6vtkDisplay = Show(foward02132014i0_6vtk, renderView1)
# trace defaults for the display properties.
foward02132014i0_6vtkDisplay.Representation = 'Surface'
foward02132014i0_6vtkDisplay.ColorArrayName = ['POINTS', 'predictedDisp11']
foward02132014i0_6vtkDisplay.LookupTable = predictedDisp11LUT
foward02132014i0_6vtkDisplay.OSPRayScaleArray = 'predictedDisp11'
foward02132014i0_6vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
foward02132014i0_6vtkDisplay.SelectOrientationVectors = 'NLP'
foward02132014i0_6vtkDisplay.ScaleFactor = 14.0
foward02132014i0_6vtkDisplay.SelectScaleArray = 'predictedDisp11'
foward02132014i0_6vtkDisplay.GlyphType = 'Arrow'
foward02132014i0_6vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
foward02132014i0_6vtkDisplay.ScalarOpacityUnitDistance = 12.347338516726966
foward02132014i0_6vtkDisplay.GaussianRadius = 7.0
foward02132014i0_6vtkDisplay.SetScaleArray = ['POINTS', 'predictedDisp11']
foward02132014i0_6vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
foward02132014i0_6vtkDisplay.OpacityArray = ['POINTS', 'predictedDisp11']
foward02132014i0_6vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
foward02132014i0_6vtkDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
foward02132014i0_7vtkDisplay = Show(foward02132014i0_7vtk, renderView1)
# trace defaults for the display properties.
foward02132014i0_7vtkDisplay.Representation = 'Surface'
foward02132014i0_7vtkDisplay.ColorArrayName = ['POINTS', 'predictedDisp11']
foward02132014i0_7vtkDisplay.LookupTable = predictedDisp11LUT
foward02132014i0_7vtkDisplay.OSPRayScaleArray = 'predictedDisp11'
foward02132014i0_7vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
foward02132014i0_7vtkDisplay.SelectOrientationVectors = 'NLP'
foward02132014i0_7vtkDisplay.ScaleFactor = 14.0
foward02132014i0_7vtkDisplay.SelectScaleArray = 'predictedDisp11'
foward02132014i0_7vtkDisplay.GlyphType = 'Arrow'
foward02132014i0_7vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
foward02132014i0_7vtkDisplay.ScalarOpacityUnitDistance = 12.347338516726966
foward02132014i0_7vtkDisplay.GaussianRadius = 7.0
foward02132014i0_7vtkDisplay.SetScaleArray = ['POINTS', 'predictedDisp11']
foward02132014i0_7vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
foward02132014i0_7vtkDisplay.OpacityArray = ['POINTS', 'predictedDisp11']
foward02132014i0_7vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
foward02132014i0_7vtkDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'measuredDisp11'
measuredDisp11LUT = GetColorTransferFunction('measuredDisp11')

# show data in view
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay = Show(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)
# trace defaults for the display properties.
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.Representation = 'Surface'
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.ColorArrayName = ['POINTS', 'measuredDisp11']
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.LookupTable = measuredDisp11LUT
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.OSPRayScaleArray = 'measuredDisp11'
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.SelectOrientationVectors = 'NLP'
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.ScaleFactor = 8.0
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.SelectScaleArray = 'measuredDisp11'
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.GlyphType = 'Arrow'
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.ScalarOpacityUnitDistance = 9.531072586789413
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.GaussianRadius = 4.0
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.SetScaleArray = ['POINTS', 'measuredDisp11']
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.OpacityArray = ['POINTS', 'measuredDisp11']
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
sMm1InvNoise3Alfa1e1203132014i12000vtkDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(foward02132014i0_1vtk)

# hide data in view
Hide(foward02132014i0_7vtk, renderView1)

# hide data in view
Hide(foward02132014i0_6vtk, renderView1)

# hide data in view
Hide(foward02132014i0_5vtk, renderView1)

# hide data in view
Hide(foward02132014i0_4vtk, renderView1)

# hide data in view
Hide(foward02132014i0_3vtk, renderView1)

# hide data in view
Hide(foward02132014i0_2vtk, renderView1)

# hide data in view
Hide(foward02132014i0_1vtk, renderView1)

# set active source
SetActiveSource(foward02132014i0_2vtk)

# set active source
SetActiveSource(foward02132014i0_3vtk)

# set active source
SetActiveSource(foward02132014i0_4vtk)

# set active source
SetActiveSource(foward02132014i0_5vtk)

# set active source
SetActiveSource(foward02132014i0_6vtk)

# set active source
SetActiveSource(foward02132014i0_7vtk)

# set active source
SetActiveSource(sMm1InvNoise3Alfa1e1203132014i12000vtk)

# set active source
SetActiveSource(foward02132014i0_1vtk)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(Input=foward02132014i0_1vtk)
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'predictedDisp11']

# show data in view
gradientOfUnstructuredDataSet1Display = Show(gradientOfUnstructuredDataSet1, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet1Display.Representation = 'Surface'
gradientOfUnstructuredDataSet1Display.ColorArrayName = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet1Display.LookupTable = predictedDisp11LUT
gradientOfUnstructuredDataSet1Display.OSPRayScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet1Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet1Display.SelectOrientationVectors = 'Gradients'
gradientOfUnstructuredDataSet1Display.ScaleFactor = 14.0
gradientOfUnstructuredDataSet1Display.SelectScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet1Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet1Display.PolarAxes = 'PolarAxesRepresentation'
gradientOfUnstructuredDataSet1Display.ScalarOpacityUnitDistance = 12.347338516726966
gradientOfUnstructuredDataSet1Display.GaussianRadius = 7.0
gradientOfUnstructuredDataSet1Display.SetScaleArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet1Display.ScaleTransferFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet1Display.OpacityArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(foward02132014i0_1vtk, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(foward02132014i0_2vtk)

# hide data in view
Hide(gradientOfUnstructuredDataSet1, renderView1)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet2 = GradientOfUnstructuredDataSet(Input=foward02132014i0_2vtk)
gradientOfUnstructuredDataSet2.ScalarArray = ['POINTS', 'predictedDisp11']

# show data in view
gradientOfUnstructuredDataSet2Display = Show(gradientOfUnstructuredDataSet2, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet2Display.Representation = 'Surface'
gradientOfUnstructuredDataSet2Display.ColorArrayName = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet2Display.LookupTable = predictedDisp11LUT
gradientOfUnstructuredDataSet2Display.OSPRayScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet2Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet2Display.SelectOrientationVectors = 'Gradients'
gradientOfUnstructuredDataSet2Display.ScaleFactor = 14.0
gradientOfUnstructuredDataSet2Display.SelectScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet2Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet2Display.PolarAxes = 'PolarAxesRepresentation'
gradientOfUnstructuredDataSet2Display.ScalarOpacityUnitDistance = 12.347338516726966
gradientOfUnstructuredDataSet2Display.GaussianRadius = 7.0
gradientOfUnstructuredDataSet2Display.SetScaleArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet2Display.ScaleTransferFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet2Display.OpacityArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet2Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(foward02132014i0_2vtk, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet2Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(gradientOfUnstructuredDataSet2, renderView1)

# set active source
SetActiveSource(foward02132014i0_3vtk)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet3 = GradientOfUnstructuredDataSet(Input=foward02132014i0_3vtk)
gradientOfUnstructuredDataSet3.ScalarArray = ['POINTS', 'predictedDisp11']

# show data in view
gradientOfUnstructuredDataSet3Display = Show(gradientOfUnstructuredDataSet3, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet3Display.Representation = 'Surface'
gradientOfUnstructuredDataSet3Display.ColorArrayName = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet3Display.LookupTable = predictedDisp11LUT
gradientOfUnstructuredDataSet3Display.OSPRayScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet3Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet3Display.SelectOrientationVectors = 'Gradients'
gradientOfUnstructuredDataSet3Display.ScaleFactor = 14.0
gradientOfUnstructuredDataSet3Display.SelectScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet3Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet3Display.PolarAxes = 'PolarAxesRepresentation'
gradientOfUnstructuredDataSet3Display.ScalarOpacityUnitDistance = 12.347338516726966
gradientOfUnstructuredDataSet3Display.GaussianRadius = 7.0
gradientOfUnstructuredDataSet3Display.SetScaleArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet3Display.ScaleTransferFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet3Display.OpacityArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet3Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(foward02132014i0_3vtk, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet3Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(gradientOfUnstructuredDataSet3, renderView1)

# set active source
SetActiveSource(foward02132014i0_4vtk)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet4 = GradientOfUnstructuredDataSet(Input=foward02132014i0_4vtk)
gradientOfUnstructuredDataSet4.ScalarArray = ['POINTS', 'predictedDisp11']

# show data in view
gradientOfUnstructuredDataSet4Display = Show(gradientOfUnstructuredDataSet4, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet4Display.Representation = 'Surface'
gradientOfUnstructuredDataSet4Display.ColorArrayName = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet4Display.LookupTable = predictedDisp11LUT
gradientOfUnstructuredDataSet4Display.OSPRayScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet4Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet4Display.SelectOrientationVectors = 'Gradients'
gradientOfUnstructuredDataSet4Display.ScaleFactor = 14.0
gradientOfUnstructuredDataSet4Display.SelectScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet4Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet4Display.PolarAxes = 'PolarAxesRepresentation'
gradientOfUnstructuredDataSet4Display.ScalarOpacityUnitDistance = 12.347338516726966
gradientOfUnstructuredDataSet4Display.GaussianRadius = 7.0
gradientOfUnstructuredDataSet4Display.SetScaleArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet4Display.ScaleTransferFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet4Display.OpacityArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet4Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(foward02132014i0_4vtk, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet4Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(gradientOfUnstructuredDataSet4, renderView1)

# set active source
SetActiveSource(foward02132014i0_5vtk)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet5 = GradientOfUnstructuredDataSet(Input=foward02132014i0_5vtk)
gradientOfUnstructuredDataSet5.ScalarArray = ['POINTS', 'predictedDisp11']

# show data in view
gradientOfUnstructuredDataSet5Display = Show(gradientOfUnstructuredDataSet5, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet5Display.Representation = 'Surface'
gradientOfUnstructuredDataSet5Display.ColorArrayName = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet5Display.LookupTable = predictedDisp11LUT
gradientOfUnstructuredDataSet5Display.OSPRayScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet5Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet5Display.SelectOrientationVectors = 'Gradients'
gradientOfUnstructuredDataSet5Display.ScaleFactor = 14.0
gradientOfUnstructuredDataSet5Display.SelectScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet5Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet5Display.PolarAxes = 'PolarAxesRepresentation'
gradientOfUnstructuredDataSet5Display.ScalarOpacityUnitDistance = 12.347338516726966
gradientOfUnstructuredDataSet5Display.GaussianRadius = 7.0
gradientOfUnstructuredDataSet5Display.SetScaleArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet5Display.ScaleTransferFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet5Display.OpacityArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet5Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(foward02132014i0_5vtk, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet5Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(gradientOfUnstructuredDataSet5, renderView1)

# set active source
SetActiveSource(foward02132014i0_6vtk)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet6 = GradientOfUnstructuredDataSet(Input=foward02132014i0_6vtk)
gradientOfUnstructuredDataSet6.ScalarArray = ['POINTS', 'predictedDisp11']

# show data in view
gradientOfUnstructuredDataSet6Display = Show(gradientOfUnstructuredDataSet6, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet6Display.Representation = 'Surface'
gradientOfUnstructuredDataSet6Display.ColorArrayName = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet6Display.LookupTable = predictedDisp11LUT
gradientOfUnstructuredDataSet6Display.OSPRayScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet6Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet6Display.SelectOrientationVectors = 'Gradients'
gradientOfUnstructuredDataSet6Display.ScaleFactor = 14.0
gradientOfUnstructuredDataSet6Display.SelectScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet6Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet6Display.PolarAxes = 'PolarAxesRepresentation'
gradientOfUnstructuredDataSet6Display.ScalarOpacityUnitDistance = 12.347338516726966
gradientOfUnstructuredDataSet6Display.GaussianRadius = 7.0
gradientOfUnstructuredDataSet6Display.SetScaleArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet6Display.ScaleTransferFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet6Display.OpacityArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet6Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(foward02132014i0_6vtk, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet6Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(foward02132014i0_7vtk)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet7 = GradientOfUnstructuredDataSet(Input=foward02132014i0_7vtk)
gradientOfUnstructuredDataSet7.ScalarArray = ['POINTS', 'predictedDisp11']

# show data in view
gradientOfUnstructuredDataSet7Display = Show(gradientOfUnstructuredDataSet7, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet7Display.Representation = 'Surface'
gradientOfUnstructuredDataSet7Display.ColorArrayName = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet7Display.LookupTable = predictedDisp11LUT
gradientOfUnstructuredDataSet7Display.OSPRayScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet7Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet7Display.SelectOrientationVectors = 'Gradients'
gradientOfUnstructuredDataSet7Display.ScaleFactor = 14.0
gradientOfUnstructuredDataSet7Display.SelectScaleArray = 'predictedDisp11'
gradientOfUnstructuredDataSet7Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet7Display.PolarAxes = 'PolarAxesRepresentation'
gradientOfUnstructuredDataSet7Display.ScalarOpacityUnitDistance = 12.347338516726966
gradientOfUnstructuredDataSet7Display.GaussianRadius = 7.0
gradientOfUnstructuredDataSet7Display.SetScaleArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet7Display.ScaleTransferFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet7Display.OpacityArray = ['POINTS', 'predictedDisp11']
gradientOfUnstructuredDataSet7Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(foward02132014i0_7vtk, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet7Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(sMm1InvNoise3Alfa1e1203132014i12000vtk)

# hide data in view
Hide(gradientOfUnstructuredDataSet6, renderView1)

# hide data in view
Hide(gradientOfUnstructuredDataSet7, renderView1)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet8 = GradientOfUnstructuredDataSet(Input=sMm1InvNoise3Alfa1e1203132014i12000vtk)
gradientOfUnstructuredDataSet8.ScalarArray = ['POINTS', 'measuredDisp11']

# show data in view
gradientOfUnstructuredDataSet8Display = Show(gradientOfUnstructuredDataSet8, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet8Display.Representation = 'Surface'
gradientOfUnstructuredDataSet8Display.ColorArrayName = ['POINTS', 'measuredDisp11']
gradientOfUnstructuredDataSet8Display.LookupTable = measuredDisp11LUT
gradientOfUnstructuredDataSet8Display.OSPRayScaleArray = 'measuredDisp11'
gradientOfUnstructuredDataSet8Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet8Display.SelectOrientationVectors = 'Gradients'
gradientOfUnstructuredDataSet8Display.ScaleFactor = 8.0
gradientOfUnstructuredDataSet8Display.SelectScaleArray = 'measuredDisp11'
gradientOfUnstructuredDataSet8Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet8Display.PolarAxes = 'PolarAxesRepresentation'
gradientOfUnstructuredDataSet8Display.ScalarOpacityUnitDistance = 9.531072586789413
gradientOfUnstructuredDataSet8Display.GaussianRadius = 4.0
gradientOfUnstructuredDataSet8Display.SetScaleArray = ['POINTS', 'measuredDisp11']
gradientOfUnstructuredDataSet8Display.ScaleTransferFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet8Display.OpacityArray = ['POINTS', 'measuredDisp11']
gradientOfUnstructuredDataSet8Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet8Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(gradientOfUnstructuredDataSet1)

CreateLayout('Layout #2')

# set active view
SetActiveView(None)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=gradientOfUnstructuredDataSet1,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point2 = [88.0, 140.0, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [1495, 720]
lineChartView1.LeftAxisRangeMaximum = 6.66
lineChartView1.BottomAxisRangeMaximum = 6.66

# get layout
layout2 = GetLayout()

# place view in the layout
layout2.AssignView(0, lineChartView1)

# show data in view
plotOverLine1Display = Show(plotOverLine1, lineChartView1)
# trace defaults for the display properties.
plotOverLine1Display.CompositeDataSetIndex = [0]
plotOverLine1Display.UseIndexForXAxis = 0
plotOverLine1Display.XArrayName = 'arc_length'
plotOverLine1Display.SeriesVisibility = ['Gradients_Magnitude', 'NLP', 'predictedDisp11', 'predictedDisp12', 'property3', 'property4', 'property5', 'property6', 'SM']
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.89', '0.1', '0.11', 'Gradients_Y', '0.22', '0.49', '0.72', 'Gradients_Z', '0.3', '0.69', '0.29', 'Gradients_Magnitude', '0.6', '0.31', '0.64', 'NLP', '1', '0.5', '0', 'predictedDisp11', '0.65', '0.34', '0.16', 'predictedDisp12', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'SM', '1', '0.5', '0', 'vtkValidPointMask', '0.65', '0.34', '0.16', 'Points_X', '0', '0', '0', 'Points_Y', '0.89', '0.1', '0.11', 'Points_Z', '0.22', '0.49', '0.72', 'Points_Magnitude', '0.3', '0.69', '0.29']
plotOverLine1Display.SeriesPlotCorner = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display.SeriesLabelPrefix = ''
plotOverLine1Display.SeriesLineStyle = ['arc_length', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display.SeriesLineThickness = ['arc_length', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display.SeriesMarkerStyle = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point2 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point2 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = []
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.889998', '0.100008', '0.110002', 'Gradients_Y', '0.220005', '0.489998', '0.719997', 'Gradients_Z', '0.300008', '0.689998', '0.289998', 'Gradients_Magnitude', '0.6', '0.310002', '0.639994', 'NLP', '1', '0.500008', '0', 'predictedDisp11', '0.650004', '0.340002', '0.160006', 'predictedDisp12', '0', '0', '0', 'property3', '0.889998', '0.100008', '0.110002', 'property4', '0.220005', '0.489998', '0.719997', 'property5', '0.300008', '0.689998', '0.289998', 'property6', '0.6', '0.310002', '0.639994', 'SM', '1', '0.500008', '0', 'vtkValidPointMask', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998']
plotOverLine1Display.SeriesPlotCorner = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesLineStyle = ['Gradients_Magnitude', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'NLP', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'SM', '1', 'arc_length', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'vtkValidPointMask', '1']
plotOverLine1Display.SeriesLineThickness = ['Gradients_Magnitude', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'NLP', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'SM', '2', 'arc_length', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'vtkValidPointMask', '2']
plotOverLine1Display.SeriesMarkerStyle = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = ['predictedDisp11']

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11(1)', 'predictedDisp12', 'predictedDisp12', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']

# set active source
SetActiveSource(gradientOfUnstructuredDataSet2)

# create a new 'Plot Over Line'
plotOverLine2 = PlotOverLine(Input=gradientOfUnstructuredDataSet2,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine2.Source.Point2 = [88.0, 140.0, 0.0]

# show data in view
plotOverLine2Display = Show(plotOverLine2, lineChartView1)
# trace defaults for the display properties.
plotOverLine2Display.CompositeDataSetIndex = [0]
plotOverLine2Display.UseIndexForXAxis = 0
plotOverLine2Display.XArrayName = 'arc_length'
plotOverLine2Display.SeriesVisibility = ['Gradients_Magnitude', 'NLP', 'predictedDisp11', 'predictedDisp12', 'property3', 'property4', 'property5', 'property6', 'SM']
plotOverLine2Display.SeriesLabel = ['arc_length', 'arc_length', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.89', '0.1', '0.11', 'Gradients_Y', '0.22', '0.49', '0.72', 'Gradients_Z', '0.3', '0.69', '0.29', 'Gradients_Magnitude', '0.6', '0.31', '0.64', 'NLP', '1', '0.5', '0', 'predictedDisp11', '0.65', '0.34', '0.16', 'predictedDisp12', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'SM', '1', '0.5', '0', 'vtkValidPointMask', '0.65', '0.34', '0.16', 'Points_X', '0', '0', '0', 'Points_Y', '0.89', '0.1', '0.11', 'Points_Z', '0.22', '0.49', '0.72', 'Points_Magnitude', '0.3', '0.69', '0.29']
plotOverLine2Display.SeriesPlotCorner = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine2Display.SeriesLabelPrefix = ''
plotOverLine2Display.SeriesLineStyle = ['arc_length', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine2Display.SeriesLineThickness = ['arc_length', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine2Display.SeriesMarkerStyle = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# Properties modified on plotOverLine2.Source
plotOverLine2.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine2.Source
plotOverLine2.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine2.Source
plotOverLine2.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine2.Source
plotOverLine2.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine2.Source
plotOverLine2.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine2.Source
plotOverLine2.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine2.Source
plotOverLine2.Source.Point2 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine2.Source
plotOverLine2.Source.Point2 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine2Display
plotOverLine2Display.SeriesVisibility = []
plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.889998', '0.100008', '0.110002', 'Gradients_Y', '0.220005', '0.489998', '0.719997', 'Gradients_Z', '0.300008', '0.689998', '0.289998', 'Gradients_Magnitude', '0.6', '0.310002', '0.639994', 'NLP', '1', '0.500008', '0', 'predictedDisp11', '0.650004', '0.340002', '0.160006', 'predictedDisp12', '0', '0', '0', 'property3', '0.889998', '0.100008', '0.110002', 'property4', '0.220005', '0.489998', '0.719997', 'property5', '0.300008', '0.689998', '0.289998', 'property6', '0.6', '0.310002', '0.639994', 'SM', '1', '0.500008', '0', 'vtkValidPointMask', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998']
plotOverLine2Display.SeriesPlotCorner = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']
plotOverLine2Display.SeriesLineStyle = ['Gradients_Magnitude', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'NLP', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'SM', '1', 'arc_length', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'vtkValidPointMask', '1']
plotOverLine2Display.SeriesLineThickness = ['Gradients_Magnitude', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'NLP', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'SM', '2', 'arc_length', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'vtkValidPointMask', '2']
plotOverLine2Display.SeriesMarkerStyle = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']

# Properties modified on plotOverLine2Display
plotOverLine2Display.SeriesVisibility = ['predictedDisp11']

# hide data in view
Hide(plotOverLine1, lineChartView1)

# hide data in view
Hide(plotOverLine2, lineChartView1)

# set active source
SetActiveSource(gradientOfUnstructuredDataSet3)

# create a new 'Plot Over Line'
plotOverLine3 = PlotOverLine(Input=gradientOfUnstructuredDataSet3,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine3.Source.Point2 = [88.0, 140.0, 0.0]

# show data in view
plotOverLine3Display = Show(plotOverLine3, lineChartView1)
# trace defaults for the display properties.
plotOverLine3Display.CompositeDataSetIndex = [0]
plotOverLine3Display.UseIndexForXAxis = 0
plotOverLine3Display.XArrayName = 'arc_length'
plotOverLine3Display.SeriesVisibility = ['Gradients_Magnitude', 'NLP', 'predictedDisp11', 'predictedDisp12', 'property3', 'property4', 'property5', 'property6', 'SM']
plotOverLine3Display.SeriesLabel = ['arc_length', 'arc_length', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.89', '0.1', '0.11', 'Gradients_Y', '0.22', '0.49', '0.72', 'Gradients_Z', '0.3', '0.69', '0.29', 'Gradients_Magnitude', '0.6', '0.31', '0.64', 'NLP', '1', '0.5', '0', 'predictedDisp11', '0.65', '0.34', '0.16', 'predictedDisp12', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'SM', '1', '0.5', '0', 'vtkValidPointMask', '0.65', '0.34', '0.16', 'Points_X', '0', '0', '0', 'Points_Y', '0.89', '0.1', '0.11', 'Points_Z', '0.22', '0.49', '0.72', 'Points_Magnitude', '0.3', '0.69', '0.29']
plotOverLine3Display.SeriesPlotCorner = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine3Display.SeriesLabelPrefix = ''
plotOverLine3Display.SeriesLineStyle = ['arc_length', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine3Display.SeriesLineThickness = ['arc_length', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine3Display.SeriesMarkerStyle = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point1 = [84.0, 0.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point1 = [84.0, 0.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point1 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point1 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point2 = [4.0, 140.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point2 = [4.0, 140.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point2 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine3.Source
plotOverLine3.Source.Point2 = [84.0, 4.0, 0.0]

# set active source
SetActiveSource(gradientOfUnstructuredDataSet4)

# create a new 'Plot Over Line'
plotOverLine4 = PlotOverLine(Input=gradientOfUnstructuredDataSet4,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine4.Source.Point2 = [88.0, 140.0, 0.0]

# show data in view
plotOverLine4Display = Show(plotOverLine4, lineChartView1)
# trace defaults for the display properties.
plotOverLine4Display.CompositeDataSetIndex = [0]
plotOverLine4Display.UseIndexForXAxis = 0
plotOverLine4Display.XArrayName = 'arc_length'
plotOverLine4Display.SeriesVisibility = ['Gradients_Magnitude', 'NLP', 'predictedDisp11', 'predictedDisp12', 'property3', 'property4', 'property5', 'property6', 'SM']
plotOverLine4Display.SeriesLabel = ['arc_length', 'arc_length', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine4Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.89', '0.1', '0.11', 'Gradients_Y', '0.22', '0.49', '0.72', 'Gradients_Z', '0.3', '0.69', '0.29', 'Gradients_Magnitude', '0.6', '0.31', '0.64', 'NLP', '1', '0.5', '0', 'predictedDisp11', '0.65', '0.34', '0.16', 'predictedDisp12', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'SM', '1', '0.5', '0', 'vtkValidPointMask', '0.65', '0.34', '0.16', 'Points_X', '0', '0', '0', 'Points_Y', '0.89', '0.1', '0.11', 'Points_Z', '0.22', '0.49', '0.72', 'Points_Magnitude', '0.3', '0.69', '0.29']
plotOverLine4Display.SeriesPlotCorner = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine4Display.SeriesLabelPrefix = ''
plotOverLine4Display.SeriesLineStyle = ['arc_length', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine4Display.SeriesLineThickness = ['arc_length', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine4Display.SeriesMarkerStyle = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# Properties modified on plotOverLine4.Source
plotOverLine4.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine4.Source
plotOverLine4.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine4.Source
plotOverLine4.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine4.Source
plotOverLine4.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine4.Source
plotOverLine4.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine4.Source
plotOverLine4.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine4.Source
plotOverLine4.Source.Point2 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine4.Source
plotOverLine4.Source.Point2 = [84.0, 4.0, 0.0]

# set active source
SetActiveSource(foward02132014i0_5vtk)

# set active source
SetActiveSource(gradientOfUnstructuredDataSet5)

# create a new 'Plot Over Line'
plotOverLine5 = PlotOverLine(Input=gradientOfUnstructuredDataSet5,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine5.Source.Point2 = [88.0, 140.0, 0.0]

# show data in view
plotOverLine5Display = Show(plotOverLine5, lineChartView1)
# trace defaults for the display properties.
plotOverLine5Display.CompositeDataSetIndex = [0]
plotOverLine5Display.UseIndexForXAxis = 0
plotOverLine5Display.XArrayName = 'arc_length'
plotOverLine5Display.SeriesVisibility = ['Gradients_Magnitude', 'NLP', 'predictedDisp11', 'predictedDisp12', 'property3', 'property4', 'property5', 'property6', 'SM']
plotOverLine5Display.SeriesLabel = ['arc_length', 'arc_length', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine5Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.89', '0.1', '0.11', 'Gradients_Y', '0.22', '0.49', '0.72', 'Gradients_Z', '0.3', '0.69', '0.29', 'Gradients_Magnitude', '0.6', '0.31', '0.64', 'NLP', '1', '0.5', '0', 'predictedDisp11', '0.65', '0.34', '0.16', 'predictedDisp12', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'SM', '1', '0.5', '0', 'vtkValidPointMask', '0.65', '0.34', '0.16', 'Points_X', '0', '0', '0', 'Points_Y', '0.89', '0.1', '0.11', 'Points_Z', '0.22', '0.49', '0.72', 'Points_Magnitude', '0.3', '0.69', '0.29']
plotOverLine5Display.SeriesPlotCorner = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine5Display.SeriesLabelPrefix = ''
plotOverLine5Display.SeriesLineStyle = ['arc_length', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine5Display.SeriesLineThickness = ['arc_length', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine5Display.SeriesMarkerStyle = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# Properties modified on plotOverLine5.Source
plotOverLine5.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine5.Source
plotOverLine5.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine5.Source
plotOverLine5.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine5.Source
plotOverLine5.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine5.Source
plotOverLine5.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine5.Source
plotOverLine5.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine5.Source
plotOverLine5.Source.Point2 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine5.Source
plotOverLine5.Source.Point2 = [84.0, 4.0, 0.0]

# set active source
SetActiveSource(gradientOfUnstructuredDataSet6)

# create a new 'Plot Over Line'
plotOverLine6 = PlotOverLine(Input=gradientOfUnstructuredDataSet6,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine6.Source.Point2 = [88.0, 140.0, 0.0]

# show data in view
plotOverLine6Display = Show(plotOverLine6, lineChartView1)
# trace defaults for the display properties.
plotOverLine6Display.CompositeDataSetIndex = [0]
plotOverLine6Display.UseIndexForXAxis = 0
plotOverLine6Display.XArrayName = 'arc_length'
plotOverLine6Display.SeriesVisibility = ['Gradients_Magnitude', 'NLP', 'predictedDisp11', 'predictedDisp12', 'property3', 'property4', 'property5', 'property6', 'SM']
plotOverLine6Display.SeriesLabel = ['arc_length', 'arc_length', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine6Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.89', '0.1', '0.11', 'Gradients_Y', '0.22', '0.49', '0.72', 'Gradients_Z', '0.3', '0.69', '0.29', 'Gradients_Magnitude', '0.6', '0.31', '0.64', 'NLP', '1', '0.5', '0', 'predictedDisp11', '0.65', '0.34', '0.16', 'predictedDisp12', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'SM', '1', '0.5', '0', 'vtkValidPointMask', '0.65', '0.34', '0.16', 'Points_X', '0', '0', '0', 'Points_Y', '0.89', '0.1', '0.11', 'Points_Z', '0.22', '0.49', '0.72', 'Points_Magnitude', '0.3', '0.69', '0.29']
plotOverLine6Display.SeriesPlotCorner = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine6Display.SeriesLabelPrefix = ''
plotOverLine6Display.SeriesLineStyle = ['arc_length', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine6Display.SeriesLineThickness = ['arc_length', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine6Display.SeriesMarkerStyle = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# Properties modified on plotOverLine6.Source
plotOverLine6.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine6.Source
plotOverLine6.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine6.Source
plotOverLine6.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine6.Source
plotOverLine6.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine6.Source
plotOverLine6.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine6.Source
plotOverLine6.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine6.Source
plotOverLine6.Source.Point2 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine6.Source
plotOverLine6.Source.Point2 = [84.0, 4.0, 0.0]

# set active source
SetActiveSource(gradientOfUnstructuredDataSet7)

# create a new 'Plot Over Line'
plotOverLine7 = PlotOverLine(Input=gradientOfUnstructuredDataSet7,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine7.Source.Point2 = [88.0, 140.0, 0.0]

# show data in view
plotOverLine7Display = Show(plotOverLine7, lineChartView1)
# trace defaults for the display properties.
plotOverLine7Display.CompositeDataSetIndex = [0]
plotOverLine7Display.UseIndexForXAxis = 0
plotOverLine7Display.XArrayName = 'arc_length'
plotOverLine7Display.SeriesVisibility = ['Gradients_Magnitude', 'NLP', 'predictedDisp11', 'predictedDisp12', 'property3', 'property4', 'property5', 'property6', 'SM']
plotOverLine7Display.SeriesLabel = ['arc_length', 'arc_length', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine7Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.89', '0.1', '0.11', 'Gradients_Y', '0.22', '0.49', '0.72', 'Gradients_Z', '0.3', '0.69', '0.29', 'Gradients_Magnitude', '0.6', '0.31', '0.64', 'NLP', '1', '0.5', '0', 'predictedDisp11', '0.65', '0.34', '0.16', 'predictedDisp12', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'SM', '1', '0.5', '0', 'vtkValidPointMask', '0.65', '0.34', '0.16', 'Points_X', '0', '0', '0', 'Points_Y', '0.89', '0.1', '0.11', 'Points_Z', '0.22', '0.49', '0.72', 'Points_Magnitude', '0.3', '0.69', '0.29']
plotOverLine7Display.SeriesPlotCorner = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine7Display.SeriesLabelPrefix = ''
plotOverLine7Display.SeriesLineStyle = ['arc_length', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine7Display.SeriesLineThickness = ['arc_length', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine7Display.SeriesMarkerStyle = ['arc_length', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# Properties modified on plotOverLine7.Source
plotOverLine7.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine7.Source
plotOverLine7.Source.Point1 = [4.0, 0.0, 0.0]

# Properties modified on plotOverLine7.Source
plotOverLine7.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine7.Source
plotOverLine7.Source.Point1 = [4.0, 4.0, 0.0]

# Properties modified on plotOverLine7.Source
plotOverLine7.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine7.Source
plotOverLine7.Source.Point2 = [84.0, 140.0, 0.0]

# Properties modified on plotOverLine7.Source
plotOverLine7.Source.Point2 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine7.Source
plotOverLine7.Source.Point2 = [84.0, 4.0, 0.0]

# set active source
SetActiveSource(gradientOfUnstructuredDataSet8)

# create a new 'Plot Over Line'
plotOverLine8 = PlotOverLine(Input=gradientOfUnstructuredDataSet8,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine8.Source.Point1 = [4.0, 4.0, 0.0]
plotOverLine8.Source.Point2 = [84.0, 76.0, 0.0]

# show data in view
plotOverLine8Display = Show(plotOverLine8, lineChartView1)
# trace defaults for the display properties.
plotOverLine8Display.CompositeDataSetIndex = [0]
plotOverLine8Display.UseIndexForXAxis = 0
plotOverLine8Display.XArrayName = 'arc_length'
plotOverLine8Display.SeriesVisibility = ['dual11', 'dual12', 'dual21', 'dual22', 'dual31', 'dual32', 'dual41', 'dual42', 'dual51', 'dual52', 'dual61', 'dual62', 'dual71', 'dual72', 'elemDataMatch', 'elemRegul', 'gradient1', 'gradient2', 'gradient3', 'gradient4', 'gradient5', 'gradient6', 'Gradients_Magnitude', 'l2grad2', 'measuredDisp11', 'measuredDisp12', 'measuredDisp21', 'measuredDisp22', 'measuredDisp31', 'measuredDisp32', 'measuredDisp41', 'measuredDisp42', 'measuredDisp51', 'measuredDisp52', 'measuredDisp61', 'measuredDisp62', 'measuredDisp71', 'measuredDisp72', 'NLP', 'predictedDisp11', 'predictedDisp12', 'predictedDisp21', 'predictedDisp22', 'predictedDisp31', 'predictedDisp32', 'predictedDisp41', 'predictedDisp42', 'predictedDisp51', 'predictedDisp52', 'predictedDisp61', 'predictedDisp62', 'predictedDisp71', 'predictedDisp72', 'property3', 'property4', 'property5', 'property6', 'SM']
plotOverLine8Display.SeriesLabel = ['arc_length', 'arc_length', 'dual11', 'dual11', 'dual12', 'dual12', 'dual21', 'dual21', 'dual22', 'dual22', 'dual31', 'dual31', 'dual32', 'dual32', 'dual41', 'dual41', 'dual42', 'dual42', 'dual51', 'dual51', 'dual52', 'dual52', 'dual61', 'dual61', 'dual62', 'dual62', 'dual71', 'dual71', 'dual72', 'dual72', 'elemDataMatch', 'elemDataMatch', 'elemRegul', 'elemRegul', 'gradient1', 'gradient1', 'gradient2', 'gradient2', 'gradient3', 'gradient3', 'gradient4', 'gradient4', 'gradient5', 'gradient5', 'gradient6', 'gradient6', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'l2grad2', 'l2grad2', 'measuredDisp11', 'measuredDisp11', 'measuredDisp12', 'measuredDisp12', 'measuredDisp21', 'measuredDisp21', 'measuredDisp22', 'measuredDisp22', 'measuredDisp31', 'measuredDisp31', 'measuredDisp32', 'measuredDisp32', 'measuredDisp41', 'measuredDisp41', 'measuredDisp42', 'measuredDisp42', 'measuredDisp51', 'measuredDisp51', 'measuredDisp52', 'measuredDisp52', 'measuredDisp61', 'measuredDisp61', 'measuredDisp62', 'measuredDisp62', 'measuredDisp71', 'measuredDisp71', 'measuredDisp72', 'measuredDisp72', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'predictedDisp21', 'predictedDisp21', 'predictedDisp22', 'predictedDisp22', 'predictedDisp31', 'predictedDisp31', 'predictedDisp32', 'predictedDisp32', 'predictedDisp41', 'predictedDisp41', 'predictedDisp42', 'predictedDisp42', 'predictedDisp51', 'predictedDisp51', 'predictedDisp52', 'predictedDisp52', 'predictedDisp61', 'predictedDisp61', 'predictedDisp62', 'predictedDisp62', 'predictedDisp71', 'predictedDisp71', 'predictedDisp72', 'predictedDisp72', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine8Display.SeriesColor = ['arc_length', '0', '0', '0', 'dual11', '0.89', '0.1', '0.11', 'dual12', '0.22', '0.49', '0.72', 'dual21', '0.3', '0.69', '0.29', 'dual22', '0.6', '0.31', '0.64', 'dual31', '1', '0.5', '0', 'dual32', '0.65', '0.34', '0.16', 'dual41', '0', '0', '0', 'dual42', '0.89', '0.1', '0.11', 'dual51', '0.22', '0.49', '0.72', 'dual52', '0.3', '0.69', '0.29', 'dual61', '0.6', '0.31', '0.64', 'dual62', '1', '0.5', '0', 'dual71', '0.65', '0.34', '0.16', 'dual72', '0', '0', '0', 'elemDataMatch', '0.89', '0.1', '0.11', 'elemRegul', '0.22', '0.49', '0.72', 'gradient1', '0.3', '0.69', '0.29', 'gradient2', '0.6', '0.31', '0.64', 'gradient3', '1', '0.5', '0', 'gradient4', '0.65', '0.34', '0.16', 'gradient5', '0', '0', '0', 'gradient6', '0.89', '0.1', '0.11', 'Gradients_X', '0.22', '0.49', '0.72', 'Gradients_Y', '0.3', '0.69', '0.29', 'Gradients_Z', '0.6', '0.31', '0.64', 'Gradients_Magnitude', '1', '0.5', '0', 'l2grad2', '0.65', '0.34', '0.16', 'measuredDisp11', '0', '0', '0', 'measuredDisp12', '0.89', '0.1', '0.11', 'measuredDisp21', '0.22', '0.49', '0.72', 'measuredDisp22', '0.3', '0.69', '0.29', 'measuredDisp31', '0.6', '0.31', '0.64', 'measuredDisp32', '1', '0.5', '0', 'measuredDisp41', '0.65', '0.34', '0.16', 'measuredDisp42', '0', '0', '0', 'measuredDisp51', '0.89', '0.1', '0.11', 'measuredDisp52', '0.22', '0.49', '0.72', 'measuredDisp61', '0.3', '0.69', '0.29', 'measuredDisp62', '0.6', '0.31', '0.64', 'measuredDisp71', '1', '0.5', '0', 'measuredDisp72', '0.65', '0.34', '0.16', 'NLP', '0', '0', '0', 'predictedDisp11', '0.89', '0.1', '0.11', 'predictedDisp12', '0.22', '0.49', '0.72', 'predictedDisp21', '0.3', '0.69', '0.29', 'predictedDisp22', '0.6', '0.31', '0.64', 'predictedDisp31', '1', '0.5', '0', 'predictedDisp32', '0.65', '0.34', '0.16', 'predictedDisp41', '0', '0', '0', 'predictedDisp42', '0.89', '0.1', '0.11', 'predictedDisp51', '0.22', '0.49', '0.72', 'predictedDisp52', '0.3', '0.69', '0.29', 'predictedDisp61', '0.6', '0.31', '0.64', 'predictedDisp62', '1', '0.5', '0', 'predictedDisp71', '0.65', '0.34', '0.16', 'predictedDisp72', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'SM', '1', '0.5', '0', 'vtkValidPointMask', '0.65', '0.34', '0.16', 'Points_X', '0', '0', '0', 'Points_Y', '0.89', '0.1', '0.11', 'Points_Z', '0.22', '0.49', '0.72', 'Points_Magnitude', '0.3', '0.69', '0.29']
plotOverLine8Display.SeriesPlotCorner = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine8Display.SeriesLabelPrefix = ''
plotOverLine8Display.SeriesLineStyle = ['arc_length', '1', 'dual11', '1', 'dual12', '1', 'dual21', '1', 'dual22', '1', 'dual31', '1', 'dual32', '1', 'dual41', '1', 'dual42', '1', 'dual51', '1', 'dual52', '1', 'dual61', '1', 'dual62', '1', 'dual71', '1', 'dual72', '1', 'elemDataMatch', '1', 'elemRegul', '1', 'gradient1', '1', 'gradient2', '1', 'gradient3', '1', 'gradient4', '1', 'gradient5', '1', 'gradient6', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'l2grad2', '1', 'measuredDisp11', '1', 'measuredDisp12', '1', 'measuredDisp21', '1', 'measuredDisp22', '1', 'measuredDisp31', '1', 'measuredDisp32', '1', 'measuredDisp41', '1', 'measuredDisp42', '1', 'measuredDisp51', '1', 'measuredDisp52', '1', 'measuredDisp61', '1', 'measuredDisp62', '1', 'measuredDisp71', '1', 'measuredDisp72', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'predictedDisp21', '1', 'predictedDisp22', '1', 'predictedDisp31', '1', 'predictedDisp32', '1', 'predictedDisp41', '1', 'predictedDisp42', '1', 'predictedDisp51', '1', 'predictedDisp52', '1', 'predictedDisp61', '1', 'predictedDisp62', '1', 'predictedDisp71', '1', 'predictedDisp72', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine8Display.SeriesLineThickness = ['arc_length', '2', 'dual11', '2', 'dual12', '2', 'dual21', '2', 'dual22', '2', 'dual31', '2', 'dual32', '2', 'dual41', '2', 'dual42', '2', 'dual51', '2', 'dual52', '2', 'dual61', '2', 'dual62', '2', 'dual71', '2', 'dual72', '2', 'elemDataMatch', '2', 'elemRegul', '2', 'gradient1', '2', 'gradient2', '2', 'gradient3', '2', 'gradient4', '2', 'gradient5', '2', 'gradient6', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'l2grad2', '2', 'measuredDisp11', '2', 'measuredDisp12', '2', 'measuredDisp21', '2', 'measuredDisp22', '2', 'measuredDisp31', '2', 'measuredDisp32', '2', 'measuredDisp41', '2', 'measuredDisp42', '2', 'measuredDisp51', '2', 'measuredDisp52', '2', 'measuredDisp61', '2', 'measuredDisp62', '2', 'measuredDisp71', '2', 'measuredDisp72', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'predictedDisp21', '2', 'predictedDisp22', '2', 'predictedDisp31', '2', 'predictedDisp32', '2', 'predictedDisp41', '2', 'predictedDisp42', '2', 'predictedDisp51', '2', 'predictedDisp52', '2', 'predictedDisp61', '2', 'predictedDisp62', '2', 'predictedDisp71', '2', 'predictedDisp72', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine8Display.SeriesMarkerStyle = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# Properties modified on plotOverLine8.Source
plotOverLine8.Source.Point2 = [84.0, 4.0, 0.0]

# Properties modified on plotOverLine8.Source
plotOverLine8.Source.Point2 = [84.0, 4.0, 0.0]

# set active source
SetActiveSource(plotOverLine3)

# Properties modified on plotOverLine3Display
plotOverLine3Display.SeriesVisibility = []
plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.889998', '0.100008', '0.110002', 'Gradients_Y', '0.220005', '0.489998', '0.719997', 'Gradients_Z', '0.300008', '0.689998', '0.289998', 'Gradients_Magnitude', '0.6', '0.310002', '0.639994', 'NLP', '1', '0.500008', '0', 'predictedDisp11', '0.650004', '0.340002', '0.160006', 'predictedDisp12', '0', '0', '0', 'property3', '0.889998', '0.100008', '0.110002', 'property4', '0.220005', '0.489998', '0.719997', 'property5', '0.300008', '0.689998', '0.289998', 'property6', '0.6', '0.310002', '0.639994', 'SM', '1', '0.500008', '0', 'vtkValidPointMask', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998']
plotOverLine3Display.SeriesPlotCorner = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']
plotOverLine3Display.SeriesLineStyle = ['Gradients_Magnitude', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'NLP', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'SM', '1', 'arc_length', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'vtkValidPointMask', '1']
plotOverLine3Display.SeriesLineThickness = ['Gradients_Magnitude', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'NLP', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'SM', '2', 'arc_length', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'vtkValidPointMask', '2']
plotOverLine3Display.SeriesMarkerStyle = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']

# hide data in view
Hide(plotOverLine3, lineChartView1)

# set active source
SetActiveSource(plotOverLine4)

# Properties modified on plotOverLine4Display
plotOverLine4Display.SeriesVisibility = []
plotOverLine4Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.889998', '0.100008', '0.110002', 'Gradients_Y', '0.220005', '0.489998', '0.719997', 'Gradients_Z', '0.300008', '0.689998', '0.289998', 'Gradients_Magnitude', '0.6', '0.310002', '0.639994', 'NLP', '1', '0.500008', '0', 'predictedDisp11', '0.650004', '0.340002', '0.160006', 'predictedDisp12', '0', '0', '0', 'property3', '0.889998', '0.100008', '0.110002', 'property4', '0.220005', '0.489998', '0.719997', 'property5', '0.300008', '0.689998', '0.289998', 'property6', '0.6', '0.310002', '0.639994', 'SM', '1', '0.500008', '0', 'vtkValidPointMask', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998']
plotOverLine4Display.SeriesPlotCorner = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']
plotOverLine4Display.SeriesLineStyle = ['Gradients_Magnitude', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'NLP', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'SM', '1', 'arc_length', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'vtkValidPointMask', '1']
plotOverLine4Display.SeriesLineThickness = ['Gradients_Magnitude', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'NLP', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'SM', '2', 'arc_length', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'vtkValidPointMask', '2']
plotOverLine4Display.SeriesMarkerStyle = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']

# hide data in view
Hide(plotOverLine4, lineChartView1)

# set active source
SetActiveSource(plotOverLine5)

# Properties modified on plotOverLine5Display
plotOverLine5Display.SeriesVisibility = []
plotOverLine5Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.889998', '0.100008', '0.110002', 'Gradients_Y', '0.220005', '0.489998', '0.719997', 'Gradients_Z', '0.300008', '0.689998', '0.289998', 'Gradients_Magnitude', '0.6', '0.310002', '0.639994', 'NLP', '1', '0.500008', '0', 'predictedDisp11', '0.650004', '0.340002', '0.160006', 'predictedDisp12', '0', '0', '0', 'property3', '0.889998', '0.100008', '0.110002', 'property4', '0.220005', '0.489998', '0.719997', 'property5', '0.300008', '0.689998', '0.289998', 'property6', '0.6', '0.310002', '0.639994', 'SM', '1', '0.500008', '0', 'vtkValidPointMask', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998']
plotOverLine5Display.SeriesPlotCorner = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']
plotOverLine5Display.SeriesLineStyle = ['Gradients_Magnitude', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'NLP', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'SM', '1', 'arc_length', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'vtkValidPointMask', '1']
plotOverLine5Display.SeriesLineThickness = ['Gradients_Magnitude', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'NLP', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'SM', '2', 'arc_length', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'vtkValidPointMask', '2']
plotOverLine5Display.SeriesMarkerStyle = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']

# hide data in view
Hide(plotOverLine5, lineChartView1)

# set active source
SetActiveSource(plotOverLine6)

# Properties modified on plotOverLine6Display
plotOverLine6Display.SeriesVisibility = []
plotOverLine6Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.889998', '0.100008', '0.110002', 'Gradients_Y', '0.220005', '0.489998', '0.719997', 'Gradients_Z', '0.300008', '0.689998', '0.289998', 'Gradients_Magnitude', '0.6', '0.310002', '0.639994', 'NLP', '1', '0.500008', '0', 'predictedDisp11', '0.650004', '0.340002', '0.160006', 'predictedDisp12', '0', '0', '0', 'property3', '0.889998', '0.100008', '0.110002', 'property4', '0.220005', '0.489998', '0.719997', 'property5', '0.300008', '0.689998', '0.289998', 'property6', '0.6', '0.310002', '0.639994', 'SM', '1', '0.500008', '0', 'vtkValidPointMask', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998']
plotOverLine6Display.SeriesPlotCorner = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']
plotOverLine6Display.SeriesLineStyle = ['Gradients_Magnitude', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'NLP', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'SM', '1', 'arc_length', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'vtkValidPointMask', '1']
plotOverLine6Display.SeriesLineThickness = ['Gradients_Magnitude', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'NLP', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'SM', '2', 'arc_length', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'vtkValidPointMask', '2']
plotOverLine6Display.SeriesMarkerStyle = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']

# hide data in view
Hide(plotOverLine6, lineChartView1)

# set active source
SetActiveSource(plotOverLine7)

# Properties modified on plotOverLine7Display
plotOverLine7Display.SeriesVisibility = []
plotOverLine7Display.SeriesColor = ['arc_length', '0', '0', '0', 'Gradients_X', '0.889998', '0.100008', '0.110002', 'Gradients_Y', '0.220005', '0.489998', '0.719997', 'Gradients_Z', '0.300008', '0.689998', '0.289998', 'Gradients_Magnitude', '0.6', '0.310002', '0.639994', 'NLP', '1', '0.500008', '0', 'predictedDisp11', '0.650004', '0.340002', '0.160006', 'predictedDisp12', '0', '0', '0', 'property3', '0.889998', '0.100008', '0.110002', 'property4', '0.220005', '0.489998', '0.719997', 'property5', '0.300008', '0.689998', '0.289998', 'property6', '0.6', '0.310002', '0.639994', 'SM', '1', '0.500008', '0', 'vtkValidPointMask', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998']
plotOverLine7Display.SeriesPlotCorner = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']
plotOverLine7Display.SeriesLineStyle = ['Gradients_Magnitude', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'NLP', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'SM', '1', 'arc_length', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'vtkValidPointMask', '1']
plotOverLine7Display.SeriesLineThickness = ['Gradients_Magnitude', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'NLP', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'SM', '2', 'arc_length', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'vtkValidPointMask', '2']
plotOverLine7Display.SeriesMarkerStyle = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']

# hide data in view
Hide(plotOverLine7, lineChartView1)

# set active source
SetActiveSource(plotOverLine8)

# Properties modified on plotOverLine8Display
plotOverLine8Display.SeriesVisibility = []
plotOverLine8Display.SeriesColor = ['arc_length', '0', '0', '0', 'dual11', '0.889998', '0.100008', '0.110002', 'dual12', '0.220005', '0.489998', '0.719997', 'dual21', '0.300008', '0.689998', '0.289998', 'dual22', '0.6', '0.310002', '0.639994', 'dual31', '1', '0.500008', '0', 'dual32', '0.650004', '0.340002', '0.160006', 'dual41', '0', '0', '0', 'dual42', '0.889998', '0.100008', '0.110002', 'dual51', '0.220005', '0.489998', '0.719997', 'dual52', '0.300008', '0.689998', '0.289998', 'dual61', '0.6', '0.310002', '0.639994', 'dual62', '1', '0.500008', '0', 'dual71', '0.650004', '0.340002', '0.160006', 'dual72', '0', '0', '0', 'elemDataMatch', '0.889998', '0.100008', '0.110002', 'elemRegul', '0.220005', '0.489998', '0.719997', 'gradient1', '0.300008', '0.689998', '0.289998', 'gradient2', '0.6', '0.310002', '0.639994', 'gradient3', '1', '0.500008', '0', 'gradient4', '0.650004', '0.340002', '0.160006', 'gradient5', '0', '0', '0', 'gradient6', '0.889998', '0.100008', '0.110002', 'Gradients_X', '0.220005', '0.489998', '0.719997', 'Gradients_Y', '0.300008', '0.689998', '0.289998', 'Gradients_Z', '0.6', '0.310002', '0.639994', 'Gradients_Magnitude', '1', '0.500008', '0', 'l2grad2', '0.650004', '0.340002', '0.160006', 'measuredDisp11', '0', '0', '0', 'measuredDisp12', '0.889998', '0.100008', '0.110002', 'measuredDisp21', '0.220005', '0.489998', '0.719997', 'measuredDisp22', '0.300008', '0.689998', '0.289998', 'measuredDisp31', '0.6', '0.310002', '0.639994', 'measuredDisp32', '1', '0.500008', '0', 'measuredDisp41', '0.650004', '0.340002', '0.160006', 'measuredDisp42', '0', '0', '0', 'measuredDisp51', '0.889998', '0.100008', '0.110002', 'measuredDisp52', '0.220005', '0.489998', '0.719997', 'measuredDisp61', '0.300008', '0.689998', '0.289998', 'measuredDisp62', '0.6', '0.310002', '0.639994', 'measuredDisp71', '1', '0.500008', '0', 'measuredDisp72', '0.650004', '0.340002', '0.160006', 'NLP', '0', '0', '0', 'predictedDisp11', '0.889998', '0.100008', '0.110002', 'predictedDisp12', '0.220005', '0.489998', '0.719997', 'predictedDisp21', '0.300008', '0.689998', '0.289998', 'predictedDisp22', '0.6', '0.310002', '0.639994', 'predictedDisp31', '1', '0.500008', '0', 'predictedDisp32', '0.650004', '0.340002', '0.160006', 'predictedDisp41', '0', '0', '0', 'predictedDisp42', '0.889998', '0.100008', '0.110002', 'predictedDisp51', '0.220005', '0.489998', '0.719997', 'predictedDisp52', '0.300008', '0.689998', '0.289998', 'predictedDisp61', '0.6', '0.310002', '0.639994', 'predictedDisp62', '1', '0.500008', '0', 'predictedDisp71', '0.650004', '0.340002', '0.160006', 'predictedDisp72', '0', '0', '0', 'property3', '0.889998', '0.100008', '0.110002', 'property4', '0.220005', '0.489998', '0.719997', 'property5', '0.300008', '0.689998', '0.289998', 'property6', '0.6', '0.310002', '0.639994', 'SM', '1', '0.500008', '0', 'vtkValidPointMask', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998']
plotOverLine8Display.SeriesPlotCorner = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']
plotOverLine8Display.SeriesLineStyle = ['Gradients_Magnitude', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'NLP', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'SM', '1', 'arc_length', '1', 'dual11', '1', 'dual12', '1', 'dual21', '1', 'dual22', '1', 'dual31', '1', 'dual32', '1', 'dual41', '1', 'dual42', '1', 'dual51', '1', 'dual52', '1', 'dual61', '1', 'dual62', '1', 'dual71', '1', 'dual72', '1', 'elemDataMatch', '1', 'elemRegul', '1', 'gradient1', '1', 'gradient2', '1', 'gradient3', '1', 'gradient4', '1', 'gradient5', '1', 'gradient6', '1', 'l2grad2', '1', 'measuredDisp11', '1', 'measuredDisp12', '1', 'measuredDisp21', '1', 'measuredDisp22', '1', 'measuredDisp31', '1', 'measuredDisp32', '1', 'measuredDisp41', '1', 'measuredDisp42', '1', 'measuredDisp51', '1', 'measuredDisp52', '1', 'measuredDisp61', '1', 'measuredDisp62', '1', 'measuredDisp71', '1', 'measuredDisp72', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'predictedDisp21', '1', 'predictedDisp22', '1', 'predictedDisp31', '1', 'predictedDisp32', '1', 'predictedDisp41', '1', 'predictedDisp42', '1', 'predictedDisp51', '1', 'predictedDisp52', '1', 'predictedDisp61', '1', 'predictedDisp62', '1', 'predictedDisp71', '1', 'predictedDisp72', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'vtkValidPointMask', '1']
plotOverLine8Display.SeriesLineThickness = ['Gradients_Magnitude', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'NLP', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'SM', '2', 'arc_length', '2', 'dual11', '2', 'dual12', '2', 'dual21', '2', 'dual22', '2', 'dual31', '2', 'dual32', '2', 'dual41', '2', 'dual42', '2', 'dual51', '2', 'dual52', '2', 'dual61', '2', 'dual62', '2', 'dual71', '2', 'dual72', '2', 'elemDataMatch', '2', 'elemRegul', '2', 'gradient1', '2', 'gradient2', '2', 'gradient3', '2', 'gradient4', '2', 'gradient5', '2', 'gradient6', '2', 'l2grad2', '2', 'measuredDisp11', '2', 'measuredDisp12', '2', 'measuredDisp21', '2', 'measuredDisp22', '2', 'measuredDisp31', '2', 'measuredDisp32', '2', 'measuredDisp41', '2', 'measuredDisp42', '2', 'measuredDisp51', '2', 'measuredDisp52', '2', 'measuredDisp61', '2', 'measuredDisp62', '2', 'measuredDisp71', '2', 'measuredDisp72', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'predictedDisp21', '2', 'predictedDisp22', '2', 'predictedDisp31', '2', 'predictedDisp32', '2', 'predictedDisp41', '2', 'predictedDisp42', '2', 'predictedDisp51', '2', 'predictedDisp52', '2', 'predictedDisp61', '2', 'predictedDisp62', '2', 'predictedDisp71', '2', 'predictedDisp72', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'vtkValidPointMask', '2']
plotOverLine8Display.SeriesMarkerStyle = ['Gradients_Magnitude', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'NLP', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SM', '0', 'arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'vtkValidPointMask', '0']

# Properties modified on plotOverLine8Display
plotOverLine8Display.SeriesVisibility = ['measuredDisp11']

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [44.0, 70.0, 10000.0]
renderView1.CameraFocalPoint = [44.0, 70.0, 0.0]
renderView1.CameraParallelScale = 82.68010643437755

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
