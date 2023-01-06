# Red-Arrow-Angle-Detection
The DetectRedArrowVideo program detects the Red Arrow from a video feed and calculates and displays it's angle from the vertical
The ArrowDetect program detects any(possibly multiple) arrows and detects their angle and displays it's angle from the vertical

Firstly the program detects contours of the red arrow, it uses polyapproxDp to carve out those corners and store them in a numpy array, in an arrow which was to be used i counted that there could be 7 corners , used that condition and found out the two points which are at the max distance from one point, these two points would be the tail of the arrow and the one other point would be the head point of the arrow, then i will find out the mid point of those tail points which should be approximately around the head point , now we got two points that make a line and hence now we can calculate the angle that the arrow makes  with the vertical
