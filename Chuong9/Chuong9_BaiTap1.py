#CHƯƠNG 9 THƯ VIỆN HỖ TRỢ XỬ LÝ MACHINE LEARNING
'''
Python là một trong những ngôn ngữ mạnh mẽ, hỗ trợ các hệ thống Machine Learning.
Có nhiều thư viện mà Python có thể sử dụng. Chẳng hạn như numpy là một thư viện phổ
biến giúp xử lý các phép toán liên quan đến các mảng nhiều chiều, hỗ trợ các hàm liên
quan tới đại số tuyến tính…, Scikit-learn là một thư viện chứa đầy đủ các thuật toán
Machine Learning. Tài liệu này chỉ liệt kê ra, không phải tài liệu hướng dẫn chi tiết.
Thư viện numpy có thể lấy ở đây: https://numpy.org/
Thư viện Scikit-learn có thể lấy ở đây: https://scikit-learn.org/ (hệ thống này có đầy đủ
Dữ liệu mẫu, coding mẫu, đặc biệt tài liệu rất chi tiết), là một thư viện mà người nghiên
cứu Machine Learning nên biết.
Machine Learning thường giải quyết các bài toán sau:
• Phân loại
• Phân cụm
• Hồi quy
• Máy dịch
• Hoàn thiện dữ liệu
Phân loại (còn gọi là classification) là một trong những bài toán được nghiên cứu và triển
khai nhiều nhất trong Machine Learning. Ví dụ như phân loại Email rác, phân loại chữ
viết tay…
Phân cụm (còn gọi là Clustering) là bài toán chia dữ liệu ban đầu thành các cụm nhỏ dựa
trên sự liên quan giữa các dữ liệu trong mỗi cụm.
Hồi quy (còn gọi là Regression), nếu tập đích gồm các giá trị thực (có thể vô hạn) thì các
bài toán này gọi là hồi quy. Ví dụ ta có tập dữ liệu chiều cao và cân nặng, giờ có dữ liệu
chiều cao của một người hỏi người này có khả năng cân nặng bao nhiêu?
Máy dịch (còn gọi là Machine Translation), chương trình máy dịch sẽ được yêu cầu
dịch một đoạn văn trong một ngôn ngữ này sang một ngôn ngữ khác.
Hoàn thiện dữ liệu (còn gọi là Data Completion), thường một bộ dữ liệu có thể có nhiều
đặc trưng nhưng việc thu thập đặc trung cho từng điểm dữ liệu đôi lúc không khả thi vì lý
do nào đó. Ví dụ như một đoạn văn bản bị thiếu, một bức ảnh bị trầy xước. Hoàn thiện dữ
liệu là giải thuật sẽ dự đoán các vùng dữ liệu thiếu đó.
Anh Vũ Hữu Tiệp biên soạn cuốn Machine Learning Cơ bản khá hay. Các bạn có thể
tham thảo tài liệu và mã nguồn tại đây: https://github.com/tiepvupsu/ebookMLCB
Dưới đây là một ví dụ sử dụng Giải thuật Hồi Quy Tuyến Tính của thư viện Scikit-learn
để dự báo cân nặng dựa vào chiều cao.
Từ bảng dữ liệu ở trên, hãy viết giải thuật để người dùng nhập vào chiều cao thì xuất ra
cân nặng của họ, sử dụng thư viện Scikit-Learn.
Mã nguồn đầy đủ cho phần hồi quy tuyến tính này (lưu ý khi dùng các thư viện mà chưa
cài đặt thì nó sẽ báo lỗi, Sinh viên tự cài đặt):

Chạy phần mềm ta được:
scikit-lean's solution:w_1= 0.5592049619396674 w_0= -33.73541020580774
our solution : w_1 = 0.5592049619425978 w_0= -33.735410206296365
Input your height:>? 170
Your height is 170 , I predict your weight is 61.32943332393572 kg
Ở trên, khi bạn nhập 170 CM thì phần mềm sẽ dự đoán là nặng 61.3 Kg (dựa vào tập dữ
liệu ban đầu để hồi quy ra).
Còn rất nhiều ví dụ thực tế khác được Scikit-Learn trình bày rất kỹ, các bạn nên chủ động
nghiên cứu trên đó.
'''
from __future__ import print_function
import numpy as np
from sklearn import datasets,linear_model
#height(cm), input data, each row is a data point
X=np.array([[147,150,153,158,163,165,168,170,173,175,178,180,183]]).T
#weight (kg)
y=np.array([49,50,51,54,58,59,60,62,63,64,66,67,68])
#Building Xbar
one=np.ones((X.shape[0],1))
#each row is one data point
Xbar=np.concatenate((one,X),axis=1)
A=np.dot(Xbar.T,Xbar)
b=np.dot(Xbar.T,y)
w=np.dot(np.linalg.pinv(A),b)
#fit the model by Linear Regression
regr=linear_model.LinearRegression()
#in scikit-learn, each sample is one row
regr.fit(X,y)
#Compare two results
print("scikit-lean's solution:w_1=",regr.coef_[0],"w_0=",regr.intercept_)
print("our solution : w_1 = ",w[1],"w_0=",w[0])
yourHeight=int(input("Input your height:"))
yourWeight=regr.coef_[0]*yourHeight+regr.intercept_
print("Your height is ",yourHeight,", I predict your weight is",yourWeight,"kg")