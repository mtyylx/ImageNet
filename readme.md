# ImageNet

> Prerequisite: Download ILSVRC2012 `train` and `val` dataset. `Caffe` installed.

1. `unpack_imagenet.sh` Untar all sub packages to separate folders.

2. `get_ilsvrc_aux.sh` Download train / val labels and imagenet_mean.

3. `resize_and_crop_images.py`

    - Install mincepie: `pip install git+https://github.com/Yangqing/mincepie.git`

    - Configure Crop Size in `resize_and_crop_images.py`
    
    - Run Script. Notes that set `num_clients=1` to avoid image lost caused by racing condition.

        ```bash
        mkdir EXP      
  
        resize_and_crop_images.py \
        --num_clients=1 \
        --image_lib=opencv \
        --input=tools/train.txt \
        --input_folder=train \
        --output_folder=EXP/train/
  
        resize_and_crop_images.py \
        --num_clients=1 \
        --image_lib=opencv \
        --input=tools/val.txt \
        --input_folder=val \
        --output_folder=EXP/val/
        ```
        
4. `create_imagenet.sh`

    - Configure Path
    
        ```bash
        EXAMPLE          # lmdb path
        TOOLS            # Caffe build/tools/
        TRAIN_DATA_ROOT  # Cropped Imagenet train folder
        VAL_DATA_ROOT    # Imagenet val folder
        
        RESIZE=false     # Already done by resize_and_crop.py
        ```

    - Run `create_imagenet.sh`    
