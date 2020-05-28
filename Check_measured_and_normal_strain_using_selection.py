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

x1 = 6.0
y1 = 6.0
x2 = 82.0
y2 = 74.0

##Change to 0 if using smaller domain; otherwise use 1 for subdomain
using_subdomain = 1;

#Select 1 to observe nrml_strain
nrml_strain = 1

#Choose 1 for x analysis or 2 for y analysis
disp = 1;

if disp == 1:
    gradient = 'X'
elif disp == 2:
    gradient = 'Y'


#Select 'predictedDisp12' to check x disp or 'predictedDisp12' for y disp
property1_gradient = 'predictedDisp1'+str(disp)
#Select 'measuredDispx1' for GradientX or 'measuredDispx2' for GradientX  for y disp Important for Gradient
property2 = ['measuredDisp1'+str(disp),'measuredDisp2'+str(disp),'measuredDisp3'+str(disp),
             'measuredDisp4'+str(disp),'measuredDisp5'+str(disp),'measuredDisp6'+str(disp),'measuredDisp7'+str(disp)]
#Select property_check1 to check x disp or 'predictedDisp12' for y disp
if nrml_strain == 0:
    property_check1 = property1_gradient
    property_check2 = property2
elif nrml_strain == 1:
    property_check1 = 'Gradients_'+gradient
    property_check2 = ['Gradients_'+gradient,'Gradients_'+gradient,'Gradients_'+gradient,
                       'Gradients_'+gradient,'Gradients_'+gradient,'Gradients_'+gradient,'Gradients_'+gradient]

######################################Create gradients ################################################

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1495, 720]

# show data in view
foward02132014i0_1vtkDisplay = Show(foward02132014i0_1vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(Input=foward02132014i0_1vtk)
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', property1_gradient]
# Hide data in view
Hide(foward02132014i0_1vtk, renderView1)

# show data in view
foward02132014i0_2vtkDisplay = Show(foward02132014i0_2vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet2 = GradientOfUnstructuredDataSet(Input=foward02132014i0_2vtk)
gradientOfUnstructuredDataSet2.ScalarArray = ['POINTS', property1_gradient]
# Hide data in view
Hide(foward02132014i0_2vtk, renderView1)

# show data in view
foward02132014i0_3vtkDisplay = Show(foward02132014i0_3vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet3 = GradientOfUnstructuredDataSet(Input=foward02132014i0_3vtk)
gradientOfUnstructuredDataSet3.ScalarArray = ['POINTS', property1_gradient]
# Hide data in view
Hide(foward02132014i0_3vtk, renderView1)

# show data in view
foward02132014i0_4vtkDisplay = Show(foward02132014i0_4vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet4 = GradientOfUnstructuredDataSet(Input=foward02132014i0_4vtk)
gradientOfUnstructuredDataSet4.ScalarArray = ['POINTS', property1_gradient]
# Hide data in view
Hide(foward02132014i0_4vtk, renderView1)

# show data in view
foward02132014i0_5vtkDisplay = Show(foward02132014i0_5vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet5 = GradientOfUnstructuredDataSet(Input=foward02132014i0_5vtk)
gradientOfUnstructuredDataSet5.ScalarArray = ['POINTS', property1_gradient]
# Hide data in view
Hide(foward02132014i0_5vtk, renderView1)

# show data in view
foward02132014i0_6vtkDisplay = Show(foward02132014i0_6vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet6 = GradientOfUnstructuredDataSet(Input=foward02132014i0_6vtk)
gradientOfUnstructuredDataSet6.ScalarArray = ['POINTS', property1_gradient]
# Hide data in view
Hide(foward02132014i0_6vtk, renderView1)

# show data in view
foward02132014i0_7vtkDisplay = Show(foward02132014i0_7vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet7 = GradientOfUnstructuredDataSet(Input=foward02132014i0_7vtk)
gradientOfUnstructuredDataSet7.ScalarArray = ['POINTS', property1_gradient]
# Hide data in view
Hide(foward02132014i0_7vtk, renderView1)

# show data in view
foward02132014i0_8vtkDisplay = Show(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet8 = GradientOfUnstructuredDataSet(Input=sMm1InvNoise3Alfa1e1203132014i12000vtk)
gradientOfUnstructuredDataSet8.ScalarArray = ['POINTS', property2[0]]
# Hide data in view
Hide(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)

# show data in view
foward02132014i0_8vtkDisplay = Show(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet9 = GradientOfUnstructuredDataSet(Input=sMm1InvNoise3Alfa1e1203132014i12000vtk)
gradientOfUnstructuredDataSet9.ScalarArray = ['POINTS', property2[1]]
# Hide data in view
Hide(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)

# show data in view
foward02132014i0_8vtkDisplay = Show(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet10 = GradientOfUnstructuredDataSet(Input=sMm1InvNoise3Alfa1e1203132014i12000vtk)
gradientOfUnstructuredDataSet10.ScalarArray = ['POINTS', property2[2]]
# Hide data in view
Hide(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)

# show data in view
foward02132014i0_8vtkDisplay = Show(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet11 = GradientOfUnstructuredDataSet(Input=sMm1InvNoise3Alfa1e1203132014i12000vtk)
gradientOfUnstructuredDataSet11.ScalarArray = ['POINTS', property2[3]]
# Hide data in view
Hide(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)

# show data in view
foward02132014i0_8vtkDisplay = Show(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet12 = GradientOfUnstructuredDataSet(Input=sMm1InvNoise3Alfa1e1203132014i12000vtk)
gradientOfUnstructuredDataSet12.ScalarArray = ['POINTS', property2[4]]
# Hide data in view
Hide(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)

# show data in view
foward02132014i0_8vtkDisplay = Show(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet13 = GradientOfUnstructuredDataSet(Input=sMm1InvNoise3Alfa1e1203132014i12000vtk)
gradientOfUnstructuredDataSet13.ScalarArray = ['POINTS', property2[5]]
# Hide data in view
Hide(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)

# show data in view
foward02132014i0_8vtkDisplay = Show(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)
# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet14 = GradientOfUnstructuredDataSet(Input=sMm1InvNoise3Alfa1e1203132014i12000vtk)
gradientOfUnstructuredDataSet14.ScalarArray = ['POINTS', property2[6]]
# Hide data in view
Hide(sMm1InvNoise3Alfa1e1203132014i12000vtk, renderView1)

################################################### End Gradient ###################################

########################################### Selection ####################################

# create a new 'Extract Selection'
extractSelection1 = ExtractSelection(Input=gradientOfUnstructuredDataSet1,Selection=None)
# create a new 'Extract Selection'
extractSelection2 = ExtractSelection(Input=gradientOfUnstructuredDataSet2,Selection=None)
# create a new 'Extract Selection'
extractSelection3 = ExtractSelection(Input=gradientOfUnstructuredDataSet3,Selection=None)
# create a new 'Extract Selection'
extractSelection4 = ExtractSelection(Input=gradientOfUnstructuredDataSet4,Selection=None)
# create a new 'Extract Selection'
extractSelection5 = ExtractSelection(Input=gradientOfUnstructuredDataSet5,Selection=None)
# create a new 'Extract Selection'
extractSelection6 = ExtractSelection(Input=gradientOfUnstructuredDataSet6,Selection=None)
# create a new 'Extract Selection'
extractSelection7 = ExtractSelection(Input=gradientOfUnstructuredDataSet7,Selection=None)

if using_subdomain == 1:
    # create a new 'Extract Selection'
    extractSelection8 = gradientOfUnstructuredDataSet8
    # create a new 'Extract Selection'
    extractSelection9 = gradientOfUnstructuredDataSet9
    # create a new 'Extract Selection'
    extractSelection10 = gradientOfUnstructuredDataSet10
    # create a new 'Extract Selection'
    extractSelection11 = gradientOfUnstructuredDataSet11
    # create a new 'Extract Selection'
    extractSelection12 = gradientOfUnstructuredDataSet12
    # create a new 'Extract Selection'
    extractSelection13 = gradientOfUnstructuredDataSet13
    # create a new 'Extract Selection'
    extractSelection14 = gradientOfUnstructuredDataSet14
else:
    # create a new 'Extract Selection'
    extractSelection8 = ExtractSelection(Input=gradientOfUnstructuredDataSet8,Selection=None)
    # create a new 'Extract Selection'
    extractSelection9 = ExtractSelection(Input=gradientOfUnstructuredDataSet9,Selection=None)
    # create a new 'Extract Selection'
    extractSelection10 = ExtractSelection(Input=gradientOfUnstructuredDataSet10,Selection=None)
    # create a new 'Extract Selection'
    extractSelection11 = ExtractSelection(Input=gradientOfUnstructuredDataSet11,Selection=None)
    # create a new 'Extract Selection'
    extractSelection12 = ExtractSelection(Input=gradientOfUnstructuredDataSet12,Selection=None)
    # create a new 'Extract Selection'
    extractSelection13 = ExtractSelection(Input=gradientOfUnstructuredDataSet13,Selection=None)
    # create a new 'Extract Selection'
    extractSelection14 = ExtractSelection(Input=gradientOfUnstructuredDataSet14,Selection=None)

########################################### End Selection ####################################

########################################### Calculator #######################################

# create a new 'Calculator'
calculator1 = Calculator(Input=extractSelection1)
calculator1.ResultArrayName = 'Result1'
calculator1.Function = property_check1
# create a new 'Calculator'
calculator2 = Calculator(Input=extractSelection2)
calculator2.ResultArrayName = 'Result2'
calculator2.Function = property_check1
# create a new 'Calculator'
calculator3 = Calculator(Input=extractSelection3)
calculator3.ResultArrayName = 'Result3'
calculator3.Function = property_check1
# create a new 'Calculator'
calculator4 = Calculator(Input=extractSelection4)
calculator4.ResultArrayName = 'Result4'
calculator4.Function = property_check1
# create a new 'Calculator'
calculator5 = Calculator(Input=extractSelection5)
calculator5.ResultArrayName = 'Result5'
calculator5.Function = property_check1
# create a new 'Calculator'
calculator6 = Calculator(Input=extractSelection6)
calculator6.ResultArrayName = 'Result6'
calculator6.Function = property_check1
# create a new 'Calculator'
calculator7 = Calculator(Input=extractSelection7)
calculator7.ResultArrayName = 'Result7'
calculator7.Function = property_check1
# create a new 'Calculator'
calculator8 = Calculator(Input=gradientOfUnstructuredDataSet8)
calculator8.ResultArrayName = 'Result8'
calculator8.Function = property_check2[0]
# create a new 'Calculator'
calculator9 = Calculator(Input=gradientOfUnstructuredDataSet9)
calculator9.ResultArrayName = 'Result9'
calculator9.Function = property_check2[1]
# create a new 'Calculator'
calculator10 = Calculator(Input=gradientOfUnstructuredDataSet10)
calculator10.ResultArrayName = 'Result10'
calculator10.Function = property_check2[2]
# create a new 'Calculator'
calculator11 = Calculator(Input=gradientOfUnstructuredDataSet11)
calculator11.ResultArrayName = 'Result11'
calculator11.Function = property_check2[3]
# create a new 'Calculator'
calculator12 = Calculator(Input=gradientOfUnstructuredDataSet12)
calculator12.ResultArrayName = 'Result12'
calculator12.Function = property_check2[4]
# create a new 'Calculator'
calculator13 = Calculator(Input=gradientOfUnstructuredDataSet13)
calculator13.ResultArrayName = 'Result13'
calculator13.Function = property_check2[5]
# create a new 'Calculator'
calculator14 = Calculator(Input=gradientOfUnstructuredDataSet14)
calculator14.ResultArrayName = 'Result14'
calculator14.Function = property_check2[6]
################################# End Calculator ###########################################

################################# Append & Append Calculator ###############################
# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(Input=[calculator1, calculator8])
calculator15 = Calculator(Input=appendAttributes1)
calculator15.Function = 'Result1-Result8'
calculator15.ResultArrayName = 'ResultBC 1'
# create a new 'Append Attributes'
appendAttributes2 = AppendAttributes(Input=[calculator2, calculator9])
calculator16 = Calculator(Input=appendAttributes2)
calculator16.Function = 'Result2-Result9'
calculator16.ResultArrayName = 'ResultBC 2'
# create a new 'Append Attributes'
appendAttributes3 = AppendAttributes(Input=[calculator3, calculator10])
calculator17 = Calculator(Input=appendAttributes3)
calculator17.Function = 'Result3-Result10'
calculator17.ResultArrayName = 'ResultBC 3'
# create a new 'Append Attributes'
appendAttributes4 = AppendAttributes(Input=[calculator4, calculator11])
calculator18 = Calculator(Input=appendAttributes4)
calculator18.Function = 'Result4-Result11'
calculator18.ResultArrayName = 'ResultBC 4'
# create a new 'Append Attributes'
appendAttributes5 = AppendAttributes(Input=[calculator5, calculator12])
calculator19 = Calculator(Input=appendAttributes5)
calculator19.Function = 'Result5-Result12'
calculator19.ResultArrayName = 'ResultBC 5'
# create a new 'Append Attributes'
appendAttributes6 = AppendAttributes(Input=[calculator6, calculator13])
calculator20 = Calculator(Input=appendAttributes6)
calculator20.Function = 'Result6-Result13'
calculator20.ResultArrayName = 'ResultBC 6'
# create a new 'Append Attributes'
appendAttributes7 = AppendAttributes(Input=[calculator7, calculator14])
calculator21 = Calculator(Input=appendAttributes7)
calculator21.Function = 'Result7-Result14'
calculator21.ResultArrayName = 'ResultBC 7'
################################# End Append & Append Calculator ###########################################


################################# Plotting Property Inner Region ###################################

CreateLayout('Layout #2')

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=calculator15,
    Source='High Resolution Line Source')
# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [x1, y1, 0.0]
plotOverLine1.Source.Point2 = [x2, y2, 0.0]


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
plotOverLine1Display.SeriesVisibility = ['ResultBC 1']
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'dual11', 'dual11', 'dual12', 'dual12', 'dual21', 'dual21', 'dual22', 'dual22', 'dual31', 'dual31', 'dual32', 'dual32', 'dual41', 'dual41', 'dual42', 'dual42', 'dual51', 'dual51', 'dual52', 'dual52', 'dual61', 'dual61', 'dual62', 'dual62', 'dual71', 'dual71', 'dual72', 'dual72', 'elemDataMatch', 'elemDataMatch', 'elemRegul', 'elemRegul', 'gradient1', 'gradient1', 'gradient2', 'gradient2', 'gradient3', 'gradient3', 'gradient4', 'gradient4', 'gradient5', 'gradient5', 'gradient6', 'gradient6', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'l2grad2', 'l2grad2', 'measuredDisp11', 'measuredDisp11', 'measuredDisp12', 'measuredDisp12', 'measuredDisp21', 'measuredDisp21', 'measuredDisp22', 'measuredDisp22', 'measuredDisp31', 'measuredDisp31', 'measuredDisp32', 'measuredDisp32', 'measuredDisp41', 'measuredDisp41', 'measuredDisp42', 'measuredDisp42', 'measuredDisp51', 'measuredDisp51', 'measuredDisp52', 'measuredDisp52', 'measuredDisp61', 'measuredDisp61', 'measuredDisp62', 'measuredDisp62', 'measuredDisp71', 'measuredDisp71', 'measuredDisp72', 'measuredDisp72', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'predictedDisp21', 'predictedDisp21', 'predictedDisp22', 'predictedDisp22', 'predictedDisp31', 'predictedDisp31', 'predictedDisp32', 'predictedDisp32', 'predictedDisp41', 'predictedDisp41', 'predictedDisp42', 'predictedDisp42', 'predictedDisp51', 'predictedDisp51', 'predictedDisp52', 'predictedDisp52', 'predictedDisp61', 'predictedDisp61', 'predictedDisp62', 'predictedDisp62', 'predictedDisp71', 'predictedDisp71', 'predictedDisp72', 'predictedDisp72', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'Result1', 'Result1', 'Result8', 'Result8', 'ResultBC 1', 'ResultBC 1', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'dual11', '0.89', '0.1', '0.11', 'dual12', '0.22', '0.49', '0.72', 'dual21', '0.3', '0.69', '0.29', 'dual22', '0.6', '0.31', '0.64', 'dual31', '1', '0.5', '0', 'dual32', '0.65', '0.34', '0.16', 'dual41', '0', '0', '0', 'dual42', '0.89', '0.1', '0.11', 'dual51', '0.22', '0.49', '0.72', 'dual52', '0.3', '0.69', '0.29', 'dual61', '0.6', '0.31', '0.64', 'dual62', '1', '0.5', '0', 'dual71', '0.65', '0.34', '0.16', 'dual72', '0', '0', '0', 'elemDataMatch', '0.89', '0.1', '0.11', 'elemRegul', '0.22', '0.49', '0.72', 'gradient1', '0.3', '0.69', '0.29', 'gradient2', '0.6', '0.31', '0.64', 'gradient3', '1', '0.5', '0', 'gradient4', '0.65', '0.34', '0.16', 'gradient5', '0', '0', '0', 'gradient6', '0.89', '0.1', '0.11', 'Gradients_X', '0.22', '0.49', '0.72', 'Gradients_Y', '0.3', '0.69', '0.29', 'Gradients_Z', '0.6', '0.31', '0.64', 'Gradients_Magnitude', '1', '0.5', '0', 'l2grad2', '0.65', '0.34', '0.16', 'measuredDisp11', '0', '0', '0', 'measuredDisp12', '0.89', '0.1', '0.11', 'measuredDisp21', '0.22', '0.49', '0.72', 'measuredDisp22', '0.3', '0.69', '0.29', 'measuredDisp31', '0.6', '0.31', '0.64', 'measuredDisp32', '1', '0.5', '0', 'measuredDisp41', '0.65', '0.34', '0.16', 'measuredDisp42', '0', '0', '0', 'measuredDisp51', '0.89', '0.1', '0.11', 'measuredDisp52', '0.22', '0.49', '0.72', 'measuredDisp61', '0.3', '0.69', '0.29', 'measuredDisp62', '0.6', '0.31', '0.64', 'measuredDisp71', '1', '0.5', '0', 'measuredDisp72', '0.65', '0.34', '0.16', 'NLP', '0', '0', '0', 'predictedDisp11', '0.89', '0.1', '0.11', 'predictedDisp12', '0.22', '0.49', '0.72', 'predictedDisp21', '0.3', '0.69', '0.29', 'predictedDisp22', '0.6', '0.31', '0.64', 'predictedDisp31', '1', '0.5', '0', 'predictedDisp32', '0.65', '0.34', '0.16', 'predictedDisp41', '0', '0', '0', 'predictedDisp42', '0.89', '0.1', '0.11', 'predictedDisp51', '0.22', '0.49', '0.72', 'predictedDisp52', '0.3', '0.69', '0.29', 'predictedDisp61', '0.6', '0.31', '0.64', 'predictedDisp62', '1', '0.5', '0', 'predictedDisp71', '0.65', '0.34', '0.16', 'predictedDisp72', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'Result1', '1', '0.5', '0', 'Result8', '0.65', '0.34', '0.16', 'ResultBC 1', '0', '0', '0', 'SM', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine1Display.SeriesPlotCorner = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result1', '0', 'Result8', '0', 'ResultBC 1', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display.SeriesLabelPrefix = ''
plotOverLine1Display.SeriesLineStyle = ['arc_length', '1', 'dual11', '1', 'dual12', '1', 'dual21', '1', 'dual22', '1', 'dual31', '1', 'dual32', '1', 'dual41', '1', 'dual42', '1', 'dual51', '1', 'dual52', '1', 'dual61', '1', 'dual62', '1', 'dual71', '1', 'dual72', '1', 'elemDataMatch', '1', 'elemRegul', '1', 'gradient1', '1', 'gradient2', '1', 'gradient3', '1', 'gradient4', '1', 'gradient5', '1', 'gradient6', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'l2grad2', '1', 'measuredDisp11', '1', 'measuredDisp12', '1', 'measuredDisp21', '1', 'measuredDisp22', '1', 'measuredDisp31', '1', 'measuredDisp32', '1', 'measuredDisp41', '1', 'measuredDisp42', '1', 'measuredDisp51', '1', 'measuredDisp52', '1', 'measuredDisp61', '1', 'measuredDisp62', '1', 'measuredDisp71', '1', 'measuredDisp72', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'predictedDisp21', '1', 'predictedDisp22', '1', 'predictedDisp31', '1', 'predictedDisp32', '1', 'predictedDisp41', '1', 'predictedDisp42', '1', 'predictedDisp51', '1', 'predictedDisp52', '1', 'predictedDisp61', '1', 'predictedDisp62', '1', 'predictedDisp71', '1', 'predictedDisp72', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'Result1', '1', 'Result8', '1', 'ResultBC 1', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display.SeriesLineThickness = ['arc_length', '2', 'dual11', '2', 'dual12', '2', 'dual21', '2', 'dual22', '2', 'dual31', '2', 'dual32', '2', 'dual41', '2', 'dual42', '2', 'dual51', '2', 'dual52', '2', 'dual61', '2', 'dual62', '2', 'dual71', '2', 'dual72', '2', 'elemDataMatch', '2', 'elemRegul', '2', 'gradient1', '2', 'gradient2', '2', 'gradient3', '2', 'gradient4', '2', 'gradient5', '2', 'gradient6', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'l2grad2', '2', 'measuredDisp11', '2', 'measuredDisp12', '2', 'measuredDisp21', '2', 'measuredDisp22', '2', 'measuredDisp31', '2', 'measuredDisp32', '2', 'measuredDisp41', '2', 'measuredDisp42', '2', 'measuredDisp51', '2', 'measuredDisp52', '2', 'measuredDisp61', '2', 'measuredDisp62', '2', 'measuredDisp71', '2', 'measuredDisp72', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'predictedDisp21', '2', 'predictedDisp22', '2', 'predictedDisp31', '2', 'predictedDisp32', '2', 'predictedDisp41', '2', 'predictedDisp42', '2', 'predictedDisp51', '2', 'predictedDisp52', '2', 'predictedDisp61', '2', 'predictedDisp62', '2', 'predictedDisp71', '2', 'predictedDisp72', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'Result1', '2', 'Result8', '2', 'ResultBC 1', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display.SeriesMarkerStyle = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result1', '0', 'Result8', '0', 'ResultBC 1', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# create a new 'Plot Over Line'
plotOverLine2 = PlotOverLine(Input=calculator16,
    Source='High Resolution Line Source')
# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine2.Source.Point1 = [x1, y1, 0.0]
plotOverLine2.Source.Point2 = [x2, y2, 0.0]
# show data in view
plotOverLine2Display = Show(plotOverLine2, lineChartView1)
# trace defaults for the display properties.
plotOverLine2Display.CompositeDataSetIndex = [0]
plotOverLine2Display.UseIndexForXAxis = 0
plotOverLine2Display.XArrayName = 'arc_length'
plotOverLine2Display.SeriesVisibility = ['ResultBC 2']
plotOverLine2Display.SeriesLabel = ['arc_length', 'arc_length', 'dual11', 'dual11', 'dual12', 'dual12', 'dual21', 'dual21', 'dual22', 'dual22', 'dual31', 'dual31', 'dual32', 'dual32', 'dual41', 'dual41', 'dual42', 'dual42', 'dual51', 'dual51', 'dual52', 'dual52', 'dual61', 'dual61', 'dual62', 'dual62', 'dual71', 'dual71', 'dual72', 'dual72', 'elemDataMatch', 'elemDataMatch', 'elemRegul', 'elemRegul', 'gradient1', 'gradient1', 'gradient2', 'gradient2', 'gradient3', 'gradient3', 'gradient4', 'gradient4', 'gradient5', 'gradient5', 'gradient6', 'gradient6', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'l2grad2', 'l2grad2', 'measuredDisp11', 'measuredDisp11', 'measuredDisp12', 'measuredDisp12', 'measuredDisp21', 'measuredDisp21', 'measuredDisp22', 'measuredDisp22', 'measuredDisp31', 'measuredDisp31', 'measuredDisp32', 'measuredDisp32', 'measuredDisp41', 'measuredDisp41', 'measuredDisp42', 'measuredDisp42', 'measuredDisp51', 'measuredDisp51', 'measuredDisp52', 'measuredDisp52', 'measuredDisp61', 'measuredDisp61', 'measuredDisp62', 'measuredDisp62', 'measuredDisp71', 'measuredDisp71', 'measuredDisp72', 'measuredDisp72', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'predictedDisp21', 'predictedDisp21', 'predictedDisp22', 'predictedDisp22', 'predictedDisp31', 'predictedDisp31', 'predictedDisp32', 'predictedDisp32', 'predictedDisp41', 'predictedDisp41', 'predictedDisp42', 'predictedDisp42', 'predictedDisp51', 'predictedDisp51', 'predictedDisp52', 'predictedDisp52', 'predictedDisp61', 'predictedDisp61', 'predictedDisp62', 'predictedDisp62', 'predictedDisp71', 'predictedDisp71', 'predictedDisp72', 'predictedDisp72', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'Result2', 'Result2', 'Result9', 'Result9', 'ResultBC 2', 'ResultBC 2', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'dual11', '0.89', '0.1', '0.11', 'dual12', '0.22', '0.49', '0.72', 'dual21', '0.3', '0.69', '0.29', 'dual22', '0.6', '0.31', '0.64', 'dual31', '1', '0.5', '0', 'dual32', '0.65', '0.34', '0.16', 'dual41', '0', '0', '0', 'dual42', '0.89', '0.1', '0.11', 'dual51', '0.22', '0.49', '0.72', 'dual52', '0.3', '0.69', '0.29', 'dual61', '0.6', '0.31', '0.64', 'dual62', '1', '0.5', '0', 'dual71', '0.65', '0.34', '0.16', 'dual72', '0', '0', '0', 'elemDataMatch', '0.89', '0.1', '0.11', 'elemRegul', '0.22', '0.49', '0.72', 'gradient1', '0.3', '0.69', '0.29', 'gradient2', '0.6', '0.31', '0.64', 'gradient3', '1', '0.5', '0', 'gradient4', '0.65', '0.34', '0.16', 'gradient5', '0', '0', '0', 'gradient6', '0.89', '0.1', '0.11', 'Gradients_X', '0.22', '0.49', '0.72', 'Gradients_Y', '0.3', '0.69', '0.29', 'Gradients_Z', '0.6', '0.31', '0.64', 'Gradients_Magnitude', '1', '0.5', '0', 'l2grad2', '0.65', '0.34', '0.16', 'measuredDisp11', '0', '0', '0', 'measuredDisp12', '0.89', '0.1', '0.11', 'measuredDisp21', '0.22', '0.49', '0.72', 'measuredDisp22', '0.3', '0.69', '0.29', 'measuredDisp31', '0.6', '0.31', '0.64', 'measuredDisp32', '1', '0.5', '0', 'measuredDisp41', '0.65', '0.34', '0.16', 'measuredDisp42', '0', '0', '0', 'measuredDisp51', '0.89', '0.1', '0.11', 'measuredDisp52', '0.22', '0.49', '0.72', 'measuredDisp61', '0.3', '0.69', '0.29', 'measuredDisp62', '0.6', '0.31', '0.64', 'measuredDisp71', '1', '0.5', '0', 'measuredDisp72', '0.65', '0.34', '0.16', 'NLP', '0', '0', '0', 'predictedDisp11', '0.89', '0.1', '0.11', 'predictedDisp12', '0.22', '0.49', '0.72', 'predictedDisp21', '0.3', '0.69', '0.29', 'predictedDisp22', '0.6', '0.31', '0.64', 'predictedDisp31', '1', '0.5', '0', 'predictedDisp32', '0.65', '0.34', '0.16', 'predictedDisp41', '0', '0', '0', 'predictedDisp42', '0.89', '0.1', '0.11', 'predictedDisp51', '0.22', '0.49', '0.72', 'predictedDisp52', '0.3', '0.69', '0.29', 'predictedDisp61', '0.6', '0.31', '0.64', 'predictedDisp62', '1', '0.5', '0', 'predictedDisp71', '0.65', '0.34', '0.16', 'predictedDisp72', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'Result2', '1', '0.5', '0', 'Result9', '0.65', '0.34', '0.16', 'ResultBC 2', '0', '0', '0', 'SM', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine2Display.SeriesPlotCorner = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result2', '0', 'Result9', '0', 'ResultBC 2', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine2Display.SeriesLabelPrefix = ''
plotOverLine2Display.SeriesLineStyle = ['arc_length', '1', 'dual11', '1', 'dual12', '1', 'dual21', '1', 'dual22', '1', 'dual31', '1', 'dual32', '1', 'dual41', '1', 'dual42', '1', 'dual51', '1', 'dual52', '1', 'dual61', '1', 'dual62', '1', 'dual71', '1', 'dual72', '1', 'elemDataMatch', '1', 'elemRegul', '1', 'gradient1', '1', 'gradient2', '1', 'gradient3', '1', 'gradient4', '1', 'gradient5', '1', 'gradient6', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'l2grad2', '1', 'measuredDisp11', '1', 'measuredDisp12', '1', 'measuredDisp21', '1', 'measuredDisp22', '1', 'measuredDisp31', '1', 'measuredDisp32', '1', 'measuredDisp41', '1', 'measuredDisp42', '1', 'measuredDisp51', '1', 'measuredDisp52', '1', 'measuredDisp61', '1', 'measuredDisp62', '1', 'measuredDisp71', '1', 'measuredDisp72', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'predictedDisp21', '1', 'predictedDisp22', '1', 'predictedDisp31', '1', 'predictedDisp32', '1', 'predictedDisp41', '1', 'predictedDisp42', '1', 'predictedDisp51', '1', 'predictedDisp52', '1', 'predictedDisp61', '1', 'predictedDisp62', '1', 'predictedDisp71', '1', 'predictedDisp72', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'Result2', '1', 'Result9', '1', 'ResultBC 2', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine2Display.SeriesLineThickness = ['arc_length', '2', 'dual11', '2', 'dual12', '2', 'dual21', '2', 'dual22', '2', 'dual31', '2', 'dual32', '2', 'dual41', '2', 'dual42', '2', 'dual51', '2', 'dual52', '2', 'dual61', '2', 'dual62', '2', 'dual71', '2', 'dual72', '2', 'elemDataMatch', '2', 'elemRegul', '2', 'gradient1', '2', 'gradient2', '2', 'gradient3', '2', 'gradient4', '2', 'gradient5', '2', 'gradient6', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'l2grad2', '2', 'measuredDisp11', '2', 'measuredDisp12', '2', 'measuredDisp21', '2', 'measuredDisp22', '2', 'measuredDisp31', '2', 'measuredDisp32', '2', 'measuredDisp41', '2', 'measuredDisp42', '2', 'measuredDisp51', '2', 'measuredDisp52', '2', 'measuredDisp61', '2', 'measuredDisp62', '2', 'measuredDisp71', '2', 'measuredDisp72', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'predictedDisp21', '2', 'predictedDisp22', '2', 'predictedDisp31', '2', 'predictedDisp32', '2', 'predictedDisp41', '2', 'predictedDisp42', '2', 'predictedDisp51', '2', 'predictedDisp52', '2', 'predictedDisp61', '2', 'predictedDisp62', '2', 'predictedDisp71', '2', 'predictedDisp72', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'Result2', '2', 'Result9', '2', 'ResultBC 2', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine2Display.SeriesMarkerStyle = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result2', '0', 'Result9', '0', 'ResultBC 2', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# create a new 'Plot Over Line'
plotOverLine3 = PlotOverLine(Input=calculator17,
    Source='High Resolution Line Source')
# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine3.Source.Point1 = [x1, y1, 0.0]
plotOverLine3.Source.Point2 = [x2, y2, 0.0]
# show data in view
plotOverLine3Display = Show(plotOverLine3, lineChartView1)
# trace defaults for the display properties.
plotOverLine3Display.CompositeDataSetIndex = [0]
plotOverLine3Display.UseIndexForXAxis = 0
plotOverLine3Display.XArrayName = 'arc_length'
plotOverLine3Display.SeriesVisibility = ['ResultBC 3']
plotOverLine3Display.SeriesLabel = ['arc_length', 'arc_length', 'dual11', 'dual11', 'dual12', 'dual12', 'dual21', 'dual21', 'dual22', 'dual22', 'dual31', 'dual31', 'dual32', 'dual32', 'dual41', 'dual41', 'dual42', 'dual42', 'dual51', 'dual51', 'dual52', 'dual52', 'dual61', 'dual61', 'dual62', 'dual62', 'dual71', 'dual71', 'dual72', 'dual72', 'elemDataMatch', 'elemDataMatch', 'elemRegul', 'elemRegul', 'gradient1', 'gradient1', 'gradient2', 'gradient2', 'gradient3', 'gradient3', 'gradient4', 'gradient4', 'gradient5', 'gradient5', 'gradient6', 'gradient6', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'l2grad2', 'l2grad2', 'measuredDisp11', 'measuredDisp11', 'measuredDisp12', 'measuredDisp12', 'measuredDisp21', 'measuredDisp21', 'measuredDisp22', 'measuredDisp22', 'measuredDisp31', 'measuredDisp31', 'measuredDisp32', 'measuredDisp32', 'measuredDisp41', 'measuredDisp41', 'measuredDisp42', 'measuredDisp42', 'measuredDisp51', 'measuredDisp51', 'measuredDisp52', 'measuredDisp52', 'measuredDisp61', 'measuredDisp61', 'measuredDisp62', 'measuredDisp62', 'measuredDisp71', 'measuredDisp71', 'measuredDisp72', 'measuredDisp72', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'predictedDisp21', 'predictedDisp21', 'predictedDisp22', 'predictedDisp22', 'predictedDisp31', 'predictedDisp31', 'predictedDisp32', 'predictedDisp32', 'predictedDisp41', 'predictedDisp41', 'predictedDisp42', 'predictedDisp42', 'predictedDisp51', 'predictedDisp51', 'predictedDisp52', 'predictedDisp52', 'predictedDisp61', 'predictedDisp61', 'predictedDisp62', 'predictedDisp62', 'predictedDisp71', 'predictedDisp71', 'predictedDisp72', 'predictedDisp72', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'Result3', 'Result3', 'Result10', 'Result10', 'ResultBC 3', 'ResultBC 3', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'dual11', '0.89', '0.1', '0.11', 'dual12', '0.22', '0.49', '0.72', 'dual21', '0.3', '0.69', '0.29', 'dual22', '0.6', '0.31', '0.64', 'dual31', '1', '0.5', '0', 'dual32', '0.65', '0.34', '0.16', 'dual41', '0', '0', '0', 'dual42', '0.89', '0.1', '0.11', 'dual51', '0.22', '0.49', '0.72', 'dual52', '0.3', '0.69', '0.29', 'dual61', '0.6', '0.31', '0.64', 'dual62', '1', '0.5', '0', 'dual71', '0.65', '0.34', '0.16', 'dual72', '0', '0', '0', 'elemDataMatch', '0.89', '0.1', '0.11', 'elemRegul', '0.22', '0.49', '0.72', 'gradient1', '0.3', '0.69', '0.29', 'gradient2', '0.6', '0.31', '0.64', 'gradient3', '1', '0.5', '0', 'gradient4', '0.65', '0.34', '0.16', 'gradient5', '0', '0', '0', 'gradient6', '0.89', '0.1', '0.11', 'Gradients_X', '0.22', '0.49', '0.72', 'Gradients_Y', '0.3', '0.69', '0.29', 'Gradients_Z', '0.6', '0.31', '0.64', 'Gradients_Magnitude', '1', '0.5', '0', 'l2grad2', '0.65', '0.34', '0.16', 'measuredDisp11', '0', '0', '0', 'measuredDisp12', '0.89', '0.1', '0.11', 'measuredDisp21', '0.22', '0.49', '0.72', 'measuredDisp22', '0.3', '0.69', '0.29', 'measuredDisp31', '0.6', '0.31', '0.64', 'measuredDisp32', '1', '0.5', '0', 'measuredDisp41', '0.65', '0.34', '0.16', 'measuredDisp42', '0', '0', '0', 'measuredDisp51', '0.89', '0.1', '0.11', 'measuredDisp52', '0.22', '0.49', '0.72', 'measuredDisp61', '0.3', '0.69', '0.29', 'measuredDisp62', '0.6', '0.31', '0.64', 'measuredDisp71', '1', '0.5', '0', 'measuredDisp72', '0.65', '0.34', '0.16', 'NLP', '0', '0', '0', 'predictedDisp11', '0.89', '0.1', '0.11', 'predictedDisp12', '0.22', '0.49', '0.72', 'predictedDisp21', '0.3', '0.69', '0.29', 'predictedDisp22', '0.6', '0.31', '0.64', 'predictedDisp31', '1', '0.5', '0', 'predictedDisp32', '0.65', '0.34', '0.16', 'predictedDisp41', '0', '0', '0', 'predictedDisp42', '0.89', '0.1', '0.11', 'predictedDisp51', '0.22', '0.49', '0.72', 'predictedDisp52', '0.3', '0.69', '0.29', 'predictedDisp61', '0.6', '0.31', '0.64', 'predictedDisp62', '1', '0.5', '0', 'predictedDisp71', '0.65', '0.34', '0.16', 'predictedDisp72', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'Result3', '1', '0.5', '0', 'Result10', '0.65', '0.34', '0.16', 'ResultBC 3', '0', '0', '0', 'SM', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine3Display.SeriesPlotCorner = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result3', '0', 'Result10', '0', 'ResultBC 3', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine3Display.SeriesLabelPrefix = ''
plotOverLine3Display.SeriesLineStyle = ['arc_length', '1', 'dual11', '1', 'dual12', '1', 'dual21', '1', 'dual22', '1', 'dual31', '1', 'dual32', '1', 'dual41', '1', 'dual42', '1', 'dual51', '1', 'dual52', '1', 'dual61', '1', 'dual62', '1', 'dual71', '1', 'dual72', '1', 'elemDataMatch', '1', 'elemRegul', '1', 'gradient1', '1', 'gradient2', '1', 'gradient3', '1', 'gradient4', '1', 'gradient5', '1', 'gradient6', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'l2grad2', '1', 'measuredDisp11', '1', 'measuredDisp12', '1', 'measuredDisp21', '1', 'measuredDisp22', '1', 'measuredDisp31', '1', 'measuredDisp32', '1', 'measuredDisp41', '1', 'measuredDisp42', '1', 'measuredDisp51', '1', 'measuredDisp52', '1', 'measuredDisp61', '1', 'measuredDisp62', '1', 'measuredDisp71', '1', 'measuredDisp72', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'predictedDisp21', '1', 'predictedDisp22', '1', 'predictedDisp31', '1', 'predictedDisp32', '1', 'predictedDisp41', '1', 'predictedDisp42', '1', 'predictedDisp51', '1', 'predictedDisp52', '1', 'predictedDisp61', '1', 'predictedDisp62', '1', 'predictedDisp71', '1', 'predictedDisp72', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'Result3', '1', 'Result10', '1', 'ResultBC 3', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine3Display.SeriesLineThickness = ['arc_length', '2', 'dual11', '2', 'dual12', '2', 'dual21', '2', 'dual22', '2', 'dual31', '2', 'dual32', '2', 'dual41', '2', 'dual42', '2', 'dual51', '2', 'dual52', '2', 'dual61', '2', 'dual62', '2', 'dual71', '2', 'dual72', '2', 'elemDataMatch', '2', 'elemRegul', '2', 'gradient1', '2', 'gradient2', '2', 'gradient3', '2', 'gradient4', '2', 'gradient5', '2', 'gradient6', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'l2grad2', '2', 'measuredDisp11', '2', 'measuredDisp12', '2', 'measuredDisp21', '2', 'measuredDisp22', '2', 'measuredDisp31', '2', 'measuredDisp32', '2', 'measuredDisp41', '2', 'measuredDisp42', '2', 'measuredDisp51', '2', 'measuredDisp52', '2', 'measuredDisp61', '2', 'measuredDisp62', '2', 'measuredDisp71', '2', 'measuredDisp72', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'predictedDisp21', '2', 'predictedDisp22', '2', 'predictedDisp31', '2', 'predictedDisp32', '2', 'predictedDisp41', '2', 'predictedDisp42', '2', 'predictedDisp51', '2', 'predictedDisp52', '2', 'predictedDisp61', '2', 'predictedDisp62', '2', 'predictedDisp71', '2', 'predictedDisp72', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'Result3', '2', 'Result10', '2', 'ResultBC 3', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine3Display.SeriesMarkerStyle = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result3', '0', 'Result10', '0', 'ResultBC 3', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# create a new 'Plot Over Line'
plotOverLine4 = PlotOverLine(Input=calculator18,
    Source='High Resolution Line Source')
# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine4.Source.Point1 = [x1, y1, 0.0]
plotOverLine4.Source.Point2 = [x2, y2, 0.0]
# show data in view
plotOverLine4Display = Show(plotOverLine4, lineChartView1)
# trace defaults for the display properties.
plotOverLine4Display.CompositeDataSetIndex = [0]
plotOverLine4Display.UseIndexForXAxis = 0
plotOverLine4Display.XArrayName = 'arc_length'
plotOverLine4Display.SeriesVisibility = ['ResultBC 4']
plotOverLine4Display.SeriesLabel = ['arc_length', 'arc_length', 'dual11', 'dual11', 'dual12', 'dual12', 'dual21', 'dual21', 'dual22', 'dual22', 'dual31', 'dual31', 'dual32', 'dual32', 'dual41', 'dual41', 'dual42', 'dual42', 'dual51', 'dual51', 'dual52', 'dual52', 'dual61', 'dual61', 'dual62', 'dual62', 'dual71', 'dual71', 'dual72', 'dual72', 'elemDataMatch', 'elemDataMatch', 'elemRegul', 'elemRegul', 'gradient1', 'gradient1', 'gradient2', 'gradient2', 'gradient3', 'gradient3', 'gradient4', 'gradient4', 'gradient5', 'gradient5', 'gradient6', 'gradient6', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'l2grad2', 'l2grad2', 'measuredDisp11', 'measuredDisp11', 'measuredDisp12', 'measuredDisp12', 'measuredDisp21', 'measuredDisp21', 'measuredDisp22', 'measuredDisp22', 'measuredDisp31', 'measuredDisp31', 'measuredDisp32', 'measuredDisp32', 'measuredDisp41', 'measuredDisp41', 'measuredDisp42', 'measuredDisp42', 'measuredDisp51', 'measuredDisp51', 'measuredDisp52', 'measuredDisp52', 'measuredDisp61', 'measuredDisp61', 'measuredDisp62', 'measuredDisp62', 'measuredDisp71', 'measuredDisp71', 'measuredDisp72', 'measuredDisp72', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'predictedDisp21', 'predictedDisp21', 'predictedDisp22', 'predictedDisp22', 'predictedDisp31', 'predictedDisp31', 'predictedDisp32', 'predictedDisp32', 'predictedDisp41', 'predictedDisp41', 'predictedDisp42', 'predictedDisp42', 'predictedDisp51', 'predictedDisp51', 'predictedDisp52', 'predictedDisp52', 'predictedDisp61', 'predictedDisp61', 'predictedDisp62', 'predictedDisp62', 'predictedDisp71', 'predictedDisp71', 'predictedDisp72', 'predictedDisp72', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'Result4', 'Result4', 'Result11', 'Result11', 'ResultBC 4', 'ResultBC 4', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine4Display.SeriesColor = ['arc_length', '0', '0', '0', 'dual11', '0.89', '0.1', '0.11', 'dual12', '0.22', '0.49', '0.72', 'dual21', '0.3', '0.69', '0.29', 'dual22', '0.6', '0.31', '0.64', 'dual31', '1', '0.5', '0', 'dual32', '0.65', '0.34', '0.16', 'dual41', '0', '0', '0', 'dual42', '0.89', '0.1', '0.11', 'dual51', '0.22', '0.49', '0.72', 'dual52', '0.3', '0.69', '0.29', 'dual61', '0.6', '0.31', '0.64', 'dual62', '1', '0.5', '0', 'dual71', '0.65', '0.34', '0.16', 'dual72', '0', '0', '0', 'elemDataMatch', '0.89', '0.1', '0.11', 'elemRegul', '0.22', '0.49', '0.72', 'gradient1', '0.3', '0.69', '0.29', 'gradient2', '0.6', '0.31', '0.64', 'gradient3', '1', '0.5', '0', 'gradient4', '0.65', '0.34', '0.16', 'gradient5', '0', '0', '0', 'gradient6', '0.89', '0.1', '0.11', 'Gradients_X', '0.22', '0.49', '0.72', 'Gradients_Y', '0.3', '0.69', '0.29', 'Gradients_Z', '0.6', '0.31', '0.64', 'Gradients_Magnitude', '1', '0.5', '0', 'l2grad2', '0.65', '0.34', '0.16', 'measuredDisp11', '0', '0', '0', 'measuredDisp12', '0.89', '0.1', '0.11', 'measuredDisp21', '0.22', '0.49', '0.72', 'measuredDisp22', '0.3', '0.69', '0.29', 'measuredDisp31', '0.6', '0.31', '0.64', 'measuredDisp32', '1', '0.5', '0', 'measuredDisp41', '0.65', '0.34', '0.16', 'measuredDisp42', '0', '0', '0', 'measuredDisp51', '0.89', '0.1', '0.11', 'measuredDisp52', '0.22', '0.49', '0.72', 'measuredDisp61', '0.3', '0.69', '0.29', 'measuredDisp62', '0.6', '0.31', '0.64', 'measuredDisp71', '1', '0.5', '0', 'measuredDisp72', '0.65', '0.34', '0.16', 'NLP', '0', '0', '0', 'predictedDisp11', '0.89', '0.1', '0.11', 'predictedDisp12', '0.22', '0.49', '0.72', 'predictedDisp21', '0.3', '0.69', '0.29', 'predictedDisp22', '0.6', '0.31', '0.64', 'predictedDisp31', '1', '0.5', '0', 'predictedDisp32', '0.65', '0.34', '0.16', 'predictedDisp41', '0', '0', '0', 'predictedDisp42', '0.89', '0.1', '0.11', 'predictedDisp51', '0.22', '0.49', '0.72', 'predictedDisp52', '0.3', '0.69', '0.29', 'predictedDisp61', '0.6', '0.31', '0.64', 'predictedDisp62', '1', '0.5', '0', 'predictedDisp71', '0.65', '0.34', '0.16', 'predictedDisp72', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'Result4', '1', '0.5', '0', 'Result11', '0.65', '0.34', '0.16', 'ResultBC 4', '0', '0', '0', 'SM', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine4Display.SeriesPlotCorner = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result4', '0', 'Result11', '0', 'ResultBC 4', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine4Display.SeriesLabelPrefix = ''
plotOverLine4Display.SeriesLineStyle = ['arc_length', '1', 'dual11', '1', 'dual12', '1', 'dual21', '1', 'dual22', '1', 'dual31', '1', 'dual32', '1', 'dual41', '1', 'dual42', '1', 'dual51', '1', 'dual52', '1', 'dual61', '1', 'dual62', '1', 'dual71', '1', 'dual72', '1', 'elemDataMatch', '1', 'elemRegul', '1', 'gradient1', '1', 'gradient2', '1', 'gradient3', '1', 'gradient4', '1', 'gradient5', '1', 'gradient6', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'l2grad2', '1', 'measuredDisp11', '1', 'measuredDisp12', '1', 'measuredDisp21', '1', 'measuredDisp22', '1', 'measuredDisp31', '1', 'measuredDisp32', '1', 'measuredDisp41', '1', 'measuredDisp42', '1', 'measuredDisp51', '1', 'measuredDisp52', '1', 'measuredDisp61', '1', 'measuredDisp62', '1', 'measuredDisp71', '1', 'measuredDisp72', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'predictedDisp21', '1', 'predictedDisp22', '1', 'predictedDisp31', '1', 'predictedDisp32', '1', 'predictedDisp41', '1', 'predictedDisp42', '1', 'predictedDisp51', '1', 'predictedDisp52', '1', 'predictedDisp61', '1', 'predictedDisp62', '1', 'predictedDisp71', '1', 'predictedDisp72', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'Result4', '1', 'Result11', '1', 'ResultBC 4', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine4Display.SeriesLineThickness = ['arc_length', '2', 'dual11', '2', 'dual12', '2', 'dual21', '2', 'dual22', '2', 'dual31', '2', 'dual32', '2', 'dual41', '2', 'dual42', '2', 'dual51', '2', 'dual52', '2', 'dual61', '2', 'dual62', '2', 'dual71', '2', 'dual72', '2', 'elemDataMatch', '2', 'elemRegul', '2', 'gradient1', '2', 'gradient2', '2', 'gradient3', '2', 'gradient4', '2', 'gradient5', '2', 'gradient6', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'l2grad2', '2', 'measuredDisp11', '2', 'measuredDisp12', '2', 'measuredDisp21', '2', 'measuredDisp22', '2', 'measuredDisp31', '2', 'measuredDisp32', '2', 'measuredDisp41', '2', 'measuredDisp42', '2', 'measuredDisp51', '2', 'measuredDisp52', '2', 'measuredDisp61', '2', 'measuredDisp62', '2', 'measuredDisp71', '2', 'measuredDisp72', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'predictedDisp21', '2', 'predictedDisp22', '2', 'predictedDisp31', '2', 'predictedDisp32', '2', 'predictedDisp41', '2', 'predictedDisp42', '2', 'predictedDisp51', '2', 'predictedDisp52', '2', 'predictedDisp61', '2', 'predictedDisp62', '2', 'predictedDisp71', '2', 'predictedDisp72', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'Result4', '2', 'Result11', '2', 'ResultBC 4', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine4Display.SeriesMarkerStyle = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result4', '0', 'Result11', '0', 'ResultBC 4', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# create a new 'Plot Over Line'
plotOverLine5 = PlotOverLine(Input=calculator19,
    Source='High Resolution Line Source')
# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine5.Source.Point1 = [x1, y1, 0.0]
plotOverLine5.Source.Point2 = [x2, y2, 0.0]
# show data in view
plotOverLine5Display = Show(plotOverLine5, lineChartView1)
# trace defaults for the display properties.
plotOverLine5Display.CompositeDataSetIndex = [0]
plotOverLine5Display.UseIndexForXAxis = 0
plotOverLine5Display.XArrayName = 'arc_length'
plotOverLine5Display.SeriesVisibility = ['ResultBC 5']
plotOverLine5Display.SeriesLabel = ['arc_length', 'arc_length', 'dual11', 'dual11', 'dual12', 'dual12', 'dual21', 'dual21', 'dual22', 'dual22', 'dual31', 'dual31', 'dual32', 'dual32', 'dual41', 'dual41', 'dual42', 'dual42', 'dual51', 'dual51', 'dual52', 'dual52', 'dual61', 'dual61', 'dual62', 'dual62', 'dual71', 'dual71', 'dual72', 'dual72', 'elemDataMatch', 'elemDataMatch', 'elemRegul', 'elemRegul', 'gradient1', 'gradient1', 'gradient2', 'gradient2', 'gradient3', 'gradient3', 'gradient4', 'gradient4', 'gradient5', 'gradient5', 'gradient6', 'gradient6', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'l2grad2', 'l2grad2', 'measuredDisp11', 'measuredDisp11', 'measuredDisp12', 'measuredDisp12', 'measuredDisp21', 'measuredDisp21', 'measuredDisp22', 'measuredDisp22', 'measuredDisp31', 'measuredDisp31', 'measuredDisp32', 'measuredDisp32', 'measuredDisp41', 'measuredDisp41', 'measuredDisp42', 'measuredDisp42', 'measuredDisp51', 'measuredDisp51', 'measuredDisp52', 'measuredDisp52', 'measuredDisp61', 'measuredDisp61', 'measuredDisp62', 'measuredDisp62', 'measuredDisp71', 'measuredDisp71', 'measuredDisp72', 'measuredDisp72', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'predictedDisp21', 'predictedDisp21', 'predictedDisp22', 'predictedDisp22', 'predictedDisp31', 'predictedDisp31', 'predictedDisp32', 'predictedDisp32', 'predictedDisp41', 'predictedDisp41', 'predictedDisp42', 'predictedDisp42', 'predictedDisp51', 'predictedDisp51', 'predictedDisp52', 'predictedDisp52', 'predictedDisp61', 'predictedDisp61', 'predictedDisp62', 'predictedDisp62', 'predictedDisp71', 'predictedDisp71', 'predictedDisp72', 'predictedDisp72', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'Result5', 'Result5', 'Result12', 'Result12', 'ResultBC 5', 'ResultBC 5', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine5Display.SeriesColor = ['arc_length', '0', '0', '0', 'dual11', '0.89', '0.1', '0.11', 'dual12', '0.22', '0.49', '0.72', 'dual21', '0.3', '0.69', '0.29', 'dual22', '0.6', '0.31', '0.64', 'dual31', '1', '0.5', '0', 'dual32', '0.65', '0.34', '0.16', 'dual41', '0', '0', '0', 'dual42', '0.89', '0.1', '0.11', 'dual51', '0.22', '0.49', '0.72', 'dual52', '0.3', '0.69', '0.29', 'dual61', '0.6', '0.31', '0.64', 'dual62', '1', '0.5', '0', 'dual71', '0.65', '0.34', '0.16', 'dual72', '0', '0', '0', 'elemDataMatch', '0.89', '0.1', '0.11', 'elemRegul', '0.22', '0.49', '0.72', 'gradient1', '0.3', '0.69', '0.29', 'gradient2', '0.6', '0.31', '0.64', 'gradient3', '1', '0.5', '0', 'gradient4', '0.65', '0.34', '0.16', 'gradient5', '0', '0', '0', 'gradient6', '0.89', '0.1', '0.11', 'Gradients_X', '0.22', '0.49', '0.72', 'Gradients_Y', '0.3', '0.69', '0.29', 'Gradients_Z', '0.6', '0.31', '0.64', 'Gradients_Magnitude', '1', '0.5', '0', 'l2grad2', '0.65', '0.34', '0.16', 'measuredDisp11', '0', '0', '0', 'measuredDisp12', '0.89', '0.1', '0.11', 'measuredDisp21', '0.22', '0.49', '0.72', 'measuredDisp22', '0.3', '0.69', '0.29', 'measuredDisp31', '0.6', '0.31', '0.64', 'measuredDisp32', '1', '0.5', '0', 'measuredDisp41', '0.65', '0.34', '0.16', 'measuredDisp42', '0', '0', '0', 'measuredDisp51', '0.89', '0.1', '0.11', 'measuredDisp52', '0.22', '0.49', '0.72', 'measuredDisp61', '0.3', '0.69', '0.29', 'measuredDisp62', '0.6', '0.31', '0.64', 'measuredDisp71', '1', '0.5', '0', 'measuredDisp72', '0.65', '0.34', '0.16', 'NLP', '0', '0', '0', 'predictedDisp11', '0.89', '0.1', '0.11', 'predictedDisp12', '0.22', '0.49', '0.72', 'predictedDisp21', '0.3', '0.69', '0.29', 'predictedDisp22', '0.6', '0.31', '0.64', 'predictedDisp31', '1', '0.5', '0', 'predictedDisp32', '0.65', '0.34', '0.16', 'predictedDisp41', '0', '0', '0', 'predictedDisp42', '0.89', '0.1', '0.11', 'predictedDisp51', '0.22', '0.49', '0.72', 'predictedDisp52', '0.3', '0.69', '0.29', 'predictedDisp61', '0.6', '0.31', '0.64', 'predictedDisp62', '1', '0.5', '0', 'predictedDisp71', '0.65', '0.34', '0.16', 'predictedDisp72', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'Result5', '1', '0.5', '0', 'Result12', '0.65', '0.34', '0.16', 'ResultBC 5', '0', '0', '0', 'SM', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine5Display.SeriesPlotCorner = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result5', '0', 'Result12', '0', 'ResultBC 5', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine5Display.SeriesLabelPrefix = ''
plotOverLine5Display.SeriesLineStyle = ['arc_length', '1', 'dual11', '1', 'dual12', '1', 'dual21', '1', 'dual22', '1', 'dual31', '1', 'dual32', '1', 'dual41', '1', 'dual42', '1', 'dual51', '1', 'dual52', '1', 'dual61', '1', 'dual62', '1', 'dual71', '1', 'dual72', '1', 'elemDataMatch', '1', 'elemRegul', '1', 'gradient1', '1', 'gradient2', '1', 'gradient3', '1', 'gradient4', '1', 'gradient5', '1', 'gradient6', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'l2grad2', '1', 'measuredDisp11', '1', 'measuredDisp12', '1', 'measuredDisp21', '1', 'measuredDisp22', '1', 'measuredDisp31', '1', 'measuredDisp32', '1', 'measuredDisp41', '1', 'measuredDisp42', '1', 'measuredDisp51', '1', 'measuredDisp52', '1', 'measuredDisp61', '1', 'measuredDisp62', '1', 'measuredDisp71', '1', 'measuredDisp72', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'predictedDisp21', '1', 'predictedDisp22', '1', 'predictedDisp31', '1', 'predictedDisp32', '1', 'predictedDisp41', '1', 'predictedDisp42', '1', 'predictedDisp51', '1', 'predictedDisp52', '1', 'predictedDisp61', '1', 'predictedDisp62', '1', 'predictedDisp71', '1', 'predictedDisp72', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'Result5', '1', 'Result12', '1', 'ResultBC 5', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine5Display.SeriesLineThickness = ['arc_length', '2', 'dual11', '2', 'dual12', '2', 'dual21', '2', 'dual22', '2', 'dual31', '2', 'dual32', '2', 'dual41', '2', 'dual42', '2', 'dual51', '2', 'dual52', '2', 'dual61', '2', 'dual62', '2', 'dual71', '2', 'dual72', '2', 'elemDataMatch', '2', 'elemRegul', '2', 'gradient1', '2', 'gradient2', '2', 'gradient3', '2', 'gradient4', '2', 'gradient5', '2', 'gradient6', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'l2grad2', '2', 'measuredDisp11', '2', 'measuredDisp12', '2', 'measuredDisp21', '2', 'measuredDisp22', '2', 'measuredDisp31', '2', 'measuredDisp32', '2', 'measuredDisp41', '2', 'measuredDisp42', '2', 'measuredDisp51', '2', 'measuredDisp52', '2', 'measuredDisp61', '2', 'measuredDisp62', '2', 'measuredDisp71', '2', 'measuredDisp72', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'predictedDisp21', '2', 'predictedDisp22', '2', 'predictedDisp31', '2', 'predictedDisp32', '2', 'predictedDisp41', '2', 'predictedDisp42', '2', 'predictedDisp51', '2', 'predictedDisp52', '2', 'predictedDisp61', '2', 'predictedDisp62', '2', 'predictedDisp71', '2', 'predictedDisp72', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'Result5', '2', 'Result12', '2', 'ResultBC 5', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine5Display.SeriesMarkerStyle = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result5', '0', 'Result12', '0', 'ResultBC 5', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# create a new 'Plot Over Line'
plotOverLine6 = PlotOverLine(Input=calculator20,
    Source='High Resolution Line Source')
# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine6.Source.Point1 = [x1, y1, 0.0]
plotOverLine6.Source.Point2 = [x2, y2, 0.0]
# show data in view
plotOverLine6Display = Show(plotOverLine6, lineChartView1)
# trace defaults for the display properties.
plotOverLine6Display.CompositeDataSetIndex = [0]
plotOverLine6Display.UseIndexForXAxis = 0
plotOverLine6Display.XArrayName = 'arc_length'
plotOverLine6Display.SeriesVisibility = ['ResultBC 6']
plotOverLine6Display.SeriesLabel = ['arc_length', 'arc_length', 'dual11', 'dual11', 'dual12', 'dual12', 'dual21', 'dual21', 'dual22', 'dual22', 'dual31', 'dual31', 'dual32', 'dual32', 'dual41', 'dual41', 'dual42', 'dual42', 'dual51', 'dual51', 'dual52', 'dual52', 'dual61', 'dual61', 'dual62', 'dual62', 'dual71', 'dual71', 'dual72', 'dual72', 'elemDataMatch', 'elemDataMatch', 'elemRegul', 'elemRegul', 'gradient1', 'gradient1', 'gradient2', 'gradient2', 'gradient3', 'gradient3', 'gradient4', 'gradient4', 'gradient5', 'gradient5', 'gradient6', 'gradient6', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'l2grad2', 'l2grad2', 'measuredDisp11', 'measuredDisp11', 'measuredDisp12', 'measuredDisp12', 'measuredDisp21', 'measuredDisp21', 'measuredDisp22', 'measuredDisp22', 'measuredDisp31', 'measuredDisp31', 'measuredDisp32', 'measuredDisp32', 'measuredDisp41', 'measuredDisp41', 'measuredDisp42', 'measuredDisp42', 'measuredDisp51', 'measuredDisp51', 'measuredDisp52', 'measuredDisp52', 'measuredDisp61', 'measuredDisp61', 'measuredDisp62', 'measuredDisp62', 'measuredDisp71', 'measuredDisp71', 'measuredDisp72', 'measuredDisp72', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'predictedDisp21', 'predictedDisp21', 'predictedDisp22', 'predictedDisp22', 'predictedDisp31', 'predictedDisp31', 'predictedDisp32', 'predictedDisp32', 'predictedDisp41', 'predictedDisp41', 'predictedDisp42', 'predictedDisp42', 'predictedDisp51', 'predictedDisp51', 'predictedDisp52', 'predictedDisp52', 'predictedDisp61', 'predictedDisp61', 'predictedDisp62', 'predictedDisp62', 'predictedDisp71', 'predictedDisp71', 'predictedDisp72', 'predictedDisp72', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'Result6', 'Result6', 'Result13', 'Result13', 'ResultBC 6', 'ResultBC 6', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine6Display.SeriesColor = ['arc_length', '0', '0', '0', 'dual11', '0.89', '0.1', '0.11', 'dual12', '0.22', '0.49', '0.72', 'dual21', '0.3', '0.69', '0.29', 'dual22', '0.6', '0.31', '0.64', 'dual31', '1', '0.5', '0', 'dual32', '0.65', '0.34', '0.16', 'dual41', '0', '0', '0', 'dual42', '0.89', '0.1', '0.11', 'dual51', '0.22', '0.49', '0.72', 'dual52', '0.3', '0.69', '0.29', 'dual61', '0.6', '0.31', '0.64', 'dual62', '1', '0.5', '0', 'dual71', '0.65', '0.34', '0.16', 'dual72', '0', '0', '0', 'elemDataMatch', '0.89', '0.1', '0.11', 'elemRegul', '0.22', '0.49', '0.72', 'gradient1', '0.3', '0.69', '0.29', 'gradient2', '0.6', '0.31', '0.64', 'gradient3', '1', '0.5', '0', 'gradient4', '0.65', '0.34', '0.16', 'gradient5', '0', '0', '0', 'gradient6', '0.89', '0.1', '0.11', 'Gradients_X', '0.22', '0.49', '0.72', 'Gradients_Y', '0.3', '0.69', '0.29', 'Gradients_Z', '0.6', '0.31', '0.64', 'Gradients_Magnitude', '1', '0.5', '0', 'l2grad2', '0.65', '0.34', '0.16', 'measuredDisp11', '0', '0', '0', 'measuredDisp12', '0.89', '0.1', '0.11', 'measuredDisp21', '0.22', '0.49', '0.72', 'measuredDisp22', '0.3', '0.69', '0.29', 'measuredDisp31', '0.6', '0.31', '0.64', 'measuredDisp32', '1', '0.5', '0', 'measuredDisp41', '0.65', '0.34', '0.16', 'measuredDisp42', '0', '0', '0', 'measuredDisp51', '0.89', '0.1', '0.11', 'measuredDisp52', '0.22', '0.49', '0.72', 'measuredDisp61', '0.3', '0.69', '0.29', 'measuredDisp62', '0.6', '0.31', '0.64', 'measuredDisp71', '1', '0.5', '0', 'measuredDisp72', '0.65', '0.34', '0.16', 'NLP', '0', '0', '0', 'predictedDisp11', '0.89', '0.1', '0.11', 'predictedDisp12', '0.22', '0.49', '0.72', 'predictedDisp21', '0.3', '0.69', '0.29', 'predictedDisp22', '0.6', '0.31', '0.64', 'predictedDisp31', '1', '0.5', '0', 'predictedDisp32', '0.65', '0.34', '0.16', 'predictedDisp41', '0', '0', '0', 'predictedDisp42', '0.89', '0.1', '0.11', 'predictedDisp51', '0.22', '0.49', '0.72', 'predictedDisp52', '0.3', '0.69', '0.29', 'predictedDisp61', '0.6', '0.31', '0.64', 'predictedDisp62', '1', '0.5', '0', 'predictedDisp71', '0.65', '0.34', '0.16', 'predictedDisp72', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'Result6', '1', '0.5', '0', 'Result13', '0.65', '0.34', '0.16', 'ResultBC 6', '0', '0', '0', 'SM', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine6Display.SeriesPlotCorner = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result6', '0', 'Result13', '0', 'ResultBC 6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine6Display.SeriesLabelPrefix = ''
plotOverLine6Display.SeriesLineStyle = ['arc_length', '1', 'dual11', '1', 'dual12', '1', 'dual21', '1', 'dual22', '1', 'dual31', '1', 'dual32', '1', 'dual41', '1', 'dual42', '1', 'dual51', '1', 'dual52', '1', 'dual61', '1', 'dual62', '1', 'dual71', '1', 'dual72', '1', 'elemDataMatch', '1', 'elemRegul', '1', 'gradient1', '1', 'gradient2', '1', 'gradient3', '1', 'gradient4', '1', 'gradient5', '1', 'gradient6', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'l2grad2', '1', 'measuredDisp11', '1', 'measuredDisp12', '1', 'measuredDisp21', '1', 'measuredDisp22', '1', 'measuredDisp31', '1', 'measuredDisp32', '1', 'measuredDisp41', '1', 'measuredDisp42', '1', 'measuredDisp51', '1', 'measuredDisp52', '1', 'measuredDisp61', '1', 'measuredDisp62', '1', 'measuredDisp71', '1', 'measuredDisp72', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'predictedDisp21', '1', 'predictedDisp22', '1', 'predictedDisp31', '1', 'predictedDisp32', '1', 'predictedDisp41', '1', 'predictedDisp42', '1', 'predictedDisp51', '1', 'predictedDisp52', '1', 'predictedDisp61', '1', 'predictedDisp62', '1', 'predictedDisp71', '1', 'predictedDisp72', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'Result6', '1', 'Result13', '1', 'ResultBC 6', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine6Display.SeriesLineThickness = ['arc_length', '2', 'dual11', '2', 'dual12', '2', 'dual21', '2', 'dual22', '2', 'dual31', '2', 'dual32', '2', 'dual41', '2', 'dual42', '2', 'dual51', '2', 'dual52', '2', 'dual61', '2', 'dual62', '2', 'dual71', '2', 'dual72', '2', 'elemDataMatch', '2', 'elemRegul', '2', 'gradient1', '2', 'gradient2', '2', 'gradient3', '2', 'gradient4', '2', 'gradient5', '2', 'gradient6', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'l2grad2', '2', 'measuredDisp11', '2', 'measuredDisp12', '2', 'measuredDisp21', '2', 'measuredDisp22', '2', 'measuredDisp31', '2', 'measuredDisp32', '2', 'measuredDisp41', '2', 'measuredDisp42', '2', 'measuredDisp51', '2', 'measuredDisp52', '2', 'measuredDisp61', '2', 'measuredDisp62', '2', 'measuredDisp71', '2', 'measuredDisp72', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'predictedDisp21', '2', 'predictedDisp22', '2', 'predictedDisp31', '2', 'predictedDisp32', '2', 'predictedDisp41', '2', 'predictedDisp42', '2', 'predictedDisp51', '2', 'predictedDisp52', '2', 'predictedDisp61', '2', 'predictedDisp62', '2', 'predictedDisp71', '2', 'predictedDisp72', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'Result6', '2', 'Result13', '2', 'ResultBC 6', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine6Display.SeriesMarkerStyle = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result6', '0', 'Result13', '0', 'ResultBC 6', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# create a new 'Plot Over Line'
plotOverLine7 = PlotOverLine(Input=calculator21,
    Source='High Resolution Line Source')
# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine7.Source.Point1 = [x1, y1, 0.0]
plotOverLine7.Source.Point2 = [x2, y2, 0.0]
# show data in view
plotOverLine7Display = Show(plotOverLine7, lineChartView1)
# trace defaults for the display properties.
plotOverLine7Display.CompositeDataSetIndex = [0]
plotOverLine7Display.UseIndexForXAxis = 0
plotOverLine7Display.XArrayName = 'arc_length'
plotOverLine7Display.SeriesVisibility = ['ResultBC 7']
plotOverLine7Display.SeriesLabel = ['arc_length', 'arc_length', 'dual11', 'dual11', 'dual12', 'dual12', 'dual21', 'dual21', 'dual22', 'dual22', 'dual31', 'dual31', 'dual32', 'dual32', 'dual41', 'dual41', 'dual42', 'dual42', 'dual51', 'dual51', 'dual52', 'dual52', 'dual61', 'dual61', 'dual62', 'dual62', 'dual71', 'dual71', 'dual72', 'dual72', 'elemDataMatch', 'elemDataMatch', 'elemRegul', 'elemRegul', 'gradient1', 'gradient1', 'gradient2', 'gradient2', 'gradient3', 'gradient3', 'gradient4', 'gradient4', 'gradient5', 'gradient5', 'gradient6', 'gradient6', 'Gradients_X', 'Gradients_X', 'Gradients_Y', 'Gradients_Y', 'Gradients_Z', 'Gradients_Z', 'Gradients_Magnitude', 'Gradients_Magnitude', 'l2grad2', 'l2grad2', 'measuredDisp11', 'measuredDisp11', 'measuredDisp12', 'measuredDisp12', 'measuredDisp21', 'measuredDisp21', 'measuredDisp22', 'measuredDisp22', 'measuredDisp31', 'measuredDisp31', 'measuredDisp32', 'measuredDisp32', 'measuredDisp41', 'measuredDisp41', 'measuredDisp42', 'measuredDisp42', 'measuredDisp51', 'measuredDisp51', 'measuredDisp52', 'measuredDisp52', 'measuredDisp61', 'measuredDisp61', 'measuredDisp62', 'measuredDisp62', 'measuredDisp71', 'measuredDisp71', 'measuredDisp72', 'measuredDisp72', 'NLP', 'NLP', 'predictedDisp11', 'predictedDisp11', 'predictedDisp12', 'predictedDisp12', 'predictedDisp21', 'predictedDisp21', 'predictedDisp22', 'predictedDisp22', 'predictedDisp31', 'predictedDisp31', 'predictedDisp32', 'predictedDisp32', 'predictedDisp41', 'predictedDisp41', 'predictedDisp42', 'predictedDisp42', 'predictedDisp51', 'predictedDisp51', 'predictedDisp52', 'predictedDisp52', 'predictedDisp61', 'predictedDisp61', 'predictedDisp62', 'predictedDisp62', 'predictedDisp71', 'predictedDisp71', 'predictedDisp72', 'predictedDisp72', 'property3', 'property3', 'property4', 'property4', 'property5', 'property5', 'property6', 'property6', 'Result7', 'Result7', 'Result14', 'Result14', 'ResultBC 7', 'ResultBC 7', 'SM', 'SM', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine7Display.SeriesColor = ['arc_length', '0', '0', '0', 'dual11', '0.89', '0.1', '0.11', 'dual12', '0.22', '0.49', '0.72', 'dual21', '0.3', '0.69', '0.29', 'dual22', '0.6', '0.31', '0.64', 'dual31', '1', '0.5', '0', 'dual32', '0.65', '0.34', '0.16', 'dual41', '0', '0', '0', 'dual42', '0.89', '0.1', '0.11', 'dual51', '0.22', '0.49', '0.72', 'dual52', '0.3', '0.69', '0.29', 'dual61', '0.6', '0.31', '0.64', 'dual62', '1', '0.5', '0', 'dual71', '0.65', '0.34', '0.16', 'dual72', '0', '0', '0', 'elemDataMatch', '0.89', '0.1', '0.11', 'elemRegul', '0.22', '0.49', '0.72', 'gradient1', '0.3', '0.69', '0.29', 'gradient2', '0.6', '0.31', '0.64', 'gradient3', '1', '0.5', '0', 'gradient4', '0.65', '0.34', '0.16', 'gradient5', '0', '0', '0', 'gradient6', '0.89', '0.1', '0.11', 'Gradients_X', '0.22', '0.49', '0.72', 'Gradients_Y', '0.3', '0.69', '0.29', 'Gradients_Z', '0.6', '0.31', '0.64', 'Gradients_Magnitude', '1', '0.5', '0', 'l2grad2', '0.65', '0.34', '0.16', 'measuredDisp11', '0', '0', '0', 'measuredDisp12', '0.89', '0.1', '0.11', 'measuredDisp21', '0.22', '0.49', '0.72', 'measuredDisp22', '0.3', '0.69', '0.29', 'measuredDisp31', '0.6', '0.31', '0.64', 'measuredDisp32', '1', '0.5', '0', 'measuredDisp41', '0.65', '0.34', '0.16', 'measuredDisp42', '0', '0', '0', 'measuredDisp51', '0.89', '0.1', '0.11', 'measuredDisp52', '0.22', '0.49', '0.72', 'measuredDisp61', '0.3', '0.69', '0.29', 'measuredDisp62', '0.6', '0.31', '0.64', 'measuredDisp71', '1', '0.5', '0', 'measuredDisp72', '0.65', '0.34', '0.16', 'NLP', '0', '0', '0', 'predictedDisp11', '0.89', '0.1', '0.11', 'predictedDisp12', '0.22', '0.49', '0.72', 'predictedDisp21', '0.3', '0.69', '0.29', 'predictedDisp22', '0.6', '0.31', '0.64', 'predictedDisp31', '1', '0.5', '0', 'predictedDisp32', '0.65', '0.34', '0.16', 'predictedDisp41', '0', '0', '0', 'predictedDisp42', '0.89', '0.1', '0.11', 'predictedDisp51', '0.22', '0.49', '0.72', 'predictedDisp52', '0.3', '0.69', '0.29', 'predictedDisp61', '0.6', '0.31', '0.64', 'predictedDisp62', '1', '0.5', '0', 'predictedDisp71', '0.65', '0.34', '0.16', 'predictedDisp72', '0', '0', '0', 'property3', '0.89', '0.1', '0.11', 'property4', '0.22', '0.49', '0.72', 'property5', '0.3', '0.69', '0.29', 'property6', '0.6', '0.31', '0.64', 'Result7', '1', '0.5', '0', 'Result14', '0.65', '0.34', '0.16', 'ResultBC 7', '0', '0', '0', 'SM', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine7Display.SeriesPlotCorner = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result7', '0', 'Result14', '0', 'ResultBC 7', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine7Display.SeriesLabelPrefix = ''
plotOverLine7Display.SeriesLineStyle = ['arc_length', '1', 'dual11', '1', 'dual12', '1', 'dual21', '1', 'dual22', '1', 'dual31', '1', 'dual32', '1', 'dual41', '1', 'dual42', '1', 'dual51', '1', 'dual52', '1', 'dual61', '1', 'dual62', '1', 'dual71', '1', 'dual72', '1', 'elemDataMatch', '1', 'elemRegul', '1', 'gradient1', '1', 'gradient2', '1', 'gradient3', '1', 'gradient4', '1', 'gradient5', '1', 'gradient6', '1', 'Gradients_X', '1', 'Gradients_Y', '1', 'Gradients_Z', '1', 'Gradients_Magnitude', '1', 'l2grad2', '1', 'measuredDisp11', '1', 'measuredDisp12', '1', 'measuredDisp21', '1', 'measuredDisp22', '1', 'measuredDisp31', '1', 'measuredDisp32', '1', 'measuredDisp41', '1', 'measuredDisp42', '1', 'measuredDisp51', '1', 'measuredDisp52', '1', 'measuredDisp61', '1', 'measuredDisp62', '1', 'measuredDisp71', '1', 'measuredDisp72', '1', 'NLP', '1', 'predictedDisp11', '1', 'predictedDisp12', '1', 'predictedDisp21', '1', 'predictedDisp22', '1', 'predictedDisp31', '1', 'predictedDisp32', '1', 'predictedDisp41', '1', 'predictedDisp42', '1', 'predictedDisp51', '1', 'predictedDisp52', '1', 'predictedDisp61', '1', 'predictedDisp62', '1', 'predictedDisp71', '1', 'predictedDisp72', '1', 'property3', '1', 'property4', '1', 'property5', '1', 'property6', '1', 'Result7', '1', 'Result14', '1', 'ResultBC 7', '1', 'SM', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine7Display.SeriesLineThickness = ['arc_length', '2', 'dual11', '2', 'dual12', '2', 'dual21', '2', 'dual22', '2', 'dual31', '2', 'dual32', '2', 'dual41', '2', 'dual42', '2', 'dual51', '2', 'dual52', '2', 'dual61', '2', 'dual62', '2', 'dual71', '2', 'dual72', '2', 'elemDataMatch', '2', 'elemRegul', '2', 'gradient1', '2', 'gradient2', '2', 'gradient3', '2', 'gradient4', '2', 'gradient5', '2', 'gradient6', '2', 'Gradients_X', '2', 'Gradients_Y', '2', 'Gradients_Z', '2', 'Gradients_Magnitude', '2', 'l2grad2', '2', 'measuredDisp11', '2', 'measuredDisp12', '2', 'measuredDisp21', '2', 'measuredDisp22', '2', 'measuredDisp31', '2', 'measuredDisp32', '2', 'measuredDisp41', '2', 'measuredDisp42', '2', 'measuredDisp51', '2', 'measuredDisp52', '2', 'measuredDisp61', '2', 'measuredDisp62', '2', 'measuredDisp71', '2', 'measuredDisp72', '2', 'NLP', '2', 'predictedDisp11', '2', 'predictedDisp12', '2', 'predictedDisp21', '2', 'predictedDisp22', '2', 'predictedDisp31', '2', 'predictedDisp32', '2', 'predictedDisp41', '2', 'predictedDisp42', '2', 'predictedDisp51', '2', 'predictedDisp52', '2', 'predictedDisp61', '2', 'predictedDisp62', '2', 'predictedDisp71', '2', 'predictedDisp72', '2', 'property3', '2', 'property4', '2', 'property5', '2', 'property6', '2', 'Result7', '2', 'Result14', '2', 'ResultBC 7', '2', 'SM', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine7Display.SeriesMarkerStyle = ['arc_length', '0', 'dual11', '0', 'dual12', '0', 'dual21', '0', 'dual22', '0', 'dual31', '0', 'dual32', '0', 'dual41', '0', 'dual42', '0', 'dual51', '0', 'dual52', '0', 'dual61', '0', 'dual62', '0', 'dual71', '0', 'dual72', '0', 'elemDataMatch', '0', 'elemRegul', '0', 'gradient1', '0', 'gradient2', '0', 'gradient3', '0', 'gradient4', '0', 'gradient5', '0', 'gradient6', '0', 'Gradients_X', '0', 'Gradients_Y', '0', 'Gradients_Z', '0', 'Gradients_Magnitude', '0', 'l2grad2', '0', 'measuredDisp11', '0', 'measuredDisp12', '0', 'measuredDisp21', '0', 'measuredDisp22', '0', 'measuredDisp31', '0', 'measuredDisp32', '0', 'measuredDisp41', '0', 'measuredDisp42', '0', 'measuredDisp51', '0', 'measuredDisp52', '0', 'measuredDisp61', '0', 'measuredDisp62', '0', 'measuredDisp71', '0', 'measuredDisp72', '0', 'NLP', '0', 'predictedDisp11', '0', 'predictedDisp12', '0', 'predictedDisp21', '0', 'predictedDisp22', '0', 'predictedDisp31', '0', 'predictedDisp32', '0', 'predictedDisp41', '0', 'predictedDisp42', '0', 'predictedDisp51', '0', 'predictedDisp52', '0', 'predictedDisp61', '0', 'predictedDisp62', '0', 'predictedDisp71', '0', 'predictedDisp72', '0', 'property3', '0', 'property4', '0', 'property5', '0', 'property6', '0', 'Result7', '0', 'Result14', '0', 'ResultBC 7', '0', 'SM', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']


# hide data in view
Hide(plotOverLine1, lineChartView1)
# hide data in view
Hide(plotOverLine2, lineChartView1)
# hide data in view
Hide(plotOverLine3, lineChartView1)
# hide data in view
Hide(plotOverLine4, lineChartView1)
# hide data in view
Hide(plotOverLine5, lineChartView1)
# hide data in view
Hide(plotOverLine6, lineChartView1)
# hide data in view
Hide(plotOverLine7, lineChartView1)




