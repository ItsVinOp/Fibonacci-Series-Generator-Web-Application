🔢 Fibonacci Series Web App
===========================

A simple Python Flask web application that generates the Fibonacci series based on user input.

Built using the MVC (Model-View-Controller) architecture with:
- Flask for backend logic and routing
- HTML & CSS for frontend UI
- Python for core logic

--------------------
📦 Features
--------------------
- Generates Fibonacci series up to N numbers
- Web interface to input number and view result
- Clean and simple UI
- MVC structured code
- Easy to run locally

--------------------
🛠 Tech Stack
--------------------
- Python 3
- Flask
- HTML
- CSS
- Jinja2 (templating)

--------------------
📁 Project Structure
--------------------
fibonacci-web-app/
│
├── main.py              # Controller (Flask app)
├── templates/
│   └── index.html       # View (HTML form)
├── static/
│   └── style.css        # Stylesheet
└── README.txt           # Documentation file

--------------------
▶️ How to Run the Project
--------------------
1. Clone the repository:

   git clone https://github.com/your-username/fibonacci-web-app.git
   cd fibonacci-web-app

2. Install Flask:

   pip install flask

3. Run the app:

   python main.py

4. Open in browser:

   http://localhost:5000

--------------------
🧠 How It Works (MVC)
--------------------
- Model: `generate_fibonacci()` Python function
- View: HTML form in `index.html` for user input
- Controller: Flask route in `main.py` processes the input, calls model, and returns view

--------------------
💡 Sample Output
--------------------
Input: 7  
Output: 0, 1, 1, 2, 3, 5, 8

--------------------
📌 Future Improvements
--------------------
- Input validation for negative or invalid numbers
- REST API version
- Add animations and UX enhancements

--------------------
👨‍💻 Author
--------------------
Vinayak Shirke  
GitHub: https://github.com/ItsVinOp  
LinkedIn: https://linkedin.com/in/itsvinop
