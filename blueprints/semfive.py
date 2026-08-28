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


@semfi.route("/cset302/lec")
def cset302_lectures():
    ppsample = "CSET302 - Lectures"
    samplename = "Automata Theory and Computability"
    llistsample = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT0_Course%20Intro.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT10.0_RegularLanguageProperties.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT10.1_Decidable%20properties%20of%20RL.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT11_RE%20to%20FA.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT12_RE%20Identities%20and%20Ardens%20Theorem.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT13_State%20elimination%20method.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT14_Pumping%20Lemma.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT15_REGULAR%20GRAMMAR.ppt",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT16_FA%20to%20RG.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT17_PUSH%20DOWN%20AUTOMATA.ppt",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT18_CGF%20and%20CFL.ppt",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT19_CNF%20and%20GNF.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT1_Introduction%20of%20Automata%20Theory%20and%20Computability.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT20_CSG%20and%20RE.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT21_TURING%20MACHINES.ppt",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT22_complexity.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT2_Introduction%20to%20DFA.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT3_NFA.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT5_NFA-Conversion.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT6_Minimization%20of%20DFA.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT7_Moore%20and%20Mealy.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT8_Moore,%20Mealy%20Conversions.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset302-lec/PPT9_Regular%20Expression.pptx",
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


@semfi.route("/cset305/lec")
def cset305_lectures():
    ppsample = "CSET305 - Lectures"
    samplename = "High Performance Computing"
    llistsample = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-1-1-overview.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-1-2-heterogeneous-computing.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-1-3-portability-scalability.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-2-1-cuda-thrust-libs.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-2-2-cuda-data-allocation-API.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-2-3-cuda-parallelism-threads.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-2-6-cuda-unified-memory.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-3-1-kernel-SPMD-parallelism.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-3-2-kernel-multidimension.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-3-3-color-to-greyscale-image-processing-example.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-3-4-blur-kernel.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-3-5-transparent-scaling.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-4-1-cuda-memories.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-4-2-tiled-algorithms.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-4-3-tiled-matrix-multiplication.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-4-4-tiled-matrix-multiplication-kernel.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-5-1-warps-simd.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-5-2-control-divergence.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-6-1-dram-bandwidth.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-6-2-memory-coalescing.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-7-1-histogram.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-7-2-data-race.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfive/cset305-lec/Lecture-7-3-CUDA-Atomic.pdf",
    ]

    return render_template(
        "foursem/s4lec.html",
        data=llistsample,
        title=ppsample,
        name=samplename,
        backlink=backlink,
        sems=ssnames,
    )
