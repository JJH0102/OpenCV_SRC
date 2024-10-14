#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    Mat img(400, 640, CV_8UC3, Scalar(255, 255, 255));
    int a = 0;

    while(true) {
        img = Scalar(255, 255, 255); // 배경 흰색으로 초기화

        line(img, Point(50, 100 + a), Point(500, 100 + a), Scalar(255, a / 2 + 50, 0), 3);
        a++;

        if (a > 400)
            a = 0;

        imshow("img", img);

        if (waitKey(10) == 27)
            break;
    }

    return 0;
}