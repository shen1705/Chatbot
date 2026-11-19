# 🤖 RAG Chatbot AI

Hệ thống Chatbot AI thông minh trả lời câu hỏi và tra cứu tài liệu nội bộ dựa trên kiến trúc **RAG (Retrieval-Augmented Generation)** và **Dynamic Few-Shot In-Context Learning**.

---

## 🚀 Tính Năng Nổi Bật

- **LlamaIndex RAG Pipeline:** Quản lý chia đoạn (chunking), lập chỉ mục (vector indexing) và truy hồi thông tin (semantic retrieval).
- **Trích xuất thông minh:** Hỗ trợ `LlamaParse` và `PyMuPDF` bóc tách dữ liệu văn bản và bảng biểu từ tài liệu PDF.
- **Dynamic Few-Shot Learning:** Tự động so khớp từ khóa và lựa chọn ví dụ mẫu theo ngữ cảnh (HR, IT Support, Chính sách, CSKH) đưa vào Prompt giúp câu trả lời chuẩn xác và hạn chế ảo giác (hallucination).
- **Hỗ trợ 2 phương thức giao tiếp:**
  - **Console CLI:** Trò chuyện trực tiếp qua dòng lệnh (`main.py`).
  - **REST API:** Cung cấp endpoint `POST /chat` qua FastAPI và Uvicorn (`app.py`).

---

## 🛠️ Cài Đặt & Khởi Chạy

### 1. Cài đặt môi trường
Khuyến nghị sử dụng môi trường ảo Python 3.10+:
```bash
python -m venv .venv
source .venv/bin/activate  # Trên Linux/macOS
# hoặc .venv\Scripts\activate trên Windows

pip install -r requirements.txt
```

### 2. Cấu hình biến môi trường
Tạo file `.env` từ file mẫu `.env.example`:
```bash
cp .env.example .env
```
Điền các API keys cần thiết:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
LLAMAPARSE_API_KEY=your_llamaparse_key_here  # Tùy chọn nếu dùng LlamaParse
LLM_MODEL=models/gemini-2.0-flash            # Hoặc models/gemini-1.5-flash
EMBEDDING_MODEL=BAAI/bge-m3                  # Hoặc sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

### 3. Khởi chạy Chatbot

- **Chạy giao diện dòng lệnh (CLI):**
```bash
python main.py
```

- **Chạy máy chủ REST API (FastAPI):**
```bash
python app.py
```
Endpoint: `http://localhost:8000/chat`
Payload mẫu:
```json
{
  "message": "Thời gian và địa điểm nộp học phí theo quy định như thế nào?"
}
```
Response mẫu:
```json
{
  "reply": "Thời gian nộp học phí được quy định như sau: ...",
  "status": "success"
}
```

---

## 🧠 Lựa Chọn Models Đề Xuất Cho RAG

| Thành phần | Model Đề xuất SOTA | Ưu điểm nổi bật |
| :--- | :--- | :--- |
| **LLM (Generation)** | `gemini-2.0-flash` / `gemini-1.5-pro` | Cửa sổ ngữ cảnh 1M token, tốc độ xử lý nhanh, hiểu và sinh tiếng Việt tự nhiên |
| **Open-source LLM** | `Qwen2.5-7B-Instruct` | Chạy offline qua Ollama/vLLM, bảo mật tuyệt đối dữ liệu nội bộ |
| **Embedding** | `BAAI/bge-m3` | Ngữ cảnh 8192 token (khắc phục giới hạn 128 token của MiniLM), Top 1 MTEB đa ngôn ngữ |
| **Reranker** | `BAAI/bge-reranker-v2-m3` / Cohere Rerank | Tăng độ chính xác truy hồi lên 20-35%, lọc bỏ triệt để các đoạn văn bản gây nhiễu |
