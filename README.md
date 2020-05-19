# FYP_What-is-computer-seeing
Project title: 'What is the computer seeing?' - A cooperative photo-driven game    
Name: Yiqiu Lei   
Supervisor: Mark Matthews    
This project is mainly to create a game that lets players know how the computer recognizes the images we upload. There are a lot of algorithms and software for computer vision, but there aren't many intuitive ways to let people know about it. I use an algorithm called Mask R-CNN that shows the parts of the image that the computer can distinguish and let the player guess. The part that the player guessed can be seen as a process of computer recognition. I compare the content inputted by the player with the answer recognized by our computer. The player will input the level and the name of photo he/she wants to guess. Then the player will input the answers according to the masked photo. They need also input their name so that they can accumulate scores before they guess it.        
Mask R-CNN code: https://github.com/matterport/Mask_RCNN    
      
Installation tips:    
PLEASE run this file in the D:\FYP\myfyp.  
PLEASE download mask_rcnn_coco.h5 ( https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5 )  
PLEASE put mask_rcnn_coco.h5 and manage.py in the same floder.  
Like:  
<img src="https://github.com/pu7aki/FYP_What-is-computer-seeing/blob/master/images/example.jpg" width="50%" height="50%">   
       
Requirements:  
Django, Python 3.4, TensorFlow 1.3, Keras 2.0.8 and other common packages.  
        
Running process:  
py3 manage.py runserver 127.0.0.1:8000    
open http://127.0.0.1:8000/    
        
There is a website template that includes the look of almost all the features. This is a static website so that it cannot use the algorithm. On this site, only normal start can choose level as user input and users can guess the photos. Everything else is fixed. These pages mainly shows the interface and flow of the entire game. If you want to play the full game, you still need to download the source code.   
( http://fyp-sharing.s3-website-eu-west-1.amazonaws.com/ )     
