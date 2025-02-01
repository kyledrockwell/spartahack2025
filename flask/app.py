# app.py
from flask import Flask, render_template, request, jsonify
import json
from markupsafe import Markup

app = Flask(__name__)

def mock_analyze_code(context, code, language):
    """
    Placeholder for API integration - replace this with your actual API call
    """
    return {
        "status": "success",
        "analysis": f"""# Analysis Result
Language: {language}
Code length: {len(code)} characters
Context length: {len(context)} characters

# Sample feedback:
- Code structure looks good
- Consider adding more comments
- Variable names are clear"""
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    context = None
    code = None
    
    if request.method == 'POST':
        context = request.form.get('context', '')
        code = request.form.get('code', '')
        language = request.form.get('language', 'python')
        
        # Here you would typically make an API call
        analysis_result = mock_analyze_code(context, code, language)
        
        if analysis_result["status"] == "success":
            result = analysis_result["analysis"]
            
    return render_template('index.html', 
                         result=result, 
                         context=context, 
                         code=code)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        context = data.get('context', '')
        code = data.get('code', '')
        language = data.get('language', 'python')
        
        analysis_result = mock_analyze_code(context, code, language)
        return jsonify(analysis_result)
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)