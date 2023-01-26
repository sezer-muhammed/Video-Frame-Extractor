# Video Frame Extractor
A Python script that extracts frames from videos at a given frequency and saves them as images with unique filenames.

## Usage
The script accepts the following command-line arguments:
* `frequency`: The frequency at which frames will be extracted (e.g. 10 to extract 1 frame every 10 frames)
* `videos_folder`: The path to the folder where the videos are located
* `images_folder`: The path to the folder where the extracted frames will be saved

To run the script, open a terminal and navigate to the script's directory, then run the following command:

```http
python extract.py --frequency 10 --videos_folder /path/to/videos/ --images_folder /path/to/images/
```

## Dependencies
* Python 3
* OpenCV

## How it works
The script loops through all the video files in the `videos_folder` and for each video, it uses OpenCV to open the video and extract frames at the specified frequency. The frames are then saved as images in the `images_folder` with unique filenames using timestamp.

## Note
* Make sure that you have read and write permission on the provided folders.
* The script will create `images_folder` if it does not exist.
* The script should work with most common video formats like mp4, avi, mov etc.
