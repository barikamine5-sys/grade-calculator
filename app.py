import streamlit as st

# عنوان الصفحة وتصميمها
st.set_page_config(page_title="حساب المعدل الإجمالي الثالثة إعدادي", page_icon="🎓")

st.title("🎓 برنامج حساب المعدل النهائي")
st.write("أدخل نقطك أدناه لحساب المعدل الإجمالي بناءً على المعاملات (المراقبة 30%، المحلي 30%، الجهوي 40%).")

# خانات إدخال النقط
controle = st.number_input("أدخل نقطة المراقبة المستمرة (من 20):", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
local = st.number_input("أدخل نقطة الامتحان المحلي (من 20):", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
regional = st.number_input("أدخل نقطة الامتحان الجهوي (من 20):", min_value=0.0, max_value=20.0, value=10.0, step=0.25)

# زر الحساب
if st.button("احسب المعدل الإجمالي"):
    # الحسابات
    total_points = (controle * 3) + (local * 3) + (regional * 4)
    final_grade = total_points / 10
    
    # عرض النتيجة
    st.markdown("---")
    st.success(f"🎯 النقطة الإجمالية هي: **{final_grade:.2f} / 20**")
    
    # رسالة النجاح أو التشجيع
    if final_grade >= 10:
        st.balloons()
        st.markdown("🎉 **مبروك! لقد نجحت.**")
    else:
        st.markdown("💪 **حظ موفق في المرات القادمة، يمكنك تدارك الأمر.**")