#!/bin/bash

#generate datasets for training and testing
python3 generate-script-dataset.py

#train k1
python3 rf-fitness-video.py -d offset-train/k1 --train --sm models/k1 -s 10

#train k2
python3 rf-fitness-video.py -d offset-train/k2 --train --sm models/k2 -s 20

#train k3
python3 rf-fitness-video.py -d offset-train/k3 --train --sm models/k3 -s 40

#train k4
python3 rf-fitness-video.py -d offset-train/k4 --train --sm models/k4 -s 80

#test k1
python3 rf-fitness-video.py -d offset-test/-10 --lm models/k1 -s 10 > outputs/k1-10.txt
python3 rf-fitness-video.py -d offset-test/-8 --lm models/k1 -s 10 > outputs/k1-8.txt
python3 rf-fitness-video.py -d offset-test/-6 --lm models/k1 -s 10 > outputs/k1-6.txt
python3 rf-fitness-video.py -d offset-test/-4 --lm models/k1 -s 10 > outputs/k1-4.txt
python3 rf-fitness-video.py -d offset-test/-2 --lm models/k1 -s 10 > outputs/k1-2.txt
python3 rf-fitness-video.py -d offset-test/0 --lm models/k1 -s 10 > outputs/k10.txt
python3 rf-fitness-video.py -d offset-test/2 --lm models/k1 -s 10 > outputs/k12.txt
python3 rf-fitness-video.py -d offset-test/4 --lm models/k1 -s 10 > outputs/k14.txt
python3 rf-fitness-video.py -d offset-test/6 --lm models/k1 -s 10 > outputs/k16.txt
python3 rf-fitness-video.py -d offset-test/8 --lm models/k1 -s 10 > outputs/k18.txt
python3 rf-fitness-video.py -d offset-test/10 --lm models/k1 -s 10 > outputs/k110.txt

#test k2
python3 rf-fitness-video.py -d offset-test/-10 --lm models/k2 -s 10 > outputs/k2-10.txt
python3 rf-fitness-video.py -d offset-test/-8 --lm models/k2 -s 10 > outputs/k2-8.txt
python3 rf-fitness-video.py -d offset-test/-6 --lm models/k2 -s 10 > outputs/k2-6.txt
python3 rf-fitness-video.py -d offset-test/-4 --lm models/k2 -s 10 > outputs/k2-4.txt
python3 rf-fitness-video.py -d offset-test/-2 --lm models/k2 -s 10 > outputs/k2-2.txt
python3 rf-fitness-video.py -d offset-test/0 --lm models/k2 -s 10 > outputs/k20.txt
python3 rf-fitness-video.py -d offset-test/2 --lm models/k2 -s 10 > outputs/k22.txt
python3 rf-fitness-video.py -d offset-test/4 --lm models/k2 -s 10 > outputs/k24.txt
python3 rf-fitness-video.py -d offset-test/6 --lm models/k2 -s 10 > outputs/k26.txt
python3 rf-fitness-video.py -d offset-test/8 --lm models/k2 -s 10 > outputs/k28.txt
python3 rf-fitness-video.py -d offset-test/10 --lm models/k2 -s 10 > outputs/k210.txt

#test k3
python3 rf-fitness-video.py -d offset-test/-10 --lm models/k3 -s 10 > outputs/k3-10.txt
python3 rf-fitness-video.py -d offset-test/-8 --lm models/k3 -s 10 > outputs/k3-8.txt
python3 rf-fitness-video.py -d offset-test/-6 --lm models/k3 -s 10 > outputs/k3-6.txt
python3 rf-fitness-video.py -d offset-test/-4 --lm models/k3 -s 10 > outputs/k3-4.txt
python3 rf-fitness-video.py -d offset-test/-2 --lm models/k3 -s 10 > outputs/k3-2.txt
python3 rf-fitness-video.py -d offset-test/0 --lm models/k3 -s 10 > outputs/k30.txt
python3 rf-fitness-video.py -d offset-test/2 --lm models/k3 -s 10 > outputs/k32.txt
python3 rf-fitness-video.py -d offset-test/4 --lm models/k3 -s 10 > outputs/k34.txt
python3 rf-fitness-video.py -d offset-test/6 --lm models/k3 -s 10 > outputs/k36.txt
python3 rf-fitness-video.py -d offset-test/8 --lm models/k3 -s 10 > outputs/k38.txt
python3 rf-fitness-video.py -d offset-test/10 --lm models/k3 -s 10 > outputs/k310.txt

#test k4
python3 rf-fitness-video.py -d offset-test/-10 --lm models/k4 -s 10 > outputs/k4-10.txt
python3 rf-fitness-video.py -d offset-test/-8 --lm models/k4 -s 10 > outputs/k4-8.txt
python3 rf-fitness-video.py -d offset-test/-6 --lm models/k4 -s 10 > outputs/k4-6.txt
python3 rf-fitness-video.py -d offset-test/-4 --lm models/k4 -s 10 > outputs/k4-4.txt
python3 rf-fitness-video.py -d offset-test/-2 --lm models/k4 -s 10 > outputs/k4-2.txt
python3 rf-fitness-video.py -d offset-test/0 --lm models/k4 -s 10 > outputs/k40.txt
python3 rf-fitness-video.py -d offset-test/2 --lm models/k4 -s 10 > outputs/k42.txt
python3 rf-fitness-video.py -d offset-test/4 --lm models/k4 -s 10 > outputs/k44.txt
python3 rf-fitness-video.py -d offset-test/6 --lm models/k4 -s 10 > outputs/k46.txt
python3 rf-fitness-video.py -d offset-test/8 --lm models/k4 -s 10 > outputs/k48.txt
python3 rf-fitness-video.py -d offset-test/10 --lm models/k4 -s 10 > outputs/k410.txt

#rmdir /data2/august/models

#rmdir /data2/august/offset-train

#rmdir /data2/august/offset-test
