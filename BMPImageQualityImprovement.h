#ifndef MISOI2_BMPIMAGEQUALITYIMPROVEMENT_H
#define MISOI2_BMPIMAGEQUALITYIMPROVEMENT_H


#include <iostream>
#include <Windows.h>
#include <math.h>
#include <vector>
#include <fstream>
#include <string>
#include <random>
#include <algorithm>

#define PI 3.14159265

template<typename T> using matrix = std::vector<std::vector<T>>;


class BMPImageQualityImprovement {
private:
    matrix<double> R;
    matrix<double> G;
    matrix<double> B;
    matrix<double> Y;
    matrix<double> changedY;
    matrix<double> thr127;
    std::string imagePath = "C:/Users/akopo/CLionProjects/misoi2/Images/";
    std::string pythonPath = "C:/Users/akopo/CLionProjects/misoi2/python/";

public:
    BMPImageQualityImprovement(std::string filename);
    BMPImageQualityImprovement(BMPImageQualityImprovement& copy);
    void readFile(std::string filename);
    void writeYcomponentFile(std::string filename);
    void writeFullColorFile(std::string filename, matrix<RGBTRIPLE> map);
    BYTE clipping(double value);
    double clippingDouble(double value);
    void RGBToY();
    double PSNR(matrix<double> original, matrix<double> recovery);
    double gaussrand(double expectation, double sigma);
    void additiveNoiseModel(double expectation, double sigma);
    void impulseNoiseModel(double Pa, double Pb);
    void frequencyHistogram(std::string filename, matrix<double> component);
    void additiveNoisePSNRgraphics(double sigmaRight, double sigmaLeft, double step);
    void impulseNoisePSNRgraphics(double PaRight, double PaLeft, double PaStep);
    matrix<double> extendedY(int R, bool thr = false);
    void movingAverageMethod(int R);
    void movingAverageMethodMaximizePSNR(int rightR, int leftR);
    void gaussFilter(int R, double sigma);
    void gaussFilterPSNRgraphics(double sigmaRight, double sigmaLeft, double step);
    void medianFilter(int R);
    void medianFilterPSNRgraphics(int rightR, int leftR);
    void impulseNoiseProcessing(int rightR, int leftR);
    void laplasian(int R, double alpha);
    void laplasImage1(std::string filename);
    void laplasFrequencyGainImage(std::string filename, double alpha);
    void laplasHFGalpha1to15();
    double averageBrightness(matrix<double> component);
    std::vector<matrix<double>> sobelOperator(int R = 1, bool thr = false);
    void thresholding();
    void gradientDirectionMap();
    void basedOnTwoReferencePoints(int x1, int y1, int x2, int y2);
    void twoReferencePointsGraphics(int x1, int y1, int x2, int y2);
    void twoReferencePointsProcessing(int x1, int y1, int x2, int y2);
    void gammaCorrection(int img);
    void gammaCorrectionGraphics();
    void histogramAlignment();
    void histogramAlignmentProcessing();
    void thresholdForContourMap();
    matrix<double> getY();
    matrix<double> getChangedY();
};


#endif //MISOI2_BMPIMAGEQUALITYIMPROVEMENT_H
