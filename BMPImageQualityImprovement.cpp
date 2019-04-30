#include "BMPImageQualityImprovement.h"


BMPImageQualityImprovement::BMPImageQualityImprovement(std::string filename) {
    readFile(filename);
    RGBToY();
    writeYcomponentFile("originalY.bmp");
}

BMPImageQualityImprovement::BMPImageQualityImprovement(BMPImageQualityImprovement& copy) {
    this->R = copy.R;
    this->G = copy.G;
    this->B = copy.B;
    this->Y = copy.Y;
    this->changedY = copy.changedY;
}

void BMPImageQualityImprovement::readFile(std::string filename) {
    std::string str = imagePath + filename + ".bmp";
    const char* a = str.c_str();

    FILE* image;
    fopen_s(&image, a, "rb");

    BITMAPFILEHEADER file_header;
    BITMAPINFOHEADER info_header;

    fread(&file_header, sizeof(file_header), 1, image);
    fread(&info_header, sizeof(info_header), 1, image);
    DWORD padding = ((4 - (info_header.biWidth * 3) % 4) & 3);
    RGBTRIPLE **triple = new RGBTRIPLE *[info_header.biHeight];
    for (int i = 0; i < info_header.biHeight; i++) {
        triple[i] = new RGBTRIPLE[info_header.biWidth];
        fread(&triple[i][0], sizeof(RGBTRIPLE), info_header.biWidth, image);
        if (padding != 0) {
            fread(&triple[i][0], padding, 1, image);
        }
    }
    fclose(image);


    for (int i = 0; i < info_header.biHeight; i++) {
        std::vector<double> Rvec;
        std::vector<double> Gvec;
        std::vector<double> Bvec;
        for (int j = 0; j < info_header.biWidth; j++) {
            Rvec.push_back(static_cast<double>(triple[i][j].rgbtRed));
            Gvec.push_back(static_cast<double>(triple[i][j].rgbtGreen));
            Bvec.push_back(static_cast<double>(triple[i][j].rgbtBlue));
        }
        R.push_back(Rvec);
        G.push_back(Gvec);
        B.push_back(Bvec);
    }


    for (int i = 0; i < info_header.biHeight; i++) {
        delete[] triple[i];
    }
    delete[] triple;
}


void BMPImageQualityImprovement::writeYcomponentFile(std::string filename) {
    std::string str = imagePath + filename + ".bmp";
    const char* a = str.c_str();

    DWORD padding = ((4 - (changedY[0].size() * 3) % 4) & 3);
    DWORD size = 3 * static_cast<DWORD>(changedY.size()) * static_cast<DWORD>(changedY[0].size())
                 + static_cast<DWORD>(padding) * static_cast<DWORD>(changedY.size());

    BITMAPFILEHEADER file_header = { 19778, size + 54, 0, 0, 54 };
    BITMAPINFOHEADER info_header = { 40, static_cast<LONG>(changedY[0].size()), static_cast<LONG>(changedY.size()),
                                     1, 24, 0, size, 0, 0, 0, 0 };

    FILE *file;
    fopen_s(&file, a, "wb");
    fwrite(&file_header, sizeof(BITMAPFILEHEADER), 1, file);
    fwrite(&info_header, sizeof(BITMAPINFOHEADER), 1, file);

    RGBTRIPLE **triple = new RGBTRIPLE *[info_header.biHeight];
    for (int i = 0; i < info_header.biHeight; i++) {
        triple[i] = new RGBTRIPLE[info_header.biWidth];
        for (int j = 0; j < info_header.biWidth; j++) {
            triple[i][j].rgbtRed = static_cast<BYTE>(changedY[i][j]);
            triple[i][j].rgbtGreen = static_cast<BYTE>(changedY[i][j]);
            triple[i][j].rgbtBlue = static_cast<BYTE>(changedY[i][j]);

            fwrite(&triple[i][j], sizeof(RGBTRIPLE), 1, file);
        }
        if (padding != 0) {
            fwrite(&triple[i][0], padding, 1, file);
        }
    }
    fclose(file);

    for (int i = 0; i < info_header.biHeight; i++) {
        delete[] triple[i];
    }
    delete[] triple;
}

void BMPImageQualityImprovement::writeFullColorFile(std::string filename, matrix<RGBTRIPLE> map) {
    std::string str = imagePath + filename + ".bmp";
    const char* a = str.c_str();

    DWORD padding = ((4 - (map[0].size() * 3) % 4) & 3);
    DWORD size = 3 * static_cast<DWORD>(map.size()) * static_cast<DWORD>(map[0].size())
                 + static_cast<DWORD>(padding) * static_cast<DWORD>(map.size());

    BITMAPFILEHEADER file_header = { 19778, size + 54, 0, 0, 54 };
    BITMAPINFOHEADER info_header = { 40, static_cast<LONG>(map[0].size()), static_cast<LONG>(map.size()),
                                     1, 24, 0, size, 0, 0, 0, 0 };

    FILE *file;
    fopen_s(&file, a, "wb");
    fwrite(&file_header, sizeof(BITMAPFILEHEADER), 1, file);
    fwrite(&info_header, sizeof(BITMAPINFOHEADER), 1, file);

    for (int i = 0; i < info_header.biHeight; i++) {
        for (int j = 0; j < info_header.biWidth; j++) {
            fwrite(&map[i][j], sizeof(RGBTRIPLE), 1, file);
        }
        if (padding != 0) {
            fwrite(&map[i][0], padding, 1, file);
        }
    }
    fclose(file);
}

BYTE BMPImageQualityImprovement::clipping(double value) {
    if (value > 255) return 255;
    else if (value < 0) return 0;
    return static_cast<BYTE>(value);
}

double BMPImageQualityImprovement::clippingDouble(double value) {
    if (value > 255) return 255;
    else if (value < 0) return 0;
    return value;
}

void BMPImageQualityImprovement::RGBToY() {
    matrix<double> Ymatrix;
    for (int i = 0; i < static_cast<int>(R.size()); i++) {
        std::vector<double> Yvec;
        for (int j = 0; j < static_cast<int>(R[0].size()); j++) {
            Yvec.push_back(clipping((0.299 * R[i][j]) + (0.587 * G[i][j]) + (0.114 * B[i][j])));
        }
        Ymatrix.push_back(Yvec);
    }
    this->Y = Ymatrix;
    this->changedY = Ymatrix;
}

double BMPImageQualityImprovement::PSNR(matrix<double> original, matrix<double> recovery) {
    double numerator = static_cast<double>(original.size()) * static_cast<double>(original[0].size());
    numerator *= 65025.0;
    double denominator = 0;

    for (int i = 0; i < static_cast<int>(original.size()); i++) {
        for (int j = 0; j < static_cast<int>(original[0].size()); j++) {
            denominator += ((original[i][j] - recovery[i][j]) * (original[i][j] - recovery[i][j]));
        }
    }

    return 10.0 * std::log10(numerator / denominator);
}

double BMPImageQualityImprovement::gaussrand(double expectation, double sigma) {
    double sum = 0, x;
    for (int i = 0; i < 28; i++)
        sum += 1.0 * rand() / RAND_MAX;
    x = (sqrt(2.0) * (sigma) * (sum - 14.0)) / 2.11233 + expectation;
    return x;
}

void BMPImageQualityImprovement::additiveNoiseModel(double expectation, double sigma) {
    matrix<double> noisyY;
    for (int i = 0; i < static_cast<int>(Y.size()); i++) {
        std::vector<double> Yvector;
        for (int j = 0; j < static_cast<int>(Y[0].size()); j++) {
            Yvector.push_back(clipping(this->Y[i][j] + gaussrand(expectation, sigma)));
        }
        noisyY.push_back(Yvector);
    }
    this->changedY = noisyY;
}

void BMPImageQualityImprovement::impulseNoiseModel(double Pa, double Pb) {
    matrix<double> noisyY;
    for (int i = 0; i < static_cast<int>(Y.size()); i++) {
        std::vector<double> Yvector;
        for (int j = 0; j < static_cast<int>(Y[0].size()); j++) {
            double p = 1.0 * rand() / RAND_MAX;
            if (p < Pa) Yvector.push_back(0);
            else if (p >= Pa && p < (Pb + Pa)) Yvector.push_back(255);
            else if (p >= (Pa + Pb)) Yvector.push_back(clipping(this->Y[i][j]));
        }
        noisyY.push_back(Yvector);
    }
    this->changedY = noisyY;
}

void BMPImageQualityImprovement::frequencyHistogram(std::string filename, matrix<double> component) {
    std::ofstream file(pythonPath + filename, std::ios_base::out | std::ios_base::binary);
    for (const auto &vector : component)
        for (const auto &pixel : vector)
            file << static_cast<int>(pixel) << ' ';

    file.close();
}

void BMPImageQualityImprovement::additiveNoisePSNRgraphics(double sigmaRight, double sigmaLeft, double step) {
    std::ofstream DataFile(pythonPath + "additivePSNR3data", std::ios_base::out | std::ios_base::binary);
    DataFile << sigmaRight << std::endl << sigmaLeft << std::endl << step;

    std::ofstream ValueFile(pythonPath + "additivePSNR3", std::ios_base::out | std::ios_base::binary);
    for (double i = sigmaRight, j = 0; i <= sigmaLeft; i += step, j++) {
        additiveNoiseModel(0, i);
        ValueFile << PSNR(Y, changedY) << ' ';
        writeYcomponentFile("AdditiveNoise" + std::to_string(static_cast<int>(j)));
        matrix<double> dif = getChangedY();
        for (int k = 0; k < static_cast<int>(dif.size()); ++k) {
            for (int l = 0; l < static_cast<int>(dif[0].size()); ++l) {
                dif[k][l] -= Y[k][l];
            }
        }
        frequencyHistogram("AdditiveNoiseHist" + std::to_string(static_cast<int>(j)), dif);
    }
}

void BMPImageQualityImprovement::impulseNoisePSNRgraphics(double PaRight, double PaLeft, double PaStep) {
    std::ofstream DataFile(pythonPath + "impulsePSNR3data", std::ios_base::out | std::ios_base::binary);
    DataFile << PaRight << std::endl << PaLeft << std::endl << PaStep;

    std::ofstream ValueFile(pythonPath + "impulsePSNR3", std::ios_base::out | std::ios_base::binary);
    for (double i = PaRight, j = 0; i <= PaLeft; i += PaStep, j++) {
        impulseNoiseModel(i, i);
        ValueFile << PSNR(Y, changedY) << ' ';
        writeYcomponentFile("ImpulseNoise" + std::to_string(static_cast<int>(j)));
        frequencyHistogram("ImpulseNoiseHist" + std::to_string(static_cast<int>(j)), getChangedY());
    }
}

matrix<double> BMPImageQualityImprovement::extendedY(int R, bool thr) {
    matrix<double> extendedMatrix;

    matrix<double> comp;
    if(thr == false) {
        comp = changedY;
    }
    else{
        comp = thr127;
    }

    for (int i = 0; i < static_cast<int>(comp.size()); i++) {
        if (i == 0) {
            for (int j = 0; j <= R; j++) {
                extendedMatrix.push_back(comp[0]);
            }
            continue;
        }
        if (i == (static_cast<int>(comp.size()) - 1)) {
            for (int j = 0; j <= R; j++) {
                extendedMatrix.push_back(comp[i]);
            }
            continue;
        }
        extendedMatrix.push_back(comp[i]);
    }

    for (int i = 0; i < static_cast<int>(extendedMatrix.size()); i++) {
        for (int j = 0; j < R; j++) {
            extendedMatrix[i].push_back(extendedMatrix[i][comp[0].size() - 1]);
        }
    }

    std::vector<double>::iterator it;
    for (int i = 0; i < static_cast<int>(extendedMatrix.size()); i++) {
        for (int j = 0; j < R; j++) {
            it = extendedMatrix[i].begin();
            extendedMatrix[i].insert(it, extendedMatrix[i][0]);
        }
    }

    return extendedMatrix;
}

void BMPImageQualityImprovement::movingAverageMethod(int R) {
    matrix<double> extendedMatrix = extendedY(R);

    matrix<double> res;
    for (int i = R; i < static_cast<int>(extendedMatrix.size()) - R; i++) {
        std::vector<double> Yvector;
        for (int j = R; j < static_cast<int>(extendedMatrix[0].size()) - R; j++) {
            double sum = 0;
            for (int k = -(R); k <= R; k++) {
                for (int m = -(R); m <= R; m++) {
                    sum += extendedMatrix[i + k][j + m];
                }
            }
            Yvector.push_back(clipping(sum / ((2 * R + 1) * (2 * R + 1))));
        }
        res.push_back(Yvector);
    }
    this->changedY = res;
}

void BMPImageQualityImprovement::movingAverageMethodMaximizePSNR(int rightR, int leftR) {
    std::ofstream DataFile(pythonPath + "MovingAveragePSNR4data", std::ios_base::out | std::ios_base::binary);
    DataFile << rightR << std::endl << leftR;

    std::ofstream ValueFile(pythonPath + "MovingAveragePSNR4", std::ios_base::out | std::ios_base::binary);
    for (int i = rightR, j = 0; i <= leftR; i++, j++) {
        additiveNoiseModel(0, 30);
        movingAverageMethod(i);
        writeYcomponentFile("MovingAverageMethodR=" + std::to_string(i) + "PSNR=" + std::to_string(PSNR(Y, changedY)));
        ValueFile << PSNR(Y, changedY) << ' ';
    }
}

void BMPImageQualityImprovement::gaussFilter(int R, double sigma) {
    matrix<double> extendedMatrix = extendedY(R);

    matrix<double> res;
    for (int i = R; i < static_cast<int>(extendedMatrix.size()) - R; i++) {
        std::vector<double> Yvector;
        for (int j = R; j < static_cast<int>(extendedMatrix[0].size()) - R; j++) {
            double sum = 0;
            double normalizationCoef = 0;
            for (int k = -(R); k <= R; k++) {
                for (int m = -(R); m <= R; m++) {
                    double w = exp((-((k * k) + (m * m))) / (2 * (sigma * sigma)));
                    normalizationCoef += w;
                    sum += w * extendedMatrix[i + k][j + m];
                }
            }
            Yvector.push_back(clipping(sum / normalizationCoef));
        }
        res.push_back(Yvector);
    }
    this->changedY = res;
}

void BMPImageQualityImprovement::gaussFilterPSNRgraphics(double sigmaRight, double sigmaLeft, double step) {
    std::ofstream DataFile(pythonPath + "GaussFilterPSNR4data", std::ios_base::out | std::ios_base::binary);
    DataFile << sigmaRight << std::endl << sigmaLeft << std::endl << step;

    std::ofstream ValueFile(pythonPath + "GaussFilterPSNR4", std::ios_base::out | std::ios_base::binary);
    for (int R = 0; R <= 3; R++) {
        std::vector<double> PSNRValue;

        for (double j = sigmaRight; j <= sigmaLeft; j += step) {
            additiveNoiseModel(0, 30);
            gaussFilter(R, j);
            double PSNRtmp = PSNR(Y, changedY);
            ValueFile << PSNRtmp << ' ';
            PSNRValue.push_back(PSNRtmp);
        }
        ValueFile << std::endl;

        additiveNoiseModel(0, 30);
        int max_elem = std::distance(PSNRValue.begin(), std::max_element(PSNRValue.begin(), PSNRValue.end()));
        gaussFilter(R, sigmaRight + (step * max_elem));
        writeYcomponentFile("GaussFilterForR=" + std::to_string(R) + "andSigma=" + std::to_string(sigmaRight + (step * max_elem)) + "PSNR=" + std::to_string(PSNR(Y, changedY)));
    }
}

void BMPImageQualityImprovement::medianFilter(int R) {
    matrix<double> extendedMatrix = extendedY(R);

    matrix<double> res;
    for (int i = R; i < static_cast<int>(extendedMatrix.size()) - R; i++) {
        std::vector<double> Yvector;
        for (int j = R; j < static_cast<int>(extendedMatrix[0].size()) - R; j++) {
            std::vector<double> median;
            for (int k = -(R); k <= R; k++) {
                for (int m = -(R); m <= R; m++) {
                    median.push_back(extendedMatrix[i + k][j + m]);
                }
            }
            std::sort(median.begin(), median.end());
            if(median.size() > 1) {
                Yvector.push_back(clipping(median[static_cast<unsigned int>(floor(((2 * R + 1) * (2 * R + 1)) / 2) + 1)]));
            }
            else{
                Yvector.push_back(clipping(median[0]));
            }
        }
        res.push_back(Yvector);
    }
    this->changedY = res;
}

void BMPImageQualityImprovement::medianFilterPSNRgraphics(int rightR, int leftR) {
    std::ofstream DataFile(pythonPath + "MedianFilterPSNR4data", std::ios_base::out | std::ios_base::binary);
    DataFile << rightR << std::endl << leftR;

    std::ofstream ValueFile(pythonPath + "MedianFilterPSNR4", std::ios_base::out | std::ios_base::binary);
    for (int i = rightR, j = 0; i <= leftR; i++, j++) {
        additiveNoiseModel(0, 30);
        medianFilter(i);
        writeYcomponentFile("MedianFilterR=" + std::to_string(i) + "PSNR=" + std::to_string(PSNR(Y, changedY)));
        ValueFile << PSNR(Y, changedY) << ' ';
    }
}

void BMPImageQualityImprovement::impulseNoiseProcessing(int rightR, int leftR) {
    std::vector<double> p = {0.05, 0.1, 0.25, 0.5};
    std::ofstream ValueFile(pythonPath + "ImpulseNoiseProcessing5", std::ios_base::out | std::ios_base::binary);

    for (int i = 0; i < static_cast<int>(p.size()); ++i) {
        impulseNoiseModel(p[i], p[i]);
        writeYcomponentFile("OriginalImpulseNoiseImageWithP="+ std::to_string(p[i]));
        ValueFile << PSNR(Y, changedY) << std::endl;
        for (int j = rightR; j <= leftR; j++) {
            impulseNoiseModel(p[i], p[i]);
            medianFilter(j);
            writeYcomponentFile("ImpulseNoiseImageAfterMedianFilterWithP="+ std::to_string(p[i]) + "andR" + std::to_string(j));
            ValueFile << PSNR(Y, changedY) << ' ';
        }
        ValueFile << std::endl;
    }
}

void BMPImageQualityImprovement::laplasian(int R, double alpha) {
    matrix<double> extendedMatrix = extendedY(R);
    std::vector<double> w = {0, -1, 0, -1, alpha + 4, -1, 0, -1, 0};

    matrix<double> res;
    for (int i = R; i < static_cast<int>(extendedMatrix.size()) - R; i++) {
        std::vector<double> Yvector;
        for (int j = R; j < static_cast<int>(extendedMatrix[0].size()) - R; j++) {
            double sum = 0;
            int countW = 0;
            for (int k = -(R); k <= R; k++) {
                for (int m = -(R); m <= R; m++) {
                    sum += w[countW] * extendedMatrix[i + k][j + m];
                    countW++;
                }
            }
            Yvector.push_back(sum);
        }
        res.push_back(Yvector);
    }
    this->changedY = res;
}

void BMPImageQualityImprovement::laplasImage1(std::string filename) {
    laplasian(0, 0);
    matrix<double> res;
    for (int i = 0; i < static_cast<int>(changedY.size()); i++) {
        std::vector<double> vector;
        for (int j = 0; j < static_cast<int>(changedY[0].size()); j++) {
            vector.push_back(clipping(changedY[i][j] + 128));
        }
        res.push_back(vector);
    }
    this->changedY = res;
    writeYcomponentFile(filename);
    this->changedY = Y;
}

void BMPImageQualityImprovement::laplasFrequencyGainImage(std::string filename, double alpha) {
    laplasian(1, alpha);
    matrix<double> res;
    for (int i = 0; i < static_cast<int>(changedY.size()); i++) {
        std::vector<double> vector;
        for (int j = 0; j < static_cast<int>(changedY[0].size()); j++) {
            vector.push_back(clipping(changedY[i][j] + Y[i][j]));
        }
        res.push_back(vector);
    }
    this->changedY = res;
    writeYcomponentFile(filename);
    frequencyHistogram(filename, changedY);
    std::cout<< "Average britness for alpha = " + std::to_string(alpha) + ": " << averageBrightness(changedY) << std::endl;
    this->changedY = Y;
}

void BMPImageQualityImprovement::laplasHFGalpha1to15() {
    frequencyHistogram("histOriginalImage", Y);
    std::cout<< "Average britness for original image: " << averageBrightness(Y) << std::endl;
    for (double i = 1.0; i < 1.6; i += 0.1) {
        laplasFrequencyGainImage("laplasHFGalpha=" + std::to_string(i), i);
    }
}

double BMPImageQualityImprovement::averageBrightness(matrix<double> component) {
    double sum = 0;
    for (int i = 0; i < static_cast<int>(component.size()); ++i) {
        for (int j = 0; j < static_cast<int>(component[0].size()); ++j) {
            sum += component[i][j];
        }
    }
    return (sum / (component.size() * component[0].size()));
}

std::vector<matrix<double>> BMPImageQualityImprovement::sobelOperator(int R, bool thr) {
    matrix<double> extendedMatrix = extendedY(R);
    std::vector<double> horizontal = {-1, 0, 1, -2, 0, 2, -1, 0, 1};
    std::vector<double> vertical = {1, 2, 1, 0, 0, 0, -1, -2, -1};

    matrix<double> I;
    matrix<double> Theta;
    for (int i = R; i < static_cast<int>(extendedMatrix.size()) - R; i++) {
        std::vector<double> Ivector;
        std::vector<double> Thetavector;
        for (int j = R; j < static_cast<int>(extendedMatrix[0].size()) - R; j++) {
            double sumH = 0;
            double sumV = 0;
            int countW = 0;
            for (int k = -(R); k <= R; k++) {
                for (int m = -(R); m <= R; m++) {
                    sumH += horizontal[countW] * extendedMatrix[i + k][j + m];
                    sumV += vertical[countW] * extendedMatrix[i + k][j + m];
                    countW++;
                }
            }
            Ivector.push_back(sqrt((sumH*sumH)+(sumV*sumV)));
            Thetavector.push_back(atan2(sumV, sumH));
        }
        I.push_back(Ivector);
        Theta.push_back(Thetavector);
    }
    std::vector<matrix<double>> res;
    res.push_back(I);
    res.push_back(Theta);
    return res;
}

void BMPImageQualityImprovement::thresholding() {
    matrix<double> I = sobelOperator()[0];

    for (int thr = 0; thr < 256; ++thr) {
        matrix<double> res;
        for (int i = 0; i < static_cast<int>(I.size()); ++i) {
            std::vector<double> resVector;
            for (int j = 0; j < static_cast<int>(I[0].size()); ++j) {
                if(I[i][j] > thr){
                    resVector.push_back(255);
                } else{
                    resVector.push_back(0);
                }
            }
            res.push_back(resVector);
        }
        this->changedY = res;
        if(thr == 127){
            this->thr127 = res;
        }
        writeYcomponentFile("thresholding/thr=" + std::to_string(thr));
        this->changedY = Y;
    }
}

void BMPImageQualityImprovement::gradientDirectionMap() {
    matrix<double> Theta = sobelOperator(1, true)[1];

    matrix<RGBTRIPLE> map;
    for (int i = 0; i < static_cast<int>(Theta.size()); ++i) {
        std::vector<RGBTRIPLE> mapVector;
        for (int j = 0; j < static_cast<int>(Theta[0].size()); ++j) {
            RGBTRIPLE tmp;
            if ((Theta[i][j] * 180.0 / PI) > 22.5 && (Theta[i][j] * 180.0 / PI) <= 67.5){      //45
                tmp.rgbtRed = 0;
                tmp.rgbtGreen = 255;
                tmp.rgbtBlue = 0;
            }
            else if ((Theta[i][j] * 180.0 / PI) > 67.5 && (Theta[i][j] * 180.0 / PI) <= 112.5) {
                tmp.rgbtRed = 0;
                tmp.rgbtGreen = 0;
                tmp.rgbtBlue = 255;
            }
            else if((Theta[i][j] * 180.0 / PI) > 112.5 && (Theta[i][j] * 180.0 / PI) <= 157.5) {
                tmp.rgbtRed = 255;
                tmp.rgbtGreen = 0;
                tmp.rgbtBlue = 0;
            }
            else {
                tmp.rgbtRed = 255;
                tmp.rgbtGreen = 255;
                tmp.rgbtBlue = 255;
            }
            mapVector.push_back(tmp);
        }
        map.push_back(mapVector);
    }
    writeFullColorFile("GradientDirectionMap", map);
    this->changedY = Y;
}

void BMPImageQualityImprovement::basedOnTwoReferencePoints(int x1, int y1, int x2, int y2) {
    double a1 = y1 * 1.0 / x1;
    double a2 = (y2 - y1) * 1.0 / (x2 - x1);
    double b2 = y1 - a2 * x1;
    double a3 = (255 - y2) * 1.0 / (255 - x2);
    double b3 = 255 - a3 * 255;

    matrix<double> res;
    for (int i = 0; i < static_cast<int>(Y.size()); ++i) {
        std::vector<double> resVector;
        for (int j = 0; j < static_cast<int>(Y[0].size()); ++j) {
            if(Y[i][j] < x1)    resVector.push_back(a1 * Y[i][j]);
            else if(Y[i][j] < x2)   resVector.push_back(a2 * Y[i][j] + b2);
            else   resVector.push_back(a3 * Y[i][j] + b3);
        }
        res.push_back(resVector);
    }
    this->changedY = res;
}

void BMPImageQualityImprovement::twoReferencePointsGraphics(int x1, int y1, int x2, int y2) {
    double a1 = y1 * 1.0 / x1;
    double a2 = (y2 - y1) * 1.0 / (x2 - x1);
    double b2 = y1 - a2 * x1;
    double a3 = (255 - y2) * 1.0 / (255 - x2);
    double b3 = 255 - a3 * 255;

    std::ofstream file(pythonPath + "TwoReferencePointsGraph", std::ios_base::out | std::ios_base::binary);

    for (double i = 0; i < 256; ++i) {
        if(i < x1)    file << (i * a1) << ' ';
        else if(i < x2)   file << (a2 * i + b2) << ' ';
        else   file << (a3 * i + b3) << ' ';
    }
}

void BMPImageQualityImprovement::twoReferencePointsProcessing(int x1, int y1, int x2, int y2) {
    twoReferencePointsGraphics(x1, y1, x2, y2);

    BMPImageQualityImprovement balance("Balance");
    balance.writeYcomponentFile("BalanceY");
    balance.frequencyHistogram("BalanceOriginalHist", balance.Y);
    BMPImageQualityImprovement bright("bright");
    bright.writeYcomponentFile("BrightY");
    bright.frequencyHistogram("BrightOriginalHist", bright.Y);
    BMPImageQualityImprovement dark("dark");
    dark.writeYcomponentFile("DarkY");
    dark.frequencyHistogram("DarkOriginalHist", dark.Y);

    balance.basedOnTwoReferencePoints(x1, y1, x2, y2);
    balance.writeYcomponentFile("BalanceTwoReferencePoints");
    balance.frequencyHistogram("BalanceTwoReferencePointsHist", balance.changedY);

    bright.basedOnTwoReferencePoints(x1, y1, x2, y2);
    bright.writeYcomponentFile("BrightTwoReferencePoints");
    bright.frequencyHistogram("BrightTwoReferencePointsHist", bright.changedY);

    dark.basedOnTwoReferencePoints(x1, y1, x2, y2);
    dark.writeYcomponentFile("DarkTwoReferencePoints");
    dark.frequencyHistogram("DarkTwoReferencePointsHist", dark.changedY);
}

void BMPImageQualityImprovement::gammaCorrection(int img) {
    std::vector<double> gamma = {0.04, 0.1, 0.2, 0.4, 0.67, 1, 1.5, 2.5, 5.0, 10.0, 25.0};
    std::string name[] = {"BalanceImage", "BrightImage", "DarkImage"};

    for (int k = 0; k < static_cast<int>(gamma.size()); ++k) {
        matrix<double> res;
        for (int i = 0; i < static_cast<int>(Y.size()); ++i) {
            std::vector<double> resVector;
            for (int j = 0; j < static_cast<int>(Y[0].size()); ++j) {
                resVector.push_back(pow((Y[i][j]/255), gamma[k]) * 255);
            }
            res.push_back(resVector);
        }
        this->changedY = res;
        writeYcomponentFile("GammaCorrection" + name[img] + std::to_string(gamma[k]));
        frequencyHistogram("GammaCorrection" + name[img] + std::to_string(gamma[k]), changedY);
    }
}

void BMPImageQualityImprovement::gammaCorrectionGraphics() {
    std::vector<double> gamma = {0.04, 0.1, 0.2, 0.4, 0.67, 1, 1.5, 2.5, 5.0, 10.0, 25.0};
    std::ofstream file(pythonPath + "GammaCorrection", std::ios_base::out | std::ios_base::binary);
    for (int k = 0; k < static_cast<int>(gamma.size()); ++k) {
        for (double y = 0.0; y < 1.000000001; y += (1.0/255.0)) {
            file << (pow(y, gamma[k]) * 255) << ' ';
        }
        file << std::endl;
    }

    BMPImageQualityImprovement balance("Balance");
    BMPImageQualityImprovement bright("bright");
    BMPImageQualityImprovement dark("dark");
    balance.gammaCorrection(0);
    bright.gammaCorrection(1);
    dark.gammaCorrection(2);
}

void BMPImageQualityImprovement::histogramAlignment() {
    double coefficient = 255.0 / (Y.size() * Y[0].size());

    std::vector<double> n;
    for (int k = 0; k < 256; ++k) {
        int count = 0;
        for (int i = 0; i < static_cast<int>(Y.size()); ++i) {
            for (int j = 0; j < static_cast<int>(Y[0].size()); ++j) {
                if(k == Y[i][j]) count++;
            }
        }
        n.push_back(count);
    }

    std::vector<double> s;
    for (int l = 0; l < 256; ++l) {
        double sumN = 0;
        for (int k = 0; k <= l; ++k) {
            sumN += n[k];
        }
        s.push_back(coefficient * sumN);
    }

    matrix<double> res;
    for (int i = 0; i < static_cast<int>(Y.size()); ++i) {
        std::vector<double> resVector;
        for (int j = 0; j < static_cast<int>(Y[0].size()); ++j) {
            resVector.push_back(s[Y[i][j]]);
        }
        res.push_back(resVector);
    }
    this->changedY = res;
}

void BMPImageQualityImprovement::histogramAlignmentProcessing() {
    BMPImageQualityImprovement balance("Balance");
    balance.writeYcomponentFile("BalanceY");
    balance.frequencyHistogram("BalanceOriginalHist", balance.Y);
    BMPImageQualityImprovement bright("bright");
    bright.writeYcomponentFile("BrightY");
    bright.frequencyHistogram("BrightOriginalHist", bright.Y);
    BMPImageQualityImprovement dark("dark");
    dark.writeYcomponentFile("DarkY");
    dark.frequencyHistogram("DarkOriginalHist", dark.Y);

    balance.histogramAlignment();
    balance.writeYcomponentFile("BalanceHAlignment");
    balance.frequencyHistogram("BalanceHAlignmentHist", balance.changedY);

    bright.histogramAlignment();
    bright.writeYcomponentFile("BrightHAlignment");
    bright.frequencyHistogram("BrightHAlignmentHist", bright.changedY);

    dark.histogramAlignment();
    dark.writeYcomponentFile("DarkHAlignment");
    dark.frequencyHistogram("DarkHAlignmentHist", dark.changedY);

}

void BMPImageQualityImprovement::thresholdForContourMap() {
    for (int T = 16; T < 241; ++T) {
        matrix<double> res;
        for (int i = 0; i < static_cast<int>(Y.size()); ++i) {
            std::vector<double> resVector;
            for (int j = 0; j < static_cast<int>(Y[0].size()); ++j) {
                if(Y[i][j] < T) resVector.push_back(0);
                else resVector.push_back(255);
            }
            res.push_back(resVector);
        }
        this->changedY = res;
        writeYcomponentFile("ContourMap/T=" + std::to_string(T));
    }
}

matrix<double> BMPImageQualityImprovement::getY() {
    return this->Y;
}

matrix<double> BMPImageQualityImprovement::getChangedY() {
    return this->changedY;
}