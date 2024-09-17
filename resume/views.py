from django.shortcuts import render

def cv(request):
    context = {
        'name': 'Aditi Aatmaja',
        'email': 'aa12918@nyu.edu',
        'phone': '(929) 355-9156',
        'linkedin': 'linkedin.com/in/aditiaatmaja',

        'education': [
            {
                'institution': 'New York University',
                'location': 'New York, NY',
                'degree': 'Master of Science in Computer Science',
                'expected_graduation': 'Expected 05/26',
                'courses': [
                    'Software Engineering', 'Algorithms', 'Operating Systems'
                ]
            },
            {
                'institution': 'SRM Institute of Science and Technology',
                'location': 'Chennai, India',
                'degree': 'Bachelor of Science in Computer Science and Engineering',
                'graduation': '05/23',
                'gpa': '3.79/4.00',
                'courses': [
                    'Data Structures', 'Discrete Math', 'Artificial Intelligence', 'Advanced Programming'
                ]
            }
        ],

        'technical_skills': {
            'programming_languages': ['Python', 'Java', 'JavaScript', 'C++', 'SQL', 'HTML', 'CSS', 'PHP'],
            'domains': ['IT (JIRA, Confluence)', 'DevOps (Kubernetes, Docker, Maven)', 'Project Management', 'AWS'],
            'certifications': ['Microsoft AZ-900', 'Oracle Database Foundations']
        },

        'experience': [
            {
                'company': 'Coined-One Technologies',
                'location': 'Cochin, India',
                'role': 'Technical Product Manager',
                'duration': '06/23 - 02/24',
                'details': [
                    'Led cross-functional teams to integrate backend systems using JavaScript, delivering user onboarding feature with ~20% engagement increase',
                    'Defined KPIs and implemented AI Virtual Assistant, reducing support ticket response times by 40%'
                ]
            },
            {
                'company': 'Reliance Industries Ltd',
                'location': 'Mumbai, India',
                'role': 'Software Engineer Intern',
                'duration': '01/23 - 04/23',
                'details': [
                    'Engineered data pipelines with Python, developed real-time inventory management with SQL',
                    'Led migration from MySQL to PostgreSQL, enhancing scalability and performance'
                ]
            },
            {
                'company': 'Walmart Global Tech',
                'location': 'Chennai, India',
                'role': 'Software Engineer Intern',
                'duration': '05/22 - 08/22',
                'details': [
                    'Developed and maintained IT playbooks in JIRA Confluence, resolving deployment issues',
                    'Achieved a 95% resolution rate for L1/L2 issues with advanced debugging and cloud tech integration'
                ]
            }
        ],

        'publications': [
            {
                'title': 'Waste Management System Using IoT & Smart Credit System',
                'published_in': 'AIP Conference Proceedings, VOL 3075, Issue 1: ICIoT 2023',
                'details': 'Optimized bin placement and collection schedules, improving operational efficiency by 30%. Received Best Paper Award.'
            },
            {
                'title': 'Neural Network Based Approach to Forecasting Bankruptcy',
                'published_in': 'IEEE Xplore, Proceedings of ICSADL 2024',
                'details': 'Developed neural network algorithm, reducing bankruptcy prediction time by 75%.'
            }
        ],

        'leadership': [
            {
                'title': 'Partnerships Project Lead',
                'organization': 'NYU Digital Learning',
                'location': 'New York',
                'details': 'Led stakeholder meetings, optimized event management using Excel, Google Sheets, Salesforce, boosting team efficiency.'
            },
            {
                'title': 'Vice President',
                'organization': 'Salesforce Student Group',
                'location': 'Chennai, India',
                'details': 'Led club initiatives, secured MoU with IEEE, implemented mentorship and girls\' cohort for inclusivity.'
            }
        ]
    }
    return render(request, 'resume/cv.html', context)
