package org.example;
import org.opencv.core.*;
import org.opencv.imgproc.Imgproc;

public class ColorUtils {

    public static Scalar[] getLimits(Scalar bgrColor) {
        Mat bgrMat = new Mat(1, 1, CvType.CV_8UC3, bgrColor);
        Mat hsvMat = new Mat();
        Imgproc.cvtColor(bgrMat, hsvMat, Imgproc.COLOR_BGR2HSV);

        double hue = hsvMat.get(0, 0)[0];

        Scalar lowerLimit, upperLimit;
        if (hue >= 165) { // Handle red wrap-around
            lowerLimit = new Scalar(hue - 10, 100, 100);
            upperLimit = new Scalar(180, 255, 255);
        } else if (hue <= 15) {
            lowerLimit = new Scalar(0, 100, 100);
            upperLimit = new Scalar(hue + 10, 255, 255);
        } else {
            lowerLimit = new Scalar(hue - 10, 100, 100);
            upperLimit = new Scalar(hue + 10, 255, 255);
        }

        return new Scalar[]{lowerLimit, upperLimit};
    }
}