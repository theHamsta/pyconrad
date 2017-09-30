import os
import pyconrad
import warnings

def generate_autocomplete_file(file, conrad_dir:str):

    dir_list = [ conrad_dir ]
    with open(file, 'w') as writer:
        zero_indentation = conrad_dir.count('/') + 1
        writer.writelines('import pyconrad\r\n')

        while len(dir_list) > 0:
            f = dir_list.pop()
            indentation = f.count('/') - zero_indentation + 1
            if os.path.isdir(f):
                writer.writelines('\t' * indentation + 'class ' + os.path.basename(f) + ':\r\n')
                for item in os.listdir(f):
                    dir_list.append(os.path.join(f,item))
            if os.path.isfile(f):
                filename, extension = os.path.splitext(os.path.basename(f))
                if extension == '.java' and filename != 'package-info':
                    writer.writelines('\t' * indentation + filename + ' = None\r\n')


if __name__ == '__main__':

    generate_autocomplete_file('/home/stephan/foo.py', '/home/stephan/projects/CONRAD/src')
    print(open('/home/stephan/foo.py','r').read())


class AutoCompleteConrad(pyconrad.ClassGetter):
    def __init__(self):
        warnings.warn('This class should never be initialized! Use it as type hint: #type: pyconrad.AutoCompleteConrad')

    Anisotropic_Filtering = None
    HandleExtraFileTypes = None
    Load_Recent = None
    Replace_Intensity_Value_Tool = None
    Copy_Convolution = None
    Dennerlein_Reader = None
    MKT_Reader = None
    Convert_to_16_bit = None
    Normalize_Image_CutOff = None
    Visualize_Ramp_Filter = None
    OpenCL_Forward_Projector = None
    Measure_All_Slices = None
    OpenCL_Forward_Projector_With_Motion = None
    Normalize_Image = None
    Measure_Slanted_Edge = None
    Nrrd_Writer = None
    Generate_Spectrum = None
    OpenCL_Volume_Renderer = None
    Generate_Beam_Hardening_Lookup_Table = None
    Generate_Photon_Mass_Attenuation_Plot = None
    ZIP_Reader = None
    class edu:
        class stanford:
            class rsl:
                class tutorial:
                    class parallel:
                        ParallelProjector2D = None
                        ParallelOnlineReconstructionExample = None
                        ParallelReconExample = None
                        ParallelOnlineBackprojectionExample = None
                        ParallelMedianReconExample = None
                        ParallelProjectionExample = None
                        ParallelBackprojector2D = None
                    DisplayUniformCircle = None
                    class fan:
                        FanBeamComparisonToCONRAD = None
                        class redundancy:
                            BinaryWeights_Normal = None
                            SilverWeights = None
                            BinaryWeights = None
                            CompensationWeights = None
                            BinaryWeights_erodeByOne = None
                            FanBeamWeightingComparison = None
                            ParkerWeights = None
                        FanBeamBackprojector2D = None
                        CosineFilter = None
                        FanBeamReconstructionExample = None
                        FanBeamProjector2D = None
                        RbRFanBeamReconstructionExample = None
                        class dynamicCollimation:
                            copyRedundantData = None
                    class test:
                        VolumeCenteringTest = None
                        CharacterEncodingTest = None
                        MaxThreadsTest = None
                    class scalespace:
                        ScaleSpaceStudies = None
                    class mammography:
                        class inbreast:
                            XMLparser = None
                            ReadMammograms = None
                        Mammogram = None
                    class ecc:
                        EpipolarConsistency = None
                        EpipolarConsistencyExample = None
                    class modelObserver:
                        TestModelGenerator = None
                        ImageHelper = None
                        ROC = None
                        Channels = None
                        Observer = None
                        ObserverPipeline = None
                        CreateImages = None
                        ModelDemo = None
                    class iterative:
                        GridOp = None
                        SartCPU = None
                        SartCL2D = None
                        Sart = None
                        IterativeReconstructionTest = None
                        SartCL = None
                        GDTest = None
                        Etv = None
                    class motion:
                        class estimation:
                            ThinPlateSplineInterpolation = None
                            RadialBasisFunctionInterpolation = None
                            SmoothKernel1D = None
                            EstimateCubic2DSpline = None
                            RunMotionEstimation = None
                            ProjectionLoader = None
                            EstimateBSplineSurface = None
                            CylinderVolumeMask = None
                            OptimizeMotionField = None
                            SobelKernel1D = None
                            OpenCLSplineRenderer = None
                            InitialOptimization = None
                        ApplyDenseMotionFieldExample = None
                        MotionCompensatedReconExample = None
                        class compensation:
                            OpenCLCompensatedBackProjector = None
                            OpenCLMotionCompensatedBackProjector = None
                            OpenCLCompensatedBackProjector1DCompressionField = None
                            OpenCLCompensatedBackProjectorTPS = None
                    class basics:
                        PointCloudMaker = None
                        ReadImageDataFromFileExample = None
                        RotationMatrixExamples = None
                        ReadImageDataFromFile = None
                        MHDImageLoader = None
                    RamLakFilteringExample = None
                    class RotationalAngiography:
                        class ResidualMotionCompensation:
                            class ECG:
                                Angiogram = None
                                ECGGating = None
                            class morphology:
                                StructuringElement = None
                                Morphology = None
                            class reconWithStreakReduction:
                                ConeBeamBackprojectorStreakReductionWithMotionCompensation = None
                                ConeBeamBackprojectorStreakReduction = None
                                OpenCLBackProjectorStreakReduction = None
                            class registration:
                                class bUnwarpJ_:
                                    bUnwarpJ_ = None
                                    PointToolbar = None
                                    CumulativeQueue = None
                                    MathTools = None
                                    MainDialog = None
                                    ClearAll = None
                                    Param = None
                                    FinalAction = None
                                    Transformation = None
                                    PointHandler = None
                                    IODialog = None
                                    EvaluateSimilarityTile = None
                                    PointAction = None
                                    Credits = None
                                    BSplineModel = None
                                    GrayscaleResultTileMaker = None
                                    ProgressBar = None
                                    Mask = None
                                    MiscTools = None
                                class math:
                                    BSpline = None
                                UnwarpJ_ = None
                            MotionCompensatedRecon = None
                            class mip:
                                OpenCLMaximumIntensityProjection = None
                    class truncation:
                        NonZeroArtifactImage = None
                        PolynomialTruncationCorrectionExample = None
                        ConstantValueZeroArtifactImage = None
                        WaterCylinderFBPExample = None
                    FanBeamParallelBeamComparison = None
                    DisplayReconstruction = None
                    class weka:
                        RegressionExample = None
                        ClassificationExample = None
                        StartWeka = None
                    class weightedtv:
                        TVGradient = None
                        Perform2DWeightedTV = None
                        TVOpenCLGridOperators = None
                        Perform3DWeightedTV = None
                        TVGradient3D = None
                    class physics:
                        SingleMaterialMonteCarlo = None
                        SpectralAbsorption = None
                        DistributionTest = None
                        XRayWorker = None
                        XRayViewer = None
                        XRayTracerSampling = None
                        XRayTracer = None
                        CreateCustomMaterial = None
                    class ringArtifactCorrection:
                        RingArtifactCorrectionExample = None
                        PolarConverter = None
                        RingArtifactCorrector = None
                    class dmip:
                        RANSAC = None
                        Registration2 = None
                        DefectPixelInterpolation = None
                        DMIP_ParallelBeam = None
                        Registration3 = None
                        Intro = None
                        SVDandFT = None
                        Registration1 = None
                        DMIP_FanBeamBackProjector2D = None
                        ImageUndistortion = None
                    class phantoms:
                        SimpleCubes3D = None
                        TestObject2 = None
                        SimpleGridsForTruncationCorrection = None
                        PohlmannPhantom = None
                        CreateOpenCLProjectionPhantomExample = None
                        TestObject1 = None
                        DotsGrid2D = None
                        Sphere3D = None
                        BrainPerfusionPhantom = None
                        SheppLogan = None
                        BrainPerfusionPhantomConfig = None
                        MTFphantom = None
                        MickeyMouseGrid2D = None
                        Phantom3D = None
                        Phantom = None
                        FilePhantom = None
                        Ellipsoid = None
                        UniformCircleGrid2D = None
                    DisplaySinogram = None
                    class filters:
                        SheppLoganKernel = None
                        RamLakKernelLinux = None
                        HilbertKernel = None
                        DerivativeKernel = None
                        RayByRayFiltering = None
                        RamLakKernel = None
                        GridKernel = None
                    class interpolation:
                        FanParameters = None
                        Interpolation = None
                    class cone:
                        ConeBeamCosineFilter = None
                        ConeBeamProjector = None
                        ConeBeamBackprojector = None
                        ConeBeamReconstructionExample = None
                    class atract:
                        AtractFilter2D = None
                        AtractExample = None
                        BorderRemoval1D = None
                        AtractFilter1D = None
                        AtractWithBinaryWeight = None
                        LaplaceKernel1D = None
                        AtractKernel1D = None
                        DisplayAtract = None
                        BorderRemoval2D = None
                        LaplaceKernel2D = None
                        AtractKernel1D_test = None
                        AtractKernel2D = None
                        Kollimator = None
                    class noncircularfov:
                        TwoCirclesGridMod = None
                        TwoCirclesGrid = None
                        EllipseGrid2D = None
                        RectangleGrid2D = None
                        TrajectoryExample = None
                        Boundaries = None
                        Correspondences = None
                    class fourierConsistency:
                        class wedgefilter:
                            DoubleWedgeFilter = None
                            DoubleWedgeFilterParallel = None
                            DoubleWedgeFilterFanEA = None
                            ProjectionEstimationExample = None
                            DoubleWedgeFilterFanES = None
                class apps:
                    class gui:
                        ReconstructionPipelineFrame = None
                        class opengl:
                            MeshViewer = None
                            TrajectoryViewer = None
                            SurfaceTest = None
                            PointCloudViewer = None
                            BSplineVolumeRenderer = None
                            OpenGLViewer = None
                        ConfigurePipelineFrame = None
                        Citeable = None
                        XCatMetricPhantomCreator = None
                        RegistryEditor = None
                        GUICompatibleObjectVisualizationPanel = None
                        UpdateableGUI = None
                        RawDataOpener = None
                        TimeLinePlot = None
                        class blobdetection:
                            MarkerDetection = None
                            ConnectedComponent3D = None
                            AutomaticMarkerDetectionWorker = None
                            MarkerDetectionWorker = None
                        PhantomMaker = None
                        class roi:
                            MeasureMTFDroege = None
                            EvaluateROI = None
                            Measure2DBeadMTFAngularRange = None
                            MeasureNoise = None
                            Measure2DBeadMTFMultiDirection = None
                            MeasureInlayMTF = None
                            CopyROI = None
                            LearnHounsfieldScaling = None
                            ZeroFill = None
                            MeasureEdgeMTF = None
                            DefineHounsfieldScaling = None
                            LinewiseFill = None
                            MeasurePatternMTF = None
                            CompareGrayValues = None
                            MeasureSlantMTF = None
                            Measure3DBeadMTF = None
                            ComputeIndependentComponents = None
                        FileTextFieldTransferHandler = None
                        ConfigurationFrame = None
                        GUIConfigurable = None
                        TrajectoryEditor = None
                        class pointselector:
                            PointSelectorWorker = None
                            PointSelector = None
                    Conrad = None
                    class activeshapemodel:
                        CreateARFF = None
                        Specificity = None
                        BuildCONRADCardiacModel = None
                        Specificity4D = None
                        LeaveOneOutTest = None
                class conrad:
                    class data:
                        class test:
                            FFTTests = None
                        class generic:
                            class iterators:
                                GenericFloatIterator = None
                                GenericPointwiseIteratorND = None
                            GenericGridOperatorInterface = None
                            GenericPointwiseOperators = None
                            GenericInterpolationOperators = None
                            GenericGrid = None
                            class complex:
                                ComplexGridOperator = None
                                ComplexGrid = None
                                ComplexGrid2D = None
                                ComplexPointwiseOperators = None
                                OpenCLComplexGridOperator = None
                                ComplexGrid1D = None
                                OpenCLGridTest = None
                                Fourier = None
                                OpenCLComplexMemoryDelegate = None
                                OpenCLTestClass = None
                                ComplexGrid3D = None
                                ComplexGridOperatorInterface = None
                            GenericGridOperator = None
                            class datatypes:
                                Double = None
                                Integer = None
                                OpenCLable = None
                                Complex = None
                                Gridable = None
                                Float = None
                            class opencl:
                                OpenCLGenericGridOperators = None
                                OpenCLGenericGridInterface = None
                        OpenCLMemoryDelegate = None
                        Grid = None
                        PointwiseIterator = None
                        class numeric:
                            NumericGrid = None
                            class iterators:
                                NumericFloatIterator = None
                                NumericPointwiseIteratorND = None
                            InterpolationOperators = None
                            MultiChannelGrid2D = None
                            Grid2DComplex = None
                            NumericPointwiseOperators = None
                            NumericGridOperator = None
                            Grid3D = None
                            MultiChannelGrid3D = None
                            Grid1D = None
                            Grid2D = None
                            BurtPyramid = None
                            Grid4D = None
                            Grid1DComplex = None
                            class opencl:
                                OpenCLGrid2D = None
                                ExtendedOpenCLGridOperators = None
                                OpenCLBenchmark = None
                                OpenCLGridInterface = None
                                OpenCLGrid1D = None
                                OpenCLGrid3D = None
                                OpenCLGridOperators = None
                                class delegates:
                                    OpenCLNumericMemoryDelegate4D = None
                                    OpenCLNumericMemoryDelegateLinear = None
                                    OpenCLNumericMemoryDelegate3D = None
                                OpenCLGridTest = None
                                OpenCLSynchProblemExample = None
                    class rendering:
                        RayDetector = None
                        WatertightRayTracer = None
                        AbstractScene = None
                        Priority1DRayTracer = None
                        SimpleScene = None
                        AbstractRayTracer = None
                        SimpleRayTracer = None
                        Simple1DRayTracer = None
                        PriorityRayTracer = None
                        PrioritizableScene = None
                    class parallel:
                        SimpleParallelThread = None
                        ParallelizableRunnable = None
                        ParallelThread = None
                        NamedParallelizableRunnable = None
                        ParallelThreadExecutor = None
                    class volume3d:
                        class operations:
                            AddSlabs = None
                            FFTShifter = None
                            MultiplySlabs = None
                            UpperLimitSlab = None
                            InitializeSquaredCosineR = None
                            InitializeLowPass = None
                            MeanOfSlab = None
                            DivideSlabs = None
                            MultiplySlabScalar = None
                            MaxOfSlab = None
                            MinOfSlab = None
                            InitializeHighPass = None
                            CopySlabData = None
                            InitializeSquaredCosine = None
                            InitializeGaussian = None
                            ParallelVolumeOperation = None
                            AddSlabScalar = None
                            MinOfSlabs = None
                            SquareRootSlab = None
                            VoxelOperation = None
                        Volume3D = None
                        ParallelVolumeOperator = None
                        VolumeOperator = None
                        MaxEigenValue = None
                        FFTVolumeHandle = None
                        JTransformsFFTVolumeHandle = None
                    class optimization:
                        LSqMinNorm = None
                        CombinedGradientOptimizableFunction = None
                        LMA = None
                        OptimizableFunction = None
                    class numerics:
                        class test:
                            RQTest = None
                            TestExpressions = None
                            SolversTest = None
                            SimpleMatrixTest = None
                            SimpleOperatorsTest = None
                            SimpleVectorTest = None
                        DecompositionSVD = None
                        DecompositionQR = None
                        DoubleFunction = None
                        SimpleOperators = None
                        SimpleMatrix = None
                        DecompositionRQ = None
                        SimpleVector = None
                        class mathexpressions:
                            Evaluator = None
                            ExpressionParser = None
                            IdentifierExpression = None
                            FloatExpression = None
                            CompoundExpression = None
                            MathExpression = None
                            FunctionExpression = None
                            AbstractMathExpression = None
                            RealExpression = None
                        Solvers = None
                    class filtering:
                        SelectChannelTool = None
                        HilbertFilteringTool = None
                        MedianFilteringTool = None
                        ImageMathFilter = None
                        ImageConstantMathFilter = None
                        TruncationCorrectionTool = None
                        MeanMarkerBasedProjectionShiftingToolForXCAT = None
                        SimulateXRayDetector = None
                        AtractResidual2D = None
                        KinectBasedDetectorSaturationCorrectionTool = None
                        class rampfilters:
                            RampFilter = None
                            IRRFilter = None
                            SheppLoganRampFilterWithRollOff = None
                            SheppLoganRampFilter = None
                            HammingRampFilter = None
                            HanningRampFilter = None
                            ArbitraryRampFilter = None
                            CosineRampFilter = None
                            RamLakRampFilter = None
                        class redundancy:
                            SilverWeightingTool = None
                            ParkerWeightingTool = None
                            TrajectoryParkerWeightingTool = None
                            NooWeightingTool = None
                            WesargWeightingTool = None
                            RiessWeightingTool = None
                        LogPoissonNoiseFilteringTool = None
                        NumericalDerivativeComputationTool = None
                        PatchwiseComponentComputationTool = None
                        ApplyLambdaWeightingTool = None
                        Rotate90DegreeLeftTool = None
                        MeanFilteringTool = None
                        class multiprojection:
                            class anisotropic:
                                AnisotropicStructureTensorNoiseFilter = None
                                AnisotropicFilterFunction = None
                                CUDAAnisotropicStructureTensorNoiseFilter = None
                                CUDAFFTAnisotropicStructureTensorNoiseFilter = None
                            BlockWiseMultiProjectionFilter = None
                            DigitalSubtractionAngiographyTool = None
                            Triangulation = None
                            BlockwiseBilateralFilter3DCL = None
                            Lambda3DDerivativeFilter = None
                            BlockWiseStructureTensor = None
                            class blocks:
                                BilateralFilter3DBlock = None
                                IdentityTransformBlock = None
                                ImageProcessingBlock = None
                                IterativeReconstructionBlock = None
                                AnisotropicStructureTensorBlock = None
                                BilateralFilter3DCLBlock = None
                            IdentityTransformFilter = None
                            ConvertToMultiChannelImageTool = None
                            ProjectionSortingFilter = None
                            IterativeReconstructionFilter = None
                            BilateralFilter3D = None
                            DiaphragmTrackingTool = None
                            MultiProjectionFilter = None
                            BackgroundSeparationTool = None
                        FastRadialSymmetryTool = None
                        ThinPlateSplinesBasedProjectionWarpingTool = None
                        BilateralFilteringTool = None
                        MeanMarkerBasedProjectionShiftingTool = None
                        FiducialMarkerDetectionTool = None
                        ImageFilteringTool = None
                        HorizontalFlippingTool = None
                        DynamicDensityOptimizationScatterCorrectionTool = None
                        NonLinearGainCorrectionTool = None
                        HideOnUIAnnotation = None
                        Filtering2DTool = None
                        ExtremeValueTruncationFilter = None
                        HoughFilteringTool = None
                        PoissonNoiseFilteringTool = None
                        ThinPlateSplinesBasedProjectionWarpingToolForXCAT = None
                        CosineWeightingTool = None
                        PrimaryModulationScatterCorrectionTool = None
                        VolumeAttenuationFactorCorrectionTool = None
                        ImageJParallelTool = None
                        AbsoluteValueTool = None
                        RampFilteringTool = None
                        NumericalLinewiseAntiderivativeFilteringTool = None
                        IndividualImageFilteringTool = None
                        ApplyHounsfieldScaling = None
                        LaplaceFilteringTool = None
                        class opencl:
                            BilateralFiltering3DTool = None
                            OpenCLFilteringTool3D = None
                    class io:
                        NrrdFileInfo = None
                        KpcaIO = None
                        IndividualFilesProjectionDataSink = None
                        TestGridRawDataIO = None
                        NrrdFileWriter = None
                        NrrdFileReader = None
                        MotionFieldReader = None
                        TiffProjectionSource = None
                        GridRawIOUtil = None
                        DennerleinProjectionSource = None
                        ParseInfoFile = None
                        SelectionCancelledException = None
                        STLFileUtil = None
                        ConfigFileParser = None
                        DicomProjectionSource = None
                        ImagePlusDataSink = None
                        VTKMeshReader = None
                        ImagePlusProjectionDataSource = None
                        InteractiveConfigFileReader = None
                        RotTransIO = None
                        SerializableFloatProcessor = None
                        ZipProjectionSource = None
                        VTKMeshIO = None
                        SafeSerializable = None
                        AdditionalDicomTag = None
                        VTKVectorField = None
                        PcaIO = None
                        FlexibleFileOpener = None
                        SEQProjectionSource = None
                        MKTProjectionSource = None
                        ConfigFile = None
                        FileProjectionSource = None
                        NRRDProjectionSource = None
                    class geometry:
                        General = None
                        class test:
                            ProjectionTest = None
                            SurfaceTests = None
                            CurveTests = None
                            GeometryTests = None
                        SeparableFootprints = None
                        AbstractCurve = None
                        Axis = None
                        AbstractSurface = None
                        class motion:
                            ArtificialMotionField = None
                            MovingCenterRotationMotionField = None
                            SimpleMotionField = None
                            WeightBearingBeadPositionBuilder = None
                            ConstantMotionField = None
                            MixedSurfaceBSplineMotionField = None
                            VICONMarkerMotionField = None
                            MotionUtil = None
                            PointBasedMotionField = None
                            AnalyticalAffineMotionField = None
                            AffineMotionField = None
                            OpenCLParzenWindowMotionField = None
                            DualMotionField = None
                            AnalyticalAffineMotionFieldEuler = None
                            MotionField = None
                            class timewarp:
                                TimeWarper = None
                                RestPhaseTimeWarper = None
                                IdentityTimeWarper = None
                                DualPhasePeriodicTimeWarper = None
                                HarmonicTimeWarper = None
                                ConstantTimeWarper = None
                                SigmoidTimeWarper = None
                                ScaledIdentitiyTimeWarper = None
                                PeriodicTimeWarper = None
                                CombinedTimeWarper = None
                            CombinedBreathingHeartMotionField = None
                            ParzenWindowMotionField = None
                            AbstractAffineMotionField = None
                            TimeVariantSurfaceBSplineListMotionField = None
                            PlanarMotionField = None
                            AnalyticalAffineMotionFieldAxisAngle = None
                            CompressionMotionField = None
                            RotationMotionField = None
                            TimeVariantSurfaceBSplineMotionField = None
                        class transforms:
                            ScaleRotate = None
                            Transform = None
                            class test:
                                TestTranslation = None
                                TestAffineTransform = None
                                TestComboTransform = None
                                TestScaleRotate = None
                                TestTransform = None
                            Quaternion = None
                            Transformable = None
                            Translation = None
                            ComboTransform = None
                            AffineTransform = None
                        AbstractShape = None
                        class trajectories:
                            ConfigFileBasedTrajectory = None
                            DennerleinProjectionTableFileTrajectory = None
                            SystemGeometryConfigFileTrajectory = None
                            HelicalTrajectory = None
                            CircularTrajectory = None
                            CirclePlusLineTrajectory = None
                            ExtrapolatedTrajectory = None
                            Trajectory = None
                            MultiSweepTrajectory = None
                            ProjectionTableFileTrajectory = None
                        Projection = None
                        class shapes:
                            class activeshapemodels:
                                class kernels:
                                    PolynomialKernel = None
                                    KernelFunction = None
                                    GaussianKernel = None
                                    RadialKernel = None
                                PCA = None
                                VarianceMeasure = None
                                ActiveShapeModel = None
                                GPA = None
                                KPCA = None
                            class simple:
                                Cylinder = None
                                StraightLine = None
                                VectorPoint3D = None
                                Box = None
                                Point3D = None
                                Cone = None
                                Triangle = None
                                ProjectPointToLineComparator = None
                                Plane3D = None
                                SwissRoll = None
                                SimpleSurface = None
                                Point2D = None
                                Pyramid = None
                                Sphere = None
                                GeometryTests = None
                                QuadricSurface = None
                                Edge = None
                                LineComparator1D = None
                                SortablePoint = None
                                Ellipsoid = None
                                PointND = None
                            ArbitrarySurface = None
                            class compound:
                                TriangleMesh = None
                                CompoundShape = None
                                NestedOctree = None
                                LinearOctree = None
                            class mesh:
                                AlexaEmbedding = None
                                DataMatrix = None
                                Mesh4D = None
                                Mesh = None
                                MeshUtil = None
                            StandardCoordinateSystem = None
                        CoordinateSystem = None
                        class bounds:
                            QuadricBoundingCondition = None
                            AbstractBoundingCondition = None
                            HalfSpaceBoundingCondition = None
                            BoundingBox = None
                        ConvexHull = None
                        class splines:
                            TorsionalMotionTimeVariantSurfaceBSpline2 = None
                            ClosedCubicBSpline = None
                            ShiftTimeVariantSurfaceBSpline = None
                            SurfaceUniformCubicBSpline = None
                            BSpline = None
                            TimeVariantSurfaceBSpline = None
                            NearestNeighborTimeVariantSurfaceBSpline = None
                            SurfaceBSpline = None
                            SurfaceBSplineVolumePhantom = None
                            SplineTests = None
                            TorsionalMotionTimeVariantSurfaceBSpline = None
                            class fitting:
                                BSplineCurveInterpolation = None
                                BSplineSurfaceInterpolation = None
                            UniformCubicBSpline = None
                            MotionDefectTimeVariantSurfaceBSpline = None
                        Rotations = None
                    class reconstruction:
                        CPUSuperShortScanBackprojector = None
                        class test:
                            IterativeReconstructionTestA = None
                            IterativeReconstructionTestB = None
                        FBPReconstructionFilter = None
                        ReconstructionFilter = None
                        class voi:
                            VolumeOfInterest = None
                            PolygonBasedVolumeOfInterest = None
                            CylinderBasedVolumeOfInterest = None
                        SimpleIterativeReconstruction = None
                        MotionCompensatedSubVolumeBackprojector = None
                        class iterative:
                            SeparableFootprints = None
                            SeparableFootprintsBasedReconstruction = None
                            RayDrivenBasedReconstruction = None
                            PenalizedLeastSquareART = None
                            huberPenalty = None
                            LeastSquaresCG = None
                            ModelBasedIterativeReconstruction = None
                            IterativeReconstruction = None
                            DistanceDrivenBasedReconstruction = None
                        SuperShortScanBackprojection = None
                        SeparableFootprintsBasedReconstruction = None
                        RayDrivenBasedReconstruction = None
                        RayWeightCorrectingCPUSuperShortScanBackprojector = None
                        MotionCompensatedVOIBasedReconstructionFilter = None
                        ModelBasedIterativeReconstruction = None
                        RigidBody3DTransformationVOIBasedReconstructionFilterForXCAT = None
                        IterativeReconstruction = None
                        DistanceDrivenBasedReconstruction = None
                        LolaBunnyBackprojector = None
                        RigidBody3DTransformationVOIBasedReconstructionFilter = None
                        SubVolumeBackprojector = None
                        VOIBasedReconstructionFilter = None
                    class utils:
                        class parsers:
                            SceneFileParser = None
                            ParserFactory = None
                            SliceWorkerParser = None
                        UserUtil = None
                        BilinearInterpolatingDoubleArray = None
                        FileJoiner = None
                        FileUtil = None
                        DoublePrecisionPointUtil = None
                        StatisticsUtil = None
                        LinearInterpolatingDoubleArray = None
                        CONRAD = None
                        ImageUtil = None
                        DicomDecoder = None
                        StringFileFilter = None
                        DoubleArrayUtil = None
                        TessellationUtil = None
                        DicomConfigurationUpdater = None
                        class interpolation:
                            LogLinearInterpolator = None
                            NumberInterpolatingTreeMap = None
                            Interpolator = None
                            LogLogInterpolator = None
                            LinearInterpolator = None
                        FFTUtil = None
                        FloatArrayUtil = None
                        VisualizationUtil = None
                        ImageGridBuffer = None
                        FHTUtil = None
                        TestingTools = None
                        ConfigurationUpdater = None
                        GUIUtil = None
                        RegKeys = None
                        XmlUtils = None
                        Configuration = None
                    class calibration:
                        PrincipalComponentAnalysis2D = None
                        GeometricCalibrationGUI = None
                        GeometricCalibration = None
                        class crossratios:
                            BeadDetection = None
                            CreateCalibration = None
                            CreateProjectionData = None
                        Factorization = None
                        CalibrationBead = None
                    class metric:
                        ImageMetric = None
                        NormalizedImprovement = None
                        MeanSquareErrorMetric = None
                        NormalizedImageMetric = None
                        RootMeanSquareErrorMetric = None
                    class physics:
                        PhysicalObject = None
                        class detector:
                            XRayDetector = None
                            SimpleMonochromaticDetector = None
                            SimplePolychromaticDetector = None
                            PolychromaticDetectorWithNoise = None
                            MaterialPathLengthDetector = None
                        class absorption:
                            SelectableEnergyMonochromaticAbsorptionModelWithNoise = None
                            SelectableEnergyMonochromaticAbsorptionModel = None
                            AbsorptionModel = None
                            PathLengthHistogramCreatingAbsorptionModel = None
                            PolychromaticAbsorptionModel = None
                            DensityAbsorptionModel = None
                        PolychromaticXRaySpectrum = None
                        LambdaFunction = None
                        EnergyDependentCoefficients = None
                        PhysicalPoint = None
                        Constants = None
                        HalfValueLayerFunction = None
                        class materials:
                            WeightedAtomicComposition = None
                            Material = None
                            class database:
                                ElementalMassAttenuationData = None
                                CompositionToAbsorptionEdgeMap = None
                                NameToFormulaMap = None
                                MaterialsDB = None
                                class xmldatagenerators:
                                    RebuildMaps = None
                                    RebuildDatabase = None
                                    RebuildMaterialDatabase = None
                                OnlineMassAttenuationDB = None
                                FormulaToNameMap = None
                            Mixture = None
                            class utils:
                                WeightedAtomicComposition = None
                                AttenuationType = None
                                AttenuationRetrievalMode = None
                                LocalMassAttenuationCalculator = None
                                MaterialUtils = None
                            Compound = None
                            class materialsTest:
                                TestMassAttenuationData = None
                            Element = None
                        XRaySpectrum = None
                    class fitting:
                        LinearFunction = None
                        class test:
                            FunctionTest = None
                        GaussianFunction = None
                        LogarithmicFunction = None
                        Surface = None
                        IdentityFunction = None
                        Function = None
                        ConstrainedRANSACFittedFunction = None
                        PolynomialFunction = None
                        Quadric = None
                        RANSACFittedFunction = None
                    class phantom:
                        XNPhantom = None
                        class electrondensity:
                            CrisEDPhantomGUI = None
                            EDInnerDisk = None
                            CrisEDPhantomM062 = None
                            EDOuterDisk = None
                            QuadricDisk = None
                            Insert = None
                        RandomizedHelixPhantom = None
                        SheppLoganPhantom = None
                        BonePhantom = None
                        SevenBeadPhantom = None
                        AnalyticPhantom = None
                        AnalyticPhantom4D = None
                        SpherePhantom = None
                        CatphanCTP528 = None
                        PyramidPhantom = None
                        class workers:
                            SliceWorker = None
                            DiracProjectionPhantom = None
                            VolumeOfInterestPhantom = None
                            AnalyticPhantom3DVolumeRenderer = None
                            MultiMaterialPhantom3DVolumeRenderer = None
                            AnalyticPhantomProjectorWorker = None
                            SheppLoganPhantomWorker = None
                        RandomDistributionPhantom = None
                        SimpleShapeTestPhantom = None
                        DefrisePhantom = None
                        NumericalSheppLogan3D = None
                        MovingBallPhantom = None
                        BoxPhantom = None
                        AffineMotionPhantom = None
                        class forbild:
                            ForbildShapeFactory = None
                            class shapes:
                                ForbildSphere = None
                                ForbildCone = None
                                ForbildEllipsoid = None
                                ForbildBox = None
                                ForbildCylinder = None
                            ForbildParser = None
                            ForbildPhantom = None
                        ConePhantom = None
                        EllipsoidPhantom = None
                        class xcat:
                            CoronaryScene = None
                            ViconAffineTransform = None
                            XCatScene = None
                            SquatScene = None
                            XCatMaterialGenerator = None
                            TessellationThread = None
                            BreathingScene = None
                            WholeBodyScene = None
                            ViconMarkerBuilder = None
                            HeartScene = None
                            CombinedBreathingHeartScene = None
                            DynamicSquatScene = None
                        CatheterPhantom = None
                        AsciiSTLMeshPhantom = None
                        WaterCylinderPhantom = None
                        class renderer:
                            PhantomRenderer = None
                            MetricPhantomRenderer = None
                            ParallelProjectionPhantomRenderer = None
                            AnalyticPhantomProjector = None
                            StreamingPhantomRenderer = None
                            CylinderPhantomRenderer = None
                            RampProjectionPhantomRenderer = None
                            SliceParallelVolumePhantomRenderer = None
                        class asmheart:
                            PredefinedModels = None
                            CONRADCardiacModel4D = None
                            CONRADCardiacModelConfig = None
                            CONRADCardiacModel3D = None
                        SheppLogan3D = None
                        BeadRemovalPhantom = None
                        MathematicalPhantom = None
                        AbstractCalibrationPhantom = None
                        SinoPhantom = None
                        MTFBeadPhantom = None
                        TrigonometryPhantom = None
                        CirclesPhantom = None
                    class pipeline:
                        ParallelImageFilterPipeliner = None
                        DevNullSink = None
                        BufferedProjectionSink = None
                        ParallelProjectionDataSinkFeeder = None
                        PipelineTests = None
                        ParallelImageFilterSink = None
                        IndividualImagePipelineFilteringTool = None
                        ProjectionSink = None
                        ProjectionSource = None
                    class cuda:
                        MouseControlable = None
                        CUDAFFTVolumeHandle = None
                        CUDABackProjector = None
                        MouseControl = None
                        ImagePlusVolumeRenderer = None
                        AdjustablePointer = None
                        CUDAVolumeOperator = None
                        CUDAForwardProjector = None
                        CUDAForwardProjectorWithMotion = None
                        CUDACompensatedBackProjector = None
                        JCudaRuntimeSample = None
                        CUDAVolumeTest = None
                        JCudaDriverTextureSample = None
                        CUDAVolume3D = None
                        CUDAUtil = None
                        class splines:
                            CUDABSpline = None
                    class opencl:
                        OpenCLEdgeForwardProjector = None
                        OpenCLProjectionPhantomRenderer = None
                        class rendering:
                            MouseControlable = None
                            MouseControl = None
                            OpenCLTextureRendering = None
                            OpenCLVolumeRenderer = None
                        OpenCLSurfacePhantomRenderer = None
                        OpenCLYBufferRenderer = None
                        OpenCLUtil = None
                        OpenCLBackProjector = None
                        TestOpenCL = None
                        OpenCLDetectorMotionBackProjector = None
                        OpenCLRenderer = None
                        class shapes:
                            OpenCLSphere = None
                            OpenCLCompoundShape = None
                            OpenCLEllipsoid = None
                            OpenCLUniformTextureBSpline = None
                            OpenCLUniformTextureSurfaceBSpline = None
                            OpenCLBox = None
                            OpenCLUniformBSpline = None
                            OpenCLTextureTimeVariantSurfaceBSpline = None
                            OpenCLPyramid = None
                            OpenCLCone = None
                            OpenCLCylinder = None
                            OpenCLUniformSurfaceBSpline = None
                            OpenCLTimeVariantSurfaceBSpline = None
                        OpenCLForwardProjector = None
                        OpenCLForwardProjectorDynamicVolume = None
                        OpenCLJointBilateralFilteringTool = None
                        OpenCLEvaluatable = None
                        OpenCLMaterialPathLengthPhantomRenderer = None
                        class GLCLDemo:
                            UserSceneInteraction = None
                            GLCLInteroperabilityDemo = None
                        OpenCLAppendBufferRenderer = None
                        OpenCLForwardProjectorWithMotion = None
    Normalize_Image_MinMax = None
    Generate_Absorption_Plot = None
    Apply_Filter = None
    Viva_Reader = None
    OpenCL_Back_Projector = None
    Count_Edge_Points = None
    Check_Trajectory_Consistency = None
    SaveAs_Viva = None
    Nrrd_Reader = None
    ZIP_Reader_Standalone = None
    Nurbs_Reader = None
    Measure_MTF_Droege = None
    Apply_ROI_Method = None
    Dennerlein_Writer = None
    Raw_Data_Opener = None
    Create_Numerical_Phantom = None
    FlexibleFileOpener = None
    Measure_MTF_Wire = None
    Raw_Data_Opener_Standalone = None
class src:
    Anisotropic_Filtering = None
    HandleExtraFileTypes = None
    Load_Recent = None
    Replace_Intensity_Value_Tool = None
    Copy_Convolution = None
    Dennerlein_Reader = None
    MKT_Reader = None
    Convert_to_16_bit = None
    Normalize_Image_CutOff = None
    Visualize_Ramp_Filter = None
    OpenCL_Forward_Projector = None
    Measure_All_Slices = None
    OpenCL_Forward_Projector_With_Motion = None
    Normalize_Image = None
    Measure_Slanted_Edge = None
    Nrrd_Writer = None
    Generate_Spectrum = None
    OpenCL_Volume_Renderer = None
    Generate_Beam_Hardening_Lookup_Table = None
    Generate_Photon_Mass_Attenuation_Plot = None
    ZIP_Reader = None
    class edu:
        class stanford:
            class rsl:
                class tutorial:
                    class parallel:
                        ParallelProjector2D = None
                        ParallelOnlineReconstructionExample = None
                        ParallelReconExample = None
                        ParallelOnlineBackprojectionExample = None
                        ParallelMedianReconExample = None
                        ParallelProjectionExample = None
                        ParallelBackprojector2D = None
                    DisplayUniformCircle = None
                    class fan:
                        FanBeamComparisonToCONRAD = None
                        class redundancy:
                            BinaryWeights_Normal = None
                            SilverWeights = None
                            BinaryWeights = None
                            CompensationWeights = None
                            BinaryWeights_erodeByOne = None
                            FanBeamWeightingComparison = None
                            ParkerWeights = None
                        FanBeamBackprojector2D = None
                        CosineFilter = None
                        FanBeamReconstructionExample = None
                        FanBeamProjector2D = None
                        RbRFanBeamReconstructionExample = None
                        class dynamicCollimation:
                            copyRedundantData = None
                    class test:
                        VolumeCenteringTest = None
                        CharacterEncodingTest = None
                        MaxThreadsTest = None
                    class scalespace:
                        ScaleSpaceStudies = None
                    class mammography:
                        class inbreast:
                            XMLparser = None
                            ReadMammograms = None
                        Mammogram = None
                    class ecc:
                        EpipolarConsistency = None
                        EpipolarConsistencyExample = None
                    class modelObserver:
                        TestModelGenerator = None
                        ImageHelper = None
                        ROC = None
                        Channels = None
                        Observer = None
                        ObserverPipeline = None
                        CreateImages = None
                        ModelDemo = None
                    class iterative:
                        GridOp = None
                        SartCPU = None
                        SartCL2D = None
                        Sart = None
                        IterativeReconstructionTest = None
                        SartCL = None
                        GDTest = None
                        Etv = None
                    class motion:
                        class estimation:
                            ThinPlateSplineInterpolation = None
                            RadialBasisFunctionInterpolation = None
                            SmoothKernel1D = None
                            EstimateCubic2DSpline = None
                            RunMotionEstimation = None
                            ProjectionLoader = None
                            EstimateBSplineSurface = None
                            CylinderVolumeMask = None
                            OptimizeMotionField = None
                            SobelKernel1D = None
                            OpenCLSplineRenderer = None
                            InitialOptimization = None
                        ApplyDenseMotionFieldExample = None
                        MotionCompensatedReconExample = None
                        class compensation:
                            OpenCLCompensatedBackProjector = None
                            OpenCLMotionCompensatedBackProjector = None
                            OpenCLCompensatedBackProjector1DCompressionField = None
                            OpenCLCompensatedBackProjectorTPS = None
                    class basics:
                        PointCloudMaker = None
                        ReadImageDataFromFileExample = None
                        RotationMatrixExamples = None
                        ReadImageDataFromFile = None
                        MHDImageLoader = None
                    RamLakFilteringExample = None
                    class RotationalAngiography:
                        class ResidualMotionCompensation:
                            class ECG:
                                Angiogram = None
                                ECGGating = None
                            class morphology:
                                StructuringElement = None
                                Morphology = None
                            class reconWithStreakReduction:
                                ConeBeamBackprojectorStreakReductionWithMotionCompensation = None
                                ConeBeamBackprojectorStreakReduction = None
                                OpenCLBackProjectorStreakReduction = None
                            class registration:
                                class bUnwarpJ_:
                                    bUnwarpJ_ = None
                                    PointToolbar = None
                                    CumulativeQueue = None
                                    MathTools = None
                                    MainDialog = None
                                    ClearAll = None
                                    Param = None
                                    FinalAction = None
                                    Transformation = None
                                    PointHandler = None
                                    IODialog = None
                                    EvaluateSimilarityTile = None
                                    PointAction = None
                                    Credits = None
                                    BSplineModel = None
                                    GrayscaleResultTileMaker = None
                                    ProgressBar = None
                                    Mask = None
                                    MiscTools = None
                                class math:
                                    BSpline = None
                                UnwarpJ_ = None
                            MotionCompensatedRecon = None
                            class mip:
                                OpenCLMaximumIntensityProjection = None
                    class truncation:
                        NonZeroArtifactImage = None
                        PolynomialTruncationCorrectionExample = None
                        ConstantValueZeroArtifactImage = None
                        WaterCylinderFBPExample = None
                    FanBeamParallelBeamComparison = None
                    DisplayReconstruction = None
                    class weka:
                        RegressionExample = None
                        ClassificationExample = None
                        StartWeka = None
                    class weightedtv:
                        TVGradient = None
                        Perform2DWeightedTV = None
                        TVOpenCLGridOperators = None
                        Perform3DWeightedTV = None
                        TVGradient3D = None
                    class physics:
                        SingleMaterialMonteCarlo = None
                        SpectralAbsorption = None
                        DistributionTest = None
                        XRayWorker = None
                        XRayViewer = None
                        XRayTracerSampling = None
                        XRayTracer = None
                        CreateCustomMaterial = None
                    class ringArtifactCorrection:
                        RingArtifactCorrectionExample = None
                        PolarConverter = None
                        RingArtifactCorrector = None
                    class dmip:
                        RANSAC = None
                        Registration2 = None
                        DefectPixelInterpolation = None
                        DMIP_ParallelBeam = None
                        Registration3 = None
                        Intro = None
                        SVDandFT = None
                        Registration1 = None
                        DMIP_FanBeamBackProjector2D = None
                        ImageUndistortion = None
                    class phantoms:
                        SimpleCubes3D = None
                        TestObject2 = None
                        SimpleGridsForTruncationCorrection = None
                        PohlmannPhantom = None
                        CreateOpenCLProjectionPhantomExample = None
                        TestObject1 = None
                        DotsGrid2D = None
                        Sphere3D = None
                        BrainPerfusionPhantom = None
                        SheppLogan = None
                        BrainPerfusionPhantomConfig = None
                        MTFphantom = None
                        MickeyMouseGrid2D = None
                        Phantom3D = None
                        Phantom = None
                        FilePhantom = None
                        Ellipsoid = None
                        UniformCircleGrid2D = None
                    DisplaySinogram = None
                    class filters:
                        SheppLoganKernel = None
                        RamLakKernelLinux = None
                        HilbertKernel = None
                        DerivativeKernel = None
                        RayByRayFiltering = None
                        RamLakKernel = None
                        GridKernel = None
                    class interpolation:
                        FanParameters = None
                        Interpolation = None
                    class cone:
                        ConeBeamCosineFilter = None
                        ConeBeamProjector = None
                        ConeBeamBackprojector = None
                        ConeBeamReconstructionExample = None
                    class atract:
                        AtractFilter2D = None
                        AtractExample = None
                        BorderRemoval1D = None
                        AtractFilter1D = None
                        AtractWithBinaryWeight = None
                        LaplaceKernel1D = None
                        AtractKernel1D = None
                        DisplayAtract = None
                        BorderRemoval2D = None
                        LaplaceKernel2D = None
                        AtractKernel1D_test = None
                        AtractKernel2D = None
                        Kollimator = None
                    class noncircularfov:
                        TwoCirclesGridMod = None
                        TwoCirclesGrid = None
                        EllipseGrid2D = None
                        RectangleGrid2D = None
                        TrajectoryExample = None
                        Boundaries = None
                        Correspondences = None
                    class fourierConsistency:
                        class wedgefilter:
                            DoubleWedgeFilter = None
                            DoubleWedgeFilterParallel = None
                            DoubleWedgeFilterFanEA = None
                            ProjectionEstimationExample = None
                            DoubleWedgeFilterFanES = None
                class apps:
                    class gui:
                        ReconstructionPipelineFrame = None
                        class opengl:
                            MeshViewer = None
                            TrajectoryViewer = None
                            SurfaceTest = None
                            PointCloudViewer = None
                            BSplineVolumeRenderer = None
                            OpenGLViewer = None
                        ConfigurePipelineFrame = None
                        Citeable = None
                        XCatMetricPhantomCreator = None
                        RegistryEditor = None
                        GUICompatibleObjectVisualizationPanel = None
                        UpdateableGUI = None
                        RawDataOpener = None
                        TimeLinePlot = None
                        class blobdetection:
                            MarkerDetection = None
                            ConnectedComponent3D = None
                            AutomaticMarkerDetectionWorker = None
                            MarkerDetectionWorker = None
                        PhantomMaker = None
                        class roi:
                            MeasureMTFDroege = None
                            EvaluateROI = None
                            Measure2DBeadMTFAngularRange = None
                            MeasureNoise = None
                            Measure2DBeadMTFMultiDirection = None
                            MeasureInlayMTF = None
                            CopyROI = None
                            LearnHounsfieldScaling = None
                            ZeroFill = None
                            MeasureEdgeMTF = None
                            DefineHounsfieldScaling = None
                            LinewiseFill = None
                            MeasurePatternMTF = None
                            CompareGrayValues = None
                            MeasureSlantMTF = None
                            Measure3DBeadMTF = None
                            ComputeIndependentComponents = None
                        FileTextFieldTransferHandler = None
                        ConfigurationFrame = None
                        GUIConfigurable = None
                        TrajectoryEditor = None
                        class pointselector:
                            PointSelectorWorker = None
                            PointSelector = None
                    Conrad = None
                    class activeshapemodel:
                        CreateARFF = None
                        Specificity = None
                        BuildCONRADCardiacModel = None
                        Specificity4D = None
                        LeaveOneOutTest = None
                class conrad:
                    class data:
                        class test:
                            FFTTests = None
                        class generic:
                            class iterators:
                                GenericFloatIterator = None
                                GenericPointwiseIteratorND = None
                            GenericGridOperatorInterface = None
                            GenericPointwiseOperators = None
                            GenericInterpolationOperators = None
                            GenericGrid = None
                            class complex:
                                ComplexGridOperator = None
                                ComplexGrid = None
                                ComplexGrid2D = None
                                ComplexPointwiseOperators = None
                                OpenCLComplexGridOperator = None
                                ComplexGrid1D = None
                                OpenCLGridTest = None
                                Fourier = None
                                OpenCLComplexMemoryDelegate = None
                                OpenCLTestClass = None
                                ComplexGrid3D = None
                                ComplexGridOperatorInterface = None
                            GenericGridOperator = None
                            class datatypes:
                                Double = None
                                Integer = None
                                OpenCLable = None
                                Complex = None
                                Gridable = None
                                Float = None
                            class opencl:
                                OpenCLGenericGridOperators = None
                                OpenCLGenericGridInterface = None
                        OpenCLMemoryDelegate = None
                        Grid = None
                        PointwiseIterator = None
                        class numeric:
                            NumericGrid = None
                            class iterators:
                                NumericFloatIterator = None
                                NumericPointwiseIteratorND = None
                            InterpolationOperators = None
                            MultiChannelGrid2D = None
                            Grid2DComplex = None
                            NumericPointwiseOperators = None
                            NumericGridOperator = None
                            Grid3D = None
                            MultiChannelGrid3D = None
                            Grid1D = None
                            Grid2D = None
                            BurtPyramid = None
                            Grid4D = None
                            Grid1DComplex = None
                            class opencl:
                                OpenCLGrid2D = None
                                ExtendedOpenCLGridOperators = None
                                OpenCLBenchmark = None
                                OpenCLGridInterface = None
                                OpenCLGrid1D = None
                                OpenCLGrid3D = None
                                OpenCLGridOperators = None
                                class delegates:
                                    OpenCLNumericMemoryDelegate4D = None
                                    OpenCLNumericMemoryDelegateLinear = None
                                    OpenCLNumericMemoryDelegate3D = None
                                OpenCLGridTest = None
                                OpenCLSynchProblemExample = None
                    class rendering:
                        RayDetector = None
                        WatertightRayTracer = None
                        AbstractScene = None
                        Priority1DRayTracer = None
                        SimpleScene = None
                        AbstractRayTracer = None
                        SimpleRayTracer = None
                        Simple1DRayTracer = None
                        PriorityRayTracer = None
                        PrioritizableScene = None
                    class parallel:
                        SimpleParallelThread = None
                        ParallelizableRunnable = None
                        ParallelThread = None
                        NamedParallelizableRunnable = None
                        ParallelThreadExecutor = None
                    class volume3d:
                        class operations:
                            AddSlabs = None
                            FFTShifter = None
                            MultiplySlabs = None
                            UpperLimitSlab = None
                            InitializeSquaredCosineR = None
                            InitializeLowPass = None
                            MeanOfSlab = None
                            DivideSlabs = None
                            MultiplySlabScalar = None
                            MaxOfSlab = None
                            MinOfSlab = None
                            InitializeHighPass = None
                            CopySlabData = None
                            InitializeSquaredCosine = None
                            InitializeGaussian = None
                            ParallelVolumeOperation = None
                            AddSlabScalar = None
                            MinOfSlabs = None
                            SquareRootSlab = None
                            VoxelOperation = None
                        Volume3D = None
                        ParallelVolumeOperator = None
                        VolumeOperator = None
                        MaxEigenValue = None
                        FFTVolumeHandle = None
                        JTransformsFFTVolumeHandle = None
                    class optimization:
                        LSqMinNorm = None
                        CombinedGradientOptimizableFunction = None
                        LMA = None
                        OptimizableFunction = None
                    class numerics:
                        class test:
                            RQTest = None
                            TestExpressions = None
                            SolversTest = None
                            SimpleMatrixTest = None
                            SimpleOperatorsTest = None
                            SimpleVectorTest = None
                        DecompositionSVD = None
                        DecompositionQR = None
                        DoubleFunction = None
                        SimpleOperators = None
                        SimpleMatrix = None
                        DecompositionRQ = None
                        SimpleVector = None
                        class mathexpressions:
                            Evaluator = None
                            ExpressionParser = None
                            IdentifierExpression = None
                            FloatExpression = None
                            CompoundExpression = None
                            MathExpression = None
                            FunctionExpression = None
                            AbstractMathExpression = None
                            RealExpression = None
                        Solvers = None
                    class filtering:
                        SelectChannelTool = None
                        HilbertFilteringTool = None
                        MedianFilteringTool = None
                        ImageMathFilter = None
                        ImageConstantMathFilter = None
                        TruncationCorrectionTool = None
                        MeanMarkerBasedProjectionShiftingToolForXCAT = None
                        SimulateXRayDetector = None
                        AtractResidual2D = None
                        KinectBasedDetectorSaturationCorrectionTool = None
                        class rampfilters:
                            RampFilter = None
                            IRRFilter = None
                            SheppLoganRampFilterWithRollOff = None
                            SheppLoganRampFilter = None
                            HammingRampFilter = None
                            HanningRampFilter = None
                            ArbitraryRampFilter = None
                            CosineRampFilter = None
                            RamLakRampFilter = None
                        class redundancy:
                            SilverWeightingTool = None
                            ParkerWeightingTool = None
                            TrajectoryParkerWeightingTool = None
                            NooWeightingTool = None
                            WesargWeightingTool = None
                            RiessWeightingTool = None
                        LogPoissonNoiseFilteringTool = None
                        NumericalDerivativeComputationTool = None
                        PatchwiseComponentComputationTool = None
                        ApplyLambdaWeightingTool = None
                        Rotate90DegreeLeftTool = None
                        MeanFilteringTool = None
                        class multiprojection:
                            class anisotropic:
                                AnisotropicStructureTensorNoiseFilter = None
                                AnisotropicFilterFunction = None
                                CUDAAnisotropicStructureTensorNoiseFilter = None
                                CUDAFFTAnisotropicStructureTensorNoiseFilter = None
                            BlockWiseMultiProjectionFilter = None
                            DigitalSubtractionAngiographyTool = None
                            Triangulation = None
                            BlockwiseBilateralFilter3DCL = None
                            Lambda3DDerivativeFilter = None
                            BlockWiseStructureTensor = None
                            class blocks:
                                BilateralFilter3DBlock = None
                                IdentityTransformBlock = None
                                ImageProcessingBlock = None
                                IterativeReconstructionBlock = None
                                AnisotropicStructureTensorBlock = None
                                BilateralFilter3DCLBlock = None
                            IdentityTransformFilter = None
                            ConvertToMultiChannelImageTool = None
                            ProjectionSortingFilter = None
                            IterativeReconstructionFilter = None
                            BilateralFilter3D = None
                            DiaphragmTrackingTool = None
                            MultiProjectionFilter = None
                            BackgroundSeparationTool = None
                        FastRadialSymmetryTool = None
                        ThinPlateSplinesBasedProjectionWarpingTool = None
                        BilateralFilteringTool = None
                        MeanMarkerBasedProjectionShiftingTool = None
                        FiducialMarkerDetectionTool = None
                        ImageFilteringTool = None
                        HorizontalFlippingTool = None
                        DynamicDensityOptimizationScatterCorrectionTool = None
                        NonLinearGainCorrectionTool = None
                        HideOnUIAnnotation = None
                        Filtering2DTool = None
                        ExtremeValueTruncationFilter = None
                        HoughFilteringTool = None
                        PoissonNoiseFilteringTool = None
                        ThinPlateSplinesBasedProjectionWarpingToolForXCAT = None
                        CosineWeightingTool = None
                        PrimaryModulationScatterCorrectionTool = None
                        VolumeAttenuationFactorCorrectionTool = None
                        ImageJParallelTool = None
                        AbsoluteValueTool = None
                        RampFilteringTool = None
                        NumericalLinewiseAntiderivativeFilteringTool = None
                        IndividualImageFilteringTool = None
                        ApplyHounsfieldScaling = None
                        LaplaceFilteringTool = None
                        class opencl:
                            BilateralFiltering3DTool = None
                            OpenCLFilteringTool3D = None
                    class io:
                        NrrdFileInfo = None
                        KpcaIO = None
                        IndividualFilesProjectionDataSink = None
                        TestGridRawDataIO = None
                        NrrdFileWriter = None
                        NrrdFileReader = None
                        MotionFieldReader = None
                        TiffProjectionSource = None
                        GridRawIOUtil = None
                        DennerleinProjectionSource = None
                        ParseInfoFile = None
                        SelectionCancelledException = None
                        STLFileUtil = None
                        ConfigFileParser = None
                        DicomProjectionSource = None
                        ImagePlusDataSink = None
                        VTKMeshReader = None
                        ImagePlusProjectionDataSource = None
                        InteractiveConfigFileReader = None
                        RotTransIO = None
                        SerializableFloatProcessor = None
                        ZipProjectionSource = None
                        VTKMeshIO = None
                        SafeSerializable = None
                        AdditionalDicomTag = None
                        VTKVectorField = None
                        PcaIO = None
                        FlexibleFileOpener = None
                        SEQProjectionSource = None
                        MKTProjectionSource = None
                        ConfigFile = None
                        FileProjectionSource = None
                        NRRDProjectionSource = None
                    class geometry:
                        General = None
                        class test:
                            ProjectionTest = None
                            SurfaceTests = None
                            CurveTests = None
                            GeometryTests = None
                        SeparableFootprints = None
                        AbstractCurve = None
                        Axis = None
                        AbstractSurface = None
                        class motion:
                            ArtificialMotionField = None
                            MovingCenterRotationMotionField = None
                            SimpleMotionField = None
                            WeightBearingBeadPositionBuilder = None
                            ConstantMotionField = None
                            MixedSurfaceBSplineMotionField = None
                            VICONMarkerMotionField = None
                            MotionUtil = None
                            PointBasedMotionField = None
                            AnalyticalAffineMotionField = None
                            AffineMotionField = None
                            OpenCLParzenWindowMotionField = None
                            DualMotionField = None
                            AnalyticalAffineMotionFieldEuler = None
                            MotionField = None
                            class timewarp:
                                TimeWarper = None
                                RestPhaseTimeWarper = None
                                IdentityTimeWarper = None
                                DualPhasePeriodicTimeWarper = None
                                HarmonicTimeWarper = None
                                ConstantTimeWarper = None
                                SigmoidTimeWarper = None
                                ScaledIdentitiyTimeWarper = None
                                PeriodicTimeWarper = None
                                CombinedTimeWarper = None
                            CombinedBreathingHeartMotionField = None
                            ParzenWindowMotionField = None
                            AbstractAffineMotionField = None
                            TimeVariantSurfaceBSplineListMotionField = None
                            PlanarMotionField = None
                            AnalyticalAffineMotionFieldAxisAngle = None
                            CompressionMotionField = None
                            RotationMotionField = None
                            TimeVariantSurfaceBSplineMotionField = None
                        class transforms:
                            ScaleRotate = None
                            Transform = None
                            class test:
                                TestTranslation = None
                                TestAffineTransform = None
                                TestComboTransform = None
                                TestScaleRotate = None
                                TestTransform = None
                            Quaternion = None
                            Transformable = None
                            Translation = None
                            ComboTransform = None
                            AffineTransform = None
                        AbstractShape = None
                        class trajectories:
                            ConfigFileBasedTrajectory = None
                            DennerleinProjectionTableFileTrajectory = None
                            SystemGeometryConfigFileTrajectory = None
                            HelicalTrajectory = None
                            CircularTrajectory = None
                            CirclePlusLineTrajectory = None
                            ExtrapolatedTrajectory = None
                            Trajectory = None
                            MultiSweepTrajectory = None
                            ProjectionTableFileTrajectory = None
                        Projection = None
                        class shapes:
                            class activeshapemodels:
                                class kernels:
                                    PolynomialKernel = None
                                    KernelFunction = None
                                    GaussianKernel = None
                                    RadialKernel = None
                                PCA = None
                                VarianceMeasure = None
                                ActiveShapeModel = None
                                GPA = None
                                KPCA = None
                            class simple:
                                Cylinder = None
                                StraightLine = None
                                VectorPoint3D = None
                                Box = None
                                Point3D = None
                                Cone = None
                                Triangle = None
                                ProjectPointToLineComparator = None
                                Plane3D = None
                                SwissRoll = None
                                SimpleSurface = None
                                Point2D = None
                                Pyramid = None
                                Sphere = None
                                GeometryTests = None
                                QuadricSurface = None
                                Edge = None
                                LineComparator1D = None
                                SortablePoint = None
                                Ellipsoid = None
                                PointND = None
                            ArbitrarySurface = None
                            class compound:
                                TriangleMesh = None
                                CompoundShape = None
                                NestedOctree = None
                                LinearOctree = None
                            class mesh:
                                AlexaEmbedding = None
                                DataMatrix = None
                                Mesh4D = None
                                Mesh = None
                                MeshUtil = None
                            StandardCoordinateSystem = None
                        CoordinateSystem = None
                        class bounds:
                            QuadricBoundingCondition = None
                            AbstractBoundingCondition = None
                            HalfSpaceBoundingCondition = None
                            BoundingBox = None
                        ConvexHull = None
                        class splines:
                            TorsionalMotionTimeVariantSurfaceBSpline2 = None
                            ClosedCubicBSpline = None
                            ShiftTimeVariantSurfaceBSpline = None
                            SurfaceUniformCubicBSpline = None
                            BSpline = None
                            TimeVariantSurfaceBSpline = None
                            NearestNeighborTimeVariantSurfaceBSpline = None
                            SurfaceBSpline = None
                            SurfaceBSplineVolumePhantom = None
                            SplineTests = None
                            TorsionalMotionTimeVariantSurfaceBSpline = None
                            class fitting:
                                BSplineCurveInterpolation = None
                                BSplineSurfaceInterpolation = None
                            UniformCubicBSpline = None
                            MotionDefectTimeVariantSurfaceBSpline = None
                        Rotations = None
                    class reconstruction:
                        CPUSuperShortScanBackprojector = None
                        class test:
                            IterativeReconstructionTestA = None
                            IterativeReconstructionTestB = None
                        FBPReconstructionFilter = None
                        ReconstructionFilter = None
                        class voi:
                            VolumeOfInterest = None
                            PolygonBasedVolumeOfInterest = None
                            CylinderBasedVolumeOfInterest = None
                        SimpleIterativeReconstruction = None
                        MotionCompensatedSubVolumeBackprojector = None
                        class iterative:
                            SeparableFootprints = None
                            SeparableFootprintsBasedReconstruction = None
                            RayDrivenBasedReconstruction = None
                            PenalizedLeastSquareART = None
                            huberPenalty = None
                            LeastSquaresCG = None
                            ModelBasedIterativeReconstruction = None
                            IterativeReconstruction = None
                            DistanceDrivenBasedReconstruction = None
                        SuperShortScanBackprojection = None
                        SeparableFootprintsBasedReconstruction = None
                        RayDrivenBasedReconstruction = None
                        RayWeightCorrectingCPUSuperShortScanBackprojector = None
                        MotionCompensatedVOIBasedReconstructionFilter = None
                        ModelBasedIterativeReconstruction = None
                        RigidBody3DTransformationVOIBasedReconstructionFilterForXCAT = None
                        IterativeReconstruction = None
                        DistanceDrivenBasedReconstruction = None
                        LolaBunnyBackprojector = None
                        RigidBody3DTransformationVOIBasedReconstructionFilter = None
                        SubVolumeBackprojector = None
                        VOIBasedReconstructionFilter = None
                    class utils:
                        class parsers:
                            SceneFileParser = None
                            ParserFactory = None
                            SliceWorkerParser = None
                        UserUtil = None
                        BilinearInterpolatingDoubleArray = None
                        FileJoiner = None
                        FileUtil = None
                        DoublePrecisionPointUtil = None
                        StatisticsUtil = None
                        LinearInterpolatingDoubleArray = None
                        CONRAD = None
                        ImageUtil = None
                        DicomDecoder = None
                        StringFileFilter = None
                        DoubleArrayUtil = None
                        TessellationUtil = None
                        DicomConfigurationUpdater = None
                        class interpolation:
                            LogLinearInterpolator = None
                            NumberInterpolatingTreeMap = None
                            Interpolator = None
                            LogLogInterpolator = None
                            LinearInterpolator = None
                        FFTUtil = None
                        FloatArrayUtil = None
                        VisualizationUtil = None
                        ImageGridBuffer = None
                        FHTUtil = None
                        TestingTools = None
                        ConfigurationUpdater = None
                        GUIUtil = None
                        RegKeys = None
                        XmlUtils = None
                        Configuration = None
                    class calibration:
                        PrincipalComponentAnalysis2D = None
                        GeometricCalibrationGUI = None
                        GeometricCalibration = None
                        class crossratios:
                            BeadDetection = None
                            CreateCalibration = None
                            CreateProjectionData = None
                        Factorization = None
                        CalibrationBead = None
                    class metric:
                        ImageMetric = None
                        NormalizedImprovement = None
                        MeanSquareErrorMetric = None
                        NormalizedImageMetric = None
                        RootMeanSquareErrorMetric = None
                    class physics:
                        PhysicalObject = None
                        class detector:
                            XRayDetector = None
                            SimpleMonochromaticDetector = None
                            SimplePolychromaticDetector = None
                            PolychromaticDetectorWithNoise = None
                            MaterialPathLengthDetector = None
                        class absorption:
                            SelectableEnergyMonochromaticAbsorptionModelWithNoise = None
                            SelectableEnergyMonochromaticAbsorptionModel = None
                            AbsorptionModel = None
                            PathLengthHistogramCreatingAbsorptionModel = None
                            PolychromaticAbsorptionModel = None
                            DensityAbsorptionModel = None
                        PolychromaticXRaySpectrum = None
                        LambdaFunction = None
                        EnergyDependentCoefficients = None
                        PhysicalPoint = None
                        Constants = None
                        HalfValueLayerFunction = None
                        class materials:
                            WeightedAtomicComposition = None
                            Material = None
                            class database:
                                ElementalMassAttenuationData = None
                                CompositionToAbsorptionEdgeMap = None
                                NameToFormulaMap = None
                                MaterialsDB = None
                                class xmldatagenerators:
                                    RebuildMaps = None
                                    RebuildDatabase = None
                                    RebuildMaterialDatabase = None
                                OnlineMassAttenuationDB = None
                                FormulaToNameMap = None
                            Mixture = None
                            class utils:
                                WeightedAtomicComposition = None
                                AttenuationType = None
                                AttenuationRetrievalMode = None
                                LocalMassAttenuationCalculator = None
                                MaterialUtils = None
                            Compound = None
                            class materialsTest:
                                TestMassAttenuationData = None
                            Element = None
                        XRaySpectrum = None
                    class fitting:
                        LinearFunction = None
                        class test:
                            FunctionTest = None
                        GaussianFunction = None
                        LogarithmicFunction = None
                        Surface = None
                        IdentityFunction = None
                        Function = None
                        ConstrainedRANSACFittedFunction = None
                        PolynomialFunction = None
                        Quadric = None
                        RANSACFittedFunction = None
                    class phantom:
                        XNPhantom = None
                        class electrondensity:
                            CrisEDPhantomGUI = None
                            EDInnerDisk = None
                            CrisEDPhantomM062 = None
                            EDOuterDisk = None
                            QuadricDisk = None
                            Insert = None
                        RandomizedHelixPhantom = None
                        SheppLoganPhantom = None
                        BonePhantom = None
                        SevenBeadPhantom = None
                        AnalyticPhantom = None
                        AnalyticPhantom4D = None
                        SpherePhantom = None
                        CatphanCTP528 = None
                        PyramidPhantom = None
                        class workers:
                            SliceWorker = None
                            DiracProjectionPhantom = None
                            VolumeOfInterestPhantom = None
                            AnalyticPhantom3DVolumeRenderer = None
                            MultiMaterialPhantom3DVolumeRenderer = None
                            AnalyticPhantomProjectorWorker = None
                            SheppLoganPhantomWorker = None
                        RandomDistributionPhantom = None
                        SimpleShapeTestPhantom = None
                        DefrisePhantom = None
                        NumericalSheppLogan3D = None
                        MovingBallPhantom = None
                        BoxPhantom = None
                        AffineMotionPhantom = None
                        class forbild:
                            ForbildShapeFactory = None
                            class shapes:
                                ForbildSphere = None
                                ForbildCone = None
                                ForbildEllipsoid = None
                                ForbildBox = None
                                ForbildCylinder = None
                            ForbildParser = None
                            ForbildPhantom = None
                        ConePhantom = None
                        EllipsoidPhantom = None
                        class xcat:
                            CoronaryScene = None
                            ViconAffineTransform = None
                            XCatScene = None
                            SquatScene = None
                            XCatMaterialGenerator = None
                            TessellationThread = None
                            BreathingScene = None
                            WholeBodyScene = None
                            ViconMarkerBuilder = None
                            HeartScene = None
                            CombinedBreathingHeartScene = None
                            DynamicSquatScene = None
                        CatheterPhantom = None
                        AsciiSTLMeshPhantom = None
                        WaterCylinderPhantom = None
                        class renderer:
                            PhantomRenderer = None
                            MetricPhantomRenderer = None
                            ParallelProjectionPhantomRenderer = None
                            AnalyticPhantomProjector = None
                            StreamingPhantomRenderer = None
                            CylinderPhantomRenderer = None
                            RampProjectionPhantomRenderer = None
                            SliceParallelVolumePhantomRenderer = None
                        class asmheart:
                            PredefinedModels = None
                            CONRADCardiacModel4D = None
                            CONRADCardiacModelConfig = None
                            CONRADCardiacModel3D = None
                        SheppLogan3D = None
                        BeadRemovalPhantom = None
                        MathematicalPhantom = None
                        AbstractCalibrationPhantom = None
                        SinoPhantom = None
                        MTFBeadPhantom = None
                        TrigonometryPhantom = None
                        CirclesPhantom = None
                    class pipeline:
                        ParallelImageFilterPipeliner = None
                        DevNullSink = None
                        BufferedProjectionSink = None
                        ParallelProjectionDataSinkFeeder = None
                        PipelineTests = None
                        ParallelImageFilterSink = None
                        IndividualImagePipelineFilteringTool = None
                        ProjectionSink = None
                        ProjectionSource = None
                    class cuda:
                        MouseControlable = None
                        CUDAFFTVolumeHandle = None
                        CUDABackProjector = None
                        MouseControl = None
                        ImagePlusVolumeRenderer = None
                        AdjustablePointer = None
                        CUDAVolumeOperator = None
                        CUDAForwardProjector = None
                        CUDAForwardProjectorWithMotion = None
                        CUDACompensatedBackProjector = None
                        JCudaRuntimeSample = None
                        CUDAVolumeTest = None
                        JCudaDriverTextureSample = None
                        CUDAVolume3D = None
                        CUDAUtil = None
                        class splines:
                            CUDABSpline = None
                    class opencl:
                        OpenCLEdgeForwardProjector = None
                        OpenCLProjectionPhantomRenderer = None
                        class rendering:
                            MouseControlable = None
                            MouseControl = None
                            OpenCLTextureRendering = None
                            OpenCLVolumeRenderer = None
                        OpenCLSurfacePhantomRenderer = None
                        OpenCLYBufferRenderer = None
                        OpenCLUtil = None
                        OpenCLBackProjector = None
                        TestOpenCL = None
                        OpenCLDetectorMotionBackProjector = None
                        OpenCLRenderer = None
                        class shapes:
                            OpenCLSphere = None
                            OpenCLCompoundShape = None
                            OpenCLEllipsoid = None
                            OpenCLUniformTextureBSpline = None
                            OpenCLUniformTextureSurfaceBSpline = None
                            OpenCLBox = None
                            OpenCLUniformBSpline = None
                            OpenCLTextureTimeVariantSurfaceBSpline = None
                            OpenCLPyramid = None
                            OpenCLCone = None
                            OpenCLCylinder = None
                            OpenCLUniformSurfaceBSpline = None
                            OpenCLTimeVariantSurfaceBSpline = None
                        OpenCLForwardProjector = None
                        OpenCLForwardProjectorDynamicVolume = None
                        OpenCLJointBilateralFilteringTool = None
                        OpenCLEvaluatable = None
                        OpenCLMaterialPathLengthPhantomRenderer = None
                        class GLCLDemo:
                            UserSceneInteraction = None
                            GLCLInteroperabilityDemo = None
                        OpenCLAppendBufferRenderer = None
                        OpenCLForwardProjectorWithMotion = None
    Normalize_Image_MinMax = None
    Generate_Absorption_Plot = None
    Apply_Filter = None
    Viva_Reader = None
    OpenCL_Back_Projector = None
    Count_Edge_Points = None
    Check_Trajectory_Consistency = None
    SaveAs_Viva = None
    Nrrd_Reader = None
    ZIP_Reader_Standalone = None
    Nurbs_Reader = None
    Measure_MTF_Droege = None
    Apply_ROI_Method = None
    Dennerlein_Writer = None
    Raw_Data_Opener = None
    Create_Numerical_Phantom = None
    FlexibleFileOpener = None
    Measure_MTF_Wire = None
    Raw_Data_Opener_Standalone = None
