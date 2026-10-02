from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":

        name = request.form["name"]
        n = int(request.form["subjects"])

        marks = []

        for i in range(n):
            mark = int(request.form[f"mark{i}"])
            marks.append(mark)

        # Total
        total = sum(marks)

        # Average
        average = total / n

        # Percentage
        percentage = total / (n * 100) * 100

        # Performance
        if percentage >= 90:
            performance = "Outstanding 🌟"
        elif percentage >= 75:
            performance = "Excellent 👍"
        elif percentage >= 60:
            performance = "Good 🙂"
        elif percentage >= 40:
            performance = "Needs Improvement 📚"
        else:
            performance = "Needs Serious Improvement ⚠️"

        # Percentage message
        if percentage >= 90:
            grade_message = "You have secured 90% or above."
        elif percentage >= 80:
            grade_message = "You have secured 80% or above."
        elif percentage >= 70:
            grade_message = "You have secured 70% or above."
        elif percentage >= 60:
            grade_message = "You have secured 60% or above."
        elif percentage >= 50:
            grade_message = "You have secured 50% or above."
        else:
            grade_message = "OOPS!!!! You have secured less than 50%."

        # Passed and failed subjects
        passed = 0
        failed = 0

        for mark in marks:
            if mark >= 40:
                passed += 1
            else:
                failed += 1

        # Final message
        if failed == 0:
            final_message = "🎉 Passed in all subjects!"
        else:
            final_message = "⚠️ You need to improve in some subjects."

        # Send result to HTML
        result = {
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "percentage": percentage,
            "performance": performance,
            "grade_message": grade_message,
            "passed": passed,
            "failed": failed,
            "final_message": final_message
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
