import sqlite3

def add_physics_questions():
    conn = sqlite3.connect("questions.db")
    cursor = conn.cursor()
    
    physics_questions = [
        # Question 1
        ("Physics", "The Scope of Physics", "The study of physics deals with", 
         "The laws of motion", "The structure of space and time", "The forces present in the universe", "All of the above", 
         "All of the above", 
         "Physics encompasses the study of motion, space-time structure, and fundamental forces in the universe.", 1, 2023, 1),
        
        # Question 2
        ("Physics", "The Scope of Physics", "The branch of science which deals with the study of matter and energy and the relationship between them is called", 
         "Astronomy", "Geology", "Physics", "Biology", 
         "Physics", 
         "Physics is specifically concerned with matter, energy, and their interactions.", 1, 2023, 1),
        
        # Question 3
        ("Physics", "The Scope of Physics", "Which of the following Muslim scientist is both poet and mathematician?", 
         "Omer-Khayyam", "Ibn-e-sina", "Al-Khawarizmi", "Al-Kindi", 
         "Omer-Khayyam", 
         "Omar Khayyam was a renowned Persian mathematician, astronomer, and poet.", 2, 2023, 1),
        
        # Question 4
        ("Physics", "The Scope of Physics", "Which Muslim scientist first invented logarithm?", 
         "Omer-Khayyam", "Al-Khawarizmi", "Ibn-e-sina", "Al-beruni", 
         "Al-beruni", 
         "Al-Biruni made significant contributions to mathematics and science during the Islamic Golden Age.", 2, 2023, 1),
        
        # Question 5
        ("Physics", "The Scope of Physics", "Al-Khawarizmi's Hisabul-jubr-Wal-Muqabla was based on which subject", 
         "Analytical Algebra", "Geometry", "Trigonometry", "Philosophy", 
         "Analytical Algebra", 
         "Hisabul-jabr wal-Muqabala is considered a foundational text in algebra.", 2, 2023, 1),
        
        # Question 6
        ("Physics", "The Scope of Physics", "Kitab-ul-Qanoon-ul-Masoodi is the famous book of", 
         "Ibn-ul-Haithem", "Al-Kindi", "Al-Beruni", "Al-Khawarizmi", 
         "Al-Beruni", 
         "Al-Biruni wrote Kitab-ul-Qanoon-ul-Masoodi, an extensive work on astronomy.", 2, 2023, 1),
        
        # Question 7
        ("Physics", "The Scope of Physics", "Pin-hole camera was invented by", 
         "Al-Beruni", "Ibn-ul-Haithem", "Al-Khawarizmi", "Al-Kindi", 
         "Ibn-ul-Haithem", 
         "Ibn al-Haytham (Alhazen) is credited with inventing the pinhole camera and pioneering work in optics.", 2, 2023, 1),
        
        # Question 8
        ("Physics", "The Scope of Physics", "The system international (SI) is built up from", 
         "Base units", "Supplementary units", "Derived units", "All of above", 
         "Base units", 
         "The SI system is built from seven base units from which all other units are derived.", 1, 2023, 1),
        
        # Question 9
        ("Physics", "The Scope of Physics", "The SI units consists of", 
         "Five basic units", "Five derive units", "Seven derived", "Seven basic units", 
         "Seven basic units", 
         "The International System of Units has seven base units from which all other units are derived.", 1, 2023, 1),
        
        # Question 10
        ("Physics", "The Scope of Physics", "The SI unit of intensity of light is", 
         "Meter", "Kilogram", "Candela", "Mole", 
         "Candela", 
         "The candela (cd) is the SI base unit for luminous intensity.", 1, 2023, 1),
        
        # Question 11
        ("Physics", "The Scope of Physics", "The dimensional formula for angular velocity is", 
         "MLT⁻²", "MLT⁻¹", "T⁻¹", "Dimensionless", 
         "T⁻¹", 
         "Angular velocity has dimensions of angle/time, which simplifies to T⁻¹ since angle is dimensionless.", 2, 2023, 1),
        
        # Question 12
        ("Physics", "The Scope of Physics", "The dimensional formula for inductance is", 
         "ML²T⁻²A⁻²", "MLT⁻²A⁻²", "ML²T⁻¹A⁻²", "MLT⁻¹A⁻¹", 
         "ML²T⁻²A⁻²", 
         "Inductance has dimensional formula ML²T⁻²A⁻² based on its definition in electromagnetic theory.", 3, 2023, 1),
        
        # Question 13
        ("Physics", "The Scope of Physics", "Significant figures in 0.51007", 
         "6", "5", "2", "None", 
         "5", 
         "The number 0.51007 has 5 significant figures. Leading zeros don't count, but zeros between non-zero digits and trailing zeros after decimal do count.", 2, 2023, 1),
        
        # Question 14
        ("Physics", "The Scope of Physics", "The dimension of co-efficient of viscosity is", 
         "[ML⁻¹T⁻¹]", "[ML⁻³T⁻²]", "[ML⁻¹T⁻²]", "[ML⁻²T⁻¹]", 
         "[ML⁻¹T⁻¹]", 
         "The coefficient of viscosity has dimensional formula [ML⁻¹T⁻¹] based on its definition in fluid mechanics.", 2, 2023, 1),
        
        # Question 15
        ("Physics", "The Scope of Physics", "Dimension of torque is?", 
         "M L² T⁻²", "M L T²", "M² L T²", "M L² T²", 
         "M L² T⁻²", 
         "Torque has dimensions of force × distance, giving [ML²T⁻²].", 2, 2023, 1),
        
        # Question 16
        ("Physics", "The Scope of Physics", "The dimension of entropy is", 
         "[ML⁶T²]", "[ML²T²K]", "[MLT⁻¹K⁻¹]", "[ML²T⁻²K⁻¹]", 
         "[ML²T⁻²K⁻¹]", 
         "Entropy has dimensions of energy/temperature, giving [ML²T⁻²K⁻¹].", 3, 2023, 1),
        
        # Question 17
        ("Physics", "The Scope of Physics", "The quantities like length, time, mass, force, electric charge and many more are called", 
         "Basic quantities", "Physical quantities", "Derived quantities", "Specified quantities", 
         "Physical quantities", 
         "These are all examples of physical quantities that can be measured.", 1, 2023, 1),
        
        # Question 18
        ("Physics", "The Scope of Physics", "Quantities like length, mass, time, temperature, electric current and intensity of light are", 
         "Basic quantities", "Physical quantities", "Derived quantities", "Specified quantities", 
         "Basic quantities", 
         "These are the seven base quantities in the SI system from which all other quantities are derived.", 1, 2023, 1),
        
        # Question 19
        ("Physics", "The Scope of Physics", "All other quantities which can be described in terms of basic quantities are", 
         "Base quantities", "Physical quantities", "Derived quantities", "Specified quantities", 
         "Derived quantities", 
         "Derived quantities are expressed in terms of the seven base quantities.", 1, 2023, 1),
        
        # Question 20
        ("Physics", "The Scope of Physics", "The S.I. unit of electric current is", 
         "Mole", "Ampere", "Candela", "Kelvin", 
         "Ampere", 
         "The ampere (A) is the SI base unit for electric current.", 1, 2023, 1),
        
        # Question 21
        ("Physics", "The Scope of Physics", "The S.I. unit of mass is", 
         "Kg", "gm", "lbs", "Slug", 
         "Kg", 
         "The kilogram (kg) is the SI base unit for mass.", 1, 2023, 1),
        
        # Question 22
        ("Physics", "The Scope of Physics", "Which of the following is not a unit of energy?", 
         "Kilowatt", "erg", "Joule", "Kilowatt-hour", 
         "Kilowatt", 
         "Kilowatt is a unit of power (energy/time), not energy itself.", 2, 2023, 1),
        
        # Question 23
        ("Physics", "The Scope of Physics", "Erg x sec is the unit of", 
         "Angular momentum", "Linear momentum", "Planck's constant", "Both A & C", 
         "Both A & C", 
         "Erg × sec can be units for both angular momentum and Planck's constant.", 3, 2023, 1),
        
        # Question 24
        ("Physics", "The Scope of Physics", "Newton second is a unit of", 
         "Energy", "Momentum", "Force", "Work", 
         "Momentum", 
         "Newton-second (N·s) is the unit of momentum (mass × velocity).", 2, 2023, 1),
        
        # Question 25
        ("Physics", "The Scope of Physics", "The S.I. unit of Pressure is", 
         "Atmosphere", "Dyne/cm²", "CO of Hg", "Pascal", 
         "Pascal", 
         "The pascal (Pa) is the SI unit of pressure, defined as one newton per square meter.", 1, 2023, 1),
        
        # Question 26
        ("Physics", "The Scope of Physics", "The dimensional formula for G is", 
         "ML²T⁻²", "M⁻¹L³T⁻²", "M⁻¹L²T⁻³", "ML²T⁻³", 
         "M⁻¹L³T⁻²", 
         "The gravitational constant G has dimensional formula [M⁻¹L³T⁻²].", 3, 2023, 1),
        
        # Question 27
        ("Physics", "The Scope of Physics", "The dimensional formula for potential difference is", 
         "ML²T⁻³A⁻¹", "M²LT⁻³A⁻¹", "ML²T⁻³A⁻²", "MLT⁻³A⁻¹", 
         "ML²T⁻³A⁻¹", 
         "Potential difference (voltage) has dimensional formula [ML²T⁻³A⁻¹].", 3, 2023, 1),
        
        # Question 28
        ("Physics", "The Scope of Physics", "The dimensional formula for resistance is", 
         "ML²T⁻³A⁻²", "ML²T⁻³A⁻¹", "ML²T⁻²A⁻²", "MLT⁻³A⁻¹", 
         "ML²T⁻³A⁻²", 
         "Electrical resistance has dimensional formula [ML²T⁻³A⁻²].", 3, 2023, 1),
        
        # Question 29
        ("Physics", "The Scope of Physics", "The dimensions of the quantities in one (or more) of the following pairs are the same. Identify the pairs.", 
         "Torque and work", "Angular momentum and work", "Energy and Young's modulus", "Light year and intensity", 
         "Torque and work", 
         "Both torque and work have the same dimensional formula [ML²T⁻²].", 3, 2023, 1),
        
        # Question 30
        ("Physics", "The Scope of Physics", "The dimensions of light-year are:", 
         "LT⁻¹", "T", "ML²T⁻²", "L", 
         "L", 
         "Light-year is a unit of distance, so it has dimensions of length [L].", 2, 2023, 1),
    ]
    
    cursor.executemany(
        "INSERT INTO questions (subject, topic, question, option1, option2, option3, option4, answer, explanation, difficulty, year, is_past_paper) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        physics_questions
    )
    
    conn.commit()
    conn.close()
    print(f"Added {len(physics_questions)} physics questions successfully!")

if __name__ == "__main__":
    add_physics_questions()