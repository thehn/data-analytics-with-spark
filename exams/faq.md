# Các câu hỏi thường gặp

1. Folder làm bài sẽ là folder exams luôn hay folder khác, nếu folder khác thì mình có tên folder hay yml để set up docker hay được set up sẵn?

*Trả lời:*

- Root path tính từ folder `data-analytics-with-spark` (root git folder)
- Folder làm bài sẽ nằm trong folder `exams` (level 1 tính từ root path): `data-analytics-with-spark\exams`
- Mỗi sinh viên tạo riêng một sub-folder với tên được đặt là mã sinh viên của mình (8 ký tư). VD: `data-analytics-with-spark\exams\12345678` (level 2 tính từ root path)
- Trong folder nộp bài sẽ có 2 files và 1 folder con:
  - `multi-choices.csv` -> chứa các câu trả lời cho phần làm bài trắc nghiệm. File này theo format csv, định dạng theo file trong ví du. Ví dụ tham khảo: data-analytics-with-spark\exams\12345678\multi-choice.csv.
  - `lab.ipynb` -> chứa các câu trả lời (codes) cho phần làm bài thực hành. Ví dụ tham khảo: data-analytics-with-spark\exams\12345678\lab.ipynb.
  - Folder con `output` chứa dữ liệu đầu ra trong quá trình làm bài thi thực hành.

2. Các path dùng trong lúc làm bài có được set biến trên đầu file notebook luôn để tránh việc đổi path nhiều nơi không ạ ?

*Trả lời:*

Các paths có thể đặt ở trên đầu hoặc khởi tạo tập trung tại 1 nơi (notebook cell) cho dễ theo dõi và quản lý.

3. Dataframe làm việc trong notebook sẽ luôn là df được gọi đầu tiên trong file hay sẽ là dataframe gần nhất được mở (kiểu mở csv load df => xử lí abc => save df as delta => open delta => vậy thì lúc này sẽ làm việc với df mở từ csv ban đầu hay df_xx mở từ delta table)

*Trả lời:*

- Mỗi một câu hỏi sẽ yêu cầu kết quả trả về 1 hoặc nhiều dataframes hay variables với tên được cho trước trong notebook cell tương ứng.
- Tên các dataframes / variables này sẽ có định dạng: df_xx, var_xx trong đó xx là số thứ tự của câu hỏi.
- Kết quả trả về của các dataframes / variables sẽ dùng để chấm điểm. Do đó tên các biến này không được thay đổi.
- Ngoài các biến này ra thì các bạn được tự do khai báo và khởi tạo các biến khác để tiện xử lý.

4. Nộp bài

- Nén folder với tên là mã sinh viên của mình theo định dạng .zip.
- Trong folder này phải chứa 2 files `multi-choices.csv`, `lab.ipynb` và folder con `output` như hướng dẫn trên. Sau đó gửi lại qua email: <hoangngocthe168@gmail.com>.
- VD: `12345678.zip`.
