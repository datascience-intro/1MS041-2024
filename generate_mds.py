import os
notebooks = os.listdir('notebooks')
notebooks = [notebook for notebook in notebooks if '.ipynb' in notebook[-6:]]
def gen_md_content(notebook):
    file_str = '''---
title: ""
permalink: /%s/
sidebar:
  nav: "lMenu"
---

Download as a jupyter [ipynb notebook](https://datascience-intro.github.io/1MS041-2024/notebooks/%s.ipynb) or view it as [html](https://datascience-intro.github.io/1MS041-2024/notebooks/%s.html).

<iframe src="https://datascience-intro.github.io/1MS041-2024/notebooks/%s.html" width="1080" height="1080" frameborder="0"></iframe>

    ''' % (notebook,notebook,notebook,notebook)

    return notebook,file_str

for i in notebooks:
    name,content = gen_md_content(i[:-6])
    print("Creating md for: %s" % name)
    with open('%s.md' % name, mode='w') as f:
        f.write(content)

preamble = '''---
## Introduction to Data Science 1MS041

You can download the Lecture notes [here](https://datascience-intro.github.io/1MS041-2024/Files/LectureNotes1MS041.pdf).

Precision Recall survey [here](https://datascience-intro.github.io/1MS041-2024/Files/AveragePrecision.pdf)


### Introductory Jupyter .ipynb Notebooks
These notebooks contain the basic theory of how to work with python and BASH, that will be needed in this course.

'''

midamble = '''
### Individual Jupyter .ipynb lecture Notebooks

These notebooks are numbered according to which lecture they coincide with and will be updated after the lectures. Before the lecture they can be considered preliminary.

'''

probssamble = '''
### Problem Solving Sessions

These notebooks are numbered according to which problem solving session they coincide with.

'''

postamble = '''
### Starting package
* Download the [Starting package](Files/first_lecture_and_data.zip)
* Unzip this into a folder that you will use as the base folder
* Whenever you download the next lectures as `ipynb` files, you put them in the same place as `*.ipynb`, this way all pathways will be the same for all of us.

### Assignment notebooks (Will be empty until it is time)

'''

appendix = [notebook for notebook in notebooks if (notebook[0] == 'A' and notebook[1]!='s')]
appendix = sorted(appendix)

assignments = [notebook for notebook in notebooks if notebook[:3] == 'Ass']
assignments = sorted(assignments)

assignments_string = ""
for notebook in assignments:
    name = notebook[:-6]
    number = str(notebook[-7])
    assignments_string+="%s. [%s](%s.md)\n" % (number,name,name)

appendices_string = ""
for notebook in appendix:
    name = notebook[:-6]
    number = notebook[:3]
    appendices_string+="%s. [%s](%s.md)\n" % (number,name,name)

no_appendix = [notebook for notebook in notebooks if notebook[0] != 'A']
no_appendix = sorted(no_appendix)

notebooks_string = ""
notebooks_string_probss = ""
for notebook in no_appendix:
    if ("ProbSS" in notebook):
        continue
    name = notebook[:-6]
    number = notebook[:2]
    notebooks_string+="%s. [%s](%s.md)\n" % (number,name,name)
for notebook in no_appendix:
    if ("ProbSS" not in notebook):
        continue
    name = notebook[:-6]
    number = notebook[:2]
    notebooks_string_probss+="%s. [%s](%s.md)\n" % (number,name,name)

print("Creating index.md using", appendix, no_appendix)
with open('index.md',mode='w') as f:
    f.write(preamble
    +appendices_string
    +midamble
    +notebooks_string
    +probssamble
    +notebooks_string_probss
    +postamble
    +assignments_string)
