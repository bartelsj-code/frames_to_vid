
import cv2
import os




def images_to_video(image_folder, video_name, fps):
    # images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

    images = []
    for i in range(1,11701):
        img = f'1stable{i}.png'
        images.append(img)


    print(len(images))
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

# Example usage:
images_to_video('run12', 'output_video.mp4', 24)  # Change the folder path and video name as needed