# BU Notes

Working on a Python Documented Flask App for BU Notes with modular code written.

<hr>
    
# 📘 How the Application Works with Respect to Different Modules

## 1. `app.py`

This is the main file, where the index route lies, wherein lies the list of semesters available on the portal.  
If any changes are to be made, then add the semester and its respective route in the following format:

/sem<number>

Example:  
Semester Five = /semfive

and so on.

---

## 2. `dirfunc.py`

This is the file that contains details of subjects within a semester.  
To add a subject you wish to add within a semester, create a list dictionary data structure and add the following three details:

- **code** → Subject code  
- **title** → Subject name  
- **link** → Route of the subject  

Example:  
Let's suppose you wish to add the practical files of **CSET109 (Java)**, and the route would be:

/semtwo/java/labs

Ensure this same format within every addition to maintain code modularity and easy understanding for contributors.

The template file for this python module is:

seml.html

The `seml.html` file already has the Jinja2 templating set in it to display the subjects effectively.  
You are encouraged **not to touch that file** unless and until a more effective templating solution has come to your mind.

---

## 3. `sem<name>.py`

In this file lies the routes for each respective semester subject and the lecture/tutorials/labs within them.  
To add resources of your own within this, follow the steps:

### a. Storage Setup

- Create a **Supabase organization**.  
- Create a project and navigate to **Storage**.  
- Ensure that **S3 configuration** is selected and create a bucket.  
- Upload your respective files in your bucket and ensure that the account is kept active so that the bucket never goes offline.

---

### b. Route Creation

- Select the subject resources you want to add and navigate to its semester route if it already exists.  
- If it does not exist, create one with appropriate function names and use that.  
- The template being followed to send individual resources within the subject-specific and type-specific route is with respect to:

foursem/sem4lec.html

---

### c. Template Structure

This is the file that has the Jinja2 templates with looping done over the list dictionary data structure that is passed to the data variable.

If you observe the foursem/sem4lec.html file, you will see that dynamic template variables are already assigned.  
The code follows a modular structure with each semester and subject following the same display format.

The parameters accepted by the foursem/s4lec.html file are as follows:

1. **name**  
   Its the name of the subject along with the lecture/practical/tutorial significance.

2. **title**  
   This is the title of the webpage, used to signify the tab name (title duh).

3. **data**  
   This is the list data structure used to store the links of the files within the S3 bucket of the specific course being added.

4. **backlink and sems**  
   These are the two variables which are preferred to be declared globally rather than a local scope as they remain unchanged and are utilized in every function.  
   - backlink refers the route which takes the user back to the semester page from the S3 bucket link list page.  
   - sems define the name of the Semester which is being displayed, more specifically the number.
  
  
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
