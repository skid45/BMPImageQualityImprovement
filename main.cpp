#include "BMPImageQualityImprovement.h"

int main() {
    BMPImageQualityImprovement original("pepper");
//3
//    original.additiveNoisePSNRgraphics(0, 105, 15);
//    original.impulseNoisePSNRgraphics(0, 0.5, 0.1);
//    system("C:/Users/akopo/CLionProjects/misoi2/python/3.py");
//    system("C:/Users/akopo/CLionProjects/misoi2/python/ImgAndHist3.py");

//4
//    original.movingAverageMethodMaximizePSNR(0, 3);
//    system("C:/Users/akopo/CLionProjects/misoi2/python/MovingAveragePSNR4.py");
//
//    original.gaussFilterPSNRgraphics(20, 20, 1);
//    system("C:/Users/akopo/CLionProjects/misoi2/python/GaussPSNR4.py");
//
//    original.medianFilterPSNRgraphics(0, 3);
//    system("C:/Users/akopo/CLionProjects/misoi2/python/MedianFilterPSNR4.py");

//5
//    original.impulseNoiseProcessing(0, 5);
//    system("C:/Users/akopo/CLionProjects/misoi2/python/ImpulseNoiseProcessing5.py");

//6
//    original.laplasImage1("FirstLaplasianImage");
//    original.laplasFrequencyGainImage("HighFrequencyGainImage", 1);
//    original.laplasHFGalpha1to15();
//    system("C:/Users/akopo/CLionProjects/misoi2/python/laplasHist.py");

//7
//    original.thresholding();
//    original.gradientDirectionMap();

//8
//    original.twoReferencePointsProcessing(50, 150, 200, 70);
//    system("C:/Users/akopo/CLionProjects/misoi2/python/TwoReferencePoints.py");

//9
//    original.gammaCorrectionGraphics();
//    system("C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrection.py");

//10
//    original.histogramAlignmentProcessing();
//    system("C:/Users/akopo/CLionProjects/misoi2/python/HistogramAlignment.py");

//11
    original.thresholdForContourMap();

    //system("pause");
    return 0;
}