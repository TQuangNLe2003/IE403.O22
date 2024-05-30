# IE403_KhaiThacDuLieu
Đồ Án Môn Học _ "Detection spam comments on the Shopee  social media platform in Vietnam "


Hướng dẫn Run app.py:

- Tải file app.py: Tải file app.py từ nguồn tài nguyên hoặc sao chép mã nguồn đã được cung cấp.

- Cài đặt các thư viện cần thiết: Mở terminal và chạy các lệnh sau để cài đặt các thư viện cần thiết:
                  pip install streamlit torch transformers Pillow
  
- Thay đổi đường dẫn phù hợp: Trong mã nguồn app.py, đảm bảo rằng đường dẫn đến file bert_model.pth, thư mục chứa tokenizer và các hình ảnh đã được chỉ định chính xác.
- Mở terminal và chạy lệnh sau:
                  streamlit run app.py
- Sau khi chạy lệnh này, một trình duyệt web mới sẽ mở và hiển thị ứng dụng web demo. Nhập văn bản vào ô văn bản và nhấn nút "Dự đoán" để xem dự đoán của mô hình về xem văn bản đó có phải là spam hay không.
