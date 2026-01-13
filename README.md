# BU Notes

Working on a Python Documented Flask App for BU Notes with modular code written.

# How the application works with respect to different modules
  1. app.py -> This is the main file, where the index route lies, wherein lies the list of semesters available on the portal. If any changes to be made then add the semester and its respective route in the following format: "/sem<number>" like for Semester Five = "/semfive". and so on.
  
  2. dirfunc.py -> This is the file that contains details of subjects within a semester. To add a subject you wish to add within a semester, create a list dictionary data structure and namely add three details in that. code, title and link. code is the subject code, title is the subject name you wish to add and link is the route of that subject.
  Let's suppose you wish to add The practical files of CSET109, Java, and the route would be /semtwo/java/labs. Ensure this same format within every addition to maintain code modularity and easy understanding for contributors. The template file for this python module is seml.html. The seml.html file already has the jinja2 templating set in it to display the subjects effectively. You are encourage not to touch that file unless and until a more effective templating solution has come to your mind.
  
  3. sem<name>.py -> In this file lies the routes for each respective semester subject and the lecture/tutorials/labs within them. To add resources of your own within this follow the steps:
    a. Create a Supabase organization, within that create a project and navigate to storage. Ensure that S3 config is selected and create a bucket. Upload your respective files in your bucket and ensure that the account is kept active so that the bucket never goes offline.
    b. Select the subject resources you want to add and navigate to its semester route if it already exists, if not create one with appropriate function names and use that. The template being followed to send individual resources within the subject specific and type specific route is w.r.t foursem/sem4lec.html.
    c. This is the file that has the jinja2 templates 
  
  
  
  
# List of Available Routes (Notes)
| Endpoint                            | Method | Route                         |
|-------------------------------------|--------|-------------------------------|
| deets                               | GET    | /details                      |
| myfunc                              | GET    | /index                        |
| pagerts.extreme_start               | GET    | /                             |
| pagerts.semester_four               | GET    | /semfour                      |
| pagerts.semester_one                | GET    | /semone                       |
| pagerts.semester_three              | GET    | /semthree                     |
| pagerts.semester_two                | GET    | /semtwo                       |
| semone.electrical_lec               | GET    | /semone/cset102/lec           |
| semone.electrical_tut               | GET    | /semone/cset102/tut           |
| smfo.alreadypyq                     | GET    | /semfour/pyq                  |
| smfo.cn_labs_prac                   | GET    | /semfour/cnlab                |
| smfo.cnlecs                         | GET    | /semfour/cn                   |
| smfo.daa_tutorials                  | GET    | /semfour/daa/tut              |
| smfo.daalecs                        | GET    | /semfour/daa                  |
| smfo.data_mining_and_pred_modelling | GET    | /semfour/dmpm                 |
| smfo.dmpm_labs_prac                 | GET    | /semfour/dmpm/lab             |
| smfo.ethics_208                     | GET    | /semfour/ethics               |
| smfo.mca_assignments                | GET    | /semfour/mca                  |
| smfo.operating_sys_lec              | GET    | /semfour/os                   |
| static                              | GET    | /static/<path:filename>       |
| stwo.dms_lec_all                    | GET    | /semtwo/dms                   |
| stwo.dms_tut                        | GET    | /semtwo/dms/tut               |
| stwo.electromagnetism_lec           | GET    | /semtwo/ephy/electro          |
| stwo.java_labs                      | GET    | /semtwo/java/lab              |
| stwo.linear_tut                     | GET    | /semtwo/emat102/tut           |
| stwo.linear_vinay_sir_lec           | GET    | /semtwo/emat102/lec           |
| stwo.mechanics_lec                  | GET    | /semtwo/ephy/mech             |
