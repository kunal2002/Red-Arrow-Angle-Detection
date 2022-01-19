import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
#using shi tomasi corner detection algorithm
def distance(xd, yd, xD,yD):
    return math.sqrt((xd - xD)**2 + (yd - yD)**2)

def Angle(corners):
    # cv2.circle(img, (x, y), 3, (255, 0, 0), 4)
    maxx = -1
    corx1, cory1 = 0,0
    corx2, cory2 = 0,0
    corx3, cory3 = 0,0
    corx4, cory4 = 0,0
    for corner in corners:
        x_1, y_1 = corner.ravel()
        for cor in corners:
            x_2,y_2 = cor.ravel()
            if x_2 != x_1 and y_2 != y_1:
                if distance(x_1,y_1,x_2,y_2) > maxx:
                    maxx = distance(x_1,y_1,x_2,y_2)
                    corx1 = x_1
                    cory1 = y_1
                    corx2 = x_2
                    cory2 = y_2
    cv2.circle(img, (corx1,cory1), 3, (255,0,0), 4)
    cv2.circle(img, (corx2,cory2), 3, (255, 0, 0), 4)
    for corner in corners:
        x_1, y_1 = corner.ravel()
        for cor in corners:
            x_2, y_2 = cor.ravel()
            if x_2 != x_1 and y_2 != y_1:
                dist1 = distance(x_1,y_1,x_2,y_2)
                if ((dist1 / maxx) <= 1.05 and (dist1 / maxx) >= 0.95 and (dist1 / maxx) != 1.0):
                    corx3 = x_1
                    cory3 = y_1
                    corx4 = x_2
                    cory4 = y_2
    cv2.circle(img, (corx3, cory3), 3, (255, 0, 0), 4)
    cv2.circle(img, (corx4, cory4), 3, (255, 0, 0), 4)
    # print(corx1,cory1)
    # print(corx2,cory2)
    # print(corx3,cory3)
    # print(corx4,cory4)
    res = [[corx1,cory1],[corx2,cory2],[corx3,cory3],[corx4,cory4]]
    points = []
    [points.append(x) for x in res if x not in points]
    # print(points)
    corfx, corfy = 0,0
    corfx1, corfy1 = 0,0
    minn = 10000000000
    points = np.array(points)
    for ele in points:
        xf, yf = ele.ravel()
        for ele1 in points:
            xf1, yf1 = ele1.ravel()
            if not(xf == xf1 and yf == yf1):
                if distance(xf,yf,xf1,yf1) < minn:
                    minn = distance(xf,yf,xf1,yf1)
                    corfx = xf
                    corfy = yf
                    corfx1 = xf1
                    corfy1 = yf1
    # cv2.circle(img, (corfx,corfy), 3, (255, 0, 0), 4)
    # cv2.circle(img, (corfx1,corfy1), 3, (255, 0, 0), 4)
    midx = np.int0((corfx + corfx1) / 2)
    midy = np.int0((corfy + corfy1) / 2)
    mid = [[corfx, corfx1],[corfy,corfy1]]
    mid = np.array(mid)
    coord = []
    [coord.append(x) for x in points if x not in mid]
    coord = np.array(coord)
    x,y = coord.ravel()
    # print(x,y)
    cv2.circle(img, (midx, midy), 3, (255, 0, 0), 4)
    cv2.circle(img, (x,y), 3, (255,0,0), 4)
    ang = math.atan2(x - midx, midy - y)
    print("The angle the arrow makes with the Vertical is ", (math.degrees(ang)))

img = cv2.imread('arrow.png',cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, 1, (0,255,0), 4)
# print("The number of contours are " + str(len(contours)))
for cont in contours:
    approx = cv2.approxPolyDP(cont, 0.009 * cv2.arcLength(cont, True), True)
    cv2.drawContours(img, [approx], 0, (0,255,0), 4)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    #cv2.circle(img,(x,y),3,(255,0,0),4)
    if len(approx) == 7:
        #cv2.putText(img, "Arrow!", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (160,50,0), 3)
        corners = cv2.goodFeaturesToTrack(thresh,7,0.2,10)
        corners = np.int0(corners)
        # for corner in corners:
        #     x4, y4 = corner.ravel()
        #     cv2.circle(img, (x4,y4), 3, (255,0,0), 4)
        Angle(approx)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
