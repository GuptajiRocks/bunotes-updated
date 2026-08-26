from flask import Blueprint, redirect, render_template

semfi = Blueprint("semfi", __name__, url_prefix="/semfive")

backlink = "/semfive"
ssnames = "5"


@semfi.route("/cset301/lec")
def sample_subject():
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
