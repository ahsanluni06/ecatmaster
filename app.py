from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = 'quiz_secret_key'  # Needed for session management

# Function to get subjects from database
def get_subjects():
    conn = sqlite3.connect("questions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT subject FROM questions")
    subjects = [row[0] for row in cursor.fetchall()]
    conn.close()
    return subjects

# Function to get topics for a specific subject
def get_topics(subject):
    conn = sqlite3.connect("questions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT topic_name FROM topics WHERE subject=?", (subject,))
    topics = [row[0] for row in cursor.fetchall()]
    conn.close()
    return topics

# Home page route - shows all subjects
@app.route("/")
def home():
    subjects = get_subjects()
    return render_template("home.html", subjects=subjects)

# Topics page route - shows all topics for a subject
@app.route("/topics/<subject>")
def topics(subject):
    topics = get_topics(subject)
    return render_template("topics.html", subject=subject, topics=topics)

# Quiz page route - shows questions for a specific topic
@app.route("/quiz/<subject>/<topic>")
def quiz(subject, topic):
    conn = sqlite3.connect("questions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions WHERE subject=? AND topic=?", (subject, topic))
    questions = cursor.fetchall()
    conn.close()
    
    if not questions:
        return f"No questions found for {subject} - {topic}"
    
    # Store questions in session for next question navigation
    session['current_topic_questions'] = questions
    session['current_question_index'] = 0
    session['score'] = 0
    session['current_subject'] = subject
    session['current_topic'] = topic
    
    # Show the first question
    return render_template("quiz_with_next.html", 
                         subject=subject, 
                         topic=topic, 
                         question=questions[0],
                         question_number=1,
                         total_questions=len(questions))

# Check answer route - processes the submitted answer
@app.route("/check_answer", methods=["POST"])
def check_answer():
    question_id = request.form.get('question_id')
    user_answer = request.form.get('answer')
    subject = request.form.get('subject')
    topic = request.form.get('topic')
    question_number = int(request.form.get('question_number', 1))
    total_questions = int(request.form.get('total_questions', 1))
    
    conn = sqlite3.connect("questions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer, explanation FROM questions WHERE id=?", (question_id,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        question_text, correct_answer, explanation = result
        is_correct = user_answer == correct_answer
        
        # Update score if correct
        if is_correct:
            session['score'] = session.get('score', 0) + 1
        
        return render_template("answer_result.html",
                             is_correct=is_correct,
                             user_answer=user_answer,
                             correct_answer=correct_answer,
                             explanation=explanation,
                             subject=subject,
                             topic=topic,
                             question_text=question_text,
                             question_number=question_number,
                             total_questions=total_questions)
    
    return "Question not found"

# Next question route
@app.route("/next_question/<subject>/<topic>")
def next_question(subject, topic):
    if 'current_question_index' not in session:
        return redirect(url_for('quiz', subject=subject, topic=topic))
    
    # Get next question index
    session['current_question_index'] += 1
    current_index = session['current_question_index']
    questions = session.get('current_topic_questions', [])
    
    if current_index >= len(questions):
        # Quiz completed - show results
        score = session.get('score', 0)
        total = len(questions)
        return render_template("quiz_results.html",
                             subject=subject,
                             topic=topic,
                             score=score,
                             total_questions=total)
    
    # Show next question
    return render_template("quiz_with_next.html",
                         subject=subject,
                         topic=topic,
                         question=questions[current_index],
                         question_number=current_index + 1,
                         total_questions=len(questions))

# Quiz results route
@app.route("/results/<subject>/<topic>")
def quiz_results(subject, topic):
    score = session.get('score', 0)
    questions = session.get('current_topic_questions', [])
    total_questions = len(questions) if questions else 0
    
    return render_template("quiz_results.html",
                         subject=subject,
                         topic=topic,
                         score=score,
                         total_questions=total_questions)

# Notes page route - Add this to your app.py
@app.route("/notes/<subject>/<topic>")
def notes(subject, topic):
    return render_template("notes.html", subject=subject, topic=topic)

# This should be at the very end of the file
if __name__ == "__main__":
    app.run(debug=True)