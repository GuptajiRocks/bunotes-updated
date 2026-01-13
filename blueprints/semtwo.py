from flask import Blueprint, jsonify, redirect, render_template

stwo = Blueprint("stwo", __name__, url_prefix="/semtwo")
backlink2 = "/semtwo"
ssname2 = "2"


@stwo.route("/dms")
def dms_lec_all():
    return redirect(
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dms/All%20Slides%20@Discrete%20Mathematical%20Structures%20@GS.pdf"
    )


@stwo.route("/dms/tut")
def dms_tut():
    ppname = "DMS Tutorials"
    dmsname = "Discrete Mathematical Structures Tutorials"
    llistdmstut = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/DMS%20Tutorial%20Sheet%201.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/Tut%201%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/DMS%20Tutorial%20Sheet%202.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/Tut%202%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/DMS%20Tutorial%20Sheet%203.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/Tut%203%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/DMS%20Tutorial%20Sheet%204.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/Tut%204%20sol.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/DMS%20Tutorial%205.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/Tut%205%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/DMS%20Tutorial%206.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/Tut%206%20sol.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/DMS%20Tutorial%207.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/Solution%20Tutorial%207.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/DMS%20Tutorial%208.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/Tutorial%208%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/Tutorial%20Sheet%209.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/dmstut/Tutorial%209%20solution.pdf",
    ]

    return render_template(
        "foursem/s4lec.html",
        name=dmsname,
        title=ppname,
        data=llistdmstut,
        backlink=backlink2,
        sems=ssname2,
    )


@stwo.route("/emat102/tut")
def linear_tut():
    ppname = "LA&ODE Tutorials"
    emattutname = "Linear Algebra and Ordinary Differential Equations Tutorials"
    llistemattut = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial-1.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Totorial-1%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Totorial-2.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%202%20Solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Totorial-3%20%204.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%203-4%20Solutions.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%20%205.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%205%20solution%20.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial-6.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%206%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%207.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%207%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Totorial-8.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%208%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%209.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%209%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%2010.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelatut/Tutorial%2010%20solution.pdf",
    ]

    return render_template(
        "foursem/s4lec.html",
        name=emattutname,
        title=ppname,
        data=llistemattut,
        backlink=backlink2,
        sems=ssname2,
    )


@stwo.route("/java/lab")
def java_labs():
    javatitle = "Java Labs"
    javatutName = "Object Oriented Programming using Java Practical Labs"
    llistjavalab = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab00_common.odt",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab01_friday.odt",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab02_friday.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab03_friday.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab04_friday.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab05_friday.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab06_friday.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab07_swing_all.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab08_all.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/CSET109_Lab09_all.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab10_all.docx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/javalab/cset109_lab11_all.docx",
    ]

    return render_template(
        "foursem/s4lec.html",
        name=javatutName,
        title=javatitle,
        data=llistjavalab,
        backlink=backlink2,
        sems=ssname2,
    )


@stwo.route("/ephy/mech")
def mechanics_lec():
    mechtitle = "EPHY111L Mechanics"
    mechName = "Mechanics Lectures"
    llistmech = [
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_1.pdf",
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_2.pdf",
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_3.pdf",
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_4.pdf",
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_5.pdf",
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_6.pdf",
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_7.pdf",
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_8.pdf",
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_9.pdf",
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_10.pdf",
        "https://trialtwo.blob.core.windows.net/ephylec/EPHY111L_11.pdf",
    ]

    return render_template(
        "foursem/s4lec.html",
        name=mechName,
        title=mechtitle,
        data=llistmech,
        backlink=backlink2,
        sems=ssname2,
    )


@stwo.route("/emat102/lec")
def linear_vinay_sir_lec():
    return redirect(
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semtwo/odelalec/Vinay_Sir_LA_ODE.zip"
    )


@stwo.route("/ephy/electro")
def electromagnetism_lec():
    electrotitle = "EPHY111L Electromagnetism"
    electroName = "Electromagnetism Lectures"

    llistelectro = [
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture14-17.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture18.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture19.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture20.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture21.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture22.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture23.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture24-25.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture26.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture27.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture28.pdf",
        "https://trialtwo.blob.core.windows.net/ephymlec/EPHY111L_lecture29.pdf",
    ]

    return render_template(
        "foursem/s4lec.html",
        name=electroName,
        title=electrotitle,
        data=llistelectro,
        backlink=backlink2,
        sems=ssname2,
    )
