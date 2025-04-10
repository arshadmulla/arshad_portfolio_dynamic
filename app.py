import streamlit as st
import urllib.parse

# --- Page Config ---
st.set_page_config(page_title="Arshad Mulla | Portfolio", page_icon=":rocket:", layout="wide")

# --- Sidebar ---
st.sidebar.title("Connect with Me")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/arshad-mulla-5b2451229/)")
st.sidebar.markdown("[GitHub](https://github.com/arshadmulla)")
st.sidebar.markdown("Email: arshadmulla75@gmail.com")

# --- Contact Button ---
email_address = "arshadmulla75@gmail.com"
subject = "Opportunity from Your Portfolio Website"
body = (
    "Dear Arshad,%0D%0A%0D%0A"
    "I came across your portfolio and was impressed by your work in data science, machine learning, and AI. "
    "We have an opportunity that may align well with your skills and interests.%0D%0A%0D%0A"
    "Please let me know a convenient time to connect, or feel free to share your updated availability.%0D%0A%0D%0A"
    "Looking forward to hearing from you.%0D%0A%0D%0A"
    "Best regards,%0D%0A"
    "[Your Name Here]"
)
mailto_link = f"mailto:{email_address}?subject={urllib.parse.quote(subject)}&body={body}"
st.sidebar.markdown(f'<a href="{mailto_link}" target="_blank"><button>📧 Contact Me</button></a>', unsafe_allow_html=True)


# --- Main Content ---
st.title("Hi, I'm Arshad Mulla")
st.subheader("Data Science | Machine Learning | AI Enthusiast")

# --- Resume Download ---
with open("ARSHADMULLA_RESUME4.pdf", "rb") as file:
    resume_bytes = file.read()
st.download_button(
    label="📄 Download My Resume",
    data=resume_bytes,
    file_name="ARSHADMULLA_RESUME4.pdf",
    mime="application/pdf"
)


# --- Bio and Goals ---
st.header("About Me")
st.write("""
As a recent graduate from Royal College with a Bachelor's degree in Computer Science, I am passionate about leveraging technology to solve complex problems. My goal is to contribute to innovative projects in the fields of data science and artificial intelligence, driving impactful solutions that enhance user experiences and business outcomes.
""")

# --- Tabs ---
tabs = st.tabs(["Projects", "Skills", "Education", "Certifications","Research & Publications", "Awards"])

# --- Projects Tab ---
# --- Projects Tab ---
with tabs[0]:
    st.header("Projects")

    st.subheader("Gemini AI Health App (Jun 2024 – july 2024)")
    st.markdown("""
- **Built With**: Python, Streamlit, Google Gemini Pro Vision API  
- **Features**: AI-powered health insights, efficient image processing with Pillow, secure environment management  
- **Impact**: 1,500+ users in the first month, 95% accuracy, <2s response time, 50,000+ data points analyzed
""")

    st.subheader("Diwali Sales Data Analysis (May 2024 – Jun 2024)")
    st.markdown("""
- **Focus**: Identified top buyers during Diwali  
- **Tech**: Pandas, Matplotlib, Seaborn  
- **Insight**: Married women (26–35) in IT/Healthcare/Aviation were top spenders  
- **Result**: Helped optimize marketing strategies
""")

    st.subheader("AI SaaS Image Platform (Feb 2024 – Apr 2024)")
    st.markdown("""
- **Stack**: Next.js, MySQL, Cloudinary, Shadcn, Stripe  
- **Features**: Image segmentation, background removal, Stripe for payments  
- **Impact**: 95% accuracy, 25% user engagement increase, 15% subscription growth
""")

    st.subheader("Robot Navigation System (Aug 2023 – Dec 2023)")
    st.markdown("""
- **Scope**: Built for Avishkar Research Competition  
- **Highlights**: Sensor fusion, RL-based decision-making  
- **Outcome**: 30% better path accuracy, 20% lower latency
""")

    st.subheader("Stock Price Prediction Web App (Jun 2023 – Dec 2023)")
    st.markdown("""
- **Tech**: LSTM, Prophet, Streamlit, Plotly  
- **Features**: Real-time forecasting, intuitive UI  
- **Performance**: Achieved 90% accuracy on predictions
""")

    st.subheader("Weather App using HTML/CSS/JS (Sep 2023 – Oct 2023)")
    st.markdown("""
- **Built With**: HTML, CSS, JavaScript  
- **Features**: Real-time API weather updates, responsive UI  
- **Bonus**: Git version control & modern design techniques
""")


# --- Skills Tab ---
# --- Skills Tab ---
with tabs[1]:
    st.header("Technical Skills")

    st.subheader("🧠 Core AI & ML")
    st.write("""
- Machine Learning
- Deep Learning
- Artificial Intelligence (AI)
- Generative AI
- AI Model Optimization
- Data Annotation & Labeling (for AI training)
""")

    st.subheader("🧮 Algorithms & Models")
    st.write("""
- Linear Regression
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Trees
- Random Forest
- Convolutional Neural Networks (CNN)
- Recurrent Neural Networks (RNN)
- Facebook Prophet
""")

    st.subheader("📊 Data Science & Analytics")
    st.write("""
- Data Analysis
- Data Visualization
- Data Management
- Data Modeling
- Statistics
- Research
- Business Analysis
""")

    st.subheader("🧰 Tools & Libraries")
    st.write("""
- Python (Programming Language)
- pandas
- NumPy
- Matplotlib
- Seaborn
- TensorFlow
- Streamlit
- Plotly
""")

    st.subheader("☁️ Cloud & Deployment")
    st.write("""
- Oracle Cloud Infrastructure (OCI)
- Cloud Computing
- Cloud Applications
- Cloud Application Development
- Cloud Security
""")


# --- Education Tab ---
with tabs[2]:
    st.header("Education")
    st.write("""
**Bachelor of Science in Computer Science**
- Royal College of Arts, Science and Commerce (University of Mumbai)
- Location: Mumbai, India
""")

# --- Certifications Tab ---
# --- Certifications Tab ---
with tabs[3]:
    st.header("Licenses & Certifications")

    st.subheader("🎓 Harvard University")
    st.markdown("""
- **CS109x: Introduction to Data Science with Python** (Issued: May 2024)  
- Skills: Python, Machine Learning, Linear & Logistic Regression, Deep Learning, KNN, Decision Trees, Data Visualization, CNN, RNN, NumPy, pandas, Data Analysis, Data Management, Random Forest
""")

    st.subheader("🎓 Great Learning")
    st.markdown("""
- **Python for Machine Learning** (Issued: Oct 2023)  
  Skills: Numerical Python, Mathematics, pandas, Python, Machine Learning, NumPy

- **Introduction to Deep Learning** (Issued: Jul 2023)  
  Skills: Deep Learning, Data Analysis, Business Analysis, Calculus

- **Introduction to Data Science**  
  Skills: Seaborn, Research, Matplotlib, pandas, TensorFlow, NumPy, Machine Learning, Calculus
""")

    st.subheader("☁️ Oracle")
    st.markdown("""
- **Oracle Cloud Infrastructure 2023 Certified Foundations Associate** (Issued: Jul 2023)  
  Skills: Cloud Computing, Cloud Applications, Cloud Security, Cloud Application Development
""")

    st.subheader("🧠 Open Weaver")
    st.markdown("""
- **Basics of HTML/CSS for Beginners – Online Bootcamp** (Issued: Jan 2023)  
  Credential ID: 85278531091036  
  Skills: HTML, CSS

- **Basics of JavaScript Programming – Bootcamp** (Issued: Jan 2023)  
  Credential ID: 52427344592059  
  Skills: JavaScript

- **Build Your Own GPT4All-based Content Generator – Bootcamp** (Issued: Jan 2023)  
  Credential ID: 64661683705284  
  Skills: Deep Learning, Data Analysis, Business Analysis, Machine Learning, Design, Entrepreneurship, Analytical Skills
""")

    st.subheader("🎓 Princeton University")
    st.markdown("""
- **Deep Learning Foundations**  
  Skills: lstm , neural networks , Transformer,algorithms
""")

# --- Research & Publications Tab ---
# --- Research & Publications Tab ---
with tabs[4]:
    st.header("🧪 Research & Publications")

    st.markdown("""
**📄 An Advanced Robot Navigation System Integrating Line Following and Obstacle Avoidance**  
*Published in Journal of Emerging Trends and Novel Research (JETNR)*  
- 📅 Published: February 2025  
- 🧠 Impact Factor: 8.27  
- 🧾 Paper ID: JETNR2502002  
- 👥 Co-authors: Ritika Lala, Asad Afsar Do Alam Quershi, Ansari Ferhan Afroz Alam  
""")

    from PIL import Image
    image = Image.open("jetnr_certificate.jpeg")  # Make sure this file exists in the same directory
    st.image(image, caption='JETNR Publication Certificate', use_column_width=True)

    st.markdown("""
**📄 Avishkar Research Project**  
*Presented at University of Mumbai – State Level Academic Competition*  
- Developed a Robot Navigation System for autonomous pathfinding  
- Integrated sensor fusion, obstacle avoidance, and line following  
- Strengthened skills in robotics, AI, and real-world deployment
""")



# --- Awards Tab ---
# --- Awards Tab ---
with tabs[5]:
    st.header("Awards & Achievements")

    st.subheader("🥇 Gold Medalist – Table Tennis, KC College, Churchgate (Jan 2024)")
    st.markdown("""
- **Event**: Intercollegiate Table Tennis Championship  
- **Issued By**: KC College, Mumbai (University of Mumbai)  
- **Achievement**:
  - Secured 1st place in a highly competitive tournament  
  - Demonstrated strategic gameplay, resilience, and sportsmanship  
  - Recognized as a top performer on campus  
- **Date**: 29th January 2024  
""")

    st.subheader("🥈 2nd Prize – Table Tennis, Mridang 2023–24 (Jan 2024)")
    st.markdown("""
- **Event**: Mridang Intercollegiate Festival  
- **Issued By**: Reena Mehta College (University of Mumbai)  
- **Achievement**:
  - Earned 2nd place among top college competitors  
  - Reflected dedication, preparation, and competitive spirit  
""")

    st.subheader("🏆 Avishkar Research Project Competition (Dec 2023)")
    st.markdown("""
- **Issued By**: University of Mumbai  
- **Achievement**:
  - Designed and led development of a Robot Navigation System  
  - Focused on Line Following, Obstacle Avoidance, and Pathfinding  
  - Sharpened skills in robotics, AI, and algorithm design  
""")

    st.subheader("🥇 Gold Medalist – Inter-Class Table Tennis Tournament (Nov 2023)")
    st.markdown("""
- **Event**: Intra-college Championship  
- **Issued By**: University of Mumbai  
- **Achievement**:
  - Clinched the Gold Medal through consistency and precision  
  - Recognized for leadership, sportsmanship, and performance  
""")

# --- Footer ---
st.markdown("---")

