# Phan tich diem thi THPT 2020 cua thanh pho HCM
Sử dụng cách random ID thí sinh để thu thập tên và điểm thi từng môn thi của các thí sinh <br/>

# Lam sach va chuan hoa du lieu
File raw thu được dưới dạng file `HTML` <br/>
Sử dụng python xóa các tag, khoảng trống, chuẩn hóa Tiếng Việt theo chuẩn `UTF-8`, tách điểm từng môn, `đánh nhãn` những môn thi thiếu điểm <br/> 
Đưa về định dạng CSV với các cột sbd, họ và tên, ngày tháng năm sinh, các điểm môn thi <br/>

# Ve nhanh mot so dac diem noi bat cua ky thi
Với file CSV đã làm sạch vẽ các biểu đồ thể hiện đắc điểm quan trọng của kỳ thi như: <br/>
  - số lượng thí sinh bỏ thi,
  - điểm trung bình theo từng môn,
  - điển trung bình theo độ tuổi, ...
</p>
hỗ trợ đưa ra nhận định chính về chất lượng kỳ thi và các yếu tố cần lưu ý về thi sinh để có những điều chỉnh cho kỳ thi sau
