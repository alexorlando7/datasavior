
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Refyne Demo', layout='wide')

st.title("Refyne – AI Data Normalization Demo")

st.markdown("""
Welcome to the Refyne platform demo. This walkthrough shows how we take messy, inconsistent data from loan documents and transform it into clean, structured, and visual insights using AI.
""")

st.header("📤 Step 1: Upload Loan Files")
st.markdown("Simulated upload of PDFs, Excels, and Notes.")

uploaded_files = ["rent_roll.xlsx", "appraisal.pdf", "loan_notes.docx"]
st.write("Uploaded files:", uploaded_files)

st.header("📊 Step 2: Parsed + Aggregated Data")
df = pd.read_csv("refyne_demo_data.csv")
st.dataframe(df)

st.header("🔎 Step 3: Missing Fields Before AI Fill")
st.markdown("Rows with missing NOI or Cap Rate are highlighted.")
missing_data = df[df['NOI'].isnull() | df['Cap Rate'].isnull()]
st.dataframe(missing_data)

st.header("🤖 Step 4: Run AI Data Fill")
if st.button("Run AI Fill"):
    df_filled = df.copy()
    df_filled.loc[df_filled['NOI'].isnull(), 'NOI'] = [275000, 295000]
    df_filled.loc[df_filled['Cap Rate'].isnull(), 'Cap Rate'] = [5.3, 5.8]
    df_filled['AI_Filled'] = True
    df_filled['Confidence Score'].fillna(value=0.92, inplace=True)
    st.success("AI Fill completed.")
    st.dataframe(df_filled)
else:
    st.info("Click the button to simulate AI filling missing data.")

st.header("✅ Step 5: Review AI-Filled Data")
st.markdown("Loans filled by AI with confidence scores.")
review_df = df[df['AI_Filled'] == True]
st.dataframe(review_df)

st.header("📈 Step 6: Sigma Dashboard Preview")
st.markdown("Sigma dashboard shows visual insights built on the cleaned data.")
st.image("https://storage.googleapis.com/pai-assets/sigma-dashboard-example.png", use_column_width=True)
