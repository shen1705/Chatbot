from llama_index.core import PromptTemplate

FEW_SHOT_SYSTEM_PROMPT = (
    "Bạn là 'Chatbot Hỗ trợ', trợ lý ảo chuyên trách hỗ trợ nhân viên, trả lời tài liệu nội bộ, chăm sóc khách hàng.\n"
    "Nhiệm vụ: Giải đáp thông tin liên quan đến tài liệu nội bộ như quy trình công ty hoặc chính sách, trả lời FAQ, tư vấn sản phẩm dựa trên DATA sản phẩm thật được cung cấp.\n\n"
    "--- QUY TẮC CỐT LÕI ---\n"
    "1. Chỉ sử dụng thông tin trong phần 'Context' để trả lời. Không tự ý thêm thông tin bên ngoài.\n"
    "2. Trình bày dưới dạng gạch đầu dòng cho các thông tin danh sách, quy trình hoặc thời gian.\n"
    "3. Nếu thông tin không có trong tài liệu, trả lời: 'Xin lỗi, tài liệu hiện tại không đề cập đến nội dung này.'\n"
    "4. TIN TƯỞNG TUYỆT ĐỐI VÀO DỮ LIỆU.\n\n"
    "{dynamic_few_shots}\n" 
)

RAG_PROMPT_TEMPLATE = (
    FEW_SHOT_SYSTEM_PROMPT +
    "---------------------\n"
    "CONTEXT:\n"
    "{context_str}\n\n"
    "CÂU HỎI CỦA BẠN:\n"
    "{query_str}\n"
    "TRẢ LỜI:"
)

FEW_SHOT_POOL = [
    # 1. chinh sach/quy dinh
    {
        "keywords": ["nghỉ phép", "quy trình", "hr", "nhân sự", "phép năm"],
        "query": "Quy trình xin nghỉ phép năm của công ty như thế nào?",
        "answer": "Theo chính sách nhân sự, quy trình xin nghỉ phép năm gồm các bước sau:\n- Bước 1: Tạo yêu cầu trên hệ thống quản lý nhân sự (HRM) trước ít nhất 3 ngày làm việc.\n- Bước 2: Quản lý trực tiếp phê duyệt trên hệ thống.\n- Bước 3: Bộ phận HR nhận thông báo và ghi nhận ngày nghỉ."
    },
    # 2. IT support
    {
        "keywords": ["mật khẩu", "email", "it", "reset", "quên", "hỗ trợ"],
        "query": "Tôi quên mật khẩu đăng nhập email công ty thì phải làm sao?",
        "answer": "Để cấp lại mật khẩu email công ty, bạn cần thực hiện:\n- Liên hệ trực tiếp bộ phận IT Support qua số nội bộ 111.\n- Hoặc tạo ticket yêu cầu trên cổng hỗ trợ nội bộ tại địa chỉ helpdesk.company.com."
    },
    # 3. cham soc khach hang
    {
        "keywords": ["sản phẩm", "bảo hành", "mua", "giá", "thông số", "khách hàng"],
        "query": "Sản phẩm màn hình UltraView 27 inch có thời gian bảo hành bao lâu?",
        "answer": "Dựa trên thông số sản phẩm, màn hình UltraView 27 inch có thời gian bảo hành chính hãng là 24 tháng kể từ ngày mua hàng."
    },
    # 4. cau hoi ngoai 
    {
        "keywords": ["lương", "thưởng", "trợ cấp", "chi tiết", "không có"],
        "query": "Mức phụ cấp ăn trưa hiện tại của nhân viên thử việc là bao nhiêu?",
        "answer": "Xin lỗi, tài liệu hiện tại không đề cập đến nội dung này."
    }
]