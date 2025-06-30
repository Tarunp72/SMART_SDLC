import streamlit as st
import requests
from ui_utils import set_custom_style, show_header

BACKEND_URL = "http://localhost:8000"  # Change this to your backend URL if needed
HEADERS = {"ngrok-skip-browser-warning": "true"}

set_custom_style()

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/906/906175.png", width=60)
    st.title("SmartSDLC")
    st.markdown("---")
    st.header("Navigation")
    page = st.radio(
        "Go to:",
        [
            "🏠 Home",
            "📝 Requirement Analysis",
            "📐 Design",
            "💻 Coding",
            "🧪 Testing",
            "💬 Chatbot Assistant"
        ],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.caption("Powered by IBM Granite 3.3_2b Instruct, FastAPI & Streamlit")

if page == "🏠 Home":
    show_header()
    st.markdown("""
    **SmartSDLC** is an AI-powered Software Development Lifecycle Automation Platform that helps you with:
    - 📝 **Requirement Analysis:** Extract requirements from PDFs and custom prompts.
    - 📐 **Design:** Generate design docs, UML diagrams, or summaries.
    - 💻 **Coding:** Generate code, explain code in multiple languages.
    - 🧪 **Testing:** Generate test cases, detect and fix bugs.
    - 💬 **Chatbot Assistant:** Ask anything about SDLC, coding, and more.
    """)
    st.info("Tip: All features are available from the sidebar menu.")

elif page == "📝 Requirement Analysis":
    st.header("📝 Requirement Analysis")
    uploaded_file = st.file_uploader("Upload a PDF containing requirements", type=["pdf"])
    user_prompt = st.text_area("Optional: Add additional context or prompt for requirement extraction", placeholder="E.g., Focus on functional requirements only.")
    if uploaded_file and st.button("Analyze Requirements"):
        files = {"file": uploaded_file.getvalue()}
        data = {"prompt": user_prompt}
        with st.spinner("Analyzing..."):
            r = requests.post(f"{BACKEND_URL}/analyze-requirements/", files=files, data=data, headers=HEADERS)
        if r.ok:
            data = r.json()
            st.success("Requirements extracted:")   
            for req in data["requirements"]:
                st.markdown(f"- {req}")
        else:
            st.error("Failed to analyze requirements.")

elif page == "📐 Design":
    st.header("📐 Design")
    design_prompt = st.text_area("Describe the system or module for design (e.g., 'Design a library management system'):")
    design_type = st.selectbox("Design Output", ["Design Document", "UML Diagram (text)", "Summary"])
    if st.button("Generate Design"):
        payload = {"prompt": design_prompt, "design_type": design_type}
        with st.spinner("Generating design..."):
            r = requests.post(f"{BACKEND_URL}/generate-design/", json=payload, headers=HEADERS)
        if r.ok:
            result = r.json()["design"]
            st.markdown(result)
        else:
            st.error("Failed to generate design.")

elif page == "💻 Coding":
    st.header("💻 Coding")
    code_tab = st.radio("Choose:", ["Generate Code", "Explain Code"])
    if code_tab == "Generate Code":
        prompt = st.text_area("Describe the requirement:")
        language = st.selectbox("Select language:", ["Python", "JavaScript", "Java"])
        if st.button("Generate Code"):
            payload = {"prompt": prompt, "language": language}
            with st.spinner("Generating code..."):
                r = requests.post(f"{BACKEND_URL}/generate-code/", json=payload, headers=HEADERS)
            if r.ok:
                code = r.json()["code"]
                st.code(code, language=language.lower())
            else:
                st.error("Failed to generate code.")
    else:
        code = st.text_area("Paste code to explain:")
        language = st.selectbox("Language:", ["Python", "JavaScript", "Java"], key="explain_lang")
        if st.button("Explain Code"):
            payload = {"code": code, "language": language}
            with st.spinner("Explaining..."):
                r = requests.post(f"{BACKEND_URL}/explain-code/", json=payload, headers=HEADERS)
            if r.ok:
                explanation = r.json()["explanation"]
                st.write(explanation)
            else:
                st.error("Failed to explain code.")

elif page == "🧪 Testing":
    st.header("🧪 Testing")
    test_tab = st.radio("Choose:", ["Generate Test Cases", "Bug Detection & Fixing"])
    if test_tab == "Generate Test Cases":
        code = st.text_area("Paste code to generate test cases for:")
        language = st.selectbox("Language:", ["Python", "JavaScript", "Java"], key="test_lang")
        if st.button("Generate Test Cases"):
            payload = {"code": code, "language": language}
            with st.spinner("Generating test cases..."):
                r = requests.post(f"{BACKEND_URL}/generate-tests/", json=payload, headers=HEADERS)
            if r.ok:
                tests = r.json()["test_cases"]
                st.code(tests, language=language.lower())
            else:
                st.error("Failed to generate test cases.")
    else:
        code = st.text_area("Paste your buggy code here:")
        language = st.selectbox("Language:", ["Python", "JavaScript", "Java"], key="bug_lang")
        if st.button("Detect & Fix Bug"):
            payload = {"code": code, "language": language}
            with st.spinner("Analyzing and fixing..."):
                r = requests.post(f"{BACKEND_URL}/fix-bug/", json=payload, headers=HEADERS)
            if r.ok:
                res = r.json()
                st.subheader("Fixed Code:")
                st.code(res["fixed_code"], language=language.lower())
                if res.get("explanation"):
                    with st.expander("Explanation"):
                        st.write(res["explanation"])
            else:
                st.error("Failed to fix bug.")

elif page == "💬 Chatbot Assistant":
    st.header("💬 AI Chatbot Assistant")
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    user_input = st.text_input("Ask anything about SDLC, coding, etc.")
    if st.button("Send"):
        payload = {"message": user_input, "history": st.session_state["chat_history"]}
        with st.spinner("Thinking..."):
            r = requests.post(f"{BACKEND_URL}/chat/", json=payload, headers=HEADERS)
        if r.ok:
            response = r.json()["response"]
            st.session_state["chat_history"].append(f"User: {user_input}")
            st.session_state["chat_history"].append(f"AI: {response}")
            st.write(response)
        else:
            st.error("Chatbot failed to respond.")
    if st.session_state["chat_history"]:
        with st.expander("Chat History"):
            for msg in st.session_state["chat_history"]:
                st.write(msg)
