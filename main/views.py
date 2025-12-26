from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
import os

def home(request):
    context = {
        'name': 'Varshitha S',
        'role': 'Technical Analyst',
        'tagline': 'Learner. Punctual. Ambitious.',
        'location': 'Bengaluru, India',
        'phone': '+91 9741630913',
        'email': 'svarshitha650@gmail.com',
        'summary': 'Data-driven Computer Science graduate with hands-on experience in machine learning, analytics, and visualization. Passionate about translating complex data into actionable business insights.',
        'skills': [
            'Machine Learning',
            'Deep Learning',
            'Data Analysis',
            'Google Analytics',
            'Medical Imaging',
            'SQL',
            'Printer Hardware & Software Support',
            'English Proficiency',
            'Attention to Detail'
        ],
        'experience': [
            {
                'role': 'Technical Analyst – Hardware Data & Performance Support',
                'company': 'Hewlett-Packard (HP Inc.)',
                'duration': 'July 2024 – Present',
                'location': 'Bengaluru, India',
                'responsibilities': [
                    'Analyzed printer hardware and software performance data to identify recurring issues and improve service metrics.',
                    'Created structured documentation and technical SOPs to improve team knowledge retention.',
                    'Collaborated cross-functionally to implement process improvements based on analytics and support trends.',
                    'Trained new team members using performance data and issue-pattern insights.'
                ]
            },
            {
                'role': 'Machine Learning Intern',
                'company': 'Forus Health Pvt. Ltd.',
                'duration': 'Oct 2023 – Jan 2024',
                'location': 'Bengaluru, India',
                'responsibilities': [
                    'Conducted unit testing of MLOps pipeline components to ensure reliability.',
                    'Led a healthcare project focused on fundus image classification using Python, improving accuracy and efficiency.'
                ]
            }
        ],
        'education': [
            {
                'degree': 'Bachelor of Engineering – Computer Science',
                'meta': 'Global Academy of Technology, Bengaluru, India (Dec 2020 – June 2024)',
                'score': 'CGPA: 8.7 / 10'
            },
            {
                'degree': 'Pre-University Course – PCMB',
                'meta': 'Deeksha PU College, Bengaluru, India (June 2018 – March 2020)',
                'score': 'Percentage: 80%'
            }
        ],
        'projects': [
            {
                'title': 'Credit Card Fraud Detection',
                'description': 'Built models using Random Forest, SVM, and Decision Tree classifiers. Applied PCA, LIME, and UMAP for feature selection and interpretability.',
                'tech': ['Python', 'Machine Learning', 'Random Forest', 'SVM', 'Decision Tree', 'PCA', 'LIME', 'UMAP']
            },
            {
                'title': 'Brain Stroke Prediction',
                'description': 'Compared multiple ML classifiers and a custom Neural Network model. Focused on early-age stroke prediction with optimization and dropout techniques.',
                'tech': ['Python', 'Machine Learning', 'Neural Networks', 'Deep Learning']
            },
            {
                'title': 'Satellite Image Segmentation',
                'description': 'Segmented satellite imagery using UMAP for improved analysis and interpretation.',
                'tech': ['Python', 'UMAP', 'Image Processing', 'Data Analysis']
            },
            {
                'title': 'University Preference Analysis',
                'description': 'Analyzed factors influencing university selection using data visualization and exploration.',
                'tech': ['Python', 'Data Visualization', 'Data Analysis']
            },
            {
                'title': 'Courier Management System',
                'description': 'Developed a booking and tracking system using HTML, PHP, and MySQL.',
                'tech': ['HTML', 'PHP', 'MySQL']
            }
        ],
        'certifications': [
            {
                'title': 'Paper Presentation on DL and ML Classifiers',
                'organization': 'IEEE International Conference (NMITCON-2023)'
            },
            {
                'title': 'Introduction to Data Science',
                'organization': 'Cisco'
            },
            {
                'title': 'Business Intelligence Fundamentals',
                'organization': 'SkillUp by Simplilearn'
            },
            {
                'title': 'Cloud Computing with AWS for Beginners',
                'organization': 'Udemy'
            },
            {
                'title': 'Masterclass on Tableau for Data Science',
                'organization': 'Scaler Academy'
            },
            {
                'title': 'Workshop on Business Intelligence using Power BI',
                'organization': 'Skill Nation'
            },
            {
                'title': 'Exemplary in Progressive Training Program (30 hours)',
                'organization': 'TalentEase'
            },
            {
                'title': 'Virtual Internship – Pledge a Smile Foundation (NGO)',
                'organization': '1 Month'
            }
        ],
        'languages': ['English', 'Hindi', 'Kannada']
    }
    return render(request, 'home.html', context)

def download_resume(request):
    """
    View to download the resume PDF file.
    """
    # Path to resume file in static directory
    resume_path = os.path.join(settings.BASE_DIR, 'static', 'resume', 'resume.pdf')
    
    # Check if file exists
    if os.path.exists(resume_path):
        # Return file as download response
        return FileResponse(
            open(resume_path, 'rb'),
            as_attachment=True,
            filename='Varshitha_S_Resume.pdf',
            content_type='application/pdf'
        )
    else:
        # File not found - return 404
        raise Http404("Resume file not found. Please add your resume.pdf file to static/resume/ directory.")
