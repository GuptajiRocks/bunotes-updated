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
    ]

    return render_template(
        "foursem/s4lec.html",
        name=emattutname,
        title=ppname,
        data=llistemattut,
        backlink=backlink2,
        sems=ssname2,
    )
