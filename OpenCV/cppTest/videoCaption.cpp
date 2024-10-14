#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    VideoCapture cap(0);
    Mat frame;

    if (!cap.isOpened())
    {
        cerr << "Video open faild.\n";
        return -1;
    }

    int delay = 100;
    while (true)
    {
        cap >> frame;
        imshow("frame", frame);
        if (waitKey(delay) == 27)
            break;
    }
    cap.release();
    destroyAllWindows();
    return 0;
}