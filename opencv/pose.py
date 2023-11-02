import sys
from pathlib import Path

import cv2
import numpy as np

BASE_DIR = Path(sys.argv[0]).resolve().parent
images_dir = BASE_DIR / 'images'
calib_path = BASE_DIR / 'calibration_data'
camera_matrix = np.loadtxt(calib_path / 'cameraMatrix.txt',
                           delimiter=',').astype(np.float32)
camera_distortion = np.loadtxt(calib_path / 'cameraDistortion.txt',
                               delimiter=',').astype(np.float32)

reference_image = cv2.imread(str(images_dir / 'ref.jpg'))
reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

feature_detector = cv2.SIFT_create(
)  # You can use other feature detectors as well
keypoints_reference, descriptors_reference = feature_detector.detectAndCompute(
    reference_gray, None)

frame = cv2.imread(str(images_dir / 'sample.jpg'))
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

keypoints_frame, descriptors_frame = feature_detector.detectAndCompute(
    gray, None)

matcher = cv2.BFMatcher(
    cv2.NORM_L2, crossCheck=True)  # You can choose other matching algorithms
matches = matcher.match(descriptors_reference, descriptors_frame)

threshold = 5
good_matches = [m for m in matches if m.distance < threshold
                ]  # You can adjust the threshold as needed

points_reference = np.array([(*keypoints_reference[m.queryIdx].pt, 0)
                             for m in good_matches]).astype(np.float32)
points_frame = np.array([keypoints_frame[m.trainIdx].pt
                         for m in good_matches]).reshape(-1, 1,
                                                         2).astype(np.float32)
print(points_reference)
print(points_frame)

if len(points_reference) >= 4 and len(points_frame) >= 4:
    _, rvec, tvec, _ = cv2.solvePnPRansac(points_reference, points_frame,
                                          camera_matrix, camera_distortion)

    axis = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0,
                                                       -1]]).reshape(-1, 3)
    image_points, _ = cv2.projectPoints(axis, rvec, tvec, camera_matrix,
                                        camera_distortion)

    # Draw coordinate axes
    frame = cv2.line(frame, tuple(image_points[0].ravel()),
                     tuple(image_points[1].ravel()), (0, 0, 255), 3)
    frame = cv2.line(frame, tuple(image_points[0].ravel()),
                     tuple(image_points[2].ravel()), (0, 255, 0), 3)
    frame = cv2.line(frame, tuple(image_points[0].ravel()),
                     tuple(image_points[3].ravel()), (255, 0, 0), 3)

    cv2.imshow('Pose Estimation', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Insufficient number of points for pose estimation")
