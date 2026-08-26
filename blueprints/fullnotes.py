from flask import Blueprint, render_template

fnot = Blueprint("fnot", __name__, url_prefix="/fullnotes")


@fnot.route("/")
def full_notes_list():
    ppnotes = "Revision Notes"
    notesname = "Vishnu Chityala Revision Notes"
    notes_list = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/ECE.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/IMD-VRC-NOTES.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC-AIML-SEM4.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC-AOI.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC_NOTES_CN.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC_SURVIVAL_CALCULUS.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC_SURVIVAL_DAA_MID.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC_SURVIVAL_IMS%20(1).pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC_SURVIVAL_LA.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC_SURVIVAL_LA_ODE.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC_SURVIVAL_NOTES.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC_SURVIVAL_PROB.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/fullnotes/VRC_SURVIVAL_SML.pdf",
    ]

    return render_template(
        "foursem/s4lec.html",
        data=notes_list,
        title=ppnotes,
        name=notesname,
        backlink="/",
        sems="Home",
    )
