from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
import os

def home(request):
    context = {
        'name': 'AKSHAY K',
        'role': 'Software Engineer',
        'tagline': 'Building the future with code and creativity.',
        'education': [
            {
                'degree': 'MCA – Computer Applications',
                'meta': 'RNS Institute of Technology (2024–2026)',
                'score': 'CGPA: 9.39'
            },
            {
                'degree': 'BCA',
                'meta': 'L.B. & S.B.S Arts, Science & Commerce College (2020–2023)',
                'score': '82.26%'
            },
            {
                'degree': '12th Grade',
                'meta': 'Karnataka PUE',
                'score': '89.60%'
            },
            {
                'degree': '10th Grade',
                'meta': 'KSEEB',
                'score': '87.84%'
            }
        ],
        'skills': [
            'Java', 'Python', 'JavaScript', 'HTML', 'CSS', 'PHP', 'C++', 'C', 'DBMS', 'SQL', 'Unix'
        ],
        'projects': [
            {
                'title': 'Blockchain Based Streaming Platform',
                'tech': ['Next.js 14', 'TypeScript', 'Tailwind', 'WebRTC', 'ethers.js', 'MongoDB'],
                'description': 'Decentralized live-streaming platform for crypto creators with USDC tipping on Ethereum Sepolia, NFT rewards, and a built-in token launchpad.'
            },
            {
                'title': 'Fitness Web Application',
                'tech': ['Java', 'PHP', 'HTML', 'CSS', 'JavaScript'],
                'description': 'Frontend development and database management for a comprehensive fitness tracking application.'
            }
        ],
        'interests': ['Sports', 'Stock Market', 'Cryptocurrency']
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
            filename='Akshay_K_Resume.pdf',
            content_type='application/pdf'
        )
    else:
        # File not found - return 404
        raise Http404("Resume file not found. Please add your resume.pdf file to static/resume/ directory.")
