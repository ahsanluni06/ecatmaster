import sqlite3

def restore_all_topics():
    conn = sqlite3.connect("questions.db")
    cursor = conn.cursor()
    
    # First, clear any existing topics
    cursor.execute("DELETE FROM topics")
    
    # Add all ECAT topics
    ecat_topics = [
        # Maths Topics
        ("Maths", "Algebra and Quadratic Equation"),
        ("Maths", "Inequalities"),
        ("Maths", "Complex Numbers"),
        ("Maths", "Binomial Theorem"),
        ("Maths", "Groups"),
        ("Maths", "Sequence and Series"),
        ("Maths", "Trigonometry"),
        ("Maths", "Matrices and Determinant"),
        ("Maths", "Sets"),
        ("Maths", "Counting Techniques"),
        ("Maths", "Probability"),
        ("Maths", "Limits"),
        ("Maths", "Functions"),
        ("Maths", "Derivative and Their Applications"),
        ("Maths", "Integration"),
        ("Maths", "Straight Line"),
        ("Maths", "Circle"),
        ("Maths", "Parabola"),
        ("Maths", "Ellipse"),
        ("Maths", "Hyperbola"),
        ("Maths", "Vectors"),
        ("Maths", "Plane Geometry"),
        
        # Physics Topics
        ("Physics", "The Scope of Physics"),
        ("Physics", "Scalars and Vectors"),
        ("Physics", "Motion and Force"),
        ("Physics", "Motion in Two Dimension"),
        ("Physics", "Torque, Angular and Equilibrium"),
        ("Physics", "Gravitation"),
        ("Physics", "Work, Power and Energy"),
        ("Physics", "Wave, Motion and Sound"),
        ("Physics", "Nature of Light"),
        ("Physics", "Geometrical Optics"),
        ("Physics", "Thermodynamics"),
        ("Physics", "Electrostatics"),
        ("Physics", "Electric Current"),
        ("Physics", "Magnetism and Electromagnetism"),
        ("Physics", "Ele Measuring Instruments"),
        ("Physics", "Alternating Current"),
        ("Physics", "Electronics"),
        ("Physics", "Advent of Modern Physics"),
        ("Physics", "The Atomic Spectra"),
        ("Physics", "The Atomic Nucleus"),
        ("Physics", "Nuclear Radiation"),
        ("Physics", "Fluid Dynamics"),
        ("Physics", "Physics of Solids"),
        
        # English Topics
        ("English", "Roots, Prefixes, Suffixes and Foreign words"),
        ("English", "Vocabulary"),
        ("English", "Grammer Basics"),
        ("English", "Subject-Verb Agreement"),
        ("English", "Pronouns"),
        ("English", "Comparative and Superlative"),
        ("English", "Parallelism"),
        ("English", "Modifiers"),
        ("English", "Odds and Ends"),
        ("English", "Tenses"),
        ("English", "Most Common errors"),
        ("English", "Preposition"),
        ("English", "Articles"),
        ("English", "Test On Article"),
        ("English", "Punctuation"),
        ("English", "Confusing Words"),
        ("English", "Common Misspellings"),
        ("English", "Sentence Completion"),
        ("English", "General Mental Ability"),
        
        # Chemistry Topics
        ("Chemistry", "Stoichiometry"),
        ("Chemistry", "Atomic Structure"),
        ("Chemistry", "Chemical Bonding"),
        ("Chemistry", "States of Matter"),
        ("Chemistry", "Solutions"),
        ("Chemistry", "Thermodynamics"),
        ("Chemistry", "Chemical Kinetics"),
        ("Chemistry", "Chemical Equilibrium"),
        ("Chemistry", "Acids & Bases"),
        ("Chemistry", "Electrochemistry"),
        ("Chemistry", "Periodic Table & Periodicity"),
        ("Chemistry", "Hydrogen"),
        ("Chemistry", "Alkali & Alkaline Earth Metals"),
        ("Chemistry", "Halogens & Noble Gases"),
        ("Chemistry", "Transition Metals"),
        ("Chemistry", "Coordination Compounds"),
        ("Chemistry", "Environmental Chemistry"),
        ("Chemistry", "Basic Organic Chemistry"),
        ("Chemistry", "Hydrocarbons"),
        ("Chemistry", "Reactions of Organic Compounds"),
        ("Chemistry", "Alcohols, Phenols, Ethers"),
        ("Chemistry", "Aldehydes & Ketones"),
        ("Chemistry", "Carboxylic Acids & Derivatives"),
        ("Chemistry", "Amines & Amino Acids"),
        ("Chemistry", "Polymers & Biomolecules"),
        ("Chemistry", "Qualitative Analysis"),
        ("Chemistry", "Volumetric Analysis"),
        ("Chemistry", "Chemical Calculations")
    ]
    
    cursor.executemany(
        "INSERT INTO topics (subject, topic_name) VALUES (?, ?)",
        ecat_topics
    )
    
    conn.commit()
    conn.close()
    print("All topics restored successfully!")
    print(f"Added {len(ecat_topics)} topics across all subjects!")

if __name__ == "__main__":
    restore_all_topics()