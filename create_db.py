import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("questions.db")
cursor = conn.cursor()

# Create enhanced questions table with explanation field
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    topic TEXT NOT NULL,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    answer TEXT NOT NULL,
    explanation TEXT NOT NULL,
    difficulty INTEGER DEFAULT 1,
    year INTEGER,
    is_past_paper BOOLEAN DEFAULT 1
)
""")

# Create topics table to organize all topics
cursor.execute("""
CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    topic_name TEXT NOT NULL,
    question_count INTEGER DEFAULT 0
)
""")

# Clear old data
cursor.execute("DELETE FROM questions")
cursor.execute("DELETE FROM topics")

# Insert all ECAT topics
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

# Insert sample questions for a few topics
sample_questions = [
    # Maths - Algebra
    ("Maths", "Algebra and Quadratic Equation", "Solve for x: x² - 5x + 6 = 0", "x = 2, 3", "x = -2, -3", "x = 1, 6", "x = -1, -6", "x = 2, 3", 
     "The quadratic equation x² - 5x + 6 = 0 can be factored as (x-2)(x-3)=0, giving solutions x=2 and x=3.", 1, 2023, 1),
    
    # Physics - Vectors
    ("Physics", "Scalars and Vectors", "Which of the following is a vector quantity?", "Mass", "Temperature", "Force", "Time", "Force", 
     "Force has both magnitude and direction, making it a vector quantity. Mass, temperature, and time are scalars as they only have magnitude.", 1, 2023, 1),
    
    # Chemistry - Atomic Structure
    ("Chemistry", "Atomic Structure", "How many electrons can occupy the fourth energy level?", "2", "8", "18", "32", "32", 
     "The maximum number of electrons that can occupy an energy level is given by 2n², where n is the principal quantum number. For n=4, 2(4)² = 32 electrons.", 2, 2023, 1),
    
    # English - Grammar
    ("English", "Grammer Basics", "Choose the correct sentence:", "She don't like apples", "She doesn't like apples", "She doesn't likes apples", "She don't likes apples", "She doesn't like apples", 
     "With third person singular (she/he/it), we use 'does' + base form of the verb. So 'She doesn't like apples' is correct.", 1, 2023, 1),
]

cursor.executemany(
    "INSERT INTO questions (subject, topic, question, option1, option2, option3, option4, answer, explanation, difficulty, year, is_past_paper) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    sample_questions
)

conn.commit()
conn.close()
print("Database created with all ECAT topics and sample questions!")
print(f"Added {len(ecat_topics)} topics across 4 subjects!")