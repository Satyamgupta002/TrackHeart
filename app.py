import streamlit as st
import pandas as pd
import io
from fpdf import FPDF
from predict import predict_disease

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="TrackHeart",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background-color:#00172F;
}

.hero{
    background:linear-gradient(90deg,#dc2626,#ef4444);
    padding:30px;
    border-radius:18px;
    color:white;
    text-align:center;
    margin-bottom:20px;
}

.hero h1{
    font-size:42px;
    margin-bottom:10px;
}

.hero p{
    font-size:20px;
}

.metric-card{
    background:#0F172AFF;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.12);
    height:200px;
    width:100%;
}

.result-high{
    background:#fee2e2;
    color:#991b1b;
    padding:18px;
    border-radius:15px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

.result-low{
    background:#dcfce7;
    color:#166534;
    padding:18px;
    border-radius:15px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

.stButton>button{
    width:100%;
    height:55px;
    background:#dc2626;
    color:white;
    border-radius:12px;
    border:none;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#b91c1c;
    color:white;
}

.stDownloadButton>button{
    width:100%;
    height:55px;
    background:#2563eb;
    color:white;
    border-radius:12px;
    border:none;
    font-size:18px;
    font-weight:bold;
    margin-top:18px;
    margin-bottom:18px;
}

.stDownloadButton>button:hover{
    background:#1d4ed8;
    color:white;
}

section[data-testid="stSidebar"]{
    background:#111827;
    padding-top:1rem;
    padding-bottom:1rem;
}

section[data-testid="stSidebar"] .block-container{
    padding-top:1rem !important;
    padding-bottom:1rem !important;
}

section[data-testid="stSidebar"] h1{
    font-size:2.4rem;
    margin-top:0.35rem;
    margin-bottom:0.75rem;
}

section[data-testid="stSidebar"] *{
    color:white;
}

</style>
""",unsafe_allow_html=True)


def generate_pdf_bytes(report_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in report_text.splitlines():
        pdf.cell(0, 10, txt=line, ln=1)
    return pdf.output(dest="S").encode("latin-1")

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("TrackHeart")

    st.markdown("---")

    st.subheader("About")

    st.write("""
Predict the likelihood of heart disease
using a Machine Learning model trained
on patient health information.
""")

    st.markdown("---")

    st.subheader("Model")

    st.success("Logistic Regression")

    st.metric("Accuracy","71.6%")

    st.markdown("---")

    st.subheader("Developer")

    st.write("Satyam Gupta")

    st.markdown("---")

    

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""

<div class="hero">

<h1>TrackHeart</h1>

<p>

Heart Disease Risk Prediction using Machine Learning

</p>

</div>

""",unsafe_allow_html=True)

st.info(
"""
Fill in the patient details and click
**Analyze Heart Risk**.
"""
)

# ==========================================================
# INPUT FORM
# ==========================================================

left,right = st.columns(2)

with left:

    st.subheader("Patient Information")

    country = st.selectbox(
        "Country",
        ["India","Indonesia","Malaysia","Singapore"],
        key="country"
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "Architect",
            "Accountant",
            "Chef",
            "Doctor",
            "Engineer",
            "Lawyer",
            "Nurse",
            "Teacher",
            "Others"
        ],
        key="occupation"
    )

    gender = st.selectbox(
        "Gender",
        [1,2],
        format_func=lambda x:"Male" if x==1 else "Female",
        key="gender"
    )

    age_months = st.number_input(
        "Age (Months)",
        min_value=12,
        max_value=1200,
        value=600,
        key="age_months"
    )

    height = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=250,
        value=170,
        key="height"
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=30.0,
        max_value=200.0,
        value=70.0,
        key="weight"
    )
    
    
    # ==========================================================
# MEDICAL INFORMATION
# ==========================================================

with right:

    st.subheader("Medical Information")

    ap_hi = st.number_input(
        "Systolic Blood Pressure",
        min_value=50,
        max_value=250,
        value=120,
        key="ap_hi"
    )

    ap_lo = st.number_input(
        "Diastolic Blood Pressure",
        min_value=40,
        max_value=200,
        value=80,
        key="ap_lo"
    )

    cholesterol = st.selectbox(
        "Cholesterol Level",
        [1,2,3],
        format_func=lambda x:
            "Normal" if x==1 else
            "Above Normal" if x==2 else
            "Well Above Normal",
        key="cholesterol"
    )

    gluc = st.selectbox(
        "Glucose Level",
        [1,2,3],
        format_func=lambda x:
            "Normal" if x==1 else
            "Above Normal" if x==2 else
            "Well Above Normal",
        key="glucose"
    )

    smoke = st.selectbox(
        "Smoking",
        [0,1],
        format_func=lambda x:"No" if x==0 else "Yes",
        key="smoke"
    )

    alco = st.selectbox(
        "Alcohol Consumption",
        [0,1],
        format_func=lambda x:"No" if x==0 else "Yes",
        key="alcohol"
    )

    active = st.selectbox(
        "Physical Activity",
        [1,0],
        format_func=lambda x:"Active" if x==1 else "Inactive",
        key="active"
    )

# ==========================================================
# BMI CALCULATOR
# ==========================================================

age_days = int(round(age_months * 30.4375))

st.markdown("---")

st.subheader("📊 Health Indicators")

bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    bmi_status = "Underweight"
    bmi_icon = "🔵"

elif bmi < 25:
    bmi_status = "Normal"
    bmi_icon = "🟢"

elif bmi < 30:
    bmi_status = "Overweight"
    bmi_icon = "🟠"

else:
    bmi_status = "Obese"
    bmi_icon = "🔴"

col1,col2,col3 = st.columns(3)

with col1:

    st.markdown(f"""
    <div class="metric-card">
        <h3>BMI</h3>
        <h1>{bmi:.2f}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="metric-card">
        <h3>Category</h3>
        <h2>{bmi_icon} {bmi_status}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:

    if bmi < 25:
        message = "Healthy"

    elif bmi < 30:
        message = "Improve Lifestyle"

    else:
        message = "Consult Doctor"

    st.markdown(f"""
    <div class="metric-card">
        <h3>Status</h3>
        <h2>{message}</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# CREATE INPUT DATAFRAME
# ==========================================================

patient = pd.DataFrame({

    "country":[country],
    "active":[active],
    "age":[age_days],
    "alco":[alco],
    "ap_hi":[ap_hi],
    "ap_lo":[ap_lo],
    "cholesterol":[cholesterol],
    "gender":[gender],
    "gluc":[gluc],
    "height":[height],
    "occupation":[occupation],
    "smoke":[smoke],
    "weight":[weight]

})

st.markdown("### Analyze Your Health")

predict = st.button(
    "Analyze Heart Risk",
    use_container_width=True,
    type="primary"
)

st.markdown("---")


# ==========================================================
# PREDICTION
# ==========================================================

if predict:

    prediction, probability = predict_disease(patient)

    st.subheader("Prediction Result")

    left_result, right_result = st.columns([2,1])

    with left_result:

        if prediction == 1:

            st.markdown("""
            <div class="result-high">
            HIGH RISK OF HEART DISEASE
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result-low">
            LOW RISK OF HEART DISEASE
            </div>
            """, unsafe_allow_html=True)

    with right_result:

        st.metric(
            "Risk Probability",
            f"{probability*100:.2f}%"
        )

    st.progress(float(probability))

    st.markdown("---")

# ==========================================================
# RECOMMENDATIONS
# ==========================================================

    st.subheader("Health Recommendations")

    if prediction == 1:

        st.error("Higher risk detected. Please consult a healthcare professional.")

        col1,col2 = st.columns(2)

        with col1:

            st.markdown("""
### Lifestyle Changes

- Walk 30-45 minutes daily
- Follow a balanced diet
- Reduce salt intake
- Avoid junk food
- Maintain healthy weight
""")

        with col2:

            st.markdown("""
### Medical Advice

- Visit a Cardiologist
- Monitor Blood Pressure
- Regular Blood Tests
- Quit Smoking
- Avoid Alcohol
""")

    else:

        st.success("Low predicted risk. Maintain your healthy lifestyle.")

        col1,col2 = st.columns(2)

        with col1:

            st.markdown("""
### Continue Healthy Habits

- Healthy Diet
- Daily Exercise
- 7-8 Hours Sleep
- Stay Hydrated
""")

        with col2:

            st.markdown("""
### Prevention

- Annual Health Check-up
- Monitor Blood Pressure
- Maintain BMI
- Avoid Smoking
""")

    st.markdown("---")

# ==========================================================
# PATIENT SUMMARY
# ==========================================================

    st.subheader("📋 Patient Summary")

    summary = pd.DataFrame({

        "Feature":[

            "Country",
            "Occupation",
            "Gender",
            "Age (Months)",
            "Height (cm)",
            "Weight (kg)",
            "BMI",
            "Blood Pressure",
            "Cholesterol",
            "Glucose",
            "Smoking",
            "Alcohol",
            "Physical Activity"

        ],

        "Value":[

            country,

            occupation,

            "Male" if gender==1 else "Female",

            age_months,

            height,

            weight,

            round(bmi,2),

            f"{ap_hi}/{ap_lo}",

            "Normal" if cholesterol==1 else
            "Above Normal" if cholesterol==2 else
            "Well Above Normal",

            "Normal" if gluc==1 else
            "Above Normal" if gluc==2 else
            "Well Above Normal",

            "Yes" if smoke else "No",

            "Yes" if alco else "No",

            "Active" if active else "Inactive"

        ]

    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

    report = f"""
TrackHeart REPORT

==================================

Prediction :
{"High Risk" if prediction==1 else "Low Risk"}

Probability :
{probability*100:.2f} %

BMI :
{round(bmi,2)}

Country :
{country}

Occupation :
{occupation}

Blood Pressure :
{ap_hi}/{ap_lo}

Generated using TrackHeart
"""

    report_pdf = generate_pdf_bytes(report)

    st.download_button(

        "📥 Download Report",

        report_pdf,

        file_name="Heart_Disease_Report.pdf",

        mime="application/pdf"

    )

    # st.markdown("---")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("""

<hr>

<div style='text-align:center;color:gray;'>

<h2 style='font-size:32px; margin-bottom:10px;'>TrackHeart</h2>

Heart Disease Prediction using Machine Learning

Developed by <b>Satyam Gupta</b>


</div>

""",unsafe_allow_html=True)
