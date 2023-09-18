from setuptools import setup, find_packages

setup(
    name='credit_system',
    version='0.1',
    description='Credit Score and Loan Approval System',
    author='Mfundo Monchwe',
    author_email='diditmfundo@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires= [
        'django==4.2.5',
        'djangorestframework==3.14.0',
        'django-cors-headers==4.2.0',
        'pandas==2.0.2',
        'numpy==1.24.3',
        'matplotlib==3.7.1',
        'scikit-learn==1.2.2',
        'seaborn==0.12.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.11.4',
        'Framework :: Django :: 4.2.5', 
        'Intended Audience :: Developers/Data Scientist',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
            'credit_system = credit_system.manage:main',
        ],
    },
)