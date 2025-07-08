# Prompt luận giải
def make_prompt_luan_giai(thienban: str, diaban: str) -> str:
    return f"""
Bạn là chuyên gia tử vi. Dưới đây là thông tin lá số gồm Thiên bàn, 12 cung và Can Chi năm/tháng/ngày/giờ sinh.

🔸 Nhiệm vụ:
- Luận giải tổng quan mệnh lý dựa trên Cung Mệnh và Can Chi ngày sinh.
- Phân tích chi tiết 12 cung, nêu rõ các sao chiếu, đặc điểm nổi bật, vận hạn (nếu có).
- Nhấn mạnh các yếu tố:
  • Cung Mệnh, Mệnh Chủ, Thân Chủ (nếu có).
  • Các sao chủ mệnh, hạn năm và ảnh hưởng chính.
  • Vòng Tràng Sinh, Tam hợp, Nhị hợp, Cục số, Âm Dương thuận/nghịch.

🔸 Thiên bàn:

{thienban}

🔸 Danh sách 12 cung (Chỉ lấy từ Cung 1 đến Cung 12):

{diaban}

🔸 Yêu cầu khi viết luận giải:
- Viết tiếng Việt rõ ràng, dễ hiểu, đúng phong cách học thuật của tử vi truyền thống.
- Chia phần theo tiêu đề (VD: 🔹 Tổng Quan Mệnh Lý, 🔸 Cung Quan Lộc…).
- Dài từ 300 từ trở lên, không rút gọn ý quan trọng.
- **Không cần đưa ra gợi ý sản phẩm hay hành vi.** Tuy nhiên, nội dung cần đủ chi tiết để có thể sử dụng trong các ngữ cảnh ứng dụng như:
  • Fintech (tài chính), BĐS, Du lịch, E-commerce, Nghề nghiệp/Cộng đồng.

Hãy bắt đầu bằng 🔹 Tổng Quan Mệnh Lý, sau đó phân tích từng cung, và kết luận chung.
"""