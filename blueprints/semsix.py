from flask import Blueprint, redirect, render_template

semsixes = Blueprint("semsixes", __name__, url_prefix="/semsix")

backlink = "/semsix"
ssnames = "6"


@semsixes.route("/noc26-cs10/assign")
def ai_for_management_assignments():
    ppaim = "AI for Mgmt - Assignments"
    aimname = "NPTEL - AI for Management"
    llistaim = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semsix/aiformgmt/Artificial%20Intelligence%20(AI)%20for%20Management%20-%20-%20Unit%203%20-%20Week%201.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semsix/aiformgmt/Artificial%20Intelligence%20(AI)%20for%20Management%20-%20-%20Unit%204%20-%20Week%202.pdf",
    ]

    return render_template(
        "foursem/s4lec.html",
        data=llistaim,
        title=ppaim,
        name=aimname,
        backlink=backlink,
        sems=ssnames,
    )
