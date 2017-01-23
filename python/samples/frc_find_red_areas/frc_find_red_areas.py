#!/usr/bin/python3

"""
Sample program that uses a generated GRIP pipeline to detect red areas in an image and publish them to NetworkTables.
"""

import cv2
from networktables import NetworkTables
from grip import GripPipeline


def extra_processing(pipeline):
    """
    Performs extra processing on the pipeline's outputs and publishes data to NetworkTables.
    :param pipeline: the pipeline that just processed an image
    :return: None
    """
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []

    # Find the bounding boxes of the contours to get x, y, width, and height
    for contour in pipeline.filter_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        center_x_positions.append(x + w / 2)  # X and Y are coordinates of the top-left corner of the bounding box
        center_y_positions.append(y + h / 2)
        widths.append(w)
        heights.append(h)

    # Publish to the '/vision/red_areas' network table
    table = NetworkTables.getTable('/vision/red_areas')
    table.putNumberArray('x', center_x_positions)
    table.putNumberArray('y', center_y_positions)
    table.putNumberArray('width', widths)
    table.putNumberArray('height', heights)


def main():
    print('Initializing NetworkTables')
    NetworkTables.setClientMode()
    NetworkTables.setIPAddress('localhost')
    NetworkTables.initialize()

    print('Creating video capture')
    cap = cv2.VideoCapture(0)

    print('Creating pipeline')
    pipeline = GripPipeline()

    print('Running pipeline')
    while cap.isOpened():
        have_frame, frame = cap.read()
        if have_frame:
            pipeline.process(frame)
            extra_processing(pipeline)

    print('Capture closed')


if __name__ == '__main__':
    main()
