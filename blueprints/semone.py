from flask import Blueprint, jsonify, render_template

sone = Blueprint("semone", __name__, url_prefix="/semone")
backlink1 = "/semone"
ssname1 = "1"


@sone.route("/cset102/lec")
def electrical_lec():
    electitle = "CSET102 Lectures"
    elecName = "Introduction to Electrical and Electronics Engineering - Lectures"
    llistelec = [
        "https://trialtwo.blob.core.windows.net/cset102-lectures/01_Intro.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/02_ohms_law_resistor_series_parallel.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/03_KCL_KVL.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/04_nodal_mesh.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/05_sorce_transform_Thevenins.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/06_Norton_maximum_power_transfer.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/07_08_09_Complex-no_cap_inductor.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/10_Filters.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/11_Semiconductor.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/12_13_14_15_p_n_junction_circuit_Zener.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/16_17_Opamp.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/19_20_Transistors.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/Example_Thevenins_Basic.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/Final%20-%20MOSFET%20-%20Not%20that%20Imp.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/Lecture%2016%20and%2017%20-%20Op-amp%20examples.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/Lecture%203%20Example_Nodal_Mesh.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/Lecture%205%20Examples%20Thevenin.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-lectures/Midterm%20practice%20-%20Same%20circuit%20all%20methods_Example.pdf",
    ]

    return render_template(
        "foursem/s4lec.html",
        name=elecName,
        title=electitle,
        data=llistelec,
        backlink=backlink1,
        sems=ssname1,
    )


@sone.route("/cset102/tut")
def electrical_tut():
    electitle = "CSET102 Tuts"
    elecName = "Introduction to Electrical and Electronics Engineering - Tutorials"
    llistelectut = [
        "https://trialtwo.blob.core.windows.net/cset102-tut/Tutorial_1.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut-sol/Solution_Tutorial_1.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut/Tutorial_2.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut-sol/Solution_tutorial_2.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut/Tutorial_3.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut-sol/Solution_tutorial_3.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut/Tutorial_4.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut-sol/Solution_tutorial_4.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut/Tutorial_5.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut-sol/Solution_Tutorial_5.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut/Tutorial_6.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut-sol/Solution_tutorial_6.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut/Tutorial_7.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut-sol/Tutorial_7_Solution.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut/Tutorial_8.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut-sol/Solution_Tutorial_8.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut/Tutorial_9.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut-sol/Tutorial_9_solutions.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut/Tutorial_10.pdf",
        "https://trialtwo.blob.core.windows.net/cset102-tut-sol/Tutorial_10_solutions.pdf",
    ]

    return render_template(
        "foursem/s4lec.html",
        name=elecName,
        title=electitle,
        data=llistelectut,
        backlink=backlink1,
        sems=ssname1,
    )
