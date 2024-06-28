python3 cross-validation.py 10

python3 rf-fitness-video.py -d dataset-231121-last1min/none --train --sm rf-video-cbw

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-cbw > outputs/cbw-rf-video-cbw-1
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw1-1
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw2-1
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw4-1
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw8-1

python3 rf-fitness-video.py -d bw1-last1min --train --sm rf-video-bw1

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw1 > outputs/bw1-rf-video-cbw-1
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw1-1
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw2-1
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw4-1
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw8-1

python3 rf-fitness-video.py -d bw2-last1min --train --sm rf-video-bw2

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw2 > outputs/bw2-rf-video-cbw-1
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw1-1
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw2-1
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw4-1
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw8-1

python3 rf-fitness-video.py -d bw4-last1min --train --sm rf-video-bw4

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw4 > outputs/bw4-rf-video-cbw-1
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw1-1
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw2-1
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw4-1
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw8-1

python3 rf-fitness-video.py -d bw8-last1min --train --sm rf-video-bw8

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw8 > outputs/bw8-rf-video-cbw-1
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw1-1
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw2-1
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw4-1
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw8-1



python3 cross-validation.py 10

python3 rf-fitness-video.py -d dataset-231121-last1min/none --train --sm rf-video-cbw

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-cbw > outputs/cbw-rf-video-cbw-2
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw1-2
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw2-2
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw4-2
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw8-2

python3 rf-fitness-video.py -d bw1-last1min --train --sm rf-video-bw1

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw1 > outputs/bw1-rf-video-cbw-2
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw1-2
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw2-2
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw4-2
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw8-2

python3 rf-fitness-video.py -d bw2-last1min --train --sm rf-video-bw2

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw2 > outputs/bw2-rf-video-cbw-2
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw1-2
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw2-2
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw4-2
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw8-2

python3 rf-fitness-video.py -d bw4-last1min --train --sm rf-video-bw4

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw4 > outputs/bw4-rf-video-cbw-2
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw1-2
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw2-2
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw4-2
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw8-2

python3 rf-fitness-video.py -d bw8-last1min --train --sm rf-video-bw8

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw8 > outputs/bw8-rf-video-cbw-2
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw1-2
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw2-2
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw4-2
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw8-2



python3 cross-validation.py 10

python3 rf-fitness-video.py -d dataset-231121-last1min/none --train --sm rf-video-cbw

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-cbw > outputs/cbw-rf-video-cbw-3
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw1-3
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw2-3
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw4-3
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw8-3

python3 rf-fitness-video.py -d bw1-last1min --train --sm rf-video-bw1

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw1 > outputs/bw1-rf-video-cbw-3
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw1-3
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw2-3
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw4-3
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw8-3

python3 rf-fitness-video.py -d bw2-last1min --train --sm rf-video-bw2

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw2 > outputs/bw2-rf-video-cbw-3
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw1-3
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw2-3
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw4-3
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw8-3

python3 rf-fitness-video.py -d bw4-last1min --train --sm rf-video-bw4

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw4 > outputs/bw4-rf-video-cbw-3
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw1-3
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw2-3
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw4-3
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw8-3

python3 rf-fitness-video.py -d bw8-last1min --train --sm rf-video-bw8

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw8 > outputs/bw8-rf-video-cbw-3
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw1-3
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw2-3
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw4-3
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw8-3



python3 cross-validation.py 10

python3 rf-fitness-video.py -d dataset-231121-last1min/none --train --sm rf-video-cbw

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-cbw > outputs/cbw-rf-video-cbw-4
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw1-4
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw2-4
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw4-4
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-cbw > outputs/cbw-rf-video-vbw8-4

python3 rf-fitness-video.py -d bw1-last1min --train --sm rf-video-bw1

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw1 > outputs/bw1-rf-video-cbw-4
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw1-4
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw2-4
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw4-4
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw1 > outputs/bw1-rf-video-vbw8-4

python3 rf-fitness-video.py -d bw2-last1min --train --sm rf-video-bw2

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw2 > outputs/bw2-rf-video-cbw-4
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw1-4
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw2-4
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw4-4
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw2 > outputs/bw2-rf-video-vbw8-4

python3 rf-fitness-video.py -d bw4-last1min --train --sm rf-video-bw4

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw4 > outputs/bw4-rf-video-cbw-4
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw1-4
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw2-4
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw4-4
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw4 > outputs/bw4-rf-video-vbw8-4

python3 rf-fitness-video.py -d bw8-last1min --train --sm rf-video-bw8

python3 rf-fitness-video.py -d dataset-231121-last1min/none --lm rf-video-bw8 > outputs/bw8-rf-video-cbw-4
python3 rf-fitness-video.py -d bw1-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw1-4
python3 rf-fitness-video.py -d bw2-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw2-4
python3 rf-fitness-video.py -d bw4-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw4-4
python3 rf-fitness-video.py -d bw8-last1min --lm rf-video-bw8 > outputs/bw8-rf-video-vbw8-4

