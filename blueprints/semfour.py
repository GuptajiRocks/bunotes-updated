from flask import Blueprint, redirect, render_template

semfo = Blueprint("smfo", __name__, url_prefix="/semfour")


@semfo.route("/os")
def operating_sys_lec():
    ppos = "OS Lectures"
    osname = "Operating System"
    llistos = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lecture_1.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lecture_2.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/lecture%203.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lect%204%20Process%20and%20Its%20concepts%20(1).pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lect%205%20Process%20states,%20Multithreading%20(1).pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lect%206%20FCFS-J%20SJF-J%20SRTF.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lect%207.1%20LJF%20and%20LRTF.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%208%20Advanced%20scheduling%20algo.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%209%20Inter_Process_Communication.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/10%20process%20synchronization.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/11%20process%20synchronization%20solution.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/12%20classical%20synchronization%20problems.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%2013-14%20Readers%20Writers%20Problem%20and%20dinning%20philosphor%20problem.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%2015%20%20Deadlock.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%2016%20%20Dealing%20with%20Deadlock.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%2017%20Memory%20Management.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%2018%20memory%20management%20%20part%202.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%2019%20%20memory%20management%20%20part%203.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%2021%20Page%20replacement.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%2022%20Page%20replacement%20anf%20frame%20allocation.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Lec%2023%20DiskScheduling%20.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Virtualization%20Technique.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Cloud%20Computing.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/os/Distributed,%20Network%20System%20and%20RPC.pptx",
    ]

    return render_template("foursem/s4lec.html", data=llistos, title=ppos, name=osname)


@semfo.route("/cn")
def cnlecs():
    ppcn = "CN Lectures"
    cnname = "Computer Networks"
    llistcn = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/Lecture-1.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/Lecture-2.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/Lecture-3_.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/Lecture-5%20_TCP_IP%20(1).pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/Lecture-6-%20Physical%20Layer_signal_performance.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/Lecture-7%20_linecoding.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/Lecture-8%20_Analog2digital.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/Lecture-8%20_Analog2digital.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L09_Framing.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L10_DLL_ErrorControl.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L11_DLL_Error_detection_Methods.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L12_DLL_FlowControl.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L13_MAC_Random%20Access.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L14_Network_Layer-IP%20Addressing.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L15_Network_IPV6.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L16_Network%20Layer%20Protocols%20(1)%20(1).pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L17_Address%20Mapping%20(1).pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L18__Routing.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L19__Network_Layer_Link_state.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L20__Multicast_Routing.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L21_TransportLayer.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L22_Socket_TCP_UDP.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L23_TransportLayer_Congestion.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L24_TransportLayer_protocol.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L25_TransportLayer_QoS.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L26-DNS.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L27-RemoteLogin_email_Application_Layer.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L28-MIME_SMTP_FTP_Application_Layer.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L29_HTTP_URL_Application_Layer.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/L30-NetworkSecurity.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/Lecture-SelfStudy_modulation_switching_multiplexing.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/cn/Lecture-Session%20and%20Presentation.pptx",
    ]

    return render_template("foursem/s4lec.html", data=llistcn, title=ppcn, name=cnname)


@semfo.route("/daa")
def daalecs():
    ppdaa = "DAA Lectures"
    daaname = "Design and Analysis of Algorithms"
    llistdaa = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L1_Welcome%20Lecture.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L2-%20Complexity.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L3_Recurrance%20Relations%20and%20Master%20Theorem.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L4_DIVIDE%20AND%20CONQUER.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L5_Matrix%20Multiplication.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L6_Large_number_multi.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L7_Bucket%20and%20%20Radix.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L8_Max-Min_Median%20problem.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L9%20%20Greedy,%20Knapsack.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L10%20Minimum%20Spanning%20trees,%20Prims%20Algorithm.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L11%20Dsjt%20Set%20Kruskals.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L12%20Kruskals,%20Dijkstra.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L13_Dijkastra%20Algorithms.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L14_Huffman%20code.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L15_DFS_bi-connectivity.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L16_Articulation%20Point.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L17_dynamic%20Programming.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L18_Backtracking.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L19_Max%20Flow%20Min%20Cut.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/daa/L20_complexity%20ClassesP_NP.pdf",
    ]

    return render_template(
        "foursem/s4lec.html", data=llistdaa, title=ppdaa, name=daaname
    )


@semfo.route("/dmpm")
def data_mining_and_pred_modelling():
    ppdmpm = "DMPM Lectures"
    dmpmname = "Data Mining and Predictive Modelling"
    llistdmpm = [
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L1.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L2.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L3.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L4.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L5_L6_Principal%20Component%20Analysis.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L7_Similarity%20Analysis.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L8_Vectorization.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L9_Association%20Rule.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L10%20Clustering.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L10_11_Regression.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L12_Confusion%20Matrix.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L13%20Decision%20Trees.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/L13_14%20Model%20Selection%20and%20Prediction.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/14-15_KNN.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/16_Decision%20Trees.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/17_Naive%20Bayes%20and%20knn%20Classifiers.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/18_Support%20Vector%20Machine%20(SVM)%20-%20Copy.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/19_Outlier%20Analysis.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/20_ANOVA.ppt",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/LDA.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/Time%20Series.pptx",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/DM_Module3.pdf",
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/dmpm/DM_Module4.pdf",
    ]

    return render_template(
        "foursem/s4lec.html", data=llistdmpm, title=ppdmpm, name=dmpmname
    )


@semfo.route("/ethics")
def ethics_208():
    return redirect(
        "https://mstytecrjnvpktdawjjr.supabase.co/storage/v1/object/public/semfour/ethics/Arihant_Arastu_Harshil_Sutejas_Samrat_Ethics_Report_CSET208_18042025.pdf"
    )


@semfo.route("/pyq")
def alreadypyq():
    return redirect("https://bu4pyq.vercel.app")


@semfo.route("/cnlab")
def cn_labs_prac():
    return redirect("https://github.com/GuptajiRocks/computer_networks_labs/tree/main")


@semfo.route("/dmpmlab")
def dmpm_labs_prac():
    return redirect("https://github.com/GuptajiRocks/data-science-sem4/tree/main")
