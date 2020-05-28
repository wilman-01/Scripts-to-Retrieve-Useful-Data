#### import the simple module from the paraview
from paraview.simple import *

#addresses contains all the directories addresses for the input files
addresses = ["C:\Users\wilma\Desktop\\Foward-02-13-2014i0.vtk",
             "C:\Users\wilma\Desktop\\SM-m1InvNoise3Alfa1e12-03-13-2014i12000.vtk"]
#naming is index for accessing destiny directories for screenshots
naming = 0
#Empty arrays that will hold the addresses and name where screenshots will be saved
NLP=[]
SM=[]
P3=[]
P4=[]
Theta=[]
#Change range if you are generating all screenshots on same directory(to keep sequence)
#Change destiny addresses for screenshots as desired
for j in range(0,len(addresses)+1):
    NLP.append("C:/Users/wilma/Desktop/Trial_Screenshots/NLP-{}.png".format(j))
    SM.append("C:/Users/wilma/Desktop/Trial_Screenshots/SM-{}.png".format(j))
    P3.append("C:/Users/wilma/Desktop/Trial_Screenshots/P3-{}.png".format(j))
    P4.append("C:/Users/wilma/Desktop/Trial_Screenshots/P4-{}.png".format(j))
    Theta.append("C:/Users/wilma/Desktop/Trial_Screenshots/Theta-{}.png".format(j))

for i in addresses:
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()
    # create a new 'Legacy VTK Reader'
    sMm1InvNoise3Alfa1e1203132014i20000vtk = LegacyVTKReader(FileNames=[i])
    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    # renderView1.ViewSize = [753, 616]
    # get color transfer function/color map for 'measuredDisp11'
    measuredDisp11LUT = GetColorTransferFunction('measuredDisp11')
    measuredDisp11LUT.RGBPoints = [-0.010142600163817406, 0.231373, 0.298039, 0.752941, -0.005071300081908703, 0.865003, 0.865003, 0.865003, 0.0, 0.705882, 0.0156863, 0.14902]
    measuredDisp11LUT.ScalarRangeInitialized = 1.0
    # show data in view
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay = Show(sMm1InvNoise3Alfa1e1203132014i20000vtk, renderView1)
    # trace defaults for the display properties.
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.Representation = 'Surface'
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.ColorArrayName = ['POINTS', 'measuredDisp11']
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.LookupTable = measuredDisp11LUT
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.OSPRayScaleArray = 'measuredDisp11'
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.SelectOrientationVectors = 'NLP'
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.ScaleFactor = 0.1
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.SelectScaleArray = 'measuredDisp11'
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.GlyphType = 'Arrow'
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.ScalarOpacityUnitDistance = 0.14647634504554957
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.GaussianRadius = 0.05
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.SetScaleArray = ['POINTS', 'measuredDisp11']
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.OpacityArray = ['POINTS', 'measuredDisp11']
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    # show color bar/color legend
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.SetScalarBarVisibility(renderView1, True)
    # set scalar coloring
    ColorBy(sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay, ('POINTS', 'NLP'))
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(measuredDisp11LUT, renderView1)
    # rescale color and/or opacity maps used to include current data range
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.RescaleTransferFunctionToDataRange(True, False)
    # show color bar/color legend
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.SetScalarBarVisibility(renderView1, True)
    # get color transfer function/color map for 'NLP'
    nLPLUT = GetColorTransferFunction('NLP')
    nLPLUT.RGBPoints = [3.569999933242798, 0.231373, 0.298039, 0.752941, 12.168950200080872, 0.865003, 0.865003, 0.865003, 20.767900466918945, 0.705882, 0.0156863, 0.14902]
    nLPLUT.ScalarRangeInitialized = 1.0
    # rescale color and/or opacity maps used to exactly fit the current data range
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.RescaleTransferFunctionToDataRange(False, True)
    # get color legend/bar for nLPLUT in view renderView1
    nLPLUTColorBar = GetScalarBar(nLPLUT, renderView1)
    nLPLUTColorBar.Title = 'NLP'
    nLPLUTColorBar.ComponentTitle = ''
    nLPLUTColorBar.TitleFontSize = 11
    nLPLUTColorBar.LabelFontSize = 14
    nLPLUTColorBar.RangeLabelFormat = '%4.4f'
    # Properties modified on nLPLUTColorBar
    nLPLUTColorBar.TitleFontSize = 42
    nLPLUTColorBar.LabelFontSize = 18
    # Properties modified on nLPLUTColorBar
    nLPLUTColorBar.TitleFontSize = 25
    nLPLUTColorBar.LabelFontSize = 25
    # change scalar bar placement
    nLPLUTColorBar.Position = [0.6839060710194731, 0.19166666666666662]
    nLPLUTColorBar.Position2 = [0.12, 0.5577777777777775]
    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [77.5313764983865, 61.96165631887991, 10000.0]
    renderView1.CameraFocalPoint = [77.5313764983865, 61.96165631887991, 0.0]
    renderView1.CameraParallelScale = 82.68010643437755
    # save screenshot
    SaveScreenshot(NLP[naming], magnification=1, quality=100, view=renderView1)
    # set scalar coloring
    ColorBy(sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay, ('POINTS', 'SM'))
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(nLPLUT, renderView1)
    # rescale color and/or opacity maps used to include current data range
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.RescaleTransferFunctionToDataRange(True, False)
    # show color bar/color legend
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.SetScalarBarVisibility(renderView1, True)
    # get color transfer function/color map for 'SM'
    sMLUT = GetColorTransferFunction('SM')
    sMLUT.RGBPoints = [1.4299999475479126, 0.231373, 0.298039, 0.752941, 6.950350105762482, 0.865003, 0.865003, 0.865003, 12.47070026397705, 0.705882, 0.0156863, 0.14902]
    sMLUT.ScalarRangeInitialized = 1.0
    # rescale color and/or opacity maps used to exactly fit the current data range
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.RescaleTransferFunctionToDataRange(False, True)
    # get color legend/bar for sMLUT in view renderView1
    sMLUTColorBar = GetScalarBar(sMLUT, renderView1)
    sMLUTColorBar.Title = 'SM'
    sMLUTColorBar.ComponentTitle = ''
    sMLUTColorBar.TitleFontSize = 25
    sMLUTColorBar.LabelFontSize = 25
    sMLUTColorBar.RangeLabelFormat = '%4.4f'
    # change scalar bar placement
    sMLUTColorBar.Position = [0.6839060710194731, 0.19166666666666662]
    sMLUTColorBar.Position2 = [0.12, 0.5577777777777775]
    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [77.5313764983865, 61.96165631887991, 10000.0]
    renderView1.CameraFocalPoint = [77.5313764983865, 61.96165631887991, 0.0]
    renderView1.CameraParallelScale = 82.68010643437755
    # save screenshot
    SaveScreenshot(SM[naming], magnification=1, quality=100, view=renderView1)
    # set scalar coloring
    ColorBy(sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay, ('POINTS', 'property3'))
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(sMLUT, renderView1)
    # rescale color and/or opacity maps used to include current data range
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.RescaleTransferFunctionToDataRange(True, False)
    # show color bar/color legend
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.SetScalarBarVisibility(renderView1, True)
    # get color transfer function/color map for 'property3'
    property3LUT = GetColorTransferFunction('property3')
    property3LUT.RGBPoints = [3.8417999744415283, 0.231373, 0.298039, 0.752941, 7.257099747657776, 0.865003, 0.865003, 0.865003, 10.672399520874023, 0.705882, 0.0156863, 0.14902]
    property3LUT.ScalarRangeInitialized = 1.0
    # rescale color and/or opacity maps used to exactly fit the current data range
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.RescaleTransferFunctionToDataRange(False, True)
    # get color legend/bar for property3LUT in view renderView1
    property3LUTColorBar = GetScalarBar(property3LUT, renderView1)
    property3LUTColorBar.Title = 'property3'
    property3LUTColorBar.ComponentTitle = ''
    property3LUTColorBar.TitleFontSize = 25
    property3LUTColorBar.LabelFontSize = 25
    property3LUTColorBar.RangeLabelFormat = '%4.4f'
    # change scalar bar placement
    property3LUTColorBar.Position = [0.6839060710194731, 0.19166666666666662]
    property3LUTColorBar.Position2 = [0.12, 0.5577777777777775]
    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [77.5313764983865, 61.96165631887991, 10000.0]
    renderView1.CameraFocalPoint = [77.5313764983865, 61.96165631887991, 0.0]
    renderView1.CameraParallelScale = 82.68010643437755
    # save screenshot
    SaveScreenshot(P3[naming], magnification=1, quality=100, view=renderView1)
    # set scalar coloring
    ColorBy(sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay, ('POINTS', 'property4'))
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(property3LUT, renderView1)
    # rescale color and/or opacity maps used to include current data range
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.RescaleTransferFunctionToDataRange(True, False)
    # show color bar/color legend
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.SetScalarBarVisibility(renderView1, True)
    # get color transfer function/color map for 'property4'
    property4LUT = GetColorTransferFunction('property4')
    property4LUT.RGBPoints = [1.0700000524520874, 0.231373, 0.298039, 0.752941, 11.101849734783173, 0.865003, 0.865003, 0.865003, 21.133699417114258, 0.705882, 0.0156863, 0.14902]
    property4LUT.ScalarRangeInitialized = 1.0
    # rescale color and/or opacity maps used to exactly fit the current data range
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.RescaleTransferFunctionToDataRange(False, True)
    # get color legend/bar for property4LUT in view renderView1
    property4LUTColorBar = GetScalarBar(property4LUT, renderView1)
    property4LUTColorBar.Title = 'property4'
    property4LUTColorBar.ComponentTitle = ''
    property4LUTColorBar.TitleFontSize = 25
    property4LUTColorBar.LabelFontSize = 25
    property4LUTColorBar.RangeLabelFormat = '%4.4f'
    # change scalar bar placement
    property4LUTColorBar.Position = [0.6839060710194731, 0.19166666666666662]
    property4LUTColorBar.Position2 = [0.12, 0.5577777777777775]
    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [77.5313764983865, 61.96165631887991, 10000.0]
    renderView1.CameraFocalPoint = [77.5313764983865, 61.96165631887991, 0.0]
    renderView1.CameraParallelScale = 82.68010643437755
    # save screenshot
    SaveScreenshot(P4[naming], magnification=1, quality=100, view=renderView1)
    # set scalar coloring
    ColorBy(sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay, ('POINTS', 'property5'))
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(property4LUT, renderView1)
    # rescale color and/or opacity maps used to include current data range
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.RescaleTransferFunctionToDataRange(True, False)
    # show color bar/color legend
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.SetScalarBarVisibility(renderView1, True)
    # get color transfer function/color map for 'property5'
    property5LUT = GetColorTransferFunction('property5')
    property5LUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5957450270652771, 0.865003, 0.865003, 0.865003, 1.1914900541305542, 0.705882, 0.0156863, 0.14902]
    property5LUT.ScalarRangeInitialized = 1.0
    # rescale color and/or opacity maps used to exactly fit the current data range
    sMm1InvNoise3Alfa1e1203132014i20000vtkDisplay.RescaleTransferFunctionToDataRange(False, True)
    # get color legend/bar for property5LUT in view renderView1
    property5LUTColorBar = GetScalarBar(property5LUT, renderView1)
    property5LUTColorBar.Title = 'property5'
    property5LUTColorBar.ComponentTitle = ''
    property5LUTColorBar.TitleFontSize = 25
    property5LUTColorBar.LabelFontSize = 25
    property5LUTColorBar.RangeLabelFormat = '%4.4f'
    # change scalar bar placement
    property5LUTColorBar.Position = [0.6839060710194731, 0.19166666666666662]
    property5LUTColorBar.Position2 = [0.12, 0.5577777777777775]
    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [77.5313764983865, 61.96165631887991, 10000.0]
    renderView1.CameraFocalPoint = [77.5313764983865, 61.96165631887991, 0.0]
    renderView1.CameraParallelScale = 82.68010643437755
    # save screenshot
    SaveScreenshot(Theta[naming], magnification=1, quality=100, view=renderView1)
    #### saving camera placements for all active views
    # current camera placement for renderView1
    #renderView1.InteractionMode = '2D'
    #renderView1.CameraPosition = [0.6928473039599669, 0.5344370185642802, 10000.0]
    #renderView1.CameraFocalPoint = [0.6928473039599669, 0.5344370185642802, 0.0]
    #renderView1.CameraParallelScale = 0.7071067811865476
    # destroy sMm1InvNoise3Alfa1e1203132014i20000vtk
    Hide(sMm1InvNoise3Alfa1e1203132014i20000vtk)
    Delete(sMm1InvNoise3Alfa1e1203132014i20000vtk)
    del sMm1InvNoise3Alfa1e1203132014i20000vtk
    naming = naming+1
    #### uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).


