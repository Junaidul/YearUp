package org.example;
import org.opencv.highgui.HighGui;
import org.opencv.core.*;
import org.opencv.imgproc.Imgproc;
import org.opencv.videoio.VideoCapture;
import java.util.*;

public class ColorTracker {
    static {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME); // Load OpenCV library
    }

    public static void main(String[] args) {
        // Color dictionary (BGR format)
        Map<String, Scalar> colorDict = new HashMap<>();
        colorDict.put("red", new Scalar(0, 0, 255));
        colorDict.put("green", new Scalar(0, 255, 0));
        colorDict.put("blue", new Scalar(255, 0, 0));
        colorDict.put("white", new Scalar(255, 255, 255));
        colorDict.put("black", new Scalar(0, 0, 0));
        colorDict.put("yellow", new Scalar(0, 255, 255));
        colorDict.put("pink", new Scalar(203, 192, 255));
        colorDict.put("purple", new Scalar(255, 0, 255));

        // Get number of colors to track
        Scanner scanner = new Scanner(System.in);
        System.out.print("How many colors do you want to track (1 - 6)? ");
        int numColors = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        List<String> colors = new ArrayList<>();
        for (int i = 0; i < numColors; i++) {
            System.out.print("Enter a color: ");
            colors.add(scanner.nextLine());
        }

        // Open webcam
        VideoCapture cam = new VideoCapture(0);
        if (!cam.isOpened()) {
            System.out.println("Error: Could not open camera.");
            return;
        }

        Mat frame = new Mat();
        while (true) {
            cam.read(frame);
            if (frame.empty()) {
                break;
            }

            Mat hsvFrame = new Mat();
            Imgproc.cvtColor(frame, hsvFrame, Imgproc.COLOR_BGR2HSV);

            for (String color : colors) {
                Scalar lowerLimit, upperLimit;
                Scalar bgrColor = colorDict.get(color);
                if (bgrColor != null) {
                    Scalar[] limits = ColorUtils.getLimits(bgrColor);
                    lowerLimit = limits[0];
                    upperLimit = limits[1];

                    Mat mask = new Mat();
                    Core.inRange(hsvFrame, lowerLimit, upperLimit, mask);

                    List<MatOfPoint> contours = new ArrayList<>();
                    Mat hierarchy = new Mat();
                    Imgproc.findContours(mask, contours, hierarchy, Imgproc.RETR_EXTERNAL, Imgproc.CHAIN_APPROX_SIMPLE);

                    for (MatOfPoint contour : contours) {
                        Rect boundingBox = Imgproc.boundingRect(contour);
                        Imgproc.rectangle(frame, boundingBox, new Scalar(0, 0, 0), 2);
                    }
                }
            }

            HighGui.imshow("Camera", frame);

            if ((HighGui.waitKey(40) & 0xFF) == 81) { // ESC key
                System.out.println("Exiting...");
                break;
            }
        }

        cam.release();
        HighGui.destroyAllWindows();
    }
}













