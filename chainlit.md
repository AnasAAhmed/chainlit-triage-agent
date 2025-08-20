# 🤖 AI Multi-Agent Assistant (Translator + Teacher)

A CLI + Chainlit project powered by **Google Gemini**. Uses a **Triage Agent** to decide between **Translator Agent** 🌍 and **Teacher Agent** 📚.

---

## 📖 Dictionary Format

**Project Name**: AI Multi-Agent Assistant (Translator + Teacher)  

**Purpose**: Showcase agent-based AI workflows as part of **Governor House AI Initiative** and **Panaverse DAO** curriculum.  

**Core Agents**:  
- 🌍 Translator Agent → Translates text into target languages  
- 📚 Teacher Agent → Explains concepts and provides educational support  
- 🧭 Triage Agent → Routes queries to correct agent  

**Technologies**:  
- Python 3.9+  
- Google Gemini (OpenAI-compatible endpoint)  
- Agents Framework (`Runner`, `Agent`, `RunConfig`)  
- Chainlit (chat-based UI)  
- `python-dotenv`  

**Features**:  
- ✅ Translation into any supported language  
- ✅ Intelligent query routing via Triage Agent  
- ✅ Educational teaching/explanation mode  
- ✅ CLI interaction (quick testing)  
- ✅ Chainlit chat UI (interactive)  
- ✅ Secure API key loading via `.env`  

**Setup Instructions**:  
1. Clone repo → `git clone https://github.com/AnasAAhmed/ai-multiagent-translator-teacher.git`  
2. Enter folder → `cd ai-multiagent-translator-teacher`  
3. Create venv → `python -m venv venv`  
4. Activate → `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (Mac/Linux)  
5. Install deps → `pip install -r requirements.txt`  
6. Add `.env` → `GEMINI_API_KEY=your_google_gemini_api_key`  
7. Run CLI → `python main.py`  
8. Run Chainlit → `chainlit run main.py`  

**Project Structure**:  
├── agents/
│ └── agent.py
├── config/
│ └── agent_config.py
├── main.py
├── requirements.txt
├── .env
└── README.md

**Example Usage**:  
- Input: `"Translate 'Good morning' to French"` → Output: `"Bonjour"`  
- Input: `"Explain recursion in simple words"` → Output: `"Recursion is when a function calls itself..."`  

---