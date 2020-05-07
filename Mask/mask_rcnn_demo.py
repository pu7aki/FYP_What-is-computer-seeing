import os
from PIL import Image
import random
import tensorflow as tf

graph = tf.get_default_graph()

import skimage.io

from Mask import coco
from Mask import model as modellib
from Mask import visualize

# %matplotlib inline
# Root directory of the project
ROOT_DIR = os.getcwd()

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = "mask_rcnn_coco.h5"

image_dir = os.path.join(ROOT_DIR, "Mask")
# Directory of images to run detection on
IMAGE_DIR = os.path.join(image_dir, "images")


class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


config = InferenceConfig()
# config.display()


# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on MS-COCO
model.load_weights(COCO_MODEL_PATH, by_name=True)

# COCO Class names
# Index of the class in the list is its ID. For example, to get ID of
# the teddy bear class, use: class_names.index('teddy bear')
class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']


def allfig():
    file_names = next(os.walk(IMAGE_DIR))[2]
    return file_names


def upload(fig, figname):
    img = Image.open(fig)
    img.save(os.path.join("D:\FYP\myfyp\Mask\images",os.path.basename(figname)))

def mask(level_str, fig_name,rando):
    # game = 0;
    # while game < 100:
    # Load a random image from the images folder
    level = int(level_str)
    with graph.as_default():
        if rando == 0:
            file_names = os.path.join(IMAGE_DIR, fig_name)
            image = skimage.io.imread(os.path.join(IMAGE_DIR, file_names))
        else:
            file_names = next(os.walk(IMAGE_DIR))[2]
            image = skimage.io.imread(os.path.join(IMAGE_DIR, random.choice(file_names)))
        # Run detection
        results = model.detect([image], verbose=1)
        # Visualize results
        r = results[0]
        label_list = visualize.display_instances(level, image, r['rois'], r['masks'], r['class_ids'],
                                                 class_names, r['scores'])
        return label_list[0], label_list[1], label_list[2]


def maskrandommiddle(level_str, fig_name,rando):
    # game = 0;
    # while game < 100:
    # Load a random image from the images folder
    level = 2
    with graph.as_default():
        if rando == 0:
            file_names = os.path.join("D:\FYP\myfyp\Mask\images\middle", fig_name)
            image = skimage.io.imread(os.path.join("D:\FYP\myfyp\Mask\images\middle", file_names))
        else:
            file_names = next(os.walk("D:\FYP\myfyp\Mask\images\middle"))[2]
            image = skimage.io.imread(os.path.join("D:\FYP\myfyp\Mask\images\middle", random.choice(file_names)))
        # Run detection
        results = model.detect([image], verbose=1)
        # Visualize results
        r = results[0]
        label_list = visualize.display_instances(level, image, r['rois'], r['masks'], r['class_ids'],
                                                 class_names, r['scores'])
        return label_list[0], label_list[1], label_list[2]

def maskrandomhard(level_str, fig_name,rando):
    # game = 0;
    # while game < 100:
    # Load a random image from the images folder
    level = 2
    with graph.as_default():
        if rando == 0:
            file_names = os.path.join("D:\FYP\myfyp\Mask\images\hard", fig_name)
            image = skimage.io.imread(os.path.join("D:\FYP\myfyp\Mask\images\hard", file_names))
        else:
            file_names = next(os.walk("D:\FYP\myfyp\Mask\images\hard"))[2]
            image = skimage.io.imread(os.path.join("D:\FYP\myfyp\Mask\images\hard", random.choice(file_names)))
        # Run detection
        results = model.detect([image], verbose=1)
        # Visualize results
        r = results[0]
        label_list = visualize.display_instances(level, image, r['rois'], r['masks'], r['class_ids'],
                                                 class_names, r['scores'])
        return label_list[0], label_list[1], label_list[2]

def maskrandomeasy(level_str, fig_name,rando):
    # game = 0;
    # while game < 100:
    # Load a random image from the images folder
    level = 2
    with graph.as_default():
        if rando == 0:
            file_names = os.path.join("D:\FYP\myfyp\Mask\images\easy", fig_name)
            image = skimage.io.imread(os.path.join("D:\FYP\myfyp\Mask\images\easy", file_names))
        else:
            file_names = next(os.walk("D:\FYP\myfyp\Mask\images\easy"))[2]
            image = skimage.io.imread(os.path.join("D:\FYP\myfyp\Mask\images\easy", random.choice(file_names)))
        # Run detection
        results = model.detect([image], verbose=1)
        # Visualize results
        r = results[0]
        label_list = visualize.display_instances(level, image, r['rois'], r['masks'], r['class_ids'],
                                                 class_names, r['scores'])
        return label_list[0], label_list[1], label_list[2]