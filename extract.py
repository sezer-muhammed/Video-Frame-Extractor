import argparse
import os
import cv2
import datetime

def extract_frames(frequency, videos_folder, images_folder):
    # create "images" folder if it does not exist
    if not os.path.exists(images_folder):
        os.makedirs(images_folder)

    # loop through videos in "videos" folder
    for i, video_file in enumerate(os.listdir(videos_folder)):
        # open video file
        video = cv2.VideoCapture(os.path.join(videos_folder, video_file))

        # get video properties
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        # extract frames
        for j in range(0, frame_count, frequency):
            video.set(cv2.CAP_PROP_POS_FRAMES, j)
            ret, frame = video.read()

            if ret:
                # generate unique filename using current timestamp
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                filename = "frame_{}_{}_{}.jpg".format(i, j, timestamp)

                # save frame to "images" folder with unique name
                cv2.imwrite(os.path.join(images_folder, filename), frame)

        video.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--frequency", type=int, help="Frequency at which to extract frames")
    parser.add_argument("--videos_folder", help="path to the folder where videos are located")
    parser.add_argument("--images_folder", help="path to the folder where images should be saved")
    args = parser.parse_args()

    extract_frames(args.frequency, args.videos_folder, args.images_folder)
