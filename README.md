# Career Compass 🧭

**Career Compass** is a premium, cyberpunk-themed web application designed to help students discover their ideal career paths. It features a modern, responsive interface for exploring Science, Arts, Commerce, and Medical streams, and includes an **AI Career Counselor** powered by Groq (LLaMA 3.1).

## ✨ Features

- **Cyberpunk Aesthetic**: High-quality dark mode design with neon glows and glassmorphism.
- **Fluid Responsiveness**: Optimized for all devices—mobiles, tablets, and desktops.
- **AI Chatbot Integration**: Personalized career guidance via the "Career Compass AI".
- **Comprehensive Roadmaps**: In-depth information for dozens of career paths across four major streams.
- **Deployment Ready**: Configured for seamless deployment on platforms like Render.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [Groq API Key](https://console.groq.com/)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tulika-125/CareerCompass.git
   cd CareerCompass
   ```

2. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```
   The site will be available at `http://127.0.0.1:5000`.

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JS
- **AI Support**: Groq SDK (Llama 3.1 8B)
- **Deployment**: Configured for Render & Gunicorn

## 📄 License

Built for educational purposes as part of the Career Compass project.

---
*Built with ❤️ by Tulika Mahato*
