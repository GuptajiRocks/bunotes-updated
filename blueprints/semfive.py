from flask import Blueprint, redirect, render_template

semfi = Blueprint("semfi", __name__, url_prefix="/semfive")

backlink = "/semfive"
ssnames = "5"


@semfi.route("/cset301/lec")
def cset301_lectures():
    ppsample = "AI&ML - Lectures"
    samplename = "Artificial Intelligence and Machine Learning"
    llistsample = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Lec%201%20-%20Overview%20of%20AI-ML.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Lec%202%20-%20Types%20of%20ML.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Lec%203%20-%20Regression%20Line.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Lec%204.-Cost%20Function%20and%20Gradient%20Descent.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Lec.%205%20-%20Logistic%20Regression.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Lec%206%20-%20Multiclass%20Classification.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Lec%207%20-%20Polynomial%20Regression.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Lec%208%20-%20Performace%20Metrics.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Lec%209%20-%20Errors%20in%20ML.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Lec%2010%20-%20Regularization.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-2_Lec-1.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-2_Lec-2.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-2_Lec-3.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-2_Lec-4.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-2_Lec-5.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-3_Lec-1.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-3_Lec-2.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-3_Lec-3.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-3_Lec-4.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-3_Lec-5.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-3_Lec-6.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-3_Lec-7.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-4_Clustering%20and%20Its%20Types.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset301-lec/Mod-5_Neural_Networks_and%20Emerging_ML_Techiques.pptx",
    ]

    return render_template(
        "foursem/s4lec.html",
        data=llistsample,
        title=ppsample,
        name=samplename,
        backlink=backlink,
        sems=ssnames,
    )


@semfi.route("/cset381/lec")
def cset381_lectures():
    ppsample = "CSET381 - Lectures (Unit 1)"
    samplename = "Course Lectures Unit 1"
    llistsample = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture1.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture10and11-2.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture10and11.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture12-1.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture12-2.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture2and3.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture3.html",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture4.html",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture4.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture5.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture6.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture7.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture8.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec/Unit1_Lecture9.pdf",
    ]

    return render_template(
        "foursem/s4lec.html",
        data=llistsample,
        title=ppsample,
        name=samplename,
        backlink=backlink,
        sems=ssnames,
    )


@semfi.route("/cset381/unit2")
def cset381_unit2_lectures():
    ppsample = "CSET381 - Lectures (Unit 2)"
    samplename = "Course Lectures Unit 2"
    llistsample = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_BayesTheoremApplications.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_BayesTheoremBasics.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture1.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture2.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture2and3.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture3%20%281%29.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture3%20%282%29.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture3BayesianNetworks.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture4.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture5.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture5.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture6.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture7%20%282%29.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture7.html",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture7.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture8.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset381-lec-unit2/Unit2_Lecture9.pptx",
    ]

    return render_template(
        "foursem/s4lec.html",
        data=llistsample,
        title=ppsample,
        name=samplename,
        backlink=backlink,
        sems=ssnames,
    )
