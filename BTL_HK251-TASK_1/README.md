# Hiện Thực Bộ Lọc Wiener

| 🧾 **Tài liệu**                                                                            | 🔗 **Mô tả**                                                                                                                       |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Bộ Lọc Wiener (MMSE)**](docs/MMSE.md)                                                   | Giải thích chi tiết về lý thuyết Bộ lọc Wiener, công thức MMSE, tự tương quan và cách ước lượng hệ số tối ưu.                                 |
| [**Hướng dẫn chạy mã**](docs/RunCode.md)                                                   | Mô tả chi tiết các bước chạy chương trình C++ và pytest, cách tổ chức thư mục và các file dữ liệu (`input.txt`, `desired.txt`, `result.txt`). |
| [**Ví dụ minh họa (Overleaf)**](https://www.overleaf.com/read/bctwhsqdkbmr#cad66c) | Tài liệu LaTeX minh họa mô hình Bộ lọc Wiener với ví dụ thực tế, biểu đồ và công thức trình bày rõ ràng.                                      |

## Mô Tả Test Case

| 🧩 **Tên test case** | 📝 **Mô tả**                                                                                                                                                                        |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **test_001**         | Trường hợp cơ bản với tín hiệu ngắn:<br> ( d = [2.0, 3.0] ), ( x = [2.5, 2.8] ). Dùng để kiểm tra tính chính xác của bộ lọc khi dữ liệu chỉ có 2 mẫu.                               |
| **test_002**         | Trường hợp cơ bản với tín hiệu dài hơn:<br> ( d = [1.5, 2.8, 3.2] ), ( x = [1.2, 2.5, 3.0] ). Dùng để đánh giá bộ lọc với dữ liệu 3 điểm và kiểm chứng tính ổn định của thuật toán. |
| **test_003**         | Trường hợp cơ bản với tín hiệu ngắn:<br> ( d = [2.0, 3.0] ), ( x = [2.5, 2.8] ). Dùng để kiểm tra tính chính xác của bộ lọc khi dữ liệu chỉ có 2 mẫu.                               |
| **test_004**         | Trường hợp cơ bản với tín hiệu dài hơn:<br> ( d = [1.5, 2.8, 3.2] ), ( x = [1.2, 2.5, 3.0] ). Dùng để đánh giá bộ lọc với dữ liệu 3 điểm và kiểm chứng tính ổn định của thuật toán. |
| **test_005**         | Sóng sin với nhiễu trắng (White Noise):<br> ( d ) là sóng sine với tần số 0.05, biên độ 1.0 (500 mẫu), ( x = d + ) nhiễu trắng (biên độ 0.3). Kiểm tra khả năng lọc nhiễu trắng cơ bản, kỳ vọng MMSE < 0.1. |
| **test_006**         | Sóng sin với nhiễu hồng (Pink Noise):<br> ( d ) là sóng sine với tần số 0.05, biên độ 1.0 (500 mẫu), ( x = d + ) nhiễu hồng (1/f noise, biên độ 0.3). Kiểm tra khả năng xử lý nhiễu có phổ tần phức tạp hơn nhiễu trắng. |
| **test_007**         | Sóng cosin với nhiễu trắng:<br> ( d ) là sóng cosine với tần số 0.03, biên độ 2.0 (500 mẫu), ( x = d + ) nhiễu trắng (biên độ 0.5). Kiểm tra bộ lọc với dạng sóng khác và mức nhiễu cao hơn. |
| **test_008**         | Tín hiệu hỗn hợp đa tần số:<br> ( d = sin(2π×0.05×n) + 0.5×sin(2π×0.1×n) + 0.3×cos(2π×0.02×n) ) (500 mẫu), ( x = d + ) nhiễu trắng (biên độ 0.4). Kiểm tra khả năng xử lý tín hiệu phức tạp với nhiều thành phần tần số. |
| **test_009**         | Kiểm tra định dạng đầu ra khi size của input và desired không match|
| **test_010**         | Kịch bản nhiễu thấp:<br> ( d ) là sóng sine (tần số 0.04, biên độ 1.5), ( x = d + ) nhiễu rất nhỏ (biên độ 0.05). Kiểm tra độ chính xác cao, kỳ vọng MMSE < 0.01. |
| **test_011**         | Kịch bản nhiễu cao:<br> ( d ) là sóng sine (tần số 0.05, biên độ 1.0), ( x = d + ) nhiễu lớn (biên độ 0.8). Kiểm tra khả năng làm việc trong môi trường nhiễu mạnh. |
| **test_012**         | Chưa mô tả |
| **test_013**         | Chưa mô tả |
| **test_014**         | Chưa mô tả |
| **test_015**         | Chưa mô tả |
| **test_016**         | Chưa mô tả |

# Plot Kết Quả

Dưới đây là biểu đồ minh họa kết quả của Bộ lọc Wiener trên các test case đã cho:

![Wiener Filter Results](tests/test_006/wiener_filter_analysis.png)

Khi chạy testcase, plot sẽ xuất hiện trong thư mục của testcase đó. Hoặc có thể dùng lệnh `python weiner_filter_plot.py` để plot. Lưu ý: lệnh này sẽ lấy 3 file input.txt, desired.txt, expect.txt trong cùng thư mục của nó.

