# DL4SN-Household-Discompose-Bag-Classification-using-Arduino-Nano-33-

![image](https://user-images.githubusercontent.com/116358810/228838784-1ddd51d3-8270-4adf-ba98-cb68f9e16488.png)

Below are three types of bag: Garbage Bag, Paper Bag, Plastic Bag
![8](https://user-images.githubusercontent.com/116358810/228840497-13e6fdd1-ffa1-4518-a966-8f279d86b236.jpg)![10](https://user-images.githubusercontent.com/116358810/228840137-5197405b-2042-4f54-b512-3104eaf09f88.jpg)![4](https://user-images.githubusercontent.com/116358810/228840199-3f9f50ff-dab0-4c79-a768-d8225fa83478.jpg)



Using MobileNet V1 since the arduinono nano 33 could adpapt for its ram

training-validation accuracy and loss plot 

<img width="374" alt="image" src="https://user-images.githubusercontent.com/116358810/228839292-8045e59f-ceff-4860-b1e5-9580fa8bbbcb.png">


In order to start task, please download the file and drag 'OV7675' and 'Bag_Classification_inferencing' into Arduino library first.

If you want to use camera to make real photo and recongize, please open into: /Users/<username>/Documents/Arduino/libraries/Bag_Classification_inferencing/examples/nano_ble33_sense/nano_ble33_sense_camera/nano_ble33_sense_camera.ino
(Based on different setting, the file path could be different)

Open the 'nano_ble33_sense_camera.ino' file using Arduino IDE, as show below
<img width="926" alt="image" src="https://user-images.githubusercontent.com/116358810/226727060-2fa8b56d-210e-4987-938e-bf9788b20122.png">

Connect to your own nano 33 and click 'upload' button to compile, when the uploading done, open serial monitor and it will return results based on your camera picture

Based on the pre-train model, the image from camera can be classified with probability.
<img width="814" alt="image" src="https://user-images.githubusercontent.com/116358810/228838247-1a7e2b2a-dd0f-4c83-a03e-525be7e1a016.png">

