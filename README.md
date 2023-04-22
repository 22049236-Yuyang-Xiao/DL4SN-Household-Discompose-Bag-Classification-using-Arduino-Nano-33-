# DL4SN-Household-Disposable-Bag-Classification-using-Arduino-Nano-33-

![image](https://user-images.githubusercontent.com/116358810/228838784-1ddd51d3-8270-4adf-ba98-cb68f9e16488.png)

Below are three types of bag: 
Garbage Bag: ![8](https://user-images.githubusercontent.com/116358810/228841073-6e190e5b-5aac-4f5d-8d06-31dcb90c53f2.jpg)

Paper Bag: ![6](https://user-images.githubusercontent.com/116358810/228841161-c5338442-6e29-4470-8639-296488f43c87.jpg)

Plastic Bag: ![4](https://user-images.githubusercontent.com/116358810/228841258-ff747280-af5b-4b6b-890b-18125812240a.jpg)



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

