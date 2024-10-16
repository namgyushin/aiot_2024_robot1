#include "opencv2/freetype.hpp"
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    Scalar green = Scalar(0, 255, 0);
    Scalar red = Scalar(0, 0, 255);
    Mat img(400, 640, CV_8UC3, Scalar(255, 255, 255));

    String text = u8"안녕 오픈CV!";
    auto ft2 = freetype::createFreeType2();
    ft2->loadFontData("/home/lmc/aiot_2024_robot1/OpenCV/cppTest/data/NanumPenScript-Regular.ttf", 0);
    Size textSize = ft2->getTextSize(text, 50, -1, 0);

    int a = 0;
    while (true)
    {
        img = Scalar(255, 255, 255);
        putText(img, "Hello, OpenCV nice to meet you!", Point(50 + a, 100), FONT_HERSHEY_PLAIN, 3, green);
        // putText(img, "안녕 오픈CV!", Point(50 + a, 200), FONT_HERSHEY_PLAIN, 3, red);
        ft2->putText(img, text, Point(50 + a, 200), 50, red, -1, LINE_AA, true);
        a++;

        if (a > 400)
            a = 0;
        imshow("img", img);
        if (waitKey(10) == 27)
            break;
    }

    return 0;
}
