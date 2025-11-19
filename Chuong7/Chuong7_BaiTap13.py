#Câu 13: Xử lý XML File - Viết phần mềm Quản Lý Thiết Bị
'''
Yêu cầu:
Chương trình quản lý thiết bị gồm có 2 tập dữ liệu
Tập lưu danh sách nhóm thiết bị có tên nhomthietbi.xml có dữ liệu mẫu và format như
dưới đây:
<?xml version="1.0" encoding="UTF-8" ?>
<nhoms>
 <nhom>
 <ma>n1</ma>
 <ten>Nhóm 1</ten>
 </nhom>
 <nhom>
 <ma>n2</ma>
 <ten>Nhóm 2</ten>
 </nhom>
 <nhom>
 <ma>n3</ma>
 <ten>Nhóm 3</ten>
 </nhom>
</nhoms>
Theo cấu trúc ở trên thì mỗi Nhóm sẽ có: Mã nhóm, tên nhóm.
Chương trình phải đọc dữ liệu danh sách nhóm thiết bị.
Tập dữ liệu thiết bị được lưu trong file ThietBi.xml, có dữ liệu và cấu trúc như sau:
<?xml version="1.0" encoding="UTF-8" ?>
<thietbis>
 <thietbi manhom="n1">
 <ma>tb1</ma>
 <ten>Thiết bị 2</ten>
 </thietbi>
 <thietbi manhom="n1">
 <ma>tb2</ma>
 <ten>Thiết bị 2</ten>
 </thietbi>
 <thietbi manhom="n2">
 <ma>tb3</ma>
 <ten>Thiết bị 3</ten>
 </thietbi>
 <thietbi manhom="n3">
 <ma>tb4</ma>
 <ten>Thiết bị 4</ten>
 </thietbi>
 <thietbi manhom="n3">
     <ma>tb5</ma>
     <ten>Thiết bị 5</ten>
 </thietbi>
</thietbis>

Theo cấu trúc ở trên, thì mỗi Thiết bị sẽ có thuộc tính Mã nhóm để phân loại thiết bị vào
đúng nhóm thiết bị. Ngoài ra mỗi thiết bị sẽ có thêm 2 thuộc tính: mã và Tên.
Chương trình cần cung cấp các chức năng:
- Hiển thị danh sách Nhóm thiết bị
- Hiển thị toàn bộ Thiết bị
- Lọc Danh sách Thiết bị theo Nhóm thiết bị
- Xuất Nhóm thiết bị có số lượng thiết bị nhiều nhất
'''
